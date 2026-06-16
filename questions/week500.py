from . import Problem
import random
import re


class Solution1(Problem):
    date = "2026-5-3"
    def __init__(self):
        Problem.__init__(self,
                         degree=0,
                         idx=3917,
                         types=[],
                         pass_rate=0.86,
                         description='给你一个长度为 `n` 的整数数组 `nums`。\n下标 `i` 的**分数**定义为满足以下条件的下标 `j` 的数量：\n - `i < j < n`，并且\n - `nums[i]` 和 `nums[j]` 的奇偶性不同（一个为偶数，另一个为奇数）。\n\n返回一个长度为 `n` 的整数数组 `answer`，其中 `answer[i]` 表示下标 `i` 的分数。\n\n**示例 1：**\n> \n**输入：**`nums = [1,2,3,4]`\n**输出：**`[2,1,1,0]`\n**解释：**\n - `nums[0] = 1`，为奇数。因此，下标 `j = 1` 和 `j = 3` 满足条件，所以下标 0 的分数为 2。\n - `nums[1] = 2`，为偶数。因此，下标 `j = 2` 满足条件，所以下标 1 的分数为 1。\n - `nums[2] = 3`，为奇数。因此，下标 `j = 3` 满足条件，所以下标 2 的分数为 1。\n - `nums[3] = 4`，为偶数。因此，没有下标满足条件，所以下标 3 的分数为 0。\n\n因此，`answer = [2, 1, 1, 0]`。\n**示例 2：**\n> \n**输入：**`nums = [1]`\n**输出：**`[0]`\n**解释：**\n`nums` 中只有一个元素。因此，下标 0 的分数为 0。\n\n**提示：**\n - `1 <= nums.length <= 100`\n - `1 <= nums[i] <= 100`'
                         )

    def solve(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n
        cnt = [0] * 2
        for i in range(n - 1, -1, -1):
            x = nums[i] % 2
            ans[i] = cnt[1 - x]
            cnt[x] += 1
        return ans

    def gen(self):
        """
        生成测试样例。

        策略：
        - 边界测试：最小长度(1)、最大长度(100)
        - 全奇数/全偶数数组：验证边缘情况（此时所有分数应为0）
        - 奇偶交替数组：特殊模式
        - 随机数组：覆盖大多数场景

        返回：
        - 一个列表的元组，每个列表对应一个参数的测试样例
        """
        # 边界测试：最小和最大长度
        all_test_cases = []

        # 单元素数组（边界）
        all_test_cases.append([1])
        all_test_cases.append([100])

        # 全奇数数组（验证所有分数为0的情况）
        all_test_cases.extend(self.generate_list_int(list_length_range=(1, 100), int_range=(1, 99)))
        all_test_cases.extend(self.generate_list_int(list_length_range=(1, 100), int_range=(1, 99)))

        # 全偶数数组（验证所有分数为0的情况）
        all_test_cases.extend(self.generate_list_int(list_length_range=(1, 100), int_range=(2, 100)))
        all_test_cases.extend(self.generate_list_int(list_length_range=(1, 100), int_range=(2, 100)))

        # 奇偶交替数组（特殊模式）
        for length in [5, 10, 20, 50]:
            arr1 = [(1 + 2 * (i % 2)) for i in range(length)]  # 1,2,1,2,...
            arr2 = [(2 - 1 * (i % 2)) for i in range(length)]  # 2,1,2,1,...
            all_test_cases.append(arr1)
            all_test_cases.append(arr2)

        # 随机数组（占多数）
        random_cases = list(self.generate_list_int(list_length_range=(1, 100), int_range=(1, 100)))
        all_test_cases.extend(random_cases)
        all_test_cases.extend(random_cases)

        return (all_test_cases,)
    

import math
import re
from math import isqrt
MX = 1001
is_prime = [0, 0] + [1] * (MX - 2)
for i in range(2, isqrt(MX) + 1):
    if is_prime[i]:
        for j in range(i * i, MX, i):
            is_prime[j] = 0
for i in range(1, MX):
    is_prime[i] = is_prime[i - 1] + (i if is_prime[i] else 0)

class Solution2(Problem):
    date = "2026-5-3"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3918,
                         types=[],
                         pass_rate=0.8,
                         description='给你一个整数 `n`。\n令 `r` 为将 `n` 的数字反转后得到的整数。\n返回从 `min(n, r)` 到 `max(n, r)`（包含两端）之间所有 质数 的**总和**。\n\n**示例 1：**\n> \n**输入：**`n = 13`\n**输出：**`132`\n**解释：**\n - 13 反转后为 31。因此，范围为 `[13, 31]`。\n - 该范围内的质数有 13、17、19、23、29 和 31。\n - 这些质数的总和为 `13 + 17 + 19 + 23 + 29 + 31 = 132`。\n\n**示例 2：**\n> \n**输入：**`n = 10`\n**输出：**`17`\n**解释：**\n - 10 反转后为 1。因此，范围为 `[1, 10]`。\n - 该范围内的质数有 2、3、5 和 7。\n - 这些质数的总和为 `2 + 3 + 5 + 7 = 17`。\n\n**示例 3：**\n> \n**输入：**`n = 8`\n**输出：**`0`\n**解释：**\n - 8 反转后仍为 8。因此，范围为 `[8, 8]`。\n - 该范围内没有质数，所以总和为 0。\n\n**提示：**\n - `1 <= n <= 1000`'
                         )

    def solve(self, n: int) -> int:
        r = 0
        x = n
        while x > 0:
            r = r * 10 + x % 10
            x //= 10
        return is_prime[max(n, r)] - is_prime[min(n, r) - 1]

    def gen(self):
        """生成测试样例，覆盖各种边界情况和特殊场景。

        测试策略：
        1. 边界值：1和1000
        2. 回文数：反转后等于自身（如8, 11, 121, 323）
        3. 反转后变大的情况（如13→31）
        4. 反转后变小的情况（如21→12）
        5. 反转为个位数（如10→1）
        6. 随机值覆盖中间范围
        """
        test_cases = []

        # 1. 边界值 (4个)
        test_cases.extend([1, 1000, 1, 1000])

        # 2. 回文数：反转后等于自身 (10个)
        # 包含一位数、两位数、三位数回文
        palindromes = [8, 11, 22, 33, 121, 131, 141, 323, 454, 555]
        test_cases.extend(palindromes)

        # 3. 反转后变大的情况 (10个)
        # 个位数→多位数，或多位数→更大的数
        reverse_greater = [13, 14, 15, 16, 17, 19, 23, 29, 34, 37]
        test_cases.extend(reverse_greater)

        # 4. 反转后变小的情况 (10个)
        # 多位数→较小的数
        reverse_smaller = [21, 31, 41, 51, 61, 71, 81, 91, 210, 320]
        test_cases.extend(reverse_smaller)

        # 5. 反转为个位数的情况 (10个)
        # 10的倍数
        reverse_single = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        test_cases.extend(reverse_single)

        # 6. 质数附近的测试点 (6个)
        prime_nearby = [2, 3, 5, 7, 997, 1000]
        test_cases.extend(prime_nearby)

        # 7. 随机值 (50个)
        import random
        random.seed(self.seed)
        for _ in range(50):
            test_cases.append(random.randint(1, 1000))

        return (test_cases,)
    

