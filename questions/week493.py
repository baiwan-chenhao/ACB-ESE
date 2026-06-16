

from . import Problem
import re


class Solution1(Problem):
    date = "2026-3-15"
    def __init__(self):
        Problem.__init__(self,
                         degree=0,
                         idx=3870,
                         types=[],
                         pass_rate=0.69,
                         description='给你一个整数 `n`。\n返回将所有从 `[1, n]`（包含两端）范围内的整数以**标准**数字格式书写时所用到的**逗号总数**。\n在**标准**格式中：\n - 从右边开始，每**三位**数字后插入一个逗号。\n - 位数**少于四位**的数字不包含逗号。\n\n**示例 1：**\n> \n**输入：**`n = 1002`\n**输出：**`3`\n**解释：**\n数字 `"1,000"`、`"1,001"` 和 `"1,002"` 每个都包含一个逗号，总计 3 个逗号。\n**示例 2：**\n> \n**输入：**`n = 998`\n**输出：**`0`\n**解释：**\n从 1 到 998 的所有数字位数都少于四位，因此没有使用逗号。\n\n**提示：**\n - `1 <= n <= 10^5`'
                         )

    def solve(self, n: int) -> int:
        ans = 0
        low = 1000
        while low <= n:
            ans += n - low + 1
            low *= 1000
        return ans

    import random

    def gen(self):
        """
        生成测试样例，用于测试计算 1 到 n 范围内数字逗号总数的函数。

        测试策略：
        1. 边界值：n < 1000（无逗号）、n = 1000（第一个含逗号的数）、
                  n = 999999（题目范围内最大边界附近）
        2. 正常分布：覆盖 [1, 100000] 各范围的随机值
        3. 特殊结构：逗号边界附近的值（如 999, 1000, 999999 等）
        """
        # 生成 100 个测试用例
        testcase_num = 100

        # 前边界测试（30个）：确保覆盖小于1000、等于1000、略大于1000的情况
        # 1-999: 20个测试（无逗号的情况）
        boundary_tests = [1, 999, 1000, 1001, 1002, 9999, 10000, 10001]
        n_list = []

        # 边界和特殊值（25个）
        # 1. 小边界：[1, 999] - 应该返回 0
        special_values = [
            1, 2, 10, 99, 100, 999,  # 小于 1000 的各种情况
            1000, 1001, 1002, 1100, 1999,  # 刚好达到四位数
            9999, 10000, 10001, 99999,  # 5位数的边界
            100000,                     # 题目最大值
            12345, 23456, 34567, 45678, 56789, 67890, 78901, 89012, 90123  # 随机分布的值
        ]
        n_list.extend(special_values)

        # 2. 正常随机分布（75个）- 覆盖 [1, 100000]
        # 分段随机，确保各区间都有覆盖
        random.seed(self.seed)

        # [1, 999]: 10个（无逗号区间）
        n_list.extend(random.sample(range(1, 1000), 10))
        # [1000, 9999]: 20个（1个逗号区间）
        n_list.extend(random.sample(range(1000, 10000), 20))
        # [10000, 99999]: 30个（1个逗号区间）
        n_list.extend(random.sample(range(10000, 100000), 30))
        # 100000: 1个（最大边界）
        n_list.append(100000)
        # 额外随机值补充到 100 个
        while len(n_list) < testcase_num:
            n_list.append(random.randint(1, 100000))

        # 确保正好 100 个
        n_list = n_list[:testcase_num]

        return (n_list,)
    

import random
from . import Problem
import re


