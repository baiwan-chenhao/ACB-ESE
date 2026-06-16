
import random
from . import Problem
import re


class Solution1(Problem):
    date = "2026-3-1"
    def __init__(self):
        Problem.__init__(self,
                         degree=0,
                         idx=3856,
                         types=[],
                         pass_rate=0.79,
                         description='给定一个由小写英文字母组成的字符串 `s`。\n返回移除字符串 `s` 尾部**所有****元音字母**后得到的字符串。\n元音字母包括字符 `\'a\'`、`\'e\'`、`\'i\'`、`\'o\'` 和 `\'u\'`。\n\n**示例 1：**\n> \n**输入：**`s = "idea"`\n**输出：**`"id"`\n**解释：**\n移除 `"id**ea**"` 后，得到字符串 `"id"`。\n**示例 2：**\n> \n**输入：**`s = "day"`\n**输出：**`"day"`\n**解释：**\n字符串 `"day"`\xa0尾部没有元音字母。\n**示例 3：**\n> \n**输入：**`s = "aeiou"`\n**输出：**`""`\n**解释：**\n移除 `"**aeiou**"` 后，得到字符串 `""`。\n\n**提示：**\n - `1 <= s.length <= 100`\n - `s` 仅由小写英文字母组成。'
                         )

    def solve(self, s: str) -> str:
        return s.rstrip('aeiou')

    def gen(self):
        """
        生成测试样例。

        测试策略：
        1. 边界值：最小长度(1)、最大长度(100)
        2. 尾部无元音字母
        3. 尾部有1个元音字母
        4. 尾部有多个连续元音字母
        5. 全元音字母（全部移除）
        6. 中间有元音字母但尾部没有
        """
        random.seed(self.seed)
        test_cases = []

        # 边界情况：最小长度1
        for vowel in 'aeiou':
            test_cases.append(vowel)  # 单个元音，应返回空字符串
        test_cases.append('b')  # 单个辅音，应保持不变

        # 边界情况：最大长度100
        max_vowels = 'a' * 50 + 'b' + 'e' * 49  # 尾部有49个元音
        test_cases.append(max_vowels)

        # 尾部无元音
        test_cases.append('bcdfg')
        test_cases.append('bcdfghjklmnpqrstvwxyz')

        # 尾部有1个元音
        test_cases.append('bcd' + 'a')
        test_cases.append('bcdfghjklmnpqrstvwxyza')

        # 尾部有多个连续元音
        test_cases.append('bcd' + 'aeiou')
        test_cases.append('hello' + 'eai')
        test_cases.append('xyz' + 'uuu')

        # 全元音字母
        test_cases.append('aeiou')
        test_cases.append('aaaaa')
        test_cases.append('eeeeeee')
        test_cases.append('iiiiii')
        test_cases.append('ooooooo')
        test_cases.append('uuuuuu')

        # 中间有元音但尾部没有
        test_cases.append('abcbd')
        test_cases.append('aebcd')
        test_cases.append('aeibcd')

        # 随机测试用例
        for _ in range(self.testcase_num - len(test_cases)):
            length = random.randint(1, 100)
            chars = []
            for _ in range(length):
                chars.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
            test_cases.append(''.join(chars))

        return (test_cases,)
    

import random
from itertools import count
from . import Problem
import re


