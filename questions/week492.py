
import math
from . import Problem
from typing import List
import re
from math import inf


class Solution1(Problem):
    date = "2026-3-8"
    def __init__(self):
        Problem.__init__(self,
                         degree=0,
                         idx=3861,
                         types=[],
                         pass_rate=0.7,
                         description='给你一个整数数组 `capacity`，其中 `capacity[i]` 表示第 `i`\xa0个箱子的容量，以及一个整数 `itemSize`，表示一个物品的大小。\n如果第 `i`\xa0个箱子的容量满足 `capacity[i] >= itemSize`，那么该箱子可以存放该物品。\n要求返回可以存放该物品的容量**最小**的箱子的下标。如果有多个这样的箱子，返回下标**最小**的一个。\n如果没有任何箱子可以存放该物品，则返回 -1。\n\n**示例 1：**\n> \n**输入：**`capacity = [1,5,3,7], itemSize = 3`\n**输出：**`2`\n**解释：**\n下标为 2 的箱子容量为 3，是可以存放该物品的容量最小的箱子，因此答案是 2。\n**示例 2：**\n> \n**输入：**`capacity = [3,5,4,3], itemSize = 2`\n**输出：**`0`\n**解释：**\n可以存放该物品的最小容量为 3，出现在下标 0 和 3。由于下标 0 更小，因此答案是 0。\n**示例 3：**\n> \n**输入：**`capacity = [4], itemSize = 5`\n**输出：**`-1`\n**解释：**\n没有任何箱子的容量足够存放该物品，因此答案是 -1。\n\n**提示：**\n - `1 <= capacity.length <= 100`\n - `1 <= capacity[i] <= 100`\n - `1 <= itemSize <= 100`'
                         )

    def solve(self, capacity: List[int], itemSize: int) -> int:
        min_c = inf
        ans = -1
        for i, c in enumerate(capacity):
            if itemSize <= c < min_c:
                min_c = c
                ans = i
        return ans

    def gen(self):
        """
        生成测试样例，覆盖以下场景：
        1. 边界值测试（数组长度1、容量边界、itemSize边界）
        2. 无解情况（所有箱子都放不下）
        3. 多个相同最小容量的箱子（测试返回最小下标）
        4. 特殊结构（全相同、严格递增/递减、单元素满足等）
        5. 正常随机情况
        """
        capacity_list = []
        itemSize_list = []

        # 1. 边界值测试 - 约占20%
        # 最小数组长度
        capacity_list.append([1])
        itemSize_list.append(1)

        capacity_list.append([50])
        itemSize_list.append(50)

        capacity_list.append([100])
        itemSize_list.append(100)

        # 容量边界测试
        capacity_list.append([1, 100])
        itemSize_list.append(1)

        capacity_list.append([1, 100])
        itemSize_list.append(100)

        # itemSize边界测试
        capacity_list.append([50, 60, 70])
        itemSize_list.append(1)

        capacity_list.append([50, 60, 70])
        itemSize_list.append(100)

        capacity_list.append([50, 60, 70])
        itemSize_list.append(50)

        # 2. 无解情况 - 约占10%
        capacity_list.append([1, 2, 3])
        itemSize_list.append(100)

        capacity_list.append([10, 20, 30, 40])
        itemSize_list.append(50)

        capacity_list.append([5])
        itemSize_list.append(10)

        # 3. 多个相同最小容量 - 约占15%
        capacity_list.append([3, 5, 3, 7, 3])
        itemSize_list.append(3)

        capacity_list.append([10, 20, 10, 15, 10])
        itemSize_list.append(10)

        capacity_list.append([5, 10, 5, 20, 5, 5])
        itemSize_list.append(5)

        capacity_list.append([2, 5, 2, 3, 2])
        itemSize_list.append(2)

        capacity_list.append([100, 50, 100, 75, 100])
        itemSize_list.append(50)

        # 4. 特殊结构 - 约占20%
        # 全相同容量
        capacity_list.append([5, 5, 5, 5, 5])
        itemSize_list.append(5)

        capacity_list.append([10, 10, 10, 10])
        itemSize_list.append(10)

        # 严格递增
        capacity_list.append([1, 2, 3, 4, 5])
        itemSize_list.append(3)

        capacity_list.append([10, 20, 30, 40, 50])
        itemSize_list.append(25)

        # 严格递减
        capacity_list.append([5, 4, 3, 2, 1])
        itemSize_list.append(3)

        capacity_list.append([50, 40, 30, 20, 10])
        itemSize_list.append(30)

        # 只有一个能放下
        capacity_list.append([1, 2, 3, 4, 5])
        itemSize_list.append(5)

        capacity_list.append([1, 2, 3, 4, 5])
        itemSize_list.append(1)

        # 5. 正常随机情况 - 约占35%
        # 使用self提供的生成方法
        remaining_cases = self.testcase_num - len(capacity_list)

        # 随机生成剩余的测试用例
        for _ in range(remaining_cases):
            # 生成长度适中的随机数组，范围控制在1-50（避免过大）
            length = self.s_generate_int((1, 50))
            # 生成随机容量
            capacities = self.s_generate_list_int((length, length), (1, 100))
            # 生成随机itemSize
            item_size = self.s_generate_int((1, 100))

            capacity_list.append(capacities)
            itemSize_list.append(item_size)

        return capacity_list, itemSize_list
    


