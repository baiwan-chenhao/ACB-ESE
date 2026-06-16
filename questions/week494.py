

from . import Problem
import re


class Solution1(Problem):
    date = "2026-3-22"
    def __init__(self):
        Problem.__init__(self,
                         degree=0,
                         idx=3875,
                         types=[],
                         pass_rate=0.75,
                         description='给你一个长度为 `n` 的数组 `nums1`，其中包含**互不相同**的整数。\n你需要构造另一个长度为 `n` 的数组 `nums2`，使得 `nums2` 中的元素要么全部为**奇数**，要么全部为**偶数**。\n对于每个下标 `i`，你必须从以下两种选择中**任选其一**（顺序不限）：\n - `nums2[i] = nums1[i]`\n - `nums2[i] = nums1[i] - nums1[j]`，其中 `j != i`\n\n如果能够构造出满足条件的数组，则返回 `true`；否则，返回 `false`。\n\n**示例 1：**\n> \n**输入：**`nums1 = [2,3]`\n**输出：**`true`\n**解释：**\n - 选择 `nums2[0] = nums1[0] - nums1[1] = 2 - 3 = -1`。\n - 选择 `nums2[1] = nums1[1] = 3`。\n - `nums2 = [-1, 3]`，两个元素均为奇数。因此答案为 `true`。\n\n**示例 2：**\n> \n**输入：**`nums1 = [4,6]`\n**输出：**`true`\n**解释：**\u200b\u200b\u200b\u200b\u200b\u200b\u200b\n - 选择 `nums2[0] = nums1[0] = 4`。\n - 选择 `nums2[1] = nums1[1] = 6`。\n - `nums2 = [4, 6]`，两个元素均为偶数。因此答案为 `true`。\n\n**提示：**\n - `1 <= n == nums1.length <= 100`\n - `1 <= nums1[i] <= 100`\n - `nums1` 中的所有整数互不相同。'
                         )

    def solve(self, nums1: list[int]) -> bool:
        True

    def gen(self):
        """
        生成测试样例。

        题目分析：
        - 给定nums1数组，需要判断能否构造nums2数组使其全部为奇数或全部为偶数
        - 每个位置i可以选择 nums2[i] = nums1[i] 或 nums2[i] = nums1[i] - nums1[j] (j != i)

        算法思路：
        - 如果nums1中同时存在奇数和偶数，可以构造全奇或全偶，返回True
        - 如果nums1全是奇数，只能构造全奇数，返回True
        - 如果nums1全是偶数，只能构造全偶数，返回True
        - 因此只要nums1长度 >= 1，总是返回True

        测试覆盖：
        - 边界情况：长度为1的数组，最大长度数组
        - 不同奇偶性组合：全奇、全偶、奇偶混合
        - 数值范围：最小值、最大值
        """
        # 减少测试用例数量以确保效率
        self.testcase_num = min(self.testcase_num, 50)

        # 生成列表：长度范围(1, 100)，数值范围(1, 100)，元素互不相同
        return [self.generate_list_int(
            list_length_range=(1, 100),
            int_range=(1, 100),
            different=True
        )]
    

import math
import random
from . import Problem
from typing import List
import re
from math import inf


