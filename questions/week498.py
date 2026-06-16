

from . import Problem
from functools import cache
import re


class Solution1(Problem):
    date = "2026-4-19"
    def __init__(self):
        Problem.__init__(self,
                         degree=0,
                         idx=3903,
                         types=[],
                         pass_rate=0.68,
                         description='给你一个长度为 `n` 的整数数组 `nums` 和一个整数 `k`。\n对于每个下标 `i`，定义它的**不稳定值**为 `max(nums[0..i]) - min(nums[i..n - 1])`。\n换句话说：\n - `max(nums[0..i])` 表示从下标 0 到下标 `i` 的元素中的**最大值**。\n - `min(nums[i..n - 1])` 表示从下标 `i` 到下标 `n - 1` 的元素中的**最小值**。\n\n如果某个下标 `i` 的不稳定值**小于等于**`k`，则称该下标为**稳定下标**。\n返回**最小**的稳定下标。如果不存在这样的下标，则返回 `-1`。\n\n**示例 1：**\n> \n**输入：**`nums = [5,0,1,4], k = 3`\n**输出：**`3`\n**解释：**\n - 在下标 0 处：`[5]` 中的最大值是 5，`[5, 0, 1, 4]` 中的最小值是 0，因此不稳定值为 `5 - 0 = 5`。\n - 在下标 1 处：`[5, 0]` 中的最大值是 5，`[0, 1, 4]` 中的最小值是 0，因此不稳定值为 `5 - 0 = 5`。\n - 在下标 2 处：`[5, 0, 1]` 中的最大值是 5，`[1, 4]` 中的最小值是 1，因此不稳定值为 `5 - 1 = 4`。\n - 在下标 3 处：`[5, 0, 1, 4]` 中的最大值是 5，`[4]` 中的最小值是 4，因此不稳定值为 `5 - 4 = 1`。\n - 这是第一个不稳定值小于等于 `k = 3` 的下标，因此答案是 3。\n\n**示例 2：**\n> \n**输入：**`nums = [3,2,1], k = 1`\n**输出：**`-1`\n**解释：**\n - 在下标 0 处，不稳定值为 `3 - 1 = 2`。\n - 在下标 1 处，不稳定值为 `3 - 1 = 2`。\n - 在下标 2 处，不稳定值为 `3 - 1 = 2`。\n - 这些值都不小于等于 `k = 1`，因此答案是 `-1`。\n\n**示例 3：**\n> \n**输入：**`nums = [0], k = 0`\n**输出：**`0`\n**解释：**\n在下标 0 处，不稳定值为 `0 - 0 = 0`，它小于等于 `k = 0`。因此答案是 0。\n\n**提示：**\n - `1 <= nums.length <= 100`\n - `0 <= nums[i] <= 10^9`\n - `0 <= k <= 10^9`'
                         )

    def solve(self, nums: list[int], k: int) -> int:
        n = len(nums)

        @cache
        def pre(i):
            if i == 0:
                return nums[i]
            return max(nums[i], pre(i - 1))

        @cache
        def suf(i):
            if i == n - 1:
                return nums[i]
            return min(nums[i], suf(i + 1))
        for i in range(n):
            if pre(i) - suf(i) <= k:
                return i
        return -1

    def gen(self):
        """生成测试样例，覆盖边界情况、正常分布和特殊结构。

        测试策略：
        1. 边界情况（25%）：极小数组、极值k、单调数列
        2. 正常分布（50%）：随机数组和随机k
        3. 特殊结构（25%）：全相同元素、严格递增/递减、V形/A形

        参数范围调整为：
        - 数组长度：1-100（符合约束）
        - nums[i]：0-10000（缩小约束中的10^9，避免过大）
        - k：0-10000（缩小约束中的10^9）
        """
        testcase_num = self.testcase_num

        # 分配测试样例：边界情况 25%，正常分布 50%，特殊结构 25%
        boundary_cases = testcase_num // 4
        normal_cases = testcase_num // 2
        special_cases = testcase_num - boundary_cases - normal_cases

        nums_list = []
        k_list = []

        # 边界情况生成 (25%)
        for i in range(boundary_cases):
            if i % 4 == 0:
                # 长度为1的数组（最小长度）
                nums = [self.s_generate_int(int_range=(0, 100))]
            elif i % 4 == 1:
                # 长度为100的数组（最大长度），k为0（最小值）
                nums = self.s_generate_list_int(list_length_range=(100, 100), int_range=(0, 1000))
            elif i % 4 == 2:
                # 严格递增数组
                length = self.s_generate_int(int_range=(5, 20))
                start = self.s_generate_int(int_range=(0, 100))
                nums = list(range(start, start + length))
            else:
                # 严格递减数组
                length = self.s_generate_int(int_range=(5, 20))
                start = self.s_generate_int(int_range=(50, 150))
                nums = list(range(start, start - length, -1))

            # k取边界值：0、小值、大值
            if i % 3 == 0:
                k = 0
            elif i % 3 == 1:
                k = self.s_generate_int(int_range=(0, 100))
            else:
                k = self.s_generate_int(int_range=(1000, 10000))

            nums_list.append(nums)
            k_list.append(k)

        # 正常分布情况：随机数组和随机k (50%)
        for _ in range(normal_cases):
            length = self.s_generate_int(int_range=(2, 50))
            nums = self.s_generate_list_int(list_length_range=(length, length), int_range=(0, 10000))
            k = self.s_generate_int(int_range=(0, 10000))

            nums_list.append(nums)
            k_list.append(k)

        # 特殊结构情况 (25%)
        for i in range(special_cases):
            if i % 5 == 0:
                # 所有元素相同（不稳定值始终为0）
                length = self.s_generate_int(int_range=(2, 30))
                val = self.s_generate_int(int_range=(0, 100))
                nums = [val] * length
            elif i % 5 == 1:
                # 单调递增（可能有重复，可能没有稳定下标）
                length = self.s_generate_int(int_range=(5, 30))
                nums = sorted(self.s_generate_list_int(list_length_range=(length, length), int_range=(0, 1000)))
            elif i % 5 == 2:
                # 单调递减（可能有重复，可能没有稳定下标）
                length = self.s_generate_int(int_range=(5, 30))
                nums = sorted(self.s_generate_list_int(list_length_range=(length, length), int_range=(0, 1000)), reverse=True)
            elif i % 5 == 3:
                # V形：先减后增（极值在中间）
                length = self.s_generate_int(int_range=(7, 30))
                half = length // 2
                left = sorted(self.s_generate_list_int(list_length_range=(half + 1, half + 1), int_range=(0, 500)), reverse=True)
                right = sorted(self.s_generate_list_int(list_length_range=(length - half - 1, length - half - 1), int_range=(100, 800)))
                nums = left + right
            else:
                # A形：先增后减（极值在中间）
                length = self.s_generate_int(int_range=(7, 30))
                half = length // 2
                left = sorted(self.s_generate_list_int(list_length_range=(half + 1, half + 1), int_range=(0, 500)))
                right = sorted(self.s_generate_list_int(list_length_range=(length - half - 1, length - half - 1), int_range=(100, 800)), reverse=True)
                nums = left + right

            # k取适中值
            k = self.s_generate_int(int_range=(0, 5000))

            nums_list.append(nums)
            k_list.append(k)

        return nums_list, k_list
    