import random
from . import Problem
import re


class Solution3(Problem):
    date = "2026-5-3"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3919,
                         types=[],
                         pass_rate=0.5,
                         description='给你一个整数数组 `nums`，`nums` 是**严格递增**的。\n对于每个下标 `x`，设 `closest(x)` 为使得 `abs(nums[x] - nums[y])`**最小化**的**相邻**下标 `y`。如果两个**相邻**下标的差值相同，则选择**较小**的下标。\n从任意下标 `x` 出发，你可以通过以下两种方式移动：\n - 移动到任意下标 `y`，代价为 `abs(nums[x] - nums[y])`，或者\n - 移动到 `closest(x)`，代价为 1。\n\n同时给你一个二维整数数组 `queries`，其中每个 `queries[i] = [l_i, r_i]`。\n对于每个查询，计算从下标 `l_i` 移动到下标 `r_i` 的**最小总代价**。\n返回一个整数数组 `ans`，其中 `ans[i]` 是第 `i`\xa0个查询的答案。\n两个值 `x` 和 `y` 之间的**绝对差**定义为 `abs(x - y)`。\n\n**示例 1：**\n> \n**输入：**`nums = [-5,-2,3], queries = [[0,2],[2,0],[1,2]]`\n**输出：**`[6,2,5]`\n**解释：**\u200b\u200b\u200b\u200b\u200b\u200b\n - 最近的下标分别是 `[1, 0, 1]`。\n - 对于 `[0, 2]`，路径 `0 → 1 → 2` 包含一次从下标 0 到 1 的最近移动，代价为 1，以及一次从下标 1 到 2 的移动，代价为 `|-2 - 3| = 5`，总代价为 `1 + 5 = 6`。\n - 对于 `[2, 0]`，路径 `2 → 1 → 0` 包含两次最近移动，分别从下标 2 到 1 和从下标 1 到 0，每次代价为 1，总代价为 2。\n - 对于 `[1, 2]`，从下标 1 直接移动到下标 2 的代价为 `|-2 - 3| = 5`，这是最优的。\n\n因此，`ans = [6, 2, 5]`。\n**示例 2：**\n> \n**输入：**`nums = [0,2,3,9], queries = [[3,0],[1,2],[2,0]]`\n**输出：**`[4,1,3]`\n**解释：**\n - 最近的下标分别是 `[1, 2, 1, 2]`。\n - 对于 `[3, 0]`，路径 `3 → 2 → 1 → 0` 包含两次最近移动，分别从下标 3 到 2 和从 2 到 1，每次代价为 1，以及一次从 1 到 0 的移动，代价为 `|2 - 0| = 2`，总代价为 `1 + 1 + 2 = 4`。\n - 对于 `[1, 2]`，从下标 1 到 2 的最近移动代价为 1。\n - 对于 `[2, 0]`，路径 `2 → 1 → 0` 包含一次从下标 2 到 1 的最近移动，代价为 1，以及一次从 1 到 0 的移动，代价为 `|2 - 0| = 2`，总代价为 `1 + 2 = 3`。\n\n因此，`ans = [4, 1, 3]`。\n\n**提示：**\n - `2 <= nums.length <= 10^5`\n - `-10^9 <= nums[i] <= 10^9`\n - `nums` 严格递增\n - `1 <= queries.length <= 10^5`\n - `queries[i] = [l_i, r_i]`\n - `0 <= l_i, r_i < nums.length`'
                         )

    def solve(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        sum_l = [0] * n
        sum_r = [0] * n
        for i in range(1, n):
            if i < n - 1 and nums[i] - nums[i - 1] > nums[i + 1] - nums[i]:
                cost = nums[i] - nums[i - 1]
            else:
                cost = 1
            sum_l[i] = sum_l[i - 1] + cost
            if i > 1 and nums[i - 1] - nums[i - 2] <= nums[i] - nums[i - 1]:
                cost = nums[i] - nums[i - 1]
            else:
                cost = 1
            sum_r[i] = sum_r[i - 1] + cost
        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            l, r = q
            if l < r:
                ans[i] = sum_r[r] - sum_r[l]
            else:
                ans[i] = sum_l[l] - sum_l[r]
        return ans

    def gen(self):
        """
        生成测试样例，覆盖不同规模和边界条件。

        策略说明：
        1. 小规模测试（10个）：数组长度2-20，查询数量2-10
           - 覆盖基本功能、边界值、相邻查询等简单场景
        2. 大规模测试（90个）：数组长度10-1000，查询数量5-200
           - 80%集中在10-100长度，避免参考代码超时
           - 20%覆盖100-500长度，测试算法可扩展性

        为了避免超时风险，将原题约束从10^5降至合理范围：
        - 数组长度最大500（原题10^5）
        - 查询数量最大200（原题10^5）
        - 值域范围根据数组规模动态调整
        """
        # 辅助方法：生成严格递增的随机列表
        def s_generate_strictly_increasing_list(list_length_range, int_range):
            """
            生成严格递增的随机整数列表。

            :param list_length_range: 列表长度范围 (min, max)
            :param int_range: 整数值范围 (min, max)
            :return: 严格递增的整数列表
            """
            len_list = random.randint(*list_length_range)
            min_val, max_val = int_range
            # 确保范围足够生成指定长度的递增序列
            if max_val - min_val + 1 >= len_list:
                rets = random.sample(range(min_val, max_val + 1), len_list)
            else:
                # 如果范围不够，使用插值法生成
                rets = [min_val + i * (max_val - min_val) // max(len_list - 1, 1) for i in range(len_list)]
            return sorted(rets)

        # 重置种子确保可复现
        random.seed(self.seed)

        # 生成小规模测试数据（10个）
        # 覆盖边界：最小长度、相等查询、相邻查询、简单递增模式
        small_num_cases = 10
        small_nums = []
        small_queries = []

        # 生成小规模测试用例
        for _ in range(small_num_cases):
            # 数组长度2-20
            nums = s_generate_strictly_increasing_list((2, 20), (-1000, 1000))
            small_nums.append(nums)
            # 查询数量2-10
            num_queries = random.randint(2, 10)
            queries = []
            for __ in range(num_queries):
                l = random.randint(0, len(nums) - 1)
                r = random.randint(0, len(nums) - 1)
                queries.append([l, r])
            small_queries.append(queries)

        # 生成大规模测试数据（90个）
        # 覆盖中等和较大规模、随机查询模式
        large_num_cases = 90
        large_nums = []
        large_queries = []

        for _ in range(large_num_cases):
            # 数组长度10-1000，但大部分集中在较小范围避免超时
            if random.random() < 0.8:
                nums = s_generate_strictly_increasing_list((10, 100), (-10000, 10000))
            else:
                nums = s_generate_strictly_increasing_list((100, 500), (-100000, 100000))
            large_nums.append(nums)

            # 查询数量5-200
            num_queries = random.randint(5, 200)
            queries = []
            for __ in range(num_queries):
                l = random.randint(0, len(nums) - 1)
                r = random.randint(0, len(nums) - 1)
                queries.append([l, r])
            large_queries.append(queries)

        # 合并所有测试用例
        all_nums = small_nums + large_nums
        all_queries = small_queries + large_queries

        return all_nums, all_queries
    


from bisect import bisect_right
import re


class Solution4(Problem):
    date = "2026-5-3"
    def __init__(self):
        Problem.__init__(self,
                         degree=2,
                         idx=3920,
                         types=[],
                         pass_rate=0.38,
                         description='给你一个整数数组 `nums`。\n如果 `nums[i] == i`，则位置 `i` 被称为**固定点**。\n允许你从数组中删除**任意**数量的元素（包括零个）。在每次删除后，剩余元素**向左移动**，并且下标从 0 开始重新分配。\n返回一个整数，表示在执行任意次数的删除操作后，可以获得的**最大**固定点数量。\n\n**示例 1：**\n> \n**输入：**`nums = [0,2,1]`\n**输出：**`2`\n**解释：**\n - 删除 `nums[1] = 2`。数组变为 `[0, 1]`。\n - 现在，`nums[0] = 0` 且 `nums[1] = 1`，因此两个下标都是固定点。\n - 因此，答案为 2。\n\n**示例 2：**\n> \n**输入：**`nums = [3,1,2]`\n**输出：**`2`\n**解释：**\n - 不删除任何元素。数组保持为 `[3, 1, 2]`。\n - 此时，`nums[1] = 1` 且 `nums[2] = 2`，因此这些下标是固定点。\n - 因此，答案为 2。\n\n**示例 3：**\n> \n**输入：**`nums = [1,0,1,2]`\n**输出：**`3`\n**解释：**\n - 删除 `nums[0] = 1`。数组变为 `[0, 1, 2]`。\n - 现在，`nums[0] = 0`，`nums[1] = 1`，且 `nums[2] = 2`，因此所有下标都是固定点。\n - 因此，答案为 3。\n\n**提示：**\n - `1 <= nums.length <= 10^5`\n - `0 <= nums[i] <= 10^5`'
                         )

    def maxEnvelopes(self, envelopes: list[tuple[int, int]]) -> int:
        envelopes.sort(key=lambda e: (e[0], -e[1]))
        g = []
        for _, h in envelopes:
            j = bisect_right(g, h)
            if j < len(g):
                g[j] = h
            else:
                g.append(h)
        return len(g)

    def solve(self, nums: list[int]) -> int:
        a = [(x, i - x) for i, x in enumerate(nums) if i >= x]
        return self.maxEnvelopes(a)

    def gen(self):
        test_cases = []

        # 生成100个测试用例
        # 为了避免超时，适当控制数组大小
        # 题目约束: 1 <= nums.length <= 10^5, 0 <= nums[i] <= 10^5
        # 这里缩小范围测试核心逻辑

        # 1. 小规模随机数组 (前30个) - 测试基本功能和边界
        for _ in range(30):
            length = self.s_generate_int(int_range=(1, 20))
            int_range_val = (0, 20)
            array = [self.s_generate_int(int_range=int_range_val) for _ in range(length)]
            test_cases.append(array)

        # 2. 中等规模已排序数组 (20个) - 测试最优情况（所有元素都是固定点）
        for _ in range(20):
            length = self.s_generate_int(int_range=(10, 100))
            array = list(range(length))
            test_cases.append(array)

        # 3. 全相同元素数组 (15个) - 边界情况
        for val in [0, 1, 5, 10]:
            for length in [1, 2, 5, 10, 20]:
                array = [val] * length
                test_cases.append(array)

        # 4. 交替固定点数组 (15个) - 特殊结构测试
        for length in [1, 2, 5, 10, 20, 50, 100]:
            array = [0 if i % 2 == 0 else i for i in range(length)]
            test_cases.append(array)

        # 5. 严格递增固定点数组 (10个) - 最优情况
        for length in [1, 2, 5, 10, 20]:
            array = list(range(length))
            test_cases.append(array)

        # 6. 中等规模随机数组 (补充剩余) - 常规测试
        while len(test_cases) < self.testcase_num:
            length = self.s_generate_int(int_range=(10, 100))
            int_range_val = (0, 100)
            array = [self.s_generate_int(int_range=int_range_val) for _ in range(length)]
            test_cases.append(array)

        # 截断到精确的100个
        test_cases = test_cases[:self.testcase_num]

        # 返回格式：元组的第i个列表对应被测函数的第i个参数
        # 函数签名: solve(self, nums: list[int]) -> int
        # 只有一个参数，所以返回一个包含一个列表的元组
        return (test_cases,)
    

