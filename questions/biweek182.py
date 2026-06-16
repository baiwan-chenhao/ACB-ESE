
import random
from . import Problem
import re
from itertools import count


class Solution1(Problem):
    date = "2026-5-9"
    def __init__(self):
        Problem.__init__(self,
                         degree=0,
                         idx=3921,
                         types=[],
                         pass_rate=0.81,
                         description='给你一个字符串数组 `events`。\n一开始，`score = 0` 且 `counter = 0`。`events` 中的每个元素为以下之一：\n - `"0"`, `"1"`, `"2"`, `"3"`, `"4"`, `"6"`：将该值加到总得分中。\n - `"W"`：计数器加 1。不增加得分。\n - `"WD"`：总得分加 1。\n - `"NB"`：总得分加 1。\n\n从左到右处理数组。当满足以下任一条件时停止处理：\n - `events` 中的所有元素都已处理完毕，或\n - 计数器变为 10。\n\n返回一个整数数组 `[score, counter]`，其中：\n - `score` 是最终的总得分。\n - `counter` 是最终的计数器值。\n\n**示例 1：**\n> \n**输入：**`events = ["1","4","W","6","WD"]`\n**输出：**`[12,1]`\n**解释：**\n| 事件 | 得分 | 计数器 |\n| --- | --- | --- |\n| `"1"` | 1 | 0 |\n| `"4"` | 5 | 0 |\n| `"W"` | 5 | 1 |\n| `"6"` | 11 | 1 |\n| `"WD"` | 12 | 1 |\n\n最终结果：`[12, 1]`。\n**示例 2：**\n> \n**输入：**`events = ["WD","NB","0","4","4"]`\n**输出：**`[10,0]`\n**解释：**\n| 事件 | 得分 | 计数器 |\n| --- | --- | --- |\n| `"WD"` | 1 | 0 |\n| `"NB"` | 2 | 0 |\n| `"0"` | 2 | 0 |\n| `"4"` | 6 | 0 |\n| `"4"` | 10 | 0 |\n\n最终结果：`[10, 0]`。\n**示例 3：**\n> \n**输入：**`events = ["W","W","W","W","W","W","W","W","W","W","W"]`\n**输出：**`[0,10]`\n**解释：**\n出现 10 次 `"W"` 后，计数器达到 10，因此停止处理。剩余的事件将被忽略。\n\n**提示：**\n - `1 <= events.length <= 1000`\n - `events[i]` 是 `"0"`、`"1"`、`"2"`、`"3"`、`"4"`、`"6"`、`"W"`、`"WD"` 或 `"NB"` 之一。'
                         )

    def solve(self, events: list[str]) -> list[int]:
        score = counter = 0
        for s in events:
            if s == 'W':
                counter += 1
                if counter == 10:
                    break
            elif len(s) > 1:
                score += 1
            else:
                score += int(s)
        return [score, counter]

    def gen(self):
        """
        生成测试样例。

        返回一个元组，包含一个列表，列表中每个元素是一个测试用例（字符串数组 events）。

        覆盖场景：
        1. 边界值：单个事件、最大长度、计数器刚好达到10
        2. 特殊结构：全是W、没有W、连续W、各种得分事件
        3. 正常分布：随机混合各种事件
        """
        valid_events = ["0", "1", "2", "3", "4", "6", "W", "WD", "NB"]
        test_cases = []

        # ========== 边界值测试 (15个) ==========

        # 单个事件 - 各种类型 (9个)
        for event in valid_events:
            test_cases.append([event])

        # 最小长度但达到停止条件 - 刚好10个W
        test_cases.append(["W"] * 10)

        # 最大长度 - 没有W，能完整处理
        test_cases.append(["1"] * 1000)

        # 最大长度 - 全是W，会在第10个停止
        test_cases.append(["W"] * 1000)

        # 刚好在第10个W时有其他事件混合
        test_cases.append(["W", "1"] * 5 + ["W"] + ["2", "3"])

        # ========== 特殊结构测试 (20个) ==========

        # 混合得分事件 - 没有W
        test_cases.append(["0", "1", "2", "3", "4", "6", "WD", "NB", "0", "1"])
        test_cases.append(["WD", "NB", "WD", "NB"])

        # 计数器刚好达到10，后面还有事件
        test_cases.append(["W"] * 10 + ["1", "2", "WD"])
        test_cases.append(["W", "1", "W", "2", "W", "3", "W", "4", "W", "6", "W", "WD", "NB"])

        # 计数器接近10但未达到
        test_cases.append(["W"] * 9 + ["1", "2", "3"])
        test_cases.append(["W", "1", "W", "2"] * 4 + ["W", "3"])

        # 各种得分值组合
        test_cases.append(["0", "0", "0", "0", "0"])  # 全是0
        test_cases.append(["6", "6", "6", "6", "6"])  # 全是6
        test_cases.append(["4", "4", "4", "4", "4"])  # 全是4
        test_cases.append(["0", "1", "2", "3", "4", "6"] * 2)  # 完整得分循环

        # WD和NB混合
        test_cases.append(["WD", "NB"] * 5)
        test_cases.append(["WD", "WD", "WD", "NB", "NB", "NB"])

        # W和得分事件混合 - 计数器未达10
        test_cases.append(["W", "1", "W", "2", "W", "3"])
        test_cases.append(["1", "W", "2", "W", "3", "W", "4"])

        # 复杂混合场景
        test_cases.append(["0", "W", "1", "WD", "W", "2", "NB", "W", "3", "W", "4", "6", "W"])

        # ========== 正常分布测试 (65个) ==========

        # 随机混合事件，长度适中，计数器未达到10
        for _ in range(30):
            length = self.s_generate_int(int_range=(5, 30))
            case = []
            w_count = 0
            for _ in range(length):
                # 控制W的数量不超过9，确保能完整处理
                if w_count >= 9:
                    event = random.choice(["0", "1", "2", "3", "4", "6", "WD", "NB"])
                else:
                    event = random.choice(valid_events)
                case.append(event)
                if event == "W":
                    w_count += 1
            test_cases.append(case)

        # 随机混合事件，长度较长，计数器可能达到10
        for _ in range(30):
            length = self.s_generate_int(int_range=(20, 100))
            case = [random.choice(valid_events) for _ in range(length)]
            test_cases.append(case)

        # 少量大长度测试（验证性能）
        for _ in range(5):
            length = self.s_generate_int(int_range=(100, 500))
            case = [random.choice(valid_events) for _ in range(length)]
            test_cases.append(case)

        return (test_cases,)
    