from . import Problem
from typing import List


class Solution2(Problem):
    date = "2026-3-8"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3862,
                         types=[],
                         pass_rate=0.22,
                         description='给你一个整数数组 `nums`。\n如果某个下标\xa0`i` 满足以下条件，则称其为**平衡下标**：\xa0`i` 左侧所有元素的总和等于 `i` 右侧所有元素的乘积。\n如果左侧没有元素，则总和视为 0。同样，如果右侧没有元素，则乘积视为 1。\n要求返回最小的**平衡下标**，如果不存在平衡下标，则返回 -1。\n\n**示例 1：**\n> \n**输入：**`nums = [2,1,2]`\n**输出：**`1`\n**解释：**\n对于下标\xa0`i = 1`：\n - 左侧总和 = `nums[0] = 2`\n - 右侧乘积 = `nums[2] = 2`\n - 由于左侧总和等于右侧乘积，下标 1 是平衡下标。\n\n没有更小的下标满足条件，因此答案是 1。\n**示例 2：**\n> \n**输入：**`nums = [2,8,2,2,5]`\n**输出：**`2`\n**解释：**\n对于下标\xa0`i = 2`：\n - 左侧总和 = `2 + 8 = 10`\n - 右侧乘积 = `2 * 5 = 10`\n - 由于左侧总和等于右侧乘积，下标\xa02 是平衡下标。\n\n没有更小的下标满足条件，因此答案是 2。\n**示例 3：**\n> \n**输入：**`nums = [1]`\n**输出：**`-1`\n对于下标\xa0`i = 0`：\n - 左侧为空，因此左侧总和为 0。\n - 右侧为空，因此右侧乘积为 1。\n - 由于左侧总和不等于右侧乘积，下标\xa00 不是平衡下标。\n\n因此，不存在平衡下标，答案是 -1。\n\n**提示：**\n - `1 <= nums.length <= 10^5`\n - `1 <= nums[i] <= 10^9`'
                         )

    def solve(self, nums: List[int]) -> int:
        pre = list(accumulate(nums, initial=0))
        mul = 1
        for i in range(len(nums) - 1, 0, -1):
            if pre[i] < mul:
                break
            if pre[i] == mul:
                return i
            mul *= nums[i]
        return -1

    def gen(self):
        """
        测试样例生成器，用于平衡下标问题
        覆盖场景：
        1. 边界情况：单元素、两元素
        2. 无平衡下标的情况
        3. 有平衡下标的情况（在不同位置）
        4. 特殊构造的测试用例
        """
        test_cases = []

        # ===== 边界情况 =====
        # 单元素数组（无平衡下标，左侧0 != 右侧1）
        test_cases.append([1])
        test_cases.append([2])

        # 两元素数组
        test_cases.append([1, 1])
        test_cases.append([2, 1])

        # ===== 无平衡下标的情况 =====
        test_cases.append([1, 1, 1])
        test_cases.append([1, 2, 3])
        test_cases.append([3, 7, 2])
        test_cases.append([2, 3, 7, 5])

        # ===== 有平衡下标的情况 =====
        # 平衡下标为1
        test_cases.append([2, 1, 2])
        test_cases.append([3, 1, 3])

        # 平衡下标为2
        test_cases.append([2, 8, 2, 2, 5])

        # 平衡下标为3
        test_cases.append([1, 1, 1, 1, 1])

        # ===== 更多特殊情况 =====
        test_cases.append([5, 1, 5])
        test_cases.append([1, 5, 2, 3])
        test_cases.append([10, 2, 5, 5, 2])

        # 不同长度的随机数组
        for length in [5, 8, 10, 15]:
            test_cases.append([random.randint(1, 5) for _ in range(length)])

        return (test_cases,)
    

import random
import string
from string import ascii_lowercase
from . import Problem
from itertools import pairwise
import re


