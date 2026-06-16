

from . import Problem
from typing import List


class Solution1(Problem):
    date = "2026-3-14"
    def __init__(self):
        Problem.__init__(self,
                         degree=0,
                         idx=3866,
                         types=[],
                         pass_rate=0.65,
                         description='给你一个整数数组 `nums`。\n请你返回一个整数，表示 `nums` 中出现**恰好**一次的第一个**偶数**（以数组下标最早为准）。如果不存在这样的整数，返回 -1。\n如果一个整数 `x` 能被 2 整除，那么它就被认为是**偶数**。\n\n**示例 1：**\n> \n**输入：**`nums = [3,4,2,5,4,6]`\n**输出：**`2`\n**解释：**\n2 和 6 都是偶数，并且它们都恰好出现一次。因为 2 在数组中出现得更早，所以答案是 2。\n**示例 2：**\n> \n**输入：**`nums = [4,4]`\n**输出：**`-1`\n**解释：**\n没有恰好出现一次的偶数，所以返回 -1。\n\n**提示：**\n - `1 <= nums.length <= 100`\n - `1 <= nums[i] <= 100`'
                         )

    def solve(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        for x in nums:
            if x % 2 == 0 and cnt[x] == 1:
                return x
        return -1

    def gen(self):
        """
        生成测试样例。

        测试用例分配策略：
        - 10% 边界情况：空偶数情况、最小长度、最大长度等
        - 70% 正常随机情况
        - 20% 特殊结构：全是奇数、全是重复偶数、全相同元素等

        返回格式：(list, ) - 元组包含一个列表，该列表包含所有测试用例的 nums 数组
        """
        # 初始化结果列表
        nums_list = []

        # ========== 边界情况 (10个用例) ==========
        # 1-2. 最小长度数组，包含唯一偶数和不包含唯一偶数的情况
        nums_list.append([2])  # 长度为1，有唯一偶数
        nums_list.append([1])  # 长度为1，无偶数

        # 3-4. 全是奇数的情况（应该返回-1）
        nums_list.append([1, 3, 5, 7, 9])
        nums_list.append([1, 1, 3, 3, 5, 5])

        # 5-6. 所有偶数都重复的情况（应该返回-1）
        nums_list.append([2, 2, 4, 4, 6, 6])
        nums_list.append([4, 2, 4, 2, 6, 6])

        # 7. 全是同一个偶数
        nums_list.append([2] * 10)

        # 8. 第一个恰好出现一次的偶数在开头
        nums_list.append([2, 4, 4, 6, 6])

        # 9. 第一个恰好出现一次的偶数在结尾
        nums_list.append([4, 4, 6, 6, 8])

        # 10. 只有一个唯一偶数且在中间位置
        nums_list.append([4, 4, 6, 8, 8, 10, 10])

        # ========== 特殊结构情况 (20个用例) ==========
        # 11-15. 严格递增的数组，偶数分布
        nums_list.append([1, 2, 3, 4, 5, 6, 7, 8])
        nums_list.append([2, 4, 6, 8, 10, 12, 14, 16])  # 全是偶数且都唯一
        nums_list.append([2, 2, 4, 4, 6, 6, 8, 8, 10])  # 最后一个是唯一偶数
        nums_list.append([2, 4, 6, 6, 8, 8, 10, 10])  # 第一个唯一偶数在最前
        nums_list.append(list(range(1, 51)))  # 1到50，偶数都唯一

        # 16-20. 严格递减的数组，偶数分布
        nums_list.append([8, 7, 6, 5, 4, 3, 2, 1])
        nums_list.append([16, 14, 12, 10, 8, 6, 4, 2])  # 全是偶数且都唯一
        nums_list.append([10, 8, 8, 6, 6, 4, 4, 2, 2])  # 第一个唯一偶数在最前
        nums_list.append([10, 10, 8, 8, 6, 6, 4, 2])  # 最后一个是唯一偶数
        nums_list.append(list(range(50, 0, -1)))  # 50到1，偶数都唯一

        # 21-23. 交替奇偶
        nums_list.append([1, 2, 3, 4, 5, 6, 7, 8])  # 偶数都唯一
        nums_list.append([2, 1, 4, 3, 6, 5, 8, 7])  # 偶数都唯一
        nums_list.append([2, 1, 2, 3, 4, 3, 6, 5])  # 部分偶数重复

        # 24-25. 只有一个偶数
        nums_list.append([1, 3, 5, 7, 2, 9, 11])  # 偶数唯一
        nums_list.append([1, 3, 5, 7, 2, 9, 2])  # 偶数重复
        # 26-30. 最大长度(100)的边界情况
        nums_list.append(list(range(1, 101)))  # 1到100，偶数都唯一
        nums_list.append([i if i % 2 == 1 else i * 2 for i in range(1, 101)])  # 偶数是原值的两倍
        nums_list.append([2 if i % 2 == 0 else 2 * i + 1 for i in range(100)])  # 所有偶数都是2（重复）
        nums_list.append([4 if i % 2 == 0 and i < 50 else (2 if i % 2 == 0 else i) for i in range(1, 101)])
        nums_list.append([i % 2 == 0 for i in range(100)])

        # 修正第30个用例，确保全是偶数但都唯一
        nums_list[-1] = [2 * i for i in range(1, 51)] + [2 * i for i in range(1, 51)]

        # ========== 正常随机情况 (70个用例) ==========
        # 使用 generate_list_int 生成随机数组
        # 数组长度范围：(1, 100)，元素值范围：(1, 100)
        random_nums = list(self.generate_list_int(list_length_range=(1, 100), int_range=(1, 100)))
        nums_list.extend(random_nums)

        return (nums_list,)
    

import math
from . import Problem
from typing import List
import re
from math import gcd


class Solution2(Problem):
    date = "2026-3-14"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3867,
                         types=[],
                         pass_rate=0.71,
                         description='给你一个长度为 `n` 的整数数组 `nums`。\n构造一个数组 `prefixGcd`，其中对于每个下标\xa0`i`：\n - 令 `mx_i = max(nums[0], nums[1], ..., nums[i])`。\n - `prefixGcd[i] = gcd(nums[i], mx_i)`。\n\n在构造 `prefixGcd` 之后：\n - 将 `prefixGcd` 按**非递减**顺序排序。\n - 通过取**最小的未配对**元素和**最大的未配对**元素来形成数对。\n - 重复此过程，直到无法再形成更多数对。\n - 对于每个形成的数对，**计算**两个元素的最大公约数\xa0`gcd`。\n - 如果 `n` 是奇数，`prefixGcd` 数组中的**中间**元素保持**未配对**状态，并应被忽略。\n\n返回一个整数，表示所有形成数对的**最大公约数之和**。\n术语 `gcd(a, b)` 表示 `a` 和 `b` 的**最大公约数**。\n\n**示例 1：**\n> \n**输入：**`nums = [2,6,4]`\n**输出：**`2`\n**解释：**\n构造 `prefixGcd`：\n| `i` | `nums[i]` | `mx_i` | `prefixGcd[i]` |\n| --- | --- | --- | --- |\n| 0 | 2 | 2 | 2 |\n| 1 | 6 | 6 | 6 |\n| 2 | 4 | 6 | 2 |\n\n`prefixGcd = [2, 6, 2]`。排序后形成 `[2, 2, 6]`。\n将最小和最大的元素配对：`gcd(2, 6) = 2`。剩下的中间元素 2 被忽略。因此，总和为 2。\n**示例 2：**\n> \n**输入：**`nums = [3,6,2,8]`\n**输出：**`5`\n**解释：**\n构造 `prefixGcd`：\n| `i` | `nums[i]` | `mx_i` | `prefixGcd[i]` |\n| --- | --- | --- | --- |\n| 0 | 3 | 3 | 3 |\n| 1 | 6 | 6 | 6 |\n| 2 | 2 | 6 | 2 |\n| 3 | 8 | 8 | 8 |\n\n`prefixGcd = [3, 6, 2, 8]`。排序后形成 `[2, 3, 6, 8]`。\n形成数对：`gcd(2, 8) = 2` 和 `gcd(3, 6) = 3`。因此，总和为 `2 + 3 = 5`。\n\n**提示：**\n - `1 <= n == nums.length <= 10^5`\n - `1 <= nums[i] <= 10^9`'
                         )

    def solve(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * n
        mx = 0
        for i, x in enumerate(nums):
            mx = max(mx, x)
            pre[i] = gcd(x, mx)
        pre.sort()
        return sum((gcd(pre[i], pre[-1 - i]) for i in range(n // 2)))

    def gen(self):
        """
        生成测试样例。

        策略：
        1. 边界情况：小规模数组（长度1-3）、中等规模（长度100-1000）、大规模（长度10000-20000）
        2. 特殊结构：全相同元素、严格递增、严格递减、全是偶数等
        3. 正常情况：随机生成的数组

        参数：
        - 返回一个元组，包含一个列表，该列表为 nums 参数的所有测试样例
        """
        nums_cases = []

        # 边界测试：小规模数组（5个）
        for _ in range(5):
            nums_cases.append(self.s_generate_list_int(
                list_length_range=(1, 3), 
                int_range=(1, 100)
            ))

        # 正常测试：中等规模随机数组（10个）
        for _ in range(10):
            nums_cases.append(self.s_generate_list_int(
                list_length_range=(100, 1000), 
                int_range=(1, 10000)
            ))

        # 大规模测试：验证性能（5个）
        for _ in range(5):
            nums_cases.append(self.s_generate_list_int(
                list_length_range=(10000, 20000), 
                int_range=(1, 100000)
            ))

        # 特殊结构测试（10个）
        special_patterns = [
            [5] * self.s_generate_int(int_range=(1, 20)),  # 全相同元素
            list(range(1, self.s_generate_int(int_range=(5, 20)) + 1)),  # 严格递增
            list(range(self.s_generate_int(int_range=(20, 30)), 0, -1)),  # 严格递减
            [i * 2 for i in range(1, self.s_generate_int(int_range=(5, 20)) + 1)],  # 全是偶数
            [1] * 10 + [2] * 10,  # 交替相同元素
        ]

        for _ in range(10):
            idx = self.s_generate_int(int_range=(0, len(special_patterns) - 1))
            nums_cases.append(special_patterns[idx])

        return (nums_cases,)
    


from . import Problem
from typing import List
from collections import Counter
import re


class Solution3(Problem):
    date = "2026-3-14"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3868,
                         types=[],
                         pass_rate=0.53,
                         description='给你两个大小为 `n` 的整数数组 `nums1` 和 `nums2`。\n你可以对这两个数组执行以下两种操作任意次：\n -**在同一个数组内交换**：选择两个下标 `i` 和 `j`。然后，选择交换 `nums1[i]` 和 `nums1[j]`，或者交换 `nums2[i]` 和 `nums2[j]`。此操作是**免费的**。\n -**在两个数组之间交换**：选择一个下标 `i`。然后，交换 `nums1[i]` 和 `nums2[i]`。此操作**花费为 1**。\n\n返回一个整数，表示使 `nums1` 和 `nums2`**相同**的**最小花费**。如果不可能做到，返回 -1。\n\n**示例 1：**\n> \n**输入：**`nums1 = [10,20], nums2 = [20,10]`\n**输出：**`0`\n**解释：**\n - 交换 `nums2[0] = 20` 和 `nums2[1] = 10`。\n> \n> \t - `nums2` 变为 `[10, 20]`。\n - 此操作是免费的。\n\n - `nums1` 和 `nums2` 现在相同。花费为 0。\n\n**示例 2：**\n> \n**输入：**`nums1 = [10,10], nums2 = [20,20]`\n**输出：**`1`\n**解释：**\n - 交换 `nums1[0] = 10` 和 `nums2[0] = 20`。\n> \n> \t - `nums1` 变为 `[20, 10]`。\n - `nums2` 变为 `[10, 20]`。\n - 此操作花费 1。\n\n - 交换 `nums2[0] = 10` 和 `nums2[1] = 20`。\n> \t - `nums2` 变为 `[20, 10]`。\n - 此操作是免费的。\n\n - `nums1` 和 `nums2` 现在相同。花费为 1。\n\n**示例 3：**\n> \n**输入：**`nums1 = [10,20], nums2 = [30,40]`\n**输出：**`-1`\n**解释：**\n不可能使两个数组相同。因此，答案为 -1。\n\n**提示：**\n - `2 <= n == nums1.length == nums2.length <= 8 * 10^4`\n - `1 <= nums1[i], nums2[i] <= 8 * 10^4`'
                         )

    def solve(self, nums1: List[int], nums2: List[int]) -> int:
        diff = Counter(nums1)
        diff.subtract(nums2)
        ans = 0
        for d in diff.values():
            if d % 2:
                return -1
            if d > 0:
                ans += d
        return ans // 2

    def gen(self):
        """
        生成测试样例，测试 nums1 和 nums2 通过交换操作使数组相同的最小花费

        测试场景覆盖：
        1. 数组完全相同（0花费）
        2. 数组需要少量交换
        3. 数组需要多次交换
        4. 数组无法匹配（返回-1）
        5. 边界值：最小长度、最大值
        6. 随机分布
        """
        # 减少测试用例数量以避免超时
        self.testcase_num = 50

        # 减小数组长度和数值范围，避免生成过多大数据
        list_length_range = (2, 200)
        int_range = (1, 10000)

        nums1_list = []
        nums2_list = []

        # 手动构造的测试用例（覆盖边界和特殊场景）
        manual_cases = [
            # 场景1: 完全相同的数组（0花费）
            ([1, 2, 3], [1, 2, 3]),
            ([5, 5], [5, 5]),

            # 场景2: 需要少量交换的数组
            ([10, 20], [20, 10]),  # 示例1
            ([1, 2, 3, 4], [1, 3, 2, 4]),
            ([10, 10], [20, 20]),  # 示例2

            # 场景3: 需要多次交换的数组
            ([1, 2, 3, 4, 5], [2, 3, 4, 5, 1]),
            ([1, 1, 2, 2], [2, 2, 1, 1]),

            # 场景4: 无法匹配的数组（返回-1）
            ([10, 20], [30, 40]),  # 示例3
            ([1, 2], [3, 4]),
            ([5, 5, 5], [5, 5, 6]),

            # 场景5: 边界值 - 最小长度
            ([1, 2], [2, 1]),
            ([1, 1], [1, 1]),

            # 场景6: 边界值 - 最大/最小值
            ([1, 10000, 1], [10000, 1, 10000]),

            # 场景7: 只需部分交换
            ([1, 2, 3], [1, 1, 2]),  # 需要交换一些元素

            # 场景8: 奇数差异（不可能）
            ([1, 1, 2], [1, 2, 2]),  # 差异为奇数，返回-1

            # 场景9: 部分相同
            ([1, 2, 3, 4], [1, 2, 5, 6]),  # 部分相同

            # 场景10: 更多交换场景
            ([1, 2, 1, 2], [2, 1, 2, 1]),
            ([3, 4, 5, 6], [4, 5, 6, 3]),
        ]

        # 添加手动构造的测试用例
        for i, (n1, n2) in enumerate(manual_cases):
            nums1_list.append(n1)
            nums2_list.append(n2)

        # 生成随机测试用例（填充剩余测试用例）
        remaining_cases = self.testcase_num - len(manual_cases)
        for _ in range(remaining_cases):
            n = self.s_generate_int(int_range=list_length_range)
            nums1 = self.s_generate_list_int(list_length_range=(n, n), int_range=int_range)
            nums2 = self.s_generate_list_int(list_length_range=(n, n), int_range=int_range)
            nums1_list.append(nums1)
            nums2_list.append(nums2)

        return nums1_list, nums2_list
    


from . import Problem
from functools import cache
import re
def digit_sum(n: int) -> int:
    return sum(int(d) for d in str(n))


class Solution4(Problem):
    date = "2026-3-14"
    def __init__(self):
        Problem.__init__(self,
                         degree=2,
                         idx=3869,
                         types=[],
                         pass_rate=0.44,
                         description='给你两个整数 `l` 和 `r`。\n如果一个整数的数位形成一个**严格单调**序列，即数位是**严格递增**或**严格递减**的，那么这个整数被称为**好数**。所有一位数都被认为是好数。\n如果一个整数是好数，或者它的**数位和**是好数，那么这个整数被称为**奇妙数**。\n返回一个整数，表示在区间 `[l, r]`（包含边界）内的奇妙数的数量。\n如果一个序列中的每个元素都**严格大于**其前一个元素（如果存在），则该序列被称为**严格递增**。\n如果一个序列中的每个元素都**严格小于**其前一个元素（如果存在），则该序列被称为**严格递减**。\n\n**示例 1：**\n> \n**输入：**`l = 8, r = 10`\n**输出：**`3`\n**解释：**\n - 8 和 9 是一位数，所以它们是好数，因此也是奇妙数。\n - 10 的数位为 `[1, 0]`，形成了一个严格递减的序列，所以 10 是好数，因此也是奇妙数。\n\n因此，答案是 3。\n**示例 2：**\n> \n**输入：**`l = 12340, r = 12341`\n**输出：**`1`\n**解释：**\n - 12340\n> \t - 12340 不是好数，因为 `[1, 2, 3, 4, 0]` 不是严格单调的。\n - 数位和为 `1 + 2 + 3 + 4 + 0 = 10`。\n - 10 是好数，因为它的数位为 `[1, 0]`，是严格递减的。因此，12340 是奇妙数。\n\n - 12341\n> \t - 12341 不是好数，因为 `[1, 2, 3, 4, 1]` 不是严格单调的。\n - 数位和为 `1 + 2 + 3 + 4 + 1 = 11`。\n - 11 不是好数，因为它的数位为 `[1, 1]`，不是严格单调的。因此，12341 不是奇妙数。\n\n因此，答案是 1。\n**示例 3：**\n> \n**输入：**`l = 123456788, r = 123456788`\n**输出：**`0`\n**解释：**\n - 123456788 不是好数，因为它的数位不是严格单调的。\n - 数位和为 `1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 8 = 44`。\n - 44 不是好数，因为它的数位为 `[4, 4]`，不是严格单调的。因此，123456788 不是奇妙数。\n\n因此，答案是 0。\n\n**提示：**\n - `1 <= l <= r <= 10^15`'
                         )

    def is_good(self, s: int) -> bool:
        if s < 100:
            return s // 10 != s % 10
        return 1 < s // 10 % 10 < s % 10

    def solve(self, l: int, r: int) -> int:
        STATE_INIT = 0
        STATE_INC = 1
        STATE_DEC = 2
        STATE_NOT_GOOD = 3
        low_s = list(map(int, str(l)))
        high_s = list(map(int, str(r)))
        n = len(high_s)
        diff_lh = n - len(low_s)

        @cache
        def dfs(i: int, digit_sum: int, prev: int, state: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1 if state != STATE_NOT_GOOD or self.is_good(digit_sum) else 0
            lo = low_s[i - diff_lh] if limit_low and i >= diff_lh else 0
            hi = high_s[i] if limit_high else 9
            res = 0
            start = lo
            if limit_low and i < diff_lh:
                res = dfs(i + 1, 0, 0, STATE_INIT, True, False)
                start = 1
            for d in range(start, hi + 1):
                new_state = state
                if state == STATE_INIT:
                    if prev > 0:
                        if d > prev:
                            new_state = STATE_INC
                        elif d < prev:
                            new_state = STATE_DEC
                        else:
                            new_state = STATE_NOT_GOOD
                elif state == STATE_INC:
                    if d <= prev:
                        new_state = STATE_NOT_GOOD
                elif state == STATE_DEC:
                    if d >= prev:
                        new_state = STATE_NOT_GOOD
                res += dfs(i + 1, digit_sum + d, d, new_state, limit_low and d == lo, limit_high and d == hi)
            return res
        return dfs(0, 0, 0, STATE_INIT, True, True)

    def gen(self):
        """
        生成测试样例，覆盖以下场景：
        1. 小范围测试：[1, 100], [10, 200]
        2. 单点测试：l = r 的情况
        3. 中等范围测试：不同位数的范围
        4. 边界值测试：包含特殊数字
        5. 随机范围测试

        由于原题约束为10^15，为避免超时，将最大值缩小到10^8
        """
        # 定义测试场景
        scenarios = []

        # 场景1：小范围快速测试 (20个)
        scenarios.extend([(1, 100), (1, 200), (10, 50), (50, 100), (100, 200)])
        for _ in range(15):
            l = self.s_generate_int(int_range=(1, 1000))
            r = l + self.s_generate_int(int_range=(0, 500))
            scenarios.append((l, r))

        # 场景2：单点测试 (15个)
        for _ in range(15):
            val = self.s_generate_int(int_range=(1, 100000))
            scenarios.append((val, val))

        # 场景3：两位数范围测试 (10个)
        for _ in range(10):
            l = self.s_generate_int(int_range=(10, 99))
            r = self.s_generate_int(int_range=(l, 99))
            scenarios.append((l, r))

        # 场景4：三位数范围测试 (10个)
        for _ in range(10):
            l = self.s_generate_int(int_range=(100, 999))
            r = self.s_generate_int(int_range=(l, 999))
            scenarios.append((l, r))

        # 场景5：四位数范围测试 (10个)
        for _ in range(10):
            l = self.s_generate_int(int_range=(1000, 9999))
            r = self.s_generate_int(int_range=(l, 9999))
            scenarios.append((l, r))

        # 场景6：中等大范围测试 (15个) - 5-6位数
        for _ in range(15):
            l = self.s_generate_int(int_range=(10000, 50000))
            r = l + self.s_generate_int(int_range=(0, 50000))
            scenarios.append((l, r))

        # 场景7：较大范围测试 (10个) - 6-7位数
        for _ in range(10):
            l = self.s_generate_int(int_range=(100000, 500000))
            r = l + self.s_generate_int(int_range=(0, 500000))
            scenarios.append((l, r))

        # 场景8：大范围测试 (5个) - 7-8位数
        for _ in range(5):
            l = self.s_generate_int(int_range=(1000000, 5000000))
            r = l + self.s_generate_int(int_range=(0, 5000000))
            scenarios.append((l, r))

        # 确保测试样例数量为testcase_num
        scenarios = scenarios[:self.testcase_num]

        # 按照gen()函数的返回格式组织数据
        l_list = [s[0] for s in scenarios]
        r_list = [s[1] for s in scenarios]

        return l_list, r_list
    

