
import random
from . import Problem
import re


class Solution1(Problem):
    date = "2026-4-11"
    def __init__(self):
        Problem.__init__(self,
                         degree=0,
                         idx=3894,
                         types=[],
                         pass_rate=0.84,
                         description='给你一个整数 `timer`，表示交通信号灯上的剩余时间（以秒为单位）。\n信号灯遵循以下规则：\n - 如果 `timer == 0`，信号灯为 `"Green"`\n - 如果 `timer == 30`，信号灯为 `"Orange"`\n - 如果 `30 < timer <= 90`，信号灯为 `"Red"`\n\n返回信号灯的当前状态。如果均不满足上述条件，返回 `"Invalid"`。\n\n**示例 1：**\n> \n**输入：**`timer = 60`\n**输出：**`"Red"`\n**解释：**\n因为 `timer = 60`，且 `30 < timer <= 90`，所以答案是 `"Red"`。\n**示例 2：**\n> \n**输入：**`timer = 5`\n**输出：**`"Invalid"`\n**解释：**\n因为 `timer = 5`，不满足任何给定的条件，所以答案是 `"Invalid"`。\n\n**提示：**\n - `0 <= timer <= 1000`'
                         )

    def solve(self, timer: int) -> str:
        if timer == 0:
            return 'Green'
        if timer == 30:
            return 'Orange'
        if 30 < timer <= 90:
            return 'Red'
        return 'Invalid'


    def gen(self):
        """
        生成测试样例，覆盖交通信号灯问题的所有情况：

        覆盖场景：
        1. 边界值测试（20个样例）：
           - timer = 0 (Green)
           - timer = 30 (Orange)  
           - timer = 31 (Red边界)
           - timer = 90 (Red边界)
           - timer = 91 (Invalid边界)
           - timer = 1000 (Invalid最大值)
           - 其他边界附近的值

        2. Red区间测试（40个样例）：
           - 30 < timer <= 90 的随机值

        3. Invalid区间测试（40个样例）：
           - (0, 30) 和 (90, 1000] 的随机值
        """
        testcases = []

        # 1. 边界值测试（20个样例）
        # 明确的边界值
        boundary_values = [0, 30, 31, 90, 91, 1000, 1, 29, 32, 89, 92, 500, 999, 2, 28, 33, 88, 93, 250, 750]
        testcases.extend(boundary_values)

        # 2. Red区间测试（40个样例）：30 < timer <= 90
        random.seed(self.seed)
        for _ in range(40):
            timer = random.randint(31, 90)
            testcases.append(timer)

        # 3. Invalid区间测试（40个样例）
        # (0, 30) 区间：20个样例
        for _ in range(20):
            timer = random.randint(1, 29)
            testcases.append(timer)

        # (90, 1000] 区间：20个样例
        for _ in range(20):
            timer = random.randint(92, 1000)
            testcases.append(timer)

        return (testcases,)
    


from . import Problem
from typing import List
import re
from itertools import count