class Solution3(Problem):
    date = "2026-3-8"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3863,
                         types=[],
                         pass_rate=0.26,
                         description='给你一个由小写英文字母组成的字符串 `s`。\n在一次操作中，你可以选择 `s` 的任意**子字符串**（但**不能**是整个字符串），并将其按**非降序字母顺序**进行**排序**。\n返回使 `s` 按**非降序**排列所需的**最小**操作次数。如果无法做到，则返回 -1。\n\n**示例 1：**\n> \n**输入：**`s = "dog"`\n**输出：**`1`\n**解释：**\n - 将子字符串 `"og"` 排序为 `"go"`。\n - 现在，`s = "dgo"`，已按升序排列。因此，答案是 1。\n\n**示例 2：**\n> \n**输入：**`s = "card"`\n**输出：**`2`\n**解释：**\n - 将子字符串 `"car"` 排序为 `"acr"`，得到 `s = "acrd"`。\n - 将子字符串 `"rd"` 排序为 `"dr"`，得到 `s = "acdr"`，已按升序排列。因此，答案是 2。\n\n**示例 3：**\n> \n**输入：**`s = "gf"`\n**输出：**`-1`\n**解释：**\n - 在给定提示下，无法对 `s` 进行排序。因此，答案是 -1。\n\n**提示：**\n - `1 <= s.length <= 10^5`\n - `s` 仅由小写英文字母组成。'
                         )

    def solve(self, s: str) -> int:
        if all((x <= y for x, y in pairwise(s))):
            return 0
        if len(s) == 2:
            return -1
        mn = min(s)
        mx = max(s)
        if s[0] == mn or s[-1] == mx:
            return 1
        if any((ch == mn or ch == mx for ch in s[1:-1])):
            return 2
        return 3

    def gen(self):
        # 根据经验，10^5级别的长度会导致超时，这里适当缩小到最大200
        # 生成策略：
        # 1. 10个长度为1-2的小字符串（边界值）
        # 2. 10个长度为3-5的短字符串（处理最小操作次数的各种情况）
        # 3. 20个长度为6-50的中等字符串
        # 4. 60个长度为51-200的长字符串

        random.seed(self.seed)
        test_cases = []

        # 阶段1: 边界值测试（1-2长度，覆盖返回0和-1的情况）
        # 生成5个长度为1的字符串（必定返回0）
        for _ in range(5):
            test_cases.append(self.s_generate_string(vocab=string.ascii_lowercase, length_range=(1, 1)))

        # 生成5个长度为2的字符串（可能返回0或-1）
        for _ in range(5):
            test_cases.append(self.s_generate_string(vocab=string.ascii_lowercase, length_range=(2, 2)))

        # 阶段2: 短字符串测试（3-5长度，覆盖各种操作次数）
        for _ in range(10):
            test_cases.append(self.s_generate_string(vocab=string.ascii_lowercase, length_range=(3, 5)))

        # 阶段3: 中等长度字符串（6-50长度）
        for _ in range(20):
            test_cases.append(self.s_generate_string(vocab=string.ascii_lowercase, length_range=(6, 50)))

        # 阶段4: 长字符串（51-200长度）
        for _ in range(60):
            test_cases.append(self.s_generate_string(vocab=string.ascii_lowercase, length_range=(51, 200)))

        return test_cases,
    

import string
from . import Problem
import re
from itertools import accumulate