from . import Problem
import re
from itertools import count


class Solution2(Problem):
    date = "2026-5-9"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3922,
                         types=[],
                         pass_rate=0.29,
                         description='给你一个二进制字符串 `s`。\n如果一个字符串**不**包含 `"011"` 或 `"110"` 作为**子序列**，则认为该字符串是**连贯的**。\n在一次操作中，你可以**翻转**`s` 中的任意字符（`\'0\'` 变为 `\'1\'`，或 `\'1\'` 变为 `\'0\'`）。\n返回一个整数，表示使 `s` 连贯所需的**最少**修改次数。\n\n**示例 1：**\n> \n**输入：**`s = "1010"`\n**输出：**`1`\n**解释：**\n翻转 `s[0]` 得到 `"0010"`，它不包含 `"011"` 或 `"110"` 子序列。\n**示例 2：**\n> \n**输入：**`s = "0110"`\n**输出：**`1`\n**解释：**\n翻转 `s[1]` 得到 `"0010"`，移除了所有禁止的子序列 `"011"` 和 `"110"`。\n**示例 3：**\n> \n**输入：**`s = "1000"`\n**输出：**`0`\n**解释：**\n该字符串已经不包含 `"011"` 或 `"110"` 子序列，因此不需要翻转。\n\n**提示：**\n - `1 <= s.length <= 10^5`\n - `s[i]` 是 `\'0\'` 或 `\'1\'`。'
                         )

    def solve(self, s: str) -> int:
        c0 = s.count('0')
        c1 = len(s) - c0 - 1
        if s[0] == '1' and s[-1] == '1':
            c1 -= 1
        return min(c0, max(c1, 0))

    def gen(self):
        """
        生成测试样例，返回一个由列表组成的元组。

        覆盖场景：
        1. 边界长度：长度为1, 2, 3的字符串
        2. 小规模随机字符串：长度4-20
        3. 中等规模随机字符串：长度50-2000
        4. 特殊结构：全0、全1、交替模式

        注意：虽然题目约束长度可达10^5，但为了避免测试超时，
        这里将最大长度控制在2000以内。
        """
        import random
        import itertools

        random.seed(self.seed)
        cases = []

        # 场景1：边界长度测试（前30个测试用例）
        # 长度为1
        for i in range(10):
            cases.append(random.choice(['0', '1']))

        # 长度为2
        for i in range(10):
            cases.append(''.join(random.choice(['0', '1']) for _ in range(2)))

        # 长度为3
        for i in range(10):
            cases.append(''.join(random.choice(['0', '1']) for _ in range(3)))

        # 场景2：小规模随机字符串（长度4-20，30个测试用例）
        for i in range(30):
            length = random.randint(4, 20)
            s = ''.join(random.choice(['0', '1']) for _ in range(length))
            cases.append(s)

        # 场景3：中等规模随机字符串（长度50-2000，30个测试用例）
        for i in range(30):
            length = random.randint(50, 2000)
            s = ''.join(random.choice(['0', '1']) for _ in range(length))
            cases.append(s)

        # 场景4：特殊结构（10个测试用例）
        # 全0字符串
        length = random.randint(5, 100)
        cases.append('0' * length)

        # 全1字符串
        length = random.randint(5, 100)
        cases.append('1' * length)

        # 交替模式 010101...
        length = random.randint(5, 50)
        cases.append('01' * (length // 2) + ('0' if length % 2 else ''))

        # 交替模式 101010...
        length = random.randint(5, 50)
        cases.append('10' * (length // 2) + ('1' if length % 2 else ''))

        # 包含011子序列
        cases.append('011')

        # 包含110子序列
        cases.append('110')

        # 连续的0后面连续的1
        cases.append('00001111')

        # 连续的1后面连续的0
        cases.append('11110000')

        # 随机选择部分特殊情况作为额外测试（补充到100个）
        special_cases = [
            '0', '1', '01', '10', '00', '11',
            '0011', '1100', '0101', '1010',
            '0110', '1001', '00110', '11001',
        ]
        remaining = 100 - len(cases)
        for i in range(remaining):
            cases.append(random.choice(special_cases))

        return (cases,)
    

import math
from . import Problem
from typing import List
from itertools import combinations
import re
import copy
from itertools import count
from math import comb
from math import floor


class Solution3(Problem):
    date = "2026-5-9"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3923,
                         types=[],
                         pass_rate=0.48,
                         description='给你一个二维整数数组 `points` ，其中 `points[i] = [x_i, y_i, z_i]` 表示三维空间中的一个点，以及一个表示目标点的整数数组 `target` 。\n定义**第 0 代**为初始点列表。对于每个整数 `k >= 1`，按如下方式形成第 `k` 代：\n - 考虑从第 0 代到第 `k - 1` 代产生的所有点中提取的每一对两个**不同的**点 `a = [x_1, y_1, z_1]` 和 `b = [x_2, y_2, z_2]`。\n - 对于每一对这样的点，计算 `c = [floor((x_1 + x_2) / 2), floor((y_1 + y_2) / 2), floor((z_1 + z_2) / 2)]` 并将每一个这样的 `c` 收集到第 `k` 代中。\n - 第 `k` 代中的所有点都是由第 0 代到第 `k - 1` 代中的点**同时**产生的。\n - 在第 `k` 代形成之后，第 `k` 代中的点将被视为可用于形成后代。\n\n返回使 `target` 出现在第 0 代到第 `k` 代之中的**最小**整数 `k`。如果 `target` 已经在初始点中，则返回 0。如果无法获得 `target`，则返回 -1。\n注意：\n -**floor**表示向**下**取整到最接近的整数。\n - “两个**不同的**点”意味着选择的两个点必须具有**不同的**`(x, y, z)` 坐标。一个点不能与自身配对，并且具有**完全相同**坐标的两个点也不可以配对。\n\n**示例 1：**\n> \n**输入：**`points = [[0,0,0],[6,6,6]], target = [3,3,3]`\n**输出：**`1`\n**解释：**\n -**第 0 代：**初始 `points = [[0, 0, 0], [6, 6, 6]]`。\n - `target = [3, 3, 3]` 不存在于第 0 代中。\n -**第 1 代：**对于第 0 代中的每一对点，我们创建新的点。\n> \t - 使用 `[0, 0, 0]` 和 `[6, 6, 6]`，我们生成 `[3, 3, 3]`。\n\n - 第 1 代之后，`points = [[0, 0, 0], [6, 6, 6], [3, 3, 3]]`。\n - `target = [3, 3, 3]` 在第 1 代中被找到，因此最小的 `k` 为 1。\n\n**示例 2：**\n> \n**输入：**`points = [[0,0,0],[5,5,5]], target = [1,1,1]`\n**输出：**`2`\n**解释：**\n -**第 0 代：**初始 `points = [[0, 0, 0], [5, 5, 5]]`。\n - `target = [1, 1, 1]` 不存在于第 0 代中。\n -**第 1 代：**对于第 0 代中的每一对点，我们创建新的点。\n> \t - 使用 `[0, 0, 0]` 和 `[5, 5, 5]`，我们生成 `[2, 2, 2]`。\n\n - 第 1 代之后，`points = [[0, 0, 0], [5, 5, 5], [2, 2, 2]]`。\n -**第 2 代：**对于第 1 代之后可用的每一对点，我们创建新的点。\n> \t - 使用 `[0, 0, 0]` 和 `[5, 5, 5]`，我们生成 `[2, 2, 2]`。\n - 使用 `[0, 0, 0]` 和 `[2, 2, 2]`，我们生成 `[1, 1, 1]`。\n - 使用 `[5, 5, 5]` 和 `[2, 2, 2]`，我们生成 `[3, 3, 3]`。\n\n - 第 2 代之后，`points = [[0, 0, 0], [5, 5, 5], [2, 2, 2], [1, 1, 1], [3, 3, 3]]`。\n - `target = [1, 1, 1]` 在第 2 代中被找到，因此最小的 `k` 为 2。\n\n**示例 3：**\n> \n**输入：**`points = [[0,0,0],[2,2,2],[3,3,3]], target = [2,2,2]`\n**输出：**`0`\n**解释：**\n -**第 0 代：**初始 `points = [[0, 0, 0], [2, 2, 2], [3, 3, 3]]`。\n - `target = [2, 2, 2]` 已经存在于第 0 代中，因此最小的 `k` 为 0。\n\n**示例 4：**\n> \n**输入：**`points = [[1,2,3]], target = [5,5,5]`\n**输出：**`-1`\n**解释：**\n - 只有一个初始点可用，因此无法生成新点。\n - 因此，无法获得目标，答案为 -1。\n\n**提示：**\n - `1 <= points.length <= 20`\n - `points[i] = [x_i, y_i, z_i]`\n - `0 <= x_i, y_i, z_i <= 6`\n - `target.length == 3`\n - `\u200b\u200b\u200b\u200b\u200b\u200b\u200b0 <= target[i] <= 6`\n - 初始点集合不包含重复项。'
                         )

    def solve(self, points: List[List[int]], target: List[int]) -> int:
        tar = tuple(target)
        cur = set(map(tuple, points))
        for ans in count(0):
            if tar in cur:
                return ans
            nxt = cur.copy()
            for (x, y, z), (a, b, c) in combinations(cur, 2):
                nxt.add(((x + a) // 2, (y + b) // 2, (z + c) // 2))
            if len(nxt) == len(cur):
                return -1
            cur = nxt

    def gen(self):
        """
        生成测试样例
        返回格式：(points_list, target_list)
        - points_list: 每个元素是一个测试用例的 points 参数
        - target_list: 每个元素是一个测试用例的 target 参数
        """
        import random
        random.seed(self.seed)

        points_list = []
        target_list = []

        # 辅助函数：生成不重复的随机点
        def s_generate_unique_points(num_points, coord_range=(0, 4)):
            points_set = set()
            while len(points_set) < num_points:
                x = random.randint(*coord_range)
                y = random.randint(*coord_range)
                z = random.randint(*coord_range)
                points_set.add((x, y, z))
            return [list(p) for p in points_set]

        # ===== 特殊边界测试用例 =====

        # 1. 单点 - 无法生成新点，target不是该点 => k=-1
        points_list.append([[1, 2, 3]])
        target_list.append([5, 5, 5])

        # 2. 单点 - target就是该点 => k=0
        points_list.append([[2, 2, 2]])
        target_list.append([2, 2, 2])

        # 3. 两个点，target在初始点中 => k=0
        points_list.append([[0, 0, 0], [2, 2, 2]])
        target_list.append([2, 2, 2])

        # 4. 两个点，恰好一次中点得到target => k=1
        points_list.append([[0, 0, 0], [2, 2, 2]])
        target_list.append([1, 1, 1])

        # 5. 两个点，target不在任何代中 => k=-1（坐标都为0，只能生成0）
        points_list.append([[0, 0, 0], [1, 1, 1]])
        target_list.append([3, 3, 3])

        # 6. 示例1 - 两个点，一次中点 => k=1
        points_list.append([[0, 0, 0], [6, 6, 6]])
        target_list.append([3, 3, 3])

        # 7. 示例2 - 需要两代 => k=2
        points_list.append([[0, 0, 0], [5, 5, 5]])
        target_list.append([1, 1, 1])

        # 8. 三个点，target在初始点中 => k=0
        points_list.append([[0, 0, 0], [2, 2, 2], [3, 3, 3]])
        target_list.append([2, 2, 2])

        # 9. 多点 - 覆盖所有可能坐标
        points_list.append([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1],
                            [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
        target_list.append([0, 0, 0])

        # 10. 边界坐标测试
        points_list.append([[0, 0, 0], [0, 0, 4], [0, 4, 0], [0, 4, 4],
                            [4, 0, 0], [4, 0, 4], [4, 4, 0], [4, 4, 4]])
        target_list.append([2, 2, 2])

        # ===== 随机测试用例 =====

        # 随机生成不同规模点集和随机target
        for i in range(30):
            num_points = random.randint(1, 5)
            coord_max = random.randint(2, 4)
            points = s_generate_unique_points(num_points, (0, coord_max))

            target = [
                random.randint(0, coord_max),
                random.randint(0, coord_max),
                random.randint(0, coord_max)
            ]

            points_list.append(points)
            target_list.append(target)

        return points_list, target_list
    

from itertools import chain
import math
import random
from itertools import count
from . import Problem
from typing import List
from collections import deque
from bisect import bisect_left
import re
from math import inf


class Solution4(Problem):
    date = "2026-5-9"
    def __init__(self):
        Problem.__init__(self,
                         degree=2,
                         idx=3924,
                         types=[],
                         pass_rate=0.4,
                         description='给你一个有 `n` 个节点的无向加权图，节点编号从 0 到 `n - 1`。\n该图由一个二维整数数组 `edges` 表示，其中每条边 `edges[i] = [u_i, v_i, w_i]` 表示节点 `u_i` 和 `v_i` 之间存在一条权重为 `w_i` 的无向边。\n另外给你整数 `source`、`target` 和 `k`。\n`threshold` 的值决定了一条边被认为是**轻的**还是**重的**：\n - \n如果一条边的权重**小于**或**等于**`threshold`，则该边是**轻的**。\n - \n如果一条边的权重**大于**`threshold`，则该边是**重的**。\n\n如果从 `source` 到 `target` 的路径包含**至多**`k` 条重边，则该路径是**有效的**。\n返回使 `source` 到 `target` 之间**至少**存在一条**有效**路径的**最小整数**`threshold`。如果不存在这样的路径，则返回 -1。\n\n**示例 1：**\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\n\u200b\u200b\u200b\u200b\u200b\u200b\u200b\n> \n**输入：**`n = 6, edges = [[0,1,5],[1,2,3],[3,4,4],[4,5,1],[1,4,2]], source = 0, target = 3, k = 1`\n**输出：**`4`\n**解释：**\n使得从节点 0 到节点 3 的路径最多使用 1 条重边的最小 `threshold` 为 4。\n - \n轻边：`[1, 2, 3]`, `[3, 4, 4]`, `[4, 5, 1]`, `[1, 4, 2]`\n - \n重边：`[0, 1, 5]`\n\n一条有效路径是 `0 → 1 → 4 → 3`。它只使用了 1 条重边（`[0, 1, 5]`），满足限制 `k = 1`。\n任何更小的 `threshold` 都会导致无法在不超过 1 条重边的情况下到达节点 3。\n**示例 2：**\n\n> \n**输入：**`n = 6, edges = [[0,1,3],[1,2,4],[3,4,5],[4,5,6]], source = 0, target = 4, k = 1`\n**输出：**`-1`\n**解释：**\n从节点 0 到节点 4 没有路径。由于无法到达目标节点，因此输出为 -1。\n**示例 3：**\n****\n> \n**输入：**`n = 4, edges = [[0,1,2],[1,2,2],[2,3,2],[3,0,2]], source = 0, target = 0, k = 0`\n**输出：**`0`\n**解释：**\n源节点和目标节点是同一个节点。不需要遍历任何边，因此最小的 `threshold` 是 0。\n\n**提示：**\n - `1 <= n <= 10^3\u200b\u200b\u200b\u200b\u200b\u200b\u200b`\n - `0 <= edges.length <= 10^3\u200b\u200b\u200b\u200b\u200b\u200b\u200b`\n - `edges[i] = [u_i, v_i, w_i]`\n - `0 <= u_i, v_i\u200b\u200b\u200b\u200b\u200b\u200b\u200b <= n - 1`\n - `1 <= w_i\u200b\u200b\u200b\u200b\u200b\u200b\u200b <= 10^9`\n - `0 <= source, target <= n - 1`\n - `0 <= k <= edges.length`'
                         )

    def solve(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        g = [[] for _ in range(n)]
        max_wt = 0
        for x, y, wt in edges:
            g[x].append((y, wt))
            g[y].append((x, wt))
            max_wt = max(max_wt, wt)

        def check(threshold: int) -> bool:
            dis = [inf] * n
            dis[source] = 0
            q = deque([(source, 0)])
            while q:
                x, d = q.popleft()
                if x == target:
                    return True
                if d > dis[x]:
                    continue
                for y, w in g[x]:
                    wt = 1 if w > threshold else 0
                    new_dis = d + wt
                    if new_dis < dis[y]:
                        dis[y] = new_dis
                        if wt == 0:
                            q.appendleft((y, new_dis))
                        elif new_dis <= k:
                            q.append((y, new_dis))
            return False
        ans = bisect_left(range(max_wt + 1), True, key=check)
        return -1 if ans > max_wt else ans

    def gen(self):
        # 缩小测试规模以避免超时，同时保持测试覆盖性
        # n: 2-50 (原1-10^3)
        # edges: 0-100 (原0-10^3)
        # weight: 1-100 (原1-10^9)

        # 特殊图结构生成辅助方法
        def generate_special_graph(n, edges_count, graph_type='random', weight_range=(1, 100)):
            """生成特殊结构的图"""
            edges = []

            if graph_type == 'chain':  # 链式图 0-1-2-3-...-(n-1)
                for i in range(n - 1):
                    edges.append((i, i + 1))
                # 随机添加额外边
                extra_edges = max(0, edges_count - (n - 1))
                for _ in range(extra_edges):
                    u = random.randint(0, n - 2)
                    v = random.randint(u + 1, min(n - 1, u + 5))
                    if (u, v) not in edges and (v, u) not in edges:
                        edges.append((u, v))
            elif graph_type == 'cycle':  # 环图 0-1-2-...-(n-1)-0
                for i in range(n):
                    edges.append((i, (i + 1) % n))
                # 随机添加额外边
                extra_edges = max(0, edges_count - n)
                for _ in range(extra_edges):
                    u = random.randint(0, n - 1)
                    v = random.randint(0, n - 1)
                    if u != v and (u, v) not in edges and (v, u) not in edges:
                        edges.append((u, v))
            elif graph_type == 'star':  # 星形图 0为中心
                center = 0
                for i in range(1, n):
                    edges.append((center, i))
                # 随机添加额外边
                extra_edges = max(0, edges_count - (n - 1))
                for _ in range(extra_edges):
                    u = random.randint(1, n - 1)
                    v = random.randint(1, n - 1)
                    if u != v and (u, v) not in edges and (v, u) not in edges:
                        edges.append((u, v))
            elif graph_type == 'complete':  # 完全图
                for i in range(n):
                    for j in range(i + 1, n):
                        edges.append((i, j))
                # 截取部分边
                if edges_count < len(edges):
                    edges = random.sample(edges, edges_count)
            else:  # 随机图
                max_possible = n * (n - 1) // 2
                edges_count = min(edges_count, max_possible)
                if n > 1 and edges_count > 0:
                    all_edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
                    edges = random.sample(all_edges, min(edges_count, len(all_edges)))

            # 添加权重并打乱顺序
            weighted_edges = []
            for u, v in edges:
                w = random.randint(*weight_range)
                weighted_edges.append([u, v, w])
            random.shuffle(weighted_edges)
            return weighted_edges

        test_cases = []

        # ========== 边界值测试 (15个) ==========
        # 1-5: source = target，返回0
        for i in range(5):
            n = random.randint(2, 10)
            node = random.randint(0, n - 1)  # 确保节点在有效范围内
            edges = generate_special_graph(n, min(n, 5), 'random')
            test_cases.append((n, edges, node, node, random.randint(0, 5)))

        # 6-10: k = 0（不允许重边，threshold需>=max_weight）
        for i in range(5):
            n = random.randint(2, 20)
            edges = generate_special_graph(n, n - 1, 'chain')
            test_cases.append((n, edges, 0, n - 1, 0))

        # 11-13: 空图或接近空图
        test_cases.append((2, [], 0, 1, 0))  # 无边，source!=target
        test_cases.append((5, [[0, 1, 10]], 0, 4, 1))  # 单条边
        test_cases.append((3, [], 0, 0, 0))  # 无边，source=target

        # 14-15: 最小和最大k值
        test_cases.append((10, generate_special_graph(10, 10, 'random'), 0, 9, 0))
        test_cases.append((10, generate_special_graph(10, 15, 'random'), 0, 9, 10))

        # ========== 特殊结构测试 (35个) ==========
        # 16-20: 链式图
        for i in range(5):
            n = random.randint(5, 20)
            edges = generate_special_graph(n, n - 1, 'chain')
            test_cases.append((n, edges, 0, n - 1, random.randint(0, 3)))

        # 21-25: 环图
        for i in range(5):
            n = random.randint(5, 20)
            edges = generate_special_graph(n, n, 'cycle')
            test_cases.append((n, edges, 0, n - 1, random.randint(0, 3)))

        # 26-30: 星形图
        for i in range(5):
            n = random.randint(5, 20)
            edges = generate_special_graph(n, n - 1, 'star')
            test_cases.append((n, edges, 0, random.randint(1, n - 1), random.randint(0, 2)))

        # 31-35: 完全图
        for i in range(5):
            n = random.randint(4, 12)
            edges = generate_special_graph(n, n * (n - 1) // 2, 'complete')
            test_cases.append((n, edges, 0, n - 1, random.randint(1, 5)))

        # 36-40: 所有边权重相同
        for i in range(5):
            n = random.randint(5, 15)
            edges = generate_special_graph(n, min(n * 2, 30), 'random', (10, 10))
            test_cases.append((n, edges, 0, n - 1, random.randint(0, 3)))

        # 41-45: 严格递增权重
        for i in range(5):
            n = random.randint(5, 15)
            edges = []
            for j in range(n - 1):
                edges.append([j, j + 1, j + 1])
            # 添加随机边但保持较小数量
            for _ in range(min(n, 10)):
                u, v = random.randint(0, n - 1), random.randint(0, n - 1)
                if u != v:
                    edges.append([u, v, random.randint(1, n)])
            test_cases.append((n, edges, 0, n - 1, random.randint(0, n // 2)))

        # 46-50: 不连通图（返回-1）
        for i in range(5):
            n = random.randint(6, 20)
            half = n // 2
            edges_part1 = generate_special_graph(half, min(half * 2, 20), 'random')
            edges_part2 = generate_special_graph(n - half, min(half * 2, 20), 'random')
            # 偏移第二部分的节点编号
            edges = edges_part1 + [[u + half, v + half, w] for u, v, w in edges_part2]
            test_cases.append((n, edges, 0, n - 1, random.randint(0, 5)))

        # ========== 正常分布测试 (50个) ==========
        # 51-70: 稀疏随机图
        for i in range(20):
            n = random.randint(5, 30)
            edges = generate_special_graph(n, random.randint(n, n * 2), 'random')
            test_cases.append((n, edges, random.randint(0, n - 1), random.randint(0, n - 1), random.randint(0, 5)))

        # 71-85: 中等密度随机图
        for i in range(15):
            n = random.randint(5, 30)
            edges = generate_special_graph(n, random.randint(n * 2, n * 4), 'random')
            test_cases.append((n, edges, random.randint(0, n - 1), random.randint(0, n - 1), random.randint(0, 8)))

        # 86-100: 小权重范围（阈值搜索更精确）
        for i in range(15):
            n = random.randint(5, 20)
            edges = generate_special_graph(n, random.randint(n, n * 3), 'random', (1, 20))
            test_cases.append((n, edges, random.randint(0, n - 1), random.randint(0, n - 1), random.randint(0, 5)))

        # 转换为按参数维度的格式
        n_list = [tc[0] for tc in test_cases]
        edges_list = [tc[1] for tc in test_cases]
        source_list = [tc[2] for tc in test_cases]
        target_list = [tc[3] for tc in test_cases]
        k_list = [tc[4] for tc in test_cases]

        return (n_list, edges_list, source_list, target_list, k_list)
    