class Solution2(Problem):
    date = "2026-4-11"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3895,
                         types=[],
                         pass_rate=0.88,
                         description='给你一个整数数组 `nums` 和一个整数 `digit`。\n返回在 `nums` 所有元素的十进制表示中 `digit` 出现的总次数。\n\n**示例 1：**\n> \n**输入：**`nums = [12,54,32,22], digit = 2`\n**输出：**`4`\n**解释：**\n数字 2 在 12 和 32 中出现一次，在 22 中出现两次。因此，数字 2 出现的总次数为 4。\n**示例 2：**\n> \n**输入：**`nums = [1,34,7], digit = 9`\n**输出：**`0`\n**解释：**\n数字 9 没有出现在 `nums` 中任何元素的十进制表示中，所以数字 9 出现的总次数为 0。\n\n**提示：**\n - `1 <= nums.length <= 1000`\n - `1 <= nums[i] <= 10^6`\n - `0 <= digit <= 9`'
                         )

    def solve(self, nums: List[int], digit: int) -> int:
        digit = str(digit)
        return sum((str(x).count(digit) for x in nums))

    def gen(self):
        """
        为数字出现次数统计问题生成测试样例。

        覆盖策略：
        1. 边界值：最小长度数组(1)、最大长度数组、digit=0、digit=9
        2. 特殊结构：
           - digit完全不出现
           - 数字中多次出现digit（如222、1000、2020）
           - 所有数字都包含digit
           - digit=0的情况（如100、1000、20000）
        3. 正常分布：随机数组和随机digit
        """
        nums_list = []
        digit_list = []

        # 为避免超时，适当减小数据规模
        # 1-20: 边界值测试
        # 最小长度数组
        for _ in range(5):
            nums_list.append([self.s_generate_int(int_range=(1, 1000000))])
            digit_list.append(self.s_generate_int(int_range=(0, 9)))

        # 数组元素为边界值
        for _ in range(5):
            nums_list.append([1, 1000000] * 5)
            digit_list.append(self.s_generate_int(int_range=(0, 9)))

        # digit=0和digit=9的边界情况
        for _ in range(5):
            nums_list.append(self.s_generate_list_int(list_length_range=(10, 50), int_range=(1, 100000)))
            digit_list.append(0)

        for _ in range(5):
            nums_list.append(self.s_generate_list_int(list_length_range=(10, 50), int_range=(1, 100000)))
            digit_list.append(9)

        # 21-40: 特殊结构测试
        # digit完全不出现的情况
        digit = 5
        for _ in range(5):
            nums = []
            for _ in range(20):
                num = self.s_generate_int(int_range=(10000, 99999))
                # 确保数字不包含digit
                while str(digit) in str(num):
                    num = self.s_generate_int(int_range=(10000, 99999))
                nums.append(num)
            nums_list.append(nums)
            digit_list.append(digit)

        # 数字中多次出现digit（如222、1000、2020、5555）
        for digit in [1, 2, 5]:
            for _ in range(3):
                nums = [int(str(digit) * self.s_generate_int(int_range=(2, 6))) for _ in range(15)]
                nums_list.append(nums)
                digit_list.append(digit)

        # 所有数字都包含digit
        digit = 3
        for _ in range(4):
            nums = []
            for _ in range(15):
                # 生成包含digit的数字
                num_str = str(digit) + str(self.s_generate_int(int_range=(0, 9999)))
                nums.append(int(num_str))
            nums_list.append(nums)
            digit_list.append(digit)

        # digit=0的特殊情况（如100、1000、20000）
        digit = 0
        for _ in range(5):
            nums = []
            for _ in range(15):
                # 生成包含0的数字
                zeros_count = self.s_generate_int(int_range=(1, 4))
                base = self.s_generate_int(int_range=(1, 9))
                nums.append(base * (10 ** zeros_count))
            nums_list.append(nums)
            digit_list.append(digit)

        # 41-100: 随机测试用例
        for _ in range(60):
            nums_list.append(self.s_generate_list_int(list_length_range=(1, 100), int_range=(1, 100000)))
            digit_list.append(self.s_generate_int(int_range=(0, 9)))

        return nums_list, digit_list
    

import math
from . import Problem
from typing import List
import re
from math import isqrt
MX = 100004
is_prime = [0, 0] + [1] * (MX - 2)
for i in range(2, isqrt(MX) + 1):
    if is_prime[i]:
        for j in range(i * i, MX, i):
            is_prime[j] = 0