from . import Problem
import re


class Solution2(Problem):
    date = "2026-4-19"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3904,
                         types=[],
                         pass_rate=0.73,
                         description='给你一个长度为 `n` 的整数数组 `nums` 和一个整数 `k`。\n对于每个下标 `i`，定义它的**不稳定值**为 `max(nums[0..i]) - min(nums[i..n - 1])`。\n换句话说：\n - `max(nums[0..i])` 表示从下标 0 到下标 `i` 的元素中的**最大值**。\n - `min(nums[i..n - 1])` 表示从下标 `i` 到下标 `n - 1` 的元素中的**最小值**。\n\n如果某个下标 `i` 的不稳定值**小于等于**`k`，则称该下标为**稳定下标**。\n返回**最小**的稳定下标。如果不存在这样的下标，则返回 `-1`。\n\n**示例 1：**\n> \n**输入：**`nums = [5,0,1,4], k = 3`\n**输出：**`3`\n**解释：**\n - 在下标 0 处：`[5]` 中的最大值是 5，`[5, 0, 1, 4]` 中的最小值是 0，因此不稳定值为 `5 - 0 = 5`。\n - 在下标 1 处：`[5, 0]` 中的最大值是 5，`[0, 1, 4]` 中的最小值是 0，因此不稳定值为 `5 - 0 = 5`。\n - 在下标 2 处：`[5, 0, 1]` 中的最大值是 5，`[1, 4]` 中的最小值是 1，因此不稳定值为 `5 - 1 = 4`。\n - 在下标 3 处：`[5, 0, 1, 4]` 中的最大值是 5，`[4]` 中的最小值是 4，因此不稳定值为 `5 - 4 = 1`。\n - 这是第一个不稳定值小于等于 `k = 3` 的下标，因此答案是 3。\n\n**示例 2：**\n> \n**输入：**`nums = [3,2,1], k = 1`\n**输出：**`-1`\n**解释：**\n - 在下标 0 处，不稳定值为 `3 - 1 = 2`。\n - 在下标 1 处，不稳定值为 `3 - 1 = 2`。\n - 在下标 2 处，不稳定值为 `3 - 1 = 2`。\n - 这些值都不小于等于 `k = 1`，因此答案是 `-1`。\n\n**示例 3：**\n> \n**输入：**`nums = [0], k = 0`\n**输出：**`0`\n**解释：**\n在下标 0 处，不稳定值为 `0 - 0 = 0`，它小于等于 `k = 0`。因此答案是 0。\n\n**提示：**\n - `1 <= nums.length <= 10^5`\n - `0 <= nums[i] <= 10^9`\n - `0 <= k <= 10^9`'
                         )

    def solve(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suf_min = [0] * n
        suf_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf_min[i] = min(suf_min[i + 1], nums[i])
        pre_max = 0
        for i, x in enumerate(nums):
            pre_max = max(pre_max, x)
            if pre_max - suf_min[i] <= k:
                return i
        return -1

    def gen(self):
        """
        生成测试样例，覆盖各种场景

        覆盖场景：
        1. 边界值：最小长度、全0元素、k=0/k=max
        2. 特殊结构：全相同、严格递增/递减、峰值在中间
        3. 结果位置：答案在开头/结尾/中间/无答案
        4. 正常随机情况
        """
        import random
        random.seed(self.seed)

        test_cases = []
        num_cases = self.testcase_num

        # 分配不同场景的测试用例数量
        case_types = {
            'min_length': 5,          # 最小长度
            'all_same': 5,            # 全相同元素
            'strict_increasing': 5,   # 严格递增
            'strict_decreasing': 5,   # 严格递减
            'answer_at_start': 10,    # 答案在开头
            'answer_at_end': 10,      # 答案在结尾
            'no_answer': 10,          # 无答案
            'normal': 50              # 正常随机
        }

        def add_case(nums, k, desc):
            """添加一个测试用例"""
            test_cases.append((nums, k, desc))

        # 1. 最小长度测试
        add_case([0], 0, "min_length_single_zero")
        add_case([5], 5, "min_length_k_equal")
        add_case([10], 5, "min_length_k_less")
        add_case([100], 200, "min_length_k_large")
        add_case([1], 0, "min_length_k_zero")

        # 2. 全相同元素
        n = 100
        add_case([0] * n, 0, "all_same_zero")
        add_case([5] * n, 0, "all_same_positive_k_zero")
        add_case([100] * n, 0, "all_same_large_k_zero")
        add_case([50] * n, 100, "all_same_k_positive")
        add_case([10] * n, 5, "all_same_k_positive_2")

        # 3. 严格递增
        add_case(list(range(10)), 9, "increasing_small")
        add_case(list(range(100)), 99, "increasing_medium")
        add_case(list(range(500)), 499, "increasing_large")
        add_case([i * 10 for i in range(50)], 490, "increasing_scaled")
        add_case([i * 100 for i in range(30)], 2900, "increasing_larger_step")

        # 4. 严格递减
        add_case(list(range(10, 0, -1)), 0, "decreasing_small")
        add_case(list(range(100, 0, -1)), 0, "decreasing_medium")
        add_case(list(range(500, 0, -1)), 0, "decreasing_large")
        add_case([i * 10 for i in range(50, 0, -1)], 0, "decreasing_scaled")
        add_case([100 - i for i in range(100)], 0, "decreasing_simple")

        # 5. 答案在开头
        add_case([1, 2, 3, 4, 5], 0, "answer_start_increasing")
        add_case([5, 5, 5, 5, 5], 0, "answer_start_constant")
        add_case([10] + [i * 10 for i in range(1, 20)], 0, "answer_start_large_first")
        add_case([100, 200, 300, 400], 0, "answer_start_increasing_2")
        add_case([50, 50, 100, 100], 0, "answer_start_prefix_constant")
        add_case([1] + list(range(1, 50)), 0, "answer_start_small_first")
        add_case([0, 100, 200, 300], 0, "answer_start_zero_first")
        add_case([10, 20, 30, 40], 10, "answer_start_k_positive")
        add_case([5, 10, 15, 20], 5, "answer_start_k_equal_diff")
        add_case([100, 200, 300, 400, 500], 100, "answer_start_large_k")

        # 6. 答案在结尾
        add_case([5, 4, 3, 2, 1], 0, "answer_end_decreasing")
        add_case([5, 5, 5, 5, 5], 0, "answer_end_constant")
        add_case([i * 10 for i in range(20, 0, -1)] + [10], 0, "answer_end_large_last")
        add_case([400, 300, 200, 100], 0, "answer_end_decreasing_2")
        add_case([100, 100, 50, 50], 0, "answer_end_suffix_constant")
        add_case(list(range(50, 0, -1)) + [0], 0, "answer_end_small_last")
        add_case([300, 200, 100, 0], 0, "answer_end_zero_last")
        add_case([40, 30, 20, 10], 10, "answer_end_k_positive")
        add_case([20, 15, 10, 5], 5, "answer_end_k_equal_diff")
        add_case([500, 400, 300, 200, 100], 100, "answer_end_large_k")

        # 7. 无答案情况
        add_case([100, 1, 1, 1], 0, "no_answer_large_first")
        add_case([10, 1, 2, 3], 0, "no_answer_diff_small")
        add_case([1000, 100, 10, 1], 0, "no_answer_big_diff")
        add_case([50, 10, 20, 30], 0, "no_answer_uneven")
        add_case([100, 50, 25, 12], 0, "no_answer_decreasing_but_not_enough")
        add_case([100, 10, 20, 30, 40], 5, "no_answer_small_k")
        add_case([500, 100, 200, 300], 50, "no_answer_medium_k")
        add_case([100, 10, 15, 20], 8, "no_answer_very_small_k")
        add_case([1000, 10, 20, 30], 90, "no_answer_small_relative_k")
        add_case([100, 1, 2, 3, 4, 5], 5, "no_answer_incremental")

        # 8. 正常随机情况
        for i in range(50):
            # 随机长度（适当控制规模）
            length = random.randint(10, 500)
            # 随机生成数组
            nums = [random.randint(0, 1000) for _ in range(length)]
            # 随机k值
            k = random.randint(0, 500)
            add_case(nums, k, f"normal_random_{i}")

        # 确保有足够的测试用例
        while len(test_cases) < num_cases:
            length = random.randint(10, 500)
            nums = [random.randint(0, 1000) for _ in range(length)]
            k = random.randint(0, 500)
            add_case(nums, k, f"extra_random_{len(test_cases)}")

        # 截取到需要的数量
        test_cases = test_cases[:num_cases]

        # 转换为gen格式：返回元组，每个元素对应一个参数的所有测试用例
        nums_list = [case[0] for case in test_cases]
        k_list = [case[1] for case in test_cases]

        return nums_list, k_list
    

from typing import List
from typing import Tuple
from . import Problem
from collections import deque
import re


class Solution3(Problem):
    date = "2026-4-19"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3905,
                         types=[],
                         pass_rate=0.54,
                         description='给你两个整数 `n` 和 `m`，分别表示一个网格的行数和列数。\n同时给你一个二维整数数组 `sources`，其中 `sources[i] = [r_i, c_i, color_i]` 表示单元格 `(r_i, c_i)` 初始被涂上颜色 `color_i`。所有其他单元格初始均未着色，用 0 表示。\n在每一单位时间中，所有当前已着色的单元格都会将其颜色向上下左右四个方向扩散到所有相邻的**未着色**单元格。所有扩散同时发生。\n如果**多个**颜色在同一时间步到达同一个未着色单元格，该单元格将采用具有**最大**值的颜色。\n这个过程持续进行，直到没有更多的单元格可以被着色。\n返回一个二维整数数组，表示网格的最终状态，其中每个单元格包含其最终的颜色。\n\n**示例 1：**\n> \n**输入：**`n = 3, m = 3, sources = [[0,0,1],[2,2,2]]`\n**输出：**`[[1,1,2],[1,2,2],[2,2,2]]`\n**解释：**\n每个时间步的网格如下：\n\n在时间步 2，单元格 `(0, 2)`，`(1, 1)` 和 `(2, 0)` 同时被两种颜色到达，因此它们被分配颜色 2，因为它是其中的最大值。\n**示例 2：**\n> \n**输入：**`n = 3, m = 3, sources = [[0,1,3],[1,1,5]]`\n**输出：**`[[3,3,3],[5,5,5],[5,5,5]]`\n**解释：**\n每个时间步的网格如下：\n\n**示例 3：**\n> \n**输入：**`n = 2, m = 2, sources = [[1,1,5]]`\n**输出：**`[[5,5],[5,5]]`\n**解释：**\n每个时间步的网格如下：\n\u200b\u200b\u200b\u200b\u200b\u200b\u200b\n由于只有一个源，所有单元格都被分配相同的颜色。\n\n**提示：**\n - `1 <= n, m <= 10^5`\n - `1 <= n * m <= 10^5`\n - `1 <= sources.length <= n * m`\n - `sources[i] = [r_i, c_i, color_i]`\n - `0 <= r_i <= n - 1`\n - `0 <= c_i <= m - 1`\n - `1 <= color_i <= 10^6\u200b\u200b\u200b\u200b\u200b\u200b\u200b`\n - `sources` 中的所有 `(r_i, c_i\u200b\u200b\u200b\u200b\u200b\u200b\u200b)` 互不相同。'
                         )

    def solve(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        ans = [[0] * m for _ in range(n)]
        for x, y, c in sources:
            ans[x][y] = c
        sources.sort(key=lambda s: -s[2])
        q = deque(sources)
        while q:
            i, j, c = q.popleft()
            for x, y in ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)):
                if 0 <= x < n and 0 <= y < m and (ans[x][y] == 0):
                    ans[x][y] = c
                    q.append((x, y, c))
        return ans

    def _gen(self):
        """
        生成网格颜色扩散问题的测试样例。

        覆盖场景：
        1. 边界情况：最小网格(1x1)、1D网格(1xn或nx1)、单源、全源
        2. 颜色冲突：多个源同时扩散、颜色值大小关系测试
        3. 特殊结构：棋盘状源、对角线源
        4. 正常分布：中等规模随机测试

        测试样例分布（共30个）：
        - 5个边界情况测试
        - 5个颜色冲突测试
        - 5个特殊结构测试
        - 15个随机测试

        Yields:
            Tuple[int, int, List[List[int]]]: (n, m, sources) 测试用例
        """
        import random
        random.seed(self.seed)

        # === 边界测试（5个） ===
        # 1. 最小网格 1x1
        yield (1, 1, [[0, 0, 1]])

        # 2. 1xN 网格，单源
        yield (1, 10, [[0, 0, 1]])

        # 3. Nx1 网格，单源
        yield (10, 1, [[0, 0, 1]])

        # 4. 最小网格但多源冲突
        yield (2, 2, [[0, 0, 1], [1, 1, 2]])

        # 5. 全源（所有格子都是源）
        n, m = 3, 3
        sources = []
        colors = list(range(1, 10))
        random.shuffle(colors)
        for i in range(n):
            for j in range(m):
                sources.append([i, j, colors[i * m + j]])
        yield (n, m, sources)

        # === 颜色冲突测试（5个） ===
        # 6. 两个源从对角扩散，边界冲突
        yield (5, 5, [[0, 0, 1], [4, 4, 10]])

        # 7. 多个源同时扩散
        yield (4, 4, [[0, 0, 1], [0, 3, 2], [3, 0, 3], [3, 3, 4]])

        # 8. 颜色值差异大
        yield (3, 10, [[0, 0, 1], [2, 9, 1000000]])

        # 9. 相邻源，颜色值不同
        yield (3, 3, [[0, 1, 1], [1, 0, 100], [1, 2, 50], [2, 1, 10]])

        # 10. 稠密源测试
        n, m = 4, 4
        sources = [[0, 0, 1], [0, 3, 2], [3, 0, 3], [3, 3, 4], [1, 1, 5]]
        yield (n, m, sources)

        # === 特殊结构测试（5个） ===
        # 11. 棋盘状源
        n, m = 4, 4
        sources = []
        for i in range(n):
            for j in range(m):
                if (i + j) % 2 == 0:
                    sources.append([i, j, 10 + i])
        yield (n, m, sources)

        # 12. 对角线源
        n, m = 5, 5
        sources = [[i, i, i + 1] for i in range(min(n, m))]
        yield (n, m, sources)

        # 13. 单行多源
        n, m = 1, 20
        sources = [[0, 0, 1], [0, 10, 5], [0, 19, 3]]
        yield (n, m, sources)

        # 14. 单列多源
        n, m = 20, 1
        sources = [[0, 0, 1], [10, 0, 5], [19, 0, 3]]
        yield (n, m, sources)

        # 15. 环形源
        n, m = 5, 5
        sources = [[0, 0, 1], [0, 4, 2], [4, 0, 3], [4, 4, 4]]
        yield (n, m, sources)

        # === 随机测试（15个） ===
        # 控制网格大小，n*m <= 10000
        for _ in range(15):
            # 随机生成网格大小，限制总单元格数
            max_cells = random.randint(10, 5000)

            # 随机分配行数和列数
            n = random.randint(1, min(100, max_cells))
            m = max_cells // n
            if m == 0:
                m = 1

            # 确保不超过最大限制
            if n * m > 10000:
                m = 10000 // n
            if m == 0:
                m = 1

            # 随机生成sources数量
            max_sources = min(20, n * m)
            num_sources = random.randint(1, max_sources)

            # 生成不同的位置
            all_positions = [(i, j) for i in range(n) for j in range(m)]
            selected_positions = random.sample(all_positions, num_sources)

            # 生成sources
            sources = []
            for (r, c) in selected_positions:
                color = random.randint(1, 1000)
                sources.append([r, c, color])

            yield (n, m, sources)

    def gen(self):
        """
        返回按参数维度组织的测试数据：
        - 返回元组 (n_list, m_list, sources_list)
        - 每个列表包含30个测试用例的对应参数值
        """
        import random
        random.seed(self.seed)

        rets = [[], [], []]

        for n, m, sources in self._gen():
            rets[0].append(n)
            rets[1].append(m)
            rets[2].append(sources)

        return rets
    