class Solution2(Problem):
    date = "2026-3-1"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3857,
                         types=[],
                         pass_rate=0.79,
                         description='给你一个整数 `n`。\n在一次操作中，你可以将整数 `x` 拆分为两个正整数 `a` 和 `b`，使得 `a + b = x`。\n此操作的代价是 `a * b`。\n返回将整数 `n` 拆分为 `n` 个 1 所需的**最小总代价**。\n\n**示例 1：**\n> \n**输入：**`n = 3`\n**输出：**`3`\n**解释：**\n一种最优的操作方案为：\n| `x` | `a` | `b` | `a + b` | `a * b` | 代价 |\n| --- | --- | --- | --- | --- | --- |\n| 3 | 1 | 2 | 3 | 2 | 2 |\n| 2 | 1 | 1 | 2 | 1 | 1 |\n\n因此，最小总代价为 `2 + 1 = 3`。\n**示例 2：**\n> \n**输入：**`n = 4`\n**输出：**`6`\n**解释：**\n> \n一种最优的操作方案为：\n| `x` | `a` | `b` | `a + b` | `a * b` | 代价 |\n| --- | --- | --- | --- | --- | --- |\n| 4 | 2 | 2 | 4 | 4 | 4 |\n| 2 | 1 | 1 | 2 | 1 | 1 |\n| 2 | 1 | 1 | 2 | 1 | 1 |\n\n因此，最小总代价为 `4 + 1 + 1 = 6`。\n\n**提示：**\n - `1 <= n <= 500`'
                         )

    def solve(self, n: int) -> int:
        return n * (n - 1) // 2

    def gen(self):
        """
        生成测试样例。

        返回一个元组，其中包含一个列表，该列表包含所有测试样例的n值。

        覆盖策略：
        1. 边界值：n=1（最小值，不需要任何拆分）, n=500（最大值）
        2. 示例值：n=3, n=4（题目示例）
        3. 小数值：n=2, n=5, n=10, n=20（基础用例）
        4. 中等数值：n=50, n=100, n=200, n=400（中等规模）
        5. 随机值：覆盖[1, 500]范围内的随机值，确保分布均匀
        """
        # 关键测试值：边界值、示例值、典型值
        key_values = [1, 2, 3, 4, 5, 10, 20, 50, 100, 200, 400, 500]

        # 剩余用例使用随机生成
        random_count = self.testcase_num - len(key_values)
        random_values = [self.s_generate_int(int_range=(1, 500)) for _ in range(random_count)]

        # 合并并打乱顺序
        all_values = key_values + random_values
        random.shuffle(all_values)

        return (all_values,)
    


from . import Problem
from typing import List