class Solution3(Problem):
    date = "2026-4-11"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3896,
                         types=[],
                         pass_rate=0.52,
                         description='给你一个整数数组 `nums`。\n如果满足以下条件，则认为数组是**交替质数**数组：\n -**偶数**下标（从 0 开始）处的元素是**质数**。\n -**奇数**下标处的元素是**非质数**。\n\n在一次操作中，你可以将任何元素**增加**1。\n返回将 `nums` 转换为**交替质数**数组所需的**最少**操作次数。\n**质数**是指大于 1 且仅有两个因数（1 和其本身）的自然数。\n\n**示例 1：**\n> \n**输入：**`nums = [1,2,3,4]`\n**输出：**`3`\n**解释：**\n - 下标 0 处的元素必须是质数。将 `nums[0] = 1` 增加到 2，使用 1 次操作。\n - 下标 1 处的元素必须是非质数。将 `nums[1] = 2` 增加到 4，使用 2 次操作。\n - 下标 2 处的元素已经是质数。\n - 下标 3 处的元素已经是非质数。\n\n总操作次数 = `1 + 2 = 3`。\n**示例 2：**\n> \n**输入：**`nums = [5,6,7,8]`\n**输出：**`0`\n**解释：**\n - 下标 0 和 2 处的元素已经是质数。\n - 下标 1 和 3 处的元素已经是非质数。\n\n不需要任何操作。\n**示例 3：**\n> \n**输入：**`nums = [4,4]`\n**输出：**`1`\n**解释：**\n - 下标 0 处的元素必须是质数。将 `nums[0] = 4` 增加到 5，使用 1 次操作。\n - 下标 1 处的元素已经是非质数。\n\n总操作次数 = 1。\n\n**提示：**\n - `1 <= nums.length <= 10^5`\n - `1 <= nums[i] <= 10^5`'
                         )

    def solve(self, nums: List[int]) -> int:
        ans = 0
        for i, x in enumerate(nums):
            while is_prime[x] == i % 2:
                ans += 1
                x += 1
        return ans

    def gen(self):
        import random

        # 减小测试规模以避免超时
        # 数组长度范围设置为 (1, 1000)
        # 元素值范围设置为 (1, 10000)
        # testcase_num 设置为 50 以避免超时
        self.testcase_num = 50

        # 重新设置种子以确保可复现性
        random.seed(self.seed)

        test_cases = []

        # 1. 边界情况 - 小长度数组 (5个)
        for length in [1, 2, 3, 4, 5]:
            arr = [random.randint(1, 100) for _ in range(length)]
            test_cases.append(arr)

        # 2. 已经满足条件的数组 (5个)
        # 偶数下标是质数，奇数下标是非质数
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        non_primes = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16]
        for _ in range(5):
            length = random.randint(5, 20)
            arr = []
            for i in range(length):
                if i % 2 == 0:
                    arr.append(random.choice(primes))
                else:
                    arr.append(random.choice(non_primes))
            test_cases.append(arr)

        # 3. 需要大量操作的数组 (10个)
        # 偶数下标用大非质数，奇数下标用质数
        for _ in range(10):
            length = random.randint(5, 50)
            arr = []
            for i in range(length):
                if i % 2 == 0:
                    arr.append(10000)  # 大非质数，需要多次加到下一个质数
                else:
                    arr.append(2)  # 质数，需要加到非质数
            test_cases.append(arr)

        # 4. 全相同元素的数组 (10个)
        for val in [1, 2, 3, 4, 5]:
            for length in [5, 10]:
                arr = [val] * length
                test_cases.append(arr)

        # 5. 随机数组 (15个)
        for _ in range(15):
            length = random.randint(10, 100)
            arr = [random.randint(1, 1000) for _ in range(length)]
            test_cases.append(arr)

        # 如果还不足，用随机数组补充
        while len(test_cases) < 50:
            length = random.randint(1, 500)
            arr = [random.randint(1, 5000) for _ in range(length)]
            test_cases.append(arr)

        # 返回格式：只有一个参数，返回一个包含一个列表的元组
        return (test_cases,)
    

import random
from . import Problem
from typing import List
import re
MOD = 1000000007
MX = 10001
pow2 = [1] * MX
for i in range(1, MX):
    pow2[i] = pow2[i - 1] * 2 % MOD