import random
from . import Problem
from functools import cache
import re


class Solution4(Problem):
    date = "2026-4-19"
    def __init__(self):
        Problem.__init__(self,
                         degree=2,
                         idx=3906,
                         types=[],
                         pass_rate=0.57,
                         description='给你两个整数 `l` 和 `r`，以及一个由**恰好**三个 `\'D\'` 字符和三个 `\'R\'` 字符组成的字符串 `directions`。\n对于范围 `[l, r]`（包含边界）内的每个整数 `x`，执行以下步骤：\n - 如果 `x` 的位数少于 16 位，请在其左侧填充**前导零**，使其成为 16 位的字符串。\n - 将这 16 个数字以**行优先**的顺序放入一个 `4 × 4` 的网格中（前 4 个数字从左到右构成第一行，接下来的 4 个数字构成第二行，依此类推）。\n - 从**左上角**单元格（`row = 0`，`column = 0`）开始，按顺序应用 `directions` 中的 6 个字符：\n\t - `\'D\'` 使行数加 1。\n - `\'R\'` 使列数加 1。\n\n - 记录沿路径访问的数字序列（包括起始单元格），生成一个长度为 7 的序列。\n\n如果记录的序列是**非递减**的，则认为整数 `x` 是一个**好**整数。\n返回一个整数，表示在范围 `[l, r]` 内好整数的数量。\n\n**示例 1：**\n> \n**输入：**`l = 8, r = 10, directions = "DDDRRR"`\n**输出：**`2`\n**解释：**\n`x = 8` 的网格：\n| 0 | 0 | 0 | 0 |\n| 0 | 0 | 0 | 0 |\n| 0 | 0 | 0 | 0 |\n| 0 | 0 | 0 | 8 |\n - 路径：`(0,0) → (1,0) → (2,0) → (3,0) → (3,1) → (3,2) → (3,3)`\n - 访问的数字序列为 `[0, 0, 0, 0, 0, 0, 8]`。\n - 由于访问的数字序列是非递减的，因此 8 是一个好整数。\n\n`x = 9` 的网格：\n| 0 | 0 | 0 | 0 |\n| 0 | 0 | 0 | 0 |\n| 0 | 0 | 0 | 0 |\n| 0 | 0 | 0 | 9 |\n - 访问的数字序列为 `[0, 0, 0, 0, 0, 0, 9]`。\n - 由于访问的数字序列是非递减的，因此 9 是一个好整数。\n\n`x = 10` 的网格：\n| 0 | 0 | 0 | 0 |\n| 0 | 0 | 0 | 0 |\n| 0 | 0 | 0 | 0 |\n| 0 | 0 | 1 | 0 |\n - 访问的数字序列为 `[0, 0, 0, 0, 0, 1, 0]`。\n - 由于访问的数字序列不是非递减的，因此 10 不是一个好整数。\n - 因此，只有 8 和 9 是好整数，在该范围内总共有 2 个好整数。\n\n**示例 2：**\n> \n**输入：**`l = 123456789, r = 123456790, directions = "DDRRDR"`\n**输出：**`1`\n**解释：**\n`x = 123456789` 的网格：\n| 0 | 0 | 0 | 0 |\n| 0 | 0 | 0 | 1 |\n| 2 | 3 | 4 | 5 |\n| 6 | 7 | 8 | 9 |\n - 路径：`(0,0) → (1,0) → (2,0) → (2,1) → (2,2) → (3,2) → (3,3)`\n - 访问的数字序列为 `[0, 0, 2, 3, 4, 8, 9]`。\n - 由于访问的数字序列是非递减的，因此 123456789 是一个好整数。\n\n`x = 123456790` 的网格：\n| 0 | 0 | 0 | 0 |\n| 0 | 0 | 0 | 1 |\n| 2 | 3 | 4 | 5 |\n| 6 | 7 | 9 | 0 |\n - 访问的数字序列为 `[0, 0, 2, 3, 4, 9, 0]`。\n - 由于访问的数字序列不是非递减的，因此 123456790 不是一个好整数。\n - 因此，只有 123456789 是好整数，在该范围内总共有 1 个好整数。\n\n**示例 3：**\n> \n**输入：**`l = 1288561398769758, r = 1288561398769758, directions = "RRRDDD"`\n**输出：**`0`\n**解释：**\n`x = 1288561398769758` 的网格：\n| 1 | 2 | 8 | 8 |\n| 5 | 6 | 1 | 3 |\n| 9 | 8 | 7 | 6 |\n| 9 | 7 | 5 | 8 |\n - 路径：`(0,0) → (0,1) → (0,2) → (0,3) → (1,3) → (2,3) → (3,3)`\n - 访问的数字序列为 `[1, 2, 8, 8, 3, 6, 8]`。\n - 由于访问的数字序列不是非递减的，因此 1288561398769758 不是一个好整数。\n - 没有好整数，在该范围内总共有 0 个好整数。\n\n**提示：**\n - `1 <= l <= r <= 9 × 10^15`\n - `directions.length == 6`\n - `directions` 由**恰好**三个 `\'D\'` 字符和三个 `\'R\'` 字符组成。'
                         )

    def solve(self, l: int, r: int, directions: str) -> int:
        high_s = list(map(int, str(r)))
        n = len(high_s)
        low_s = list(map(int, str(l).zfill(n)))
        in_path = [False] * n
        in_path[-1] = True
        pos = n - 1
        for d in reversed(directions):
            pos -= 1 if d == 'R' else 4
            if pos < 0:
                break
            in_path[pos] = True

        @cache
        def dfs(i: int, pre: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1
            lo = low_s[i] if limit_low else 0
            hi = high_s[i] if limit_high else 9
            res = 0
            start = max(lo, pre) if in_path[i] else lo
            for d in range(start, hi + 1):
                res += dfs(i + 1, d if in_path[i] else pre, limit_low and d == lo, limit_high and d == hi)
            return res
        return dfs(0, 0, True, True)

    def gen(self):
        """
        生成测试样例：返回元组 (l_values, r_values, directions_values)
        其中每个列表包含testcase_num个元素

        测试策略：
        1. 边界场景：单点范围、小范围、中范围、大范围
        2. directions多样性：覆盖不同的路径组合（3个D和3个R的所有可能排列）
        3. 数值规模：覆盖不同位数的数字

        避免过大范围导致超时，范围控制在1-10^6区间内。
        """
        l_values = []
        r_values = []
        directions_values = []

        # 所有可能的directions组合（从20种中采样）
        all_directions = [
            "DDDRRR", "DDRRDR", "DDRRRD", "DRDDRR", "DRDRDR",
            "DRDRRD", "DRRDDR", "DRRDRD", "DRRRDD", "RDDDRR",
            "RDDRDR", "RDDRRD", "RDRDDR", "RDRDRD", "RDRRDD",
            "RRDDDR", "RRDDRD", "RRDRDD", "RRRDDD"
        ]

        random.seed(self.seed)

        # 生成20个小范围测试用例（1-1000）
        for _ in range(20):
            l = self.s_generate_int(int_range=(1, 1000))
            r = self.s_generate_int(int_range=(l, min(l + 100, 1000)))
            d = random.choice(all_directions)
            l_values.append(l)
            r_values.append(r)
            directions_values.append(d)

        # 生成15个中等范围测试用例（1000-100000）  
        for _ in range(15):
            l = self.s_generate_int(int_range=(1000, 100000))
            r = self.s_generate_int(int_range=(l, min(l + 10000, 100000)))
            d = random.choice(all_directions)
            l_values.append(l)
            r_values.append(r)
            directions_values.append(d)

        # 生成15个大范围测试用例（100000-1000000）
        for _ in range(15):
            l = self.s_generate_int(int_range=(100000, 1000000))
            r = self.s_generate_int(int_range=(l, min(l + 100000, 1000000)))
            d = random.choice(all_directions)
            l_values.append(l)
            r_values.append(r)
            directions_values.append(d)

        return (l_values, r_values, directions_values)
    