class Solution2(Problem):
    date = "2026-3-22"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3876,
                         types=[],
                         pass_rate=0.51,
                         description='给你一个长度为 `n` 的数组 `nums1`，其中包含**互不相同**的整数。\n你需要构造另一个长度为 `n` 的数组 `nums2`，使得 `nums2` 中的元素要么全部为**奇数**，要么全部为**偶数**。\n对于每个下标 `i`，你必须从以下两种选择中**任选其一**（顺序不限）：\n - `nums2[i] = nums1[i]`\u200b\u200b\u200b\u200b\u200b\u200b\u200b\n - `nums2[i] = nums1[i] - nums1[j]`，其中 `j != i`，且满足 `nums1[i] - nums1[j] >= 1`\n\n如果能够构造出满足条件的数组，则返回 `true`；否则，返回 `false`。\n\n**示例 1：**\n> \n**输入：**`nums1 = [1,4,7]`\n**输出：**`true`\n**解释：**\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\n - 设置 `nums2[0] = nums1[0] = 1`。\n - 设置 `nums2[1] = nums1[1] - nums1[0] = 4 - 1 = 3`。\n - 设置 `nums2[2] = nums1[2] = 7`。\n - `nums2 = [1, 3, 7]`，所有元素均为奇数。因此答案为 `true`。\n\n**示例 2：**\n> \n**输入：**`nums1 = [2,3]`\n**输出：**`false`\n**解释：**\n无法构造出满足所有元素奇偶性相同的 `nums2`。因此答案为 `false`。\n**示例 3：**\n> \n**输入：**`nums1 = [4,6]`\n**输出：**`true`\n**解释：**\n - 设置 `nums2[0] = nums1[0] = 4`。\n - 设置 `nums2[1] = nums1[1] = 6`。\n - `nums2 = [4, 6]`，所有元素均为偶数。因此答案为 `true`。\n\n**提示：**\n - `1 <= n == nums1.length <= 10^5`\n - `1 <= nums1[i] <= 10^9`\n - `nums1` 中的所有整数互不相同。'
                         )

    def solve(self, nums1: List[int]) -> bool:
        mn = [inf] * 2
        for x in nums1:
            mn[x % 2] = min(mn[x % 2], x)
        return mn[1] == inf or mn[0] > mn[1]

    def gen(self):
        """
        为奇偶数组构造问题生成测试样例。

        生成策略：
        1. 边界情况（20%）：单元素、全奇数、全偶数
        2. 正常随机情况（50%）：混合奇偶数的随机数组
        3. 特殊结构（30%）：
           - 连续整数数组（检验临界条件）
           - 全奇数+一个较大偶数（应返回true）
           - 全偶数+一个较小奇数（应返回false）
        """
        # 减少测试数量以避免超时（原题长度可达10^5）
        testcase_num = 100
        self.testcase_num = testcase_num
        self.list_length_range = (2, 100)
        self.int_range = (1, 1000)

        cases_per_type = testcase_num // 5  # 每种类型约20个
        test_cases = []

        # 类型1: 边界情况 - 单元素（应全返回true）
        for _ in range(5):
            test_cases.append(([self.s_generate_int(int_range=self.int_range)],))

        # 类型2: 全奇数（应返回true）
        for _ in range(cases_per_type):
            length = self.s_generate_int(int_range=(2, 20))
            # 生成奇数：奇数 = 2*x + 1
            arr = [2 * self.s_generate_int(int_range=(0, 100)) + 1 for _ in range(length)]
            test_cases.append((arr,))

        # 类型3: 全偶数（应返回true）
        for _ in range(cases_per_type):
            length = self.s_generate_int(int_range=(2, 20))
            # 生成偶数：偶数 = 2*x
            arr = [2 * self.s_generate_int(int_range=(1, 100)) for _ in range(length)]
            test_cases.append((arr,))

        # 类型4: 混合奇偶数 - 最小偶数 > 最小奇数（应返回true）
        for _ in range(cases_per_type):
            length = self.s_generate_int(int_range=(3, 20))
            min_odd = 2 * self.s_generate_int(int_range=(0, 50)) + 1
            # 最小偶数必须大于最小奇数
            min_even = min_odd + 1 if min_odd % 2 == 0 else min_odd + 1
            if min_even % 2 != 0:
                min_even += 1

            # 包含最小奇数
            arr = [min_odd]
            # 添加其他奇数（都大于min_odd）
            for _ in range(length // 3):
                arr.append(min_odd + 2 * (self.s_generate_int(int_range=(1, 10)) + 1))
            # 添加偶数（都大于min_odd）
            for _ in range(length - len(arr)):
                arr.append(min_even + 2 * self.s_generate_int(int_range=(0, 10)))

            # 确保元素互不相同
            arr = list(dict.fromkeys(arr))  # 去重
            random.shuffle(arr)
            test_cases.append((arr,))

        # 类型5: 混合奇偶数 - 最小偶数 <= 最小奇数（应返回false）
        for _ in range(cases_per_type):
            length = self.s_generate_int(int_range=(3, 20))
            min_even = 2 * self.s_generate_int(int_range=(1, 50))
            # 最小奇数必须大于或等于最小偶数
            min_odd = min_even + 1 if min_even % 2 == 1 else min_even + 1
            if min_odd % 2 != 1:
                min_odd += 1

            # 包含最小偶数
            arr = [min_even]
            # 添加其他偶数（都大于min_even）
            for _ in range(length // 3):
                arr.append(min_even + 2 * (self.s_generate_int(int_range=(1, 10)) + 1))
            # 添加奇数（都 >= min_odd > min_even）
            for _ in range(length - len(arr)):
                arr.append(min_odd + 2 * self.s_generate_int(int_range=(0, 10)))

            # 确保元素互不相同
            arr = list(dict.fromkeys(arr))
            random.shuffle(arr)
            test_cases.append((arr,))

        # 填充剩余测试用例为随机混合情况
        while len(test_cases) < testcase_num:
            length = self.s_generate_int(int_range=(3, 20))
            arr = self.s_generate_list_int(list_length_range=(length, length), 
                                          int_range=(1, 1000), 
                                          different=True)
            test_cases.append((arr,))

        # 只取前testcase_num个
        test_cases = test_cases[:testcase_num]

        # 转换为按参数组织的格式
        rets = [[]]
        for case in test_cases:
            rets[0].append(case[0])

        return tuple(rets)
    

import math
import random
from . import Problem
from typing import List
import re
from math import inf


class Solution3(Problem):
    date = "2026-3-22"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3877,
                         types=[],
                         pass_rate=0.41,
                         description='给你一个整数数组 `nums` 和一个整数 `target`。\n你可以从 `nums` 中移除**任意**数量的元素（可能为零）。\n返回使剩余元素的**按位异或和**等于 `target` 所需的**最小**移除次数。如果无法达到 `target`，则返回 -1。\n空数组的按位异或和为 0。\n\n**示例 1：**\n> \n**输入：**`nums = [1,2,3], target = 2`\n**输出：**`1`\n**解释：**\n - 移除 `nums[1] = 2` 后剩余 `[nums[0], nums[2]] = [1, 3]`。\n - `[1, 3]` 的异或和为 2，等于 `target`。\n - 无法在少于 1 次移除的情况下达到异或和 = 2，因此答案为 1。\n\n**示例 2：**\n> \n**输入：**`nums = [2,4], target = 1`\n**输出：**`-1`\n**解释：**\n无法通过移除元素来达到 `target`。因此，答案为 -1。\n**示例 3：**\n> \n**输入：**`nums = [7], target = 7`\n**输出：**`0`\n**解释：**\n所有元素的异或和为 `nums[0] = 7`，等于 `target`。因此，无需移除任何元素。\n\n**提示：**\n - `1 <= nums.length <= 40`\n - `0 <= nums[i] <= 10^4`\n - `0 <= target <= 10^4`'
                         )

    def solve(self, nums: List[int], target: int) -> int:
        m = max(nums).bit_length()
        if 1 << m <= target:
            return -1
        n = len(nums)
        f = [[-inf] * (1 << m) for _ in range(n + 1)]
        f[0][0] = 0
        for i, x in enumerate(nums):
            for j in range(1 << m):
                f[i + 1][j] = max(f[i][j], f[i][j ^ x] + 1)
        if f[n][target] < 0:
            return -1
        return len(nums) - f[n][target]

    def gen(self):
        """
        生成测试样例。

        测试样例分为以下几个部分：
        1. 边界测试（15个）：覆盖最小/最大数组长度、特殊target值
        2. 随机测试（10个）：随机生成的数组和target
        3. 特殊结构测试（5个）：全相同、0元素、需全部移除等场景
        """
        testcase_num = self.testcase_num
        if testcase_num != 100:
            testcase_num = 30

        nums_list = []
        target_list = []

        # 使用已定义的生成方法
        random.seed(self.seed)

        # ===== 边界测试 (15个) =====
        # 1-3. 最小数组长度1的情况，不同target
        nums_list.extend([
            [7],      # target等于唯一元素
            [5],      # target不等于唯一元素
            [0],      # 元素为0
        ])
        target_list.extend([7, 3, 0])

        # 4-6. 小数组，target=0
        nums_list.extend([
            [1, 2, 3],
            [5, 5],
            [0, 1, 2, 3],
        ])
        target_list.extend([0, 0, 0])

        # 7-9. 中等长度数组
        nums_list.extend([
            [1, 2, 3, 4, 5],
            [7, 7, 7, 7, 7],
            [0, 0, 0, 0, 0],
        ])
        target_list.extend([3, 7, 0])

        # 10-12. 最大长度附近（用较小的数值范围避免超大计算）
        large_len = 15
        nums_list.extend([
            [random.randint(0, 255) for _ in range(large_len)],
            [random.randint(0, 255) for _ in range(large_len)],
            [1, 2, 3] + [0] * (large_len - 3),
        ])
        target_list.extend([
            random.randint(0, 255),
            random.randint(0, 255),
            3,
        ])

        # 13-15. 特殊边界值
        nums_list.extend([
            [1023],           # 2^10 - 1
            [256, 256, 256],  # 2^8
            [10000, 10000],   # 大数值
        ])
        target_list.extend([1023, 256, 0])

        # ===== 随机测试 (10个) =====
        # 使用中等到较大的随机数组
        for _ in range(10):
            length = random.randint(5, 15)
            nums = [random.randint(0, 511) for _ in range(length)]
            target = random.randint(0, 511)
            nums_list.append(nums)
            target_list.append(target)

        # ===== 特殊结构测试 (5个) =====
        # 26. 无需移除：整个数组异或和即为target
        arr = [random.randint(1, 255) for _ in range(5)]
        xor_sum = 0
        for x in arr:
            xor_sum ^= x
        nums_list.append(arr)
        target_list.append(xor_sum)

        # 27. 需移除全部：只能通过空数组达到target=0
        arr = [random.randint(1, 255) for _ in range(5)]
        nums_list.append(arr)
        target_list.append(0)

        # 28. 全相同元素
        val = random.randint(1, 255)
        arr = [val] * 5
        nums_list.append(arr)
        target_list.append(val if val % 2 == 1 else 0)

        # 29. 两个元素，无法达到target
        nums_list.append([2, 4])
        target_list.append(1)

        # 30. 示例中的情况
        nums_list.append([1, 2, 3])
        target_list.append(2)

        return nums_list, target_list
    

import random
from . import Problem
from typing import List


class Solution4(Problem):
    date = "2026-3-22"
    def __init__(self):
        Problem.__init__(self,
                         degree=2,
                         idx=3878,
                         types=[],
                         pass_rate=0.39,
                         description='给你一个整数数组 `nums`。\n如果一个**子数组**中所有元素的**按位或**等于该子数组中**至少出现一次**的元素，则称其为**好**子数组。\n返回 `nums` 中好子数组的数量。\n**子数组**是数组中一段连续的**非空**元素序列。\n这里，两个整数 `a` 和 `b` 的按位或表示为 `a | b`。\n\n**示例 1：**\n> \n**输入：**`nums = [4,2,3]`\n**输出：**`4`\n**解释：**\n`nums` 的子数组有：\n| 子数组 | 按位或 | 存在于子数组中 |\n| --- | --- | --- |\n| `[4]` | `4 = 4` | 是 |\n| `[2]` | `2 = 2` | 是 |\n| `[3]` | `3 = 3` | 是 |\n| `[4, 2]` | `4 | 2 = 6` | 否 |\n| `[2, 3]` | `2 | 3 = 3` | 是 |\n| `[4, 2, 3]` | `4 | 2 | 3 = 7` | 否 |\n\n因此，`nums` 的好子数组是 `[4]`、`[2]`、`[3]` 和 `[2, 3]`。所以答案为 4。\n**示例 2：**\n> \n**输入：**`nums = [1,3,1]`\n**输出：**`6`\n**解释：**\n`nums` 中任何包含 3 的子数组的按位或都等于 3，只包含 1 的子数组的按位或都等于 1。\n在这两种情况下，结果都存在于子数组中，因此所有子数组都是好子数组，答案为 6。\n\n**提示：**\n - `1 <= nums.length <= 10^5`\n - `0 <= nums[i] <= 10^9`'
                         )

    def solve(self, nums: List[int]) -> int:
        or_left = []
        last = {}
        ans = 0
        for i, x in enumerate(nums):
            last[x] = i
            for p in or_left:
                p[0] |= x
            or_left.append([x, i])
            idx = 1
            for j in range(1, len(or_left)):
                if or_left[j][0] != or_left[j - 1][0]:
                    or_left[idx] = or_left[j]
                    idx += 1
            del or_left[idx:]
            for k, (or_val, left) in enumerate(or_left):
                right = or_left[k + 1][1] - 1 if k < len(or_left) - 1 else i
                j = last.get(or_val, -1)
                if j >= left:
                    ans += min(right, j) - left + 1
        return ans

    def gen(self):
            """
            生成测试样例来测试好子数组的数量。

            策略：
            1. 边界情况：最小长度（1）、单元素数组
            2. 特殊结构：全相同元素、全0、全1、特定位模式
            3. 不同长度范围：小规模（1-10）、中规模（10-100）、较大规模（100-1000）
            4. 随机数据：随机长度和随机值

            注意：虽然题目允许长度达到10^5，但为了确保参考代码在100秒内完成测试，
            我们将最大长度限制在2000以内。
            """
            # 设置随机种子
            random.seed(self.seed)

            # 定义测试用例分配
            # 总共100个测试用例
            # 边界用例：20个（单元素、全相同、全0、全1等）
            # 特殊模式：20个（递增、递减、交替、特定位值）
            # 随机用例：60个（不同长度和随机值）

            cases = []
            case_idx = 0

            # === 边界用例 (20个) ===
            # 单元素数组 (5个)
            for _ in range(5):
                cases.append([random.randint(0, 1000)])
                case_idx += 1

            # 全相同元素 (5个)
            for _ in range(5):
                val = random.randint(0, 100)
                length = random.randint(2, 20)
                cases.append([val] * length)
                case_idx += 1

            # 全0 (3个)
            for length in [1, 10, 100]:
                cases.append([0] * length)
                case_idx += 1

            # 全1 (3个)
            for length in [1, 10, 100]:
                cases.append([1] * length)
                case_idx += 1

            # 两个元素的数组 (4个)
            for _ in range(4):
                cases.append([random.randint(0, 1000), random.randint(0, 1000)])
                case_idx += 1

            # === 特殊模式用例 (20个) ===
            # 严格递增 (5个)
            for _ in range(5):
                length = random.randint(5, 30)
                start = random.randint(0, 100)
                cases.append(list(range(start, start + length)))
                case_idx += 1

            # 严格递减 (5个)
            for _ in range(5):
                length = random.randint(5, 30)
                start = random.randint(50, 150)
                cases.append(list(range(start, start - length, -1)))
                case_idx += 1

            # 0/1交替 (5个)
            for _ in range(5):
                length = random.randint(5, 30)
                cases.append([i % 2 for i in range(length)])
                case_idx += 1

            # 2的幂次 (5个)
            for _ in range(5):
                length = random.randint(5, 30)
                cases.append([1 << random.randint(0, 10) for _ in range(length)])
                case_idx += 1

            # === 随机用例 (60个) ===
            # 分为3个长度范围，各20个
            for length_min, length_max in [(2, 10), (11, 100), (101, 2000)]:
                for _ in range(20):
                    length = random.randint(length_min, length_max)
                    cases.append([random.randint(0, 10000) for _ in range(length)])
                    case_idx += 1

            # 按参数维度组织返回值
            # 只有一个参数 nums，所以返回一个包含一个列表的元组
            return (cases,)
    