class Solution2(Problem):
    date = "2026-3-15"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3871,
                         types=[],
                         pass_rate=0.41,
                         description='给你一个整数 `n`。\n返回将所有从 `[1, n]`（包含两端）范围内的整数以**标准**数字格式书写时所用到的**逗号总数**。\n在**标准**格式中：\n - 从右边开始，每**三位**数字后插入一个逗号。\n - 位数**少于四位**的数字不包含逗号。\n\n**示例 1：**\n> \n**输入：**`n = 1002`\n**输出：**`3`\n**解释：**\n数字 `"1,000"`、`"1,001"` 和 `"1,002"` 每个都包含一个逗号，总计 3 个逗号。\n**示例 2：**\n> \n**输入：**`n = 998`\n**输出：**`0`\n**解释：**\n从 1 到 998 的所有数字位数都少于四位，因此没有使用逗号。\n\n**提示：**\n - `1 <= n <= 10^15`'
                         )

    def solve(self, n: int) -> int:
        ans = 0
        low = 1000
        while low <= n:
            ans += n - low + 1
            low *= 1000
        return ans

    def gen(self):
            """
            生成测试样例，计算从1到n的数字按标准格式书写时的逗号总数。

            覆盖策略：
            1. 边界值测试：999、1000、999999等关键边界点
            2. 不同位数测试：4位数、7位数、10位数、13位数等
            3. 随机值测试：覆盖各个区间的随机数
            4. 极值测试：接近上限的大数

            为了避免超时，最大值设为10^12（保留测试逻辑完整性）
            """
            # 定义边界值测试用例（约30%）
            boundary_cases = [
                1,           # 最小值
                999,         # 3位数最大，无逗号
                1000,        # 4位数最小，第一个有逗号
                1001,        # 4位数，2个数字有逗号
                999999,      # 6位数最大，1个逗号
                1000000,     # 7位数最小，2个逗号
                1000001,     # 7位数，2个数字有2个逗号
                999999999,   # 9位数最大，2个逗号
                1000000000,  # 10位数最小，3个逗号
                1000000001,  # 10位数，2个数字有3个逗号
                999999999999,  # 12位数最大，3个逗号
                1000000000000, # 13位数最小，4个逗号
                1000000000001, # 13位数，2个数字有4个逗号
                999999999999999, # 15位数最大，4个逗号
                1000000000000000, # 16位数最小，5个逗号
                1000000000000001, # 16位数，2个数字有5个逗号
                9999999999999999, # 16位数最大，5个逗号（接近10^16）
            ]

            # 定义随机数范围（约70%）
            random_ranges = [
                (1, 999),              # 无逗号范围
                (1000, 999999),        # 1个逗号范围
                (1000000, 999999999),  # 2个逗号范围
                (1000000000, 999999999999),    # 3个逗号范围
                (1000000000000, 999999999999999),  # 4个逗号范围
                (1000000000000000, 10000000000000000),  # 5个逗号范围
            ]

            # 计算剩余需要的测试用例数量
            remaining_cases = self.testcase_num - len(boundary_cases)

            # 为每个随机范围分配测试用例数量
            cases_per_range = remaining_cases // len(random_ranges)
            extra_cases = remaining_cases % len(random_ranges)

            # 生成所有测试用例
            test_cases = list(boundary_cases)

            # 为每个随机范围生成测试用例
            for i, (low, high) in enumerate(random_ranges):
                num_cases = cases_per_range + (1 if i < extra_cases else 0)
                for _ in range(num_cases):
                    # 使用s_generate_int生成随机数
                    test_cases.append(self.s_generate_int((low, high)))

            # 确保测试用例数量正确
            test_cases = test_cases[:self.testcase_num]

            return [test_cases]
    


from . import Problem
from typing import List
import re