class Solution4(Problem):
    date = "2026-4-11"
    def __init__(self):
        Problem.__init__(self,
                         degree=2,
                         idx=3897,
                         types=[],
                         pass_rate=0.38,
                         description='给你两个整数数组 `nums1` 和 `nums0`，每个数组的大小均为 `n`。\n - `nums1[i]` 表示第 `i` 个片段中 `\'1\'` 的数量。\n - `nums0[i]` 表示第 `i` 个片段中 `\'0\'` 的数量。\n\n对于每个下标 `i`，构造一个由以下组成的二进制片段：\n - `nums1[i]` 个 `\'1\'`，后跟\n - `nums0[i]` 个 `\'0\'`。\n\n你可以以任何方式**重新排列**这些**片段**的先后顺序。重新排列后，将所有片段**连接**起来形成一个单一的二进制字符串。\n返回连接后的二进制字符串可能表示的**最大**整数值。\n由于结果可能非常大，请返回对 `10^9 + 7`**取余**后的结果。\n\n**示例 1：**\n> \n**输入：**`nums1 = [1,2], nums0 = [1,0]`\n**输出：**`14`\n**解释：**\n - 在下标 0 处，`nums1[0] = 1` 且 `nums0[0] = 1`，因此形成的片段为 `"10"`。\n - 在下标 1 处，`nums1[1] = 2` 且 `nums0[1] = 0`，因此形成的片段为 `"11"`。\n - 将片段重新排序为 `"11"` 后跟 `"10"`，生成二进制字符串 `"1110"`。\n - 二进制数 `"1110"` 的值为 14，这是可能的最大值。\n\n**示例 2：**\n> \n**输入：**`nums1 = [3,1], nums0 = [0,3]`\n**输出：**`120`\n**解释：**\n - 在下标 0 处，`nums1[0] = 3` 且 `nums0[0] = 0`，因此形成的片段为 `"111"`。\n - 在下标 1 处，`nums1[1] = 1` 且 `nums0[1] = 3`，因此形成的片段为 `"1000"`。\n - 将片段重新排序为 `"111"` 后跟 `"1000"`，生成二进制字符串 `"1111000"`。\n - 二进制数 `"1111000"` 的值为 120，这是可能的最大值。\n\n**提示：**\n - `1 <= n == nums1.length == nums0.length <= 10^5`\n - `0 <= nums1[i], nums0[i] <= 10^4`\n - `nums1[i] + nums0[i] > 0`\n - `nums1` 和 `nums0` 中所有元素的总和不超过 2 * 10^5。'
                         )

    def solve(self, nums1: List[int], nums0: List[int]) -> int:
        idx = sorted(range(len(nums1)), key=lambda i: (nums0[i] != 0, -nums1[i], nums0[i]))
        ans = 0
        for i in idx:
            ans = ((ans + 1) * pow2[nums1[i]] - 1) * pow2[nums0[i]] % MOD
        return ans

    def gen(self):
        """
        生成测试样例：生成两个等长的数组 nums1 和 nums0

        测试策略：
        1. 边界情况测试（小规模、全1片段、全0片段等）
        2. 随机规模测试（中等规模、随机分布）
        3. 特殊结构测试（交替、极端值）

        注意：由于总元素数约束为 2 * 10^5，且 n 可达 10^5，
        为避免超时，将最大规模控制在合理范围内。
        """
        # 分配测试用例类型
        nums1_cases = []
        nums0_cases = []

        # --- 边界测试用例 (20%) ---
        # 单个片段，全是1
        nums1_cases.append([1])
        nums0_cases.append([0])

        # 单个片段，全是0
        nums1_cases.append([0])
        nums0_cases.append([1])

        # 单个片段，混合
        nums1_cases.append([3])
        nums0_cases.append([2])

        # 两个片段，一个全1，一个全0
        nums1_cases.append([5, 0])
        nums0_cases.append([0, 3])

        # 两个片段，都是混合
        nums1_cases.append([2, 1])
        nums0_cases.append([1, 3])

        # 最小长度，极端值（nums1[i] = 0, nums0[i] = 10000）
        nums1_cases.append([0])
        nums0_cases.append([100])

        # 最小长度，极端值（nums1[i] = 10000, nums0[i] = 0）
        nums1_cases.append([100])
        nums0_cases.append([0])

        # 三个片段，包含全1、全0、混合
        nums1_cases.append([4, 0, 2])
        nums0_cases.append([0, 3, 1])

        # --- 随机测试用例 (70%) ---
        random.seed(self.seed)

        for _ in range(70):
            # 控制列表长度和元素范围，确保总和合理
            n = random.randint(2, 20)  # 控制最大长度
            total_limit = random.randint(20, 100)  # 控制总和限制

            nums1 = []
            nums0 = []
            current_total = 0

            for i in range(n):
                # 确保还能生成至少一个元素
                remaining = total_limit - current_total
                if i == n - 1:
                    max_val = remaining
                else:
                    max_val = max(1, remaining - (n - i - 1))

                # 生成 nums1[i] 和 nums0[i]
                num1 = random.randint(0, min(max_val, 10))
                num0 = random.randint(0, min(max_val - num1, 10))

                # 确保至少有一个
                if num1 == 0 and num0 == 0:
                    num1 = 1

                nums1.append(num1)
                nums0.append(num0)
                current_total += num1 + num0

            nums1_cases.append(nums1)
            nums0_cases.append(nums0)

        # --- 特殊结构测试用例 (10%) ---
        # 交替片段：全1、全0、全1、全0
        nums1_cases.append([5, 0, 3, 0, 4])
        nums0_cases.append([0, 5, 0, 4, 0])

        # 渐增的 1 的数量，固定的 0
        nums1_cases.append([1, 2, 3, 4, 5])
        nums0_cases.append([2, 2, 2, 2, 2])

        # 渐减的 1 的数量，固定的 0
        nums1_cases.append([5, 4, 3, 2, 1])
        nums0_cases.append([2, 2, 2, 2, 2])

        # 固定的 1，渐增的 0
        nums1_cases.append([3, 3, 3, 3])
        nums0_cases.append([1, 2, 3, 4])

        # 全是混合片段
        nums1_cases.extend([
            [1, 1],
            [2, 2, 2],
            [1, 2, 3, 2, 1],
        ])
        nums0_cases.extend([
            [1, 1],
            [1, 1, 1],
            [2, 1, 1, 1, 2],
        ])

        return nums1_cases, nums0_cases
    