class Solution3(Problem):
    date = "2026-3-1"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3858,
                         types=[],
                         pass_rate=0.49,
                         description='给你一个大小为 `m x n` 的二维整数数组 `grid`。\n你必须从 `grid` 的每一行中**选择恰好一个整数**。\n返回一个整数，表示从每行中选出的整数的**按位或**（bitwise OR）的**最小可能值**。\n\n**示例 1：**\n> \n**输入：**`grid = [[1,5],[2,4]]`\n**输出：**`3`\n**解释：**\n - 从第一行选择 1，从第二行选择 2。\n - `1 | 2 = 3`\u200b\u200b\u200b\u200b\u200b\u200b\u200b，这是最小可能值。\n\n**示例 2：**\n> \n**输入：**`grid = [[3,5],[6,4]]`\n**输出：**`5`\n**解释：**\n - 从第一行选择 5，从第二行选择 4。\n - `5 | 4 = 5`\u200b\u200b\u200b\u200b\u200b\u200b\u200b，这是最小可能值。\n\n**示例 3：**\n> \n**输入：**`grid = [[7,9,8]]`\n**输出：**`7`\n**解释：**\n - 选择 7 即可得到最小按位或值。\n\n**提示：**\n - `1 <= m == grid.length <= 10^5`\n - `1 <= n == grid[i].length <= 10^5`\n - `m * n <= 10^5`\n - `1 <= grid[i][j] <= 10^5\u200b\u200b\u200b\u200b\u200b\u200b\u200b`'
                         )

    def solve(self, grid: List[List[int]]) -> int:
        mx = max(map(min, grid))
        ans = 0
        for i in range(mx.bit_length() - 1, -1, -1):
            mask = ans | (1 << i) - 1
            for row in grid:
                for x in row:
                    if x | mask == mask:
                        break
                else:
                    ans |= 1 << i
                    break
        return ans

    def gen(self):
        """
        生成测试样例，用于测试求解每行选择一个数使按位或最小的问题。

        覆盖场景：
        1. 边界情况：最小网格(1x1)、单行多列、多行单列
        2. 随机测试：中等规模随机网格
        3. 特殊结构：全相同元素、递增序列、递减序列、连续2的幂
        4. 位运算特征：最高位相同、不同位覆盖

        数据规模控制：
        - 由于 m*n <= 10^5 且需要多组测试样例，将最大总元素数控制在 10^4 以内
        - 元素值范围：1 到 10^5
        - 测试样例数：50组（保证执行效率）
        """
        num_cases = 50

        # 由于 m*n <= 10^5，但需要多组测试用例，将最大元素数降至 10^4 以提高效率
        max_total_elements = 10000

        grids = []

        for case_idx in range(num_cases):
            # 根据用例索引选择不同的生成策略
            if case_idx < 3:
                # 边界情况：1x1 最小网格
                grid = [[self.s_generate_int(int_range=(1, 100000))]]

            elif case_idx < 6:
                # 单行多列（1 x n）
                n = min(self.s_generate_int(int_range=(2, 100)), max_total_elements)
                row = [self.s_generate_int(int_range=(1, 100000)) for _ in range(n)]
                grid = [row]

            elif case_idx < 9:
                # 多行单列（m x 1）
                m = min(self.s_generate_int(int_range=(2, 100)), max_total_elements)
                grid = [[self.s_generate_int(int_range=(1, 100000))] for _ in range(m)]

            elif case_idx < 14:
                # 小型网格（每行元素数较小）
                m = min(self.s_generate_int(int_range=(2, 20)), max_total_elements)
                n = min(self.s_generate_int(int_range=(2, 20)), max_total_elements // m)
                grid = [[self.s_generate_int(int_range=(1, 100000)) for _ in range(n)] for _ in range(m)]

            elif case_idx < 24:
                # 中等规模随机网格
                m = min(self.s_generate_int(int_range=(2, 100)), max_total_elements)
                n = min(self.s_generate_int(int_range=(2, 100)), max_total_elements // m)
                grid = [[self.s_generate_int(int_range=(1, 100000)) for _ in range(n)] for _ in range(m)]

            elif case_idx < 29:
                # 特殊结构：全相同元素
                m = min(self.s_generate_int(int_range=(2, 50)), max_total_elements)
                n = min(self.s_generate_int(int_range=(2, 50)), max_total_elements // m)
                val = self.s_generate_int(int_range=(1, 100000))
                grid = [[val for _ in range(n)] for _ in range(m)]

            elif case_idx < 34:
                # 特殊结构：递增序列
                m = min(self.s_generate_int(int_range=(2, 50)), max_total_elements)
                n = min(self.s_generate_int(int_range=(2, 50)), max_total_elements // m)
                grid = [[i * n + j + 1 for j in range(n)] for i in range(m)]
                # 确保值在范围内
                grid = [[min(x, 100000) for x in row] for row in grid]

            elif case_idx < 39:
                # 特殊结构：递减序列
                m = min(self.s_generate_int(int_range=(2, 50)), max_total_elements)
                n = min(self.s_generate_int(int_range=(2, 50)), max_total_elements // m)
                grid = [[max_total_elements - i * n - j for j in range(n)] for i in range(m)]
                # 确保值在范围内
                grid = [[max(1, min(x, 100000)) for x in row] for row in grid]

            elif case_idx < 44:
                # 特殊结构：连续的2的幂
                m = min(self.s_generate_int(int_range=(2, 50)), max_total_elements)
                n = min(self.s_generate_int(int_range=(2, 50)), max_total_elements // m)
                powers_of_two = [1 << i for i in range(1, 17)]  # 2, 4, 8, ..., 65536
                grid = [[powers_of_two[(i * n + j) % len(powers_of_two)] for j in range(n)] for i in range(m)]

            else:
                # 特殊结构：每行有相同的数，但行间不同
                m = min(self.s_generate_int(int_range=(2, 50)), max_total_elements)
                n = min(self.s_generate_int(int_range=(2, 50)), max_total_elements // m)
                grid = [[i + 1 for _ in range(n)] for i in range(m)]

            grids.append(grid)

        return (grids,)
    

from itertools import count
from . import Problem
from collections import defaultdict
import re


class Solution4(Problem):
    date = "2026-3-1"
    def __init__(self):
        Problem.__init__(self,
                         degree=2,
                         idx=3859,
                         types=[],
                         pass_rate=0.38,
                         description='给你一个整数数组 `nums` 和两个整数 `k` 和 `m`。\n返回一个整数，表示满足以下条件的**子数组**的数量：\n - 子数组**恰好**包含\xa0\u200b\u200b\u200b\u200b\u200b\u200b\u200b`k` 个**不同的**整数。\n - 在子数组中，每个**不同的**整数**至少**出现 `m` 次。\n\n**子数组**是数组中一个连续的、**非空**元素序列。\n\n**示例 1：**\n> \n**输入：**`nums = [1,2,1,2,2], k = 2, m = 2`\n**输出：**`2`\n**解释：**\n满足条件的子数组为：\n| 子数组 | 不同整数 | 频率 |\n| --- | --- | --- |\n| [1, 2, 1, 2] | {1, 2} → 2 | {1: 2, 2: 2} |\n| [1, 2, 1, 2, 2] | {1, 2} → 2 | {1: 2, 2: 3} |\n\n因此，答案是 2。\n**示例 2：**\n> \n**输入：**`nums = [3,1,2,4], k = 2, m = 1`\n**输出：**`3`\n**解释：**\n满足条件的子数组为：\n| 子数组 | 不同整数 | 频率 |\n| --- | --- | --- |\n| [3, 1] | {3, 1} → 2 | {3: 1, 1: 1} |\n| [1, 2] | {1, 2} → 2 | {1: 1, 2: 1} |\n| [2, 4] | {2, 4} → 2 | {2: 1, 4: 1} |\n\n因此，答案是 3。\n\n**提示：**\n - `1 <= nums.length <= 10^5`\n - `1 <= nums[i] <= 10^5`\n - `1 <= k, m <= nums.length`'
                         )

    def solve(self, nums: list[int], k: int, m: int) -> int:

        def calc(distinct_limit: int) -> int:
            cnt = defaultdict(int)
            ge_m = 0
            ans = left = 0
            for x in nums:
                cnt[x] += 1
                if cnt[x] == m:
                    ge_m += 1
                while len(cnt) >= distinct_limit and ge_m >= k:
                    out = nums[left]
                    if cnt[out] == m:
                        ge_m -= 1
                    cnt[out] -= 1
                    if cnt[out] == 0:
                        del cnt[out]
                    left += 1
                ans += left
            return ans
        return calc(k) - calc(k + 1)

    def gen(self):
        """
        生成测试样例，覆盖以下场景：
        1. 边界值：最小数组长度、k=1、m=1、k等于数组长度
        2. 特殊结构：所有元素相同、所有元素不同、交替模式
        3. 正常分布：中等规模的随机数组
        """
        # 减少测试样例数量，降低运行时间
        self.testcase_num = 50
        nums_list = []
        k_list = []
        m_list = []

        # 设置参数范围
        length_range = (1, 200)  # 适当减小最大长度，避免超时
        value_range = (1, 50)    # 减小数值范围
        param_range = (1, 50)    # k和m的范围

        # 第一部分：边界值测试 (20%)
        for i in range(10):
            # 单元素数组
            if i < 3:
                nums = [self.s_generate_int(int_range=value_range)]
                k = 1
                m = 1
            # 小数组，k=m=1
            elif i < 6:
                nums = self.s_generate_list_int(list_length_range=(1, 10), int_range=value_range)
                k = 1
                m = 1
            # 小数组，k接近数组长度
            elif i < 8:
                nums = self.s_generate_list_int(list_length_range=(5, 10), int_range=value_range, different=True)
                k = len(set(nums)) - 1 if len(set(nums)) > 1 else 1
                m = 1
            # 小数组，m接近数组长度
            else:
                nums = self.s_generate_list_int(list_length_range=(5, 10), int_range=value_range)
                k = min(2, len(nums))
                m = len(nums) // 2 + 1

            nums_list.append(nums)
            k_list.append(k)
            m_list.append(m)

        # 第二部分：特殊结构 (30%)
        # 所有元素相同
        for i in range(5):
            val = self.s_generate_int(int_range=value_range)
            length = self.s_generate_int(int_range=(5, 30))
            nums = [val] * length
            k = 1
            m = self.s_generate_int(int_range=(1, length))
            nums_list.append(nums)
            k_list.append(k)
            m_list.append(m)

        # 所有元素不同
        for i in range(5):
            nums = self.s_generate_list_int(list_length_range=(5, 20), int_range=value_range, different=True)
            k = self.s_generate_int(int_range=(1, len(set(nums))))
            m = 1
            nums_list.append(nums)
            k_list.append(k)
            m_list.append(m)

        # 交替模式 [1,2,1,2,...]
        for i in range(5):
            val1 = self.s_generate_int(int_range=value_range)
            val2 = self.s_generate_int(int_range=value_range)
            while val2 == val1:
                val2 = self.s_generate_int(int_range=value_range)
            length = self.s_generate_int(int_range=(4, 20)) * 2  # 确保是偶数
            nums = [val1 if j % 2 == 0 else val2 for j in range(length)]
            k = 1 if val1 == val2 else 2
            m = self.s_generate_int(int_range=(1, min(length // 2, 10)))
            nums_list.append(nums)
            k_list.append(k)
            m_list.append(m)

        # 第三部分：正常分布 (50%)
        for i in range(25):
            nums = self.s_generate_list_int(list_length_range=(10, 100), int_range=value_range)
            distinct_count = len(set(nums))
            # 确保 k 不超过不同元素数量
            max_k = min(distinct_count, param_range[1])
            k = self.s_generate_int(int_range=(1, max_k)) if max_k > 0 else 1
            # 确保 m 不超过数组长度
            max_m = min(len(nums), param_range[1])
            m = self.s_generate_int(int_range=(1, max_m)) if max_m > 0 else 1
            nums_list.append(nums)
            k_list.append(k)
            m_list.append(m)

        return nums_list, k_list, m_list
    