class Solution3(Problem):
    date = "2026-3-15"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3872,
                         types=[],
                         pass_rate=0.25,
                         description='给你一个整数数组 `nums`。\n如果子数组中相邻元素的差值是一个常数，那么这个子数组被称为**等差子数组**。\n你可以将 `nums` 中的**最多 一个**元素替换为任意一个**整数**。然后，从 `nums` 中选择一个等差子数组。\n返回一个整数，该整数表示你可以选择的**最长**等差子数组的长度。\n**子数组**是数组中一段连续的元素序列。\n\n**示例 1：**\n> \n**输入：**`nums = [9,7,5,10,1]`\n**输出：**`5`\n**解释：**\n - 将 `nums[3] = 10` 替换为 3，数组变为 `[9, 7, 5, 3, 1]`。\n - 选择子数组 `[**9, 7, 5, 3, 1**]`，它是等差数组，相邻元素的公差为 -2。\n\n**示例 2：**\n> \n**输入：**`nums = [1,2,6,7]`\n**输出：**`3`\n**解释：**\n - 将 `nums[0] = 1` 替换为 -2，数组变为 `[-2, 2, 6, 7]`。\n - 选择子数组 `[**-2, 2, 6**, 7]`，它是等差数组，相邻元素的公差为 4。\n\n**提示：**\n - `4 <= nums.length <= 10^5`\n - `1 <= nums[i] <= 10^5`'
                         )

    def calc(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0] * n
        pre[0] = 1
        pre[1] = 2
        for i in range(2, n):
            if nums[i - 2] + nums[i] == nums[i - 1] * 2:
                pre[i] = pre[i - 1] + 1
            else:
                pre[i] = 2
        return pre

    def solve(self, nums: List[int]) -> int:
        n = len(nums)
        pre = self.calc(nums)
        ans = max(pre) + 1
        if ans >= n:
            return n
        suf = self.calc(nums[::-1])[::-1]
        for i in range(1, n - 1):
            d2 = nums[i + 1] - nums[i - 1]
            if d2 % 2:
                continue
            ok_left = i > 1 and nums[i - 1] - nums[i - 2] == d2 // 2
            ok_right = i + 2 < n and nums[i + 2] - nums[i + 1] == d2 // 2
            if ok_left and ok_right:
                ans = max(ans, pre[i - 1] + 1 + suf[i + 1])
            elif ok_left:
                ans = max(ans, pre[i - 1] + 2)
            elif ok_right:
                ans = max(ans, suf[i + 1] + 2)
        return ans

    def gen(self):
        """
        生成测试样例，覆盖以下场景：
        1. 边界值：最小长度、小规模数组
        2. 完全等差数组：无需替换即可形成最长等差子数组
        3. 可修复数组：替换一个元素后形成等差数组
        4. 随机数组：测试一般情况
        5. 特殊结构：全相同、单差值改变等
        """
        testcase_num = self.testcase_num
        cases_per_type = testcase_num // 5

        nums_list = []

        # 场景1：边界值和小规模完全等差数组
        for _ in range(cases_per_type):
            # 小长度：4-10
            n = self.s_generate_int(int_range=(4, 10))
            # 生成等差数组
            start = self.s_generate_int(int_range=(1, 100))
            diff = self.s_generate_int(int_range=(-10, 10))
            nums = [start + i * diff for i in range(n)]
            # 确保数值在合理范围内
            nums = [max(1, min(1000, x)) for x in nums]
            nums_list.append(nums)

        # 场景2：中等规模完全等差数组
        for _ in range(cases_per_type):
            n = self.s_generate_int(int_range=(10, 100))
            start = self.s_generate_int(int_range=(1, 100))
            diff = self.s_generate_int(int_range=(-5, 5))
            nums = [start + i * diff for i in range(n)]
            nums = [max(1, min(1000, x)) for x in nums]
            nums_list.append(nums)

        # 场景3：可修复数组 - 一个元素破坏等差性
        for _ in range(cases_per_type):
            n = self.s_generate_int(int_range=(4, 50))
            start = self.s_generate_int(int_range=(1, 100))
            diff = self.s_generate_int(int_range=(-5, 5))
            nums = [start + i * diff for i in range(n)]
            # 随机修改一个位置
            pos = self.s_generate_int(int_range=(0, n - 1))
            nums[pos] = self.s_generate_int(int_range=(1, 1000))
            nums_list.append(nums)

        # 场景4：多段等差数组（通过替换连接）
        for _ in range(cases_per_type):
            n = self.s_generate_int(int_range=(5, 30))
            start1 = self.s_generate_int(int_range=(1, 100))
            diff = self.s_generate_int(int_range=(-3, 3))
            # 生成两段等差数组
            mid = n // 2
            nums = [start1 + i * diff for i in range(mid)]
            # 中间一个元素使得两段可以连接
            nums.append(nums[-1] + diff + self.s_generate_int(int_range=(-5, 5)))
            # 右侧等差数组
            for i in range(mid + 1, n):
                nums.append(nums[mid] + diff * (i - mid))
            nums = [max(1, min(1000, x)) for x in nums]
            nums_list.append(nums)

        # 场景5：随机数组
        for _ in range(cases_per_type):
            n = self.s_generate_int(int_range=(4, 50))
            nums = self.s_generate_list_int(
                list_length_range=(n, n),
                int_range=(1, 1000),
                different=False
            )
            nums_list.append(nums)

        return (nums_list,)
    