class Solution4(Problem):
    date = "2026-3-8"
    def __init__(self):
        Problem.__init__(self,
                         degree=2,
                         idx=3864,
                         types=[],
                         pass_rate=0.55,
                         description='给你一个二进制字符串 `s` 和两个整数 `encCost` 与 `flatCost`。\n对于每个下标\xa0`i`，`s[i] = \'1\'` 表示第 `i`\xa0个元素是敏感的，而 `s[i] = \'0\'` 表示它不是敏感的。\n该字符串必须被划分为**分段**。最初，整个字符串形成一个单一的分段。\n对于一个长度为 `L` 且包含 `X` 个敏感元素的分段:\n - 如果 `X = 0`，费用为 `flatCost`。\n - 如果 `X > 0`，费用为 `L * X * encCost`。\n\n如果一个分段具有**偶数长度**，你可以将其拆分为两个长度**相等**的**连续分段**，此次拆分的费用是所得分段的**费用之和**。\n返回一个整数，表示所有有效划分中的**最小可能总费用**。\n\n**示例 1：**\n> \n**输入：**`s = "1010", encCost = 2, flatCost = 1`\n**输出：**`6`\n**解释：**\n - 整个字符串 `s = "1010"` 长度为 4，包含 2 个敏感元素，费用为 `4 * 2 * 2 = 16`。\n - 由于长度为偶数，它可以被拆分为 `"10"` 和 `"10"`。每个分段长度为 2 且包含 1 个敏感元素，因此每个分段的费用为 `2 * 1 * 2 = 4`，总计 8。\n - 将两个分段继续拆分为四个单字符分段，得到 `"1"`、`"0"`、`"1"` 和 `"0"`。包含 `"1"` 的分段长度为 1 且恰好有一个敏感元素，费用为 `1 * 1 * 2 = 2`；而包含 `"0"` 的分段没有敏感元素，因此费用为 `flatCost = 1`。\n - 因此总费用为 `2 + 1 + 2 + 1 = 6`，这是最小可能的总费用。\n\n**示例 2：**\n> \n**输入：**`s = "1010", encCost = 3, flatCost = 10`\n**输出：**`12`\n**解释：**\n - 整个字符串 `s = "1010"` 长度为 4，包含 2 个敏感元素，费用为 `4 * 2 * 3 = 24`。\n - 由于长度为偶数，它可以被拆分为两个分段 `"10"` 和 `"10"`。\n - 每个分段长度为 2 且包含一个敏感元素，因此每个分段费用为 `2 * 1 * 3 = 6`，总计 12，这是最小可能的总费用。\n\n**示例 3：**\n> \n**输入：**`s = "00", encCost = 1, flatCost = 2`\n**输出：**`2`\n**解释：**\n字符串 `s = "00"` 长度为 2 且不包含敏感元素，因此将其作为一个单一分段存储的费用为 `flatCost = 2`，这是最小可能的总费用。\n\n**提示：**\n - `1 <= s.length <= 10^5`\n - `s` 仅由 `\'0\'` 和 `\'1\'` 组成。\n - `1 <= encCost, flatCost <= 10^5`'
                         )

    def solve(self, s: str, encCost: int, flatCost: int) -> int:
        n = len(s)
        pre = list(accumulate(map(int, s), initial=0))

        def dfs(l: int, r: int) -> int:
            x = pre[r] - pre[l]
            res = (r - l) * x * encCost if x else flatCost
            if (r - l) % 2 == 0:
                m = (l + r) // 2
                res = min(res, dfs(l, m) + dfs(m, r))
            return res
        return dfs(0, n)

    def gen(self):
        """
        生成测试样例。

        覆盖场景：
        1. 边界值：最小长度(1)、长度为2、全0/全1、极小/极大的成本值
        2. 正常分布：随机字符串、随机成本值
        3. 特殊结构：交替0/1、连续相同字符、敏感元素集中
        """
        import random
        random.seed(self.seed)

        testcase_num = self.testcase_num
        strings = []
        enc_costs = []
        flat_costs = []

        # 辅助函数：生成固定长度的随机二进制字符串
        def generate_binary_string(length, prob_one=0.5):
            return ''.join('1' if random.random() < prob_one else '0' for _ in range(length))

        # 辅助函数：生成交替的0和1
        def generate_alternating_string(length):
            return ''.join('1' if i % 2 == 0 else '0' for i in range(length))

        # 辅助函数：生成敏感元素集中在两端的字符串
        def generate_concentrated_sensitive(length):
            half = length // 2
            # 前半段随机，后半段补0或补1
            first_half = generate_binary_string(half)
            second_half = '0' * (length - half)
            return first_half + second_half

        # 1. 边界测试 (30%)
        for i in range(30):
            if i < 10:
                # 最小长度1-5
                length = random.randint(1, 5)
                s = generate_binary_string(length)
            elif i < 20:
                # 长度为2的小偶数
                length = 2
                if i % 2 == 0:
                    s = "00"
                elif i % 4 == 1:
                    s = "11"
                elif i % 4 == 3:
                    s = "01"
                else:
                    s = "10"
            else:
                # 长度为3-5的小奇数
                length = random.randint(3, 5)
                s = generate_binary_string(length)

            encCost = random.randint(1, 5)
            flatCost = random.randint(1, 5)

            strings.append(s)
            enc_costs.append(encCost)
            flat_costs.append(flatCost)

        # 2. 随机正常测试 (50%)
        for i in range(50):
            length = random.randint(6, 100)
            s = generate_binary_string(length, random.random())
            encCost = random.randint(1, 50)
            flatCost = random.randint(1, 50)

            strings.append(s)
            enc_costs.append(encCost)
            flat_costs.append(flatCost)

        # 3. 特殊结构测试 (20%)
        for i in range(20):
            if i < 7:
                # 交替0和1的模式
                length = random.choice([4, 6, 8, 10, 12, 16, 20])
                s = generate_alternating_string(length)
            elif i < 14:
                # 全0或全1
                length = random.choice([2, 4, 8, 10, 16, 20, 32])
                s = '0' * length if i % 2 == 0 else '1' * length
            else:
                # 敏感元素集中的情况
                length = random.choice([8, 12, 16, 20, 24, 32])
                s = generate_concentrated_sensitive(length)

            # 特殊结构使用较大的成本值，测试决策逻辑
            encCost = random.randint(1, 100)
            flatCost = random.randint(1, 100)

            strings.append(s)
            enc_costs.append(encCost)
            flat_costs.append(flatCost)

        return strings, enc_costs, flat_costs
    