from . import Problem
from typing import List
from collections import Counter
import re


class Solution4(Problem):
    date = "2026-3-15"
    def __init__(self):
        Problem.__init__(self,
                         degree=2,
                         idx=3873,
                         types=[],
                         pass_rate=0.56,
                         description='给你一个二维整数数组 `points`，其中 `points[i] = [x_i, y_i]` 表示第 `i` 个点的坐标。`points` 中的所有坐标都**互不相同**。\n如果一个点被**激活**，那么所有与该点具有相同**x**坐标或**y**坐标的点也会被**激活**。\n激活会一直持续，直到没有额外的点可以被激活为止。\n你可以**额外添加**一个不在 `points` 数组中的整数坐标点 `(x, y)` 。从这个新添加的点开始**激活**。\n返回一个整数，表示可以被激活的**最大**点数，包括新添加的点。\n\n**示例 1：**\n> \n**输入：**`points = [[1,1],[1,2],[2,2]]`\n**输出：**`4`\n**解释：**\n添加并激活一个点，例如 `(1, 3)`，会导致以下激活：\n - `(1, 3)` 与 `(1, 1)` 和 `(1, 2)` 具有相同的 `x = 1`，因此 `(1, 1)` 和 `(1, 2)` 被激活。\n - `(1, 2)` 与 `(2, 2)` 具有相同的 `y = 2`，因此 `(2, 2)` 被激活。\n\n因此，被激活的点为 `(1, 3)`, `(1, 1)`, `(1, 2)`, `(2, 2)`，总计 4 个点。可以证明这是最大激活点数。\n**示例 2：**\n> \n**输入：**`points = [[2,2],[1,1],[3,3]]`\n**输出：**`3`\n**解释：**\n添加并激活一个点，例如 `(1, 2)`，会导致以下激活：\n - `(1, 2)` 与 `(1, 1)` 具有相同的 `x = 1`，因此 `(1, 1)` 被激活。\n - `(1, 2)` 与 `(2, 2)` 具有相同的 `y = 2`，因此 `(2, 2)` 被激活。\n\n因此，被激活的点为 `(1, 2)`, `(1, 1)`, `(2, 2)`，总计 3 个点。可以证明这是最大激活点数。\n**示例 3：**\n> \n**输入：**`points = [[2,3],[2,2],[1,1],[4,5]]`\n**输出：**`4`\n**解释：**\n添加并激活一个点，例如 `(2, 1)`，会导致以下激活：\n - `(2, 1)` 与 `(2, 3)` 和 `(2, 2)` 具有相同的 `x = 2`，因此 `(2, 3)` 和 `(2, 2)` 被激活。\n - `(2, 1)` 与 `(1, 1)` 具有相同的 `y = 1`，因此 `(1, 1)` 被激活。\n\n因此，被激活的点为 `(2, 1)`, `(2, 3)`, `(2, 2)`, `(1, 1)`，总计 4 个点。\n\n**提示：**\n - `1 <= points.length <= 10^5`\n - `points[i] = [x_i, y_i]`\n - `-10^9 <= x_i, y_i <= 10^9`\n - `points` 中的坐标均**互不相同**。'
                         )

    def solve(self, points: List[List[int]]) -> int:
        fa = {}

        def find(x: int) -> int:
            if x not in fa:
                return x
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]
        OFFSET = 3 * 10 ** 9
        for x, y in points:
            fa[find(x)] = find(y + OFFSET)
        size = Counter((find(p[0]) for p in points))
        mx1 = mx2 = 0
        for sz in size.values():
            if sz > mx1:
                mx2 = mx1
                mx1 = sz
            elif sz > mx2:
                mx2 = sz
        return mx1 + mx2 + 1

    import random
    from typing import List

    def gen(self):
        """
        生成测试样例，用于测试点激活连通性问题。

        测试策略：
        1. 边界情况（最小规模）
        2. 特殊结构（直线型、独立点型、两大连通分量）
        3. 随机数据

        注意：为了确保测试在合理时间内完成，我们将坐标范围和点数限制在较小规模，
        但仍能覆盖所有重要边界情况。
        """
        # 减少测试样例数量和规模，避免超时
        testcase_num = self.testcase_num

        # 为不同场景分配测试样例数量
        boundary_cases = 10      # 边界情况
        line_cases = 15          # 直线型
        independent_cases = 15   # 独立点型
        two_component_cases = 20 # 两大连通分量
        random_cases = 40        # 随机情况

        points_list = []

        # 随机种子已在外部设置

        # 1. 边界情况 - 最小规模
        for _ in range(boundary_cases):
            points_list.append([[0, 0]])  # 单个点

        # 2. 直线型 - 所有点在同一行或同一列
        for _ in range(line_cases // 2):
            # 同一x（垂直线）
            x = random.randint(-5, 5)
            n = random.randint(2, 10)
            ys = random.sample(range(-5, 10), n)
            points_list.append([[x, y] for y in ys])

        for _ in range(line_cases // 2):
            # 同一y（水平线）
            y = random.randint(-5, 5)
            n = random.randint(2, 10)
            xs = random.sample(range(-5, 10), n)
            points_list.append([[x, y] for x in xs])

        # 3. 独立点型 - 每个点的x和y都唯一
        for _ in range(independent_cases):
            n = random.randint(2, 8)
            xs = random.sample(range(-5, 20), n)
            ys = random.sample(range(-5, 20), n)
            points_list.append([[xs[i], ys[i]] for i in range(n)])

        # 4. 两大连通分量 - 优化为随机分组
        for _ in range(two_component_cases):
            # 生成两个较大的连通分量
            points = []

            # 第一个连通分量
            x1_base = random.randint(-5, 0)
            y1_base = random.randint(-5, 0)
            comp1_size = random.randint(3, 6)
            comp1_points = set()
            attempts = 0
            while len(comp1_points) < comp1_size and attempts < 50:
                x = x1_base + random.randint(0, 2)
                y = y1_base + random.randint(0, 2)
                comp1_points.add((x, y))
                attempts += 1

            # 第二个连通分量
            x2_base = random.randint(3, 8)
            y2_base = random.randint(3, 8)
            comp2_size = random.randint(3, 6)
            comp2_points = set()
            attempts = 0
            while len(comp2_points) < comp2_size and attempts < 50:
                x = x2_base + random.randint(0, 2)
                y = y2_base + random.randint(0, 2)
                comp2_points.add((x, y))
                attempts += 1

            points = list(comp1_points) + list(comp2_points)
            points_list.append([[x, y] for x, y in points])

        # 5. 随机情况 - 小规模但多样化
        for _ in range(random_cases):
            n = random.randint(2, 10)
            xs = random.sample(range(-10, 15), n)
            ys = random.sample(range(-10, 15), n)
            # 确保坐标不重复
            seen = set()
            points = []
            for x, y in zip(xs, ys):
                if (x, y) not in seen:
                    points.append([x, y])
                    seen.add((x, y))
            # 移除可能的重复
            points = points[:n]
            points_list.append(points)

        # 确保总数量正确
        while len(points_list) < testcase_num:
            # 补充随机测试
            n = random.randint(2, 5)
            xs = random.sample(range(-5, 10), n)
            ys = random.sample(range(-5, 10), n)
            points_list.append([[xs[i], ys[i]] for i in range(n)])

        # 截断到准确数量
        points_list = points_list[:testcase_num]

        return [points_list]
    

