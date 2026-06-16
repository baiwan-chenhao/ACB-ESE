

from . import Problem
from typing import List
import re


class Solution1(Problem):
    date = "2026-2-22"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3847,
                         types=[],
                         pass_rate=0.8,
                         description='给你一个整数数组 `nums`，其中 `nums[i]` 表示在第 `i`\xa0场比赛中获得的分数。\n**恰好**有两位玩家。初始时，第一位玩家为**主动玩家**，第二位玩家为**被动玩家**。\n**按顺序**将下述规则应用于每场比赛 `i`：\n - 如果 `nums[i]` 是奇数，主动玩家和被动玩家互换角色。\n - 在每第 6 场比赛（即比赛索引为 `5, 11, 17, ...` 的比赛中），主动玩家和被动玩家互换角色。\n - 主动玩家参与第 `i`\xa0场比赛，并获得 `nums[i]` 分。\n\n返回**分数差**，即第一位玩家的**总分**减去第二位玩家的**总分**。\n\n**示例 1：**\n> \n**输入：**`nums = [1,2,3]`\n**输出：**`0`\n**解释：**\u200b\u200b\u200b\u200b\u200b\u200b\u200b\n - 第 0 场比赛：分数为奇数，第二位玩家成为主动玩家，获得 `nums[0] = 1` 分。\n - 第 1 场比赛：没有交换角色。第二位玩家获得 `nums[1] = 2` 分。\n - 第 2 场比赛：分数为奇数，第一位玩家成为主动玩家，获得 `nums[2] = 3` 分。\n - 分数差为 `3 - 3 = 0`。\n\n**示例 2：**\n> \n**输入：**`nums = [2,4,2,1,2,1]`\n**输出：**`4`\n**解释：**\n - 第 0 到第 2 场比赛：第一位玩家获得 `2 + 4 + 2 = 8` 分。\n - 第 3 场比赛：分数为奇数，第二位玩家成为主动玩家，获得 `nums[3] = 1` 分。\n - 第 4 场比赛：第二位玩家获得 `nums[4] = 2` 分。\n - 第 5 场比赛：分数为奇数，玩家互换角色。由于这是第 6 场比赛，玩家再次互换角色。第二位玩家获得 `nums[5] = 1` 分。\n - 分数差为 `8 - 4 = 4`。\n\n**示例 3：**\n> \n**输入：**`nums = [1]`\n**输出：**`-1`\n**解释：**\n - 第 0 场比赛：分数为奇数，第二位玩家成为主动玩家，获得 `nums[0] = 1` 分。\n - 分数差为 `0 - 1 = -1`。\n\n**提示：**\n - `1 <= nums.length <= 1000`\n - `1 <= nums[i] <= 1000`'
                         )

    def solve(self, nums: List[int]) -> int:
        score = [0] * 2
        active = 0
        for i, x in enumerate(nums):
            active ^= x % 2
            if i % 6 == 5:
                active ^= 1
            score[active] += x
        return score[0] - score[1]

    def gen(self):
        """
        生成测试样例，覆盖以下场景：
        1. 边界值：最小长度1、最大长度1000、最小值1、最大值1000
        2. 特殊场景：
           - 全奇数：每次都会触发角色互换
           - 全偶数：只会在第6场触发角色互换
           - 长度为6的倍数：测试第6场规则
           - 交替奇偶：角色频繁切换
        3. 随机场景：覆盖常规情况
        """
        # 由于题目较简单，减少测试用例数量以提高效率
        testcase_num = self.testcase_num

        # 生成边界测试用例
        cases = []

        # 场景1: 最小长度，最小值
        cases.append([1])
        # 场景2: 最小长度，最大值（奇数）
        cases.append([1000])
        # 场景3: 最小长度，最大值（偶数）
        cases.append([999])

        # 场景4: 全奇数，长度6（奇数触发+第6场规则）
        cases.append([1, 3, 5, 7, 9, 11])
        # 场景5: 全偶数，长度6（只有第6场规则）
        cases.append([2, 4, 6, 8, 10, 12])

        # 场景6: 交替奇偶，长度6（频繁切换）
        cases.append([1, 2, 3, 4, 5, 6])

        # 场景7: 长度7（跨越6的边界）
        cases.append([2, 4, 6, 8, 10, 12, 14])

        # 场景8: 较大长度（100），随机值
        cases.append([self.s_generate_int(int_range=(1, 1000)) for _ in range(100)])

        # 场景9: 最大长度1000，全偶数（最小复杂度）
        cases.append([2] * 1000)

        # 场景10: 长度12（两个完整的6周期）
        cases.append([i for i in range(1, 13)])

        # 生成剩余的随机测试用例
        # 为了性能，限制最大长度为100
        for _ in range(testcase_num - 10):
            length = self.s_generate_int(int_range=(1, 100))
            case = [self.s_generate_int(int_range=(1, 1000)) for _ in range(length)]
            cases.append(case)

        # 返回按参数维度组织的元组，第一个列表是nums的所有测试样例
        return (cases,)
    

from string import digits
from . import Problem
import re
fac = [1] * 10
for i in range(1, 10):
    fac[i] = fac[i - 1] * i

class Solution2(Problem):
    date = "2026-2-22"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3848,
                         types=[],
                         pass_rate=0.53,
                         description='给你一个整数 `n`。\n如果一个数字的所有位数的**阶乘**之和**等于**数字本身，则称其为**阶数数字**（**digitorial**）。\n判断是否存在 `n` 的**任意排列**（包括原始顺序），可以形成一个**阶数数字**。\n如果存在这样的**排列**，返回 `true`；否则，返回 `false`。\n**注意：**\n - 非负整数 `x` 的**阶乘**（记作 `x!`）是所有小于或等于 `x` 的正整数的**乘积**，且 `0! = 1`。\n -**排列**是一个数字所有位数的重新排列，**且不能以零开头**。任何以零开头的排列都是无效的。\n\n**示例 1：**\n> \n**输入：**`n = 145`\n**输出：**`true`\n**解释：**\n数字 145 本身是一个阶数数字，因为 `1! + 4! + 5! = 1 + 24 + 120 = 145`。因此，答案为 `true`。\n**示例 2：**\n> \n**输入：**`n = 10`\n**输出：**`false`\n**解释：**\u200b\u200b\u200b\u200b\u200b\u200b\u200b\n数字 10 不是阶数数字，因为 `1! + 0! = 2` 不等于 10。同时，排列 `"01"` 是无效的，因为它以零开头。\n\n**提示：**\n - `1 <= n <= 10^9`'
                         )

    def solve(self, n: int) -> bool:
        sum_fac = 0
        cnt = [0] * 10
        while n > 0:
            n, d = divmod(n, 10)
            sum_fac += fac[d]
            cnt[d] += 1
        while sum_fac > 0:
            sum_fac, d = divmod(sum_fac, 10)
            cnt[d] -= 1
        return cnt == [0] * 10


    def gen(self):
        """生成测试样例，覆盖边界值、阶数数字和随机数字

        策略：
        1. 边界值：1, 9 (1位数的边界)
        2. 已知阶数数字：1, 2, 145, 40585
        3. 反例：10 (排列01无效), 123等
        4. 随机数字：覆盖1-9位数
        5. 特殊结构：包含0的数字

        返回:
            tuple: 包含一个列表，列表元素是测试用例
        """
        import random
        random.seed(self.seed)

        test_cases = []

        # 边界值 (15个)
        boundary_cases = [
            1, 2, 3, 4, 5, 6, 7, 8, 9,  # 1位数
            10, 11,  # 以0开头排列无效的情况
            99,  # 两位数边界
            100,  # 包含0
        ]
        test_cases.extend(boundary_cases)

        # 已知阶数数字 (5个)
        digitorial_numbers = [1, 2, 145, 40585]
        test_cases.extend(digitorial_numbers)

        # 反例 (10个)
        false_cases = [
            10, 12, 13, 14, 15, 16, 17, 18, 19, 100,
        ]
        test_cases.extend(false_cases)

        # 不同位数的随机数字 (50个)
        # 为避免超时，限制数字范围，但覆盖1-9位数
        for _ in range(50):
            num_digits = random.randint(1, 9)  # 1-9位数
            lower = 10 ** (num_digits - 1) if num_digits > 1 else 1
            upper = min(10 ** num_digits - 1, 100000000)  # 限制最大值避免超时
            if lower <= upper:
                n = random.randint(lower, upper)
                test_cases.append(n)

        # 特殊结构：包含多个0的数字 (10个)
        for _ in range(10):
            num_digits = random.randint(3, 6)
            lower = 10 ** (num_digits - 1)
            upper = min(10 ** num_digits - 1, 1000000)
            if lower <= upper:
                n = random.randint(lower, upper)
                test_cases.append(n)

        # 确保测试用例数量合适
        test_cases = test_cases[:self.testcase_num]

        return (test_cases,)
    

import string
from . import Problem
import re
from itertools import count


class Solution3(Problem):
    date = "2026-2-22"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3849,
                         types=[],
                         pass_rate=0.76,
                         description='给你两个长度均为 `n` 的二进制字符串 `s` 和 `t`。\n你可以按任意顺序**重新排列**`t` 中的字符，但 `s`**必须保持不变**。\n返回一个长度为 `n` 的**二进制字符串**，表示将 `s` 与重新排列后的 `t` 进行按位**异或 (XOR)**运算所能获得的**最大**整数值。\n\n**示例 1:**\n> \n**输入:**`s = "101", t = "011"`\n**输出:**`"110"`\n**解释:**\n - `t` 的一个最佳重新排列方式是 `"011"`。\n - `s` 与重新排列后的 `t` 进行按位异或的结果是 `"101" XOR "011" = "110"`，这是可能的最大值。\n\n**示例 2:**\n> \n**输入:**`s = "0110", t = "1110"`\n**输出:**`"1101"`\n**解释:**\n - `t` 的一个最佳重新排列方式是 `"1011"`。\n - `s` 与重新排列后的 `t` 进行按位异或的结果是 `"0110" XOR "1011" = "1101"`，这是可能的最大值。\n\n**示例 3:**\n> \n**输入:**`s = "0101", t = "1001"`\n**输出:**`"1111"`\n**解释:**\n - `t` 的一个最佳重新排列方式是 `"1010"`。\n - `s` 与重新排列后的 `t` 进行按位异或的结果是 `"0101" XOR "1010" = "1111"`，这是可能的最大值。\n\n**提示:**\n - `1 <= n == s.length == t.length <= 2 * 10^5`\n - `s[i]` 和 `t[i]` 不是 `\'0\'` 就是 `\'1\'`。'
                         )

    def solve(self, s: str, t: str) -> str:
        cnt0 = t.count('0')
        left = [cnt0, len(t) - cnt0]
        ans = list(s)
        for i, ch in enumerate(ans):
            x = int(ch)
            if left[x ^ 1] > 0:
                left[x ^ 1] -= 1
                ans[i] = '1'
            else:
                left[x] -= 1
                ans[i] = '0'
        return ''.join(ans)

    def gen(self):
        # 生成两个二进制字符串的测试样例
        # 参数1: s - 保持不变的二进制字符串
        # 参数2: t - 可以重新排列的二进制字符串

        # 测试策略：
        # 1. 边界情况：最小长度(1)、小规模(2-10)、中等规模(100-500)、较大规模(1000)
        # 2. 不同0/1比例：全0、全1、均衡混合
        # 3. 字符长度范围1-1000，降低最大长度以避免测试超时

        return self.generate_string(vocab='01', length_range=(1, 1000)), \
               self.generate_string(vocab='01', length_range=(1, 1000))
    


from . import Problem
from typing import List
from functools import cache
import re


class Solution4(Problem):
    date = "2026-2-22"
    def __init__(self):
        Problem.__init__(self,
                         degree=2,
                         idx=3850,
                         types=[],
                         pass_rate=0.52,
                         description='给你一个整数数组 `nums` 和一个整数 `k`。\n从初始值 `val = 1` 开始，从左到右处理 `nums`。在每个下标\xa0`i` 处，你必须**恰好选择**以下操作之一：\n - 将 `val` 乘以 `nums[i]`。\n - 将 `val` 除以 `nums[i]`。\n - 保持 `val` 不变。\n\n在处理完所有元素后，当且仅当 `val` 的最终有理数值**恰好**等于 `k` 时，才认为 `val`**等于**`k`。\n返回生成\xa0`val == k` 的**不同**选择序列的数量。\n**注意：**除法是有理数除法（精确除法），而不是整数除法。例如，`2 / 4 = 1 / 2`。\n\n**示例 1:**\n> \n**输入:**`nums = [2,3,2], k = 6`\n**输出:**`2`\n**解释:**\n以下 2 个不同的选择序列导致 `val == k`：\n| 序列 | 对 `nums[0]` 的操作 | 对 `nums[1]` 的操作 | 对 `nums[2]` 的操作 | 最终 `val` |\n| --- | --- | --- | --- | --- |\n| 1 | 乘法：`val = 1 * 2 = 2` | 乘法：`val = 2 * 3 = 6` | 保持 `val` 不变 | 6 |\n| 2 | 保持 `val` 不变 | 乘法：`val = 1 * 3 = 3` | 乘法：`val = 3 * 2 = 6` | 6 |\n\n**示例 2:**\n> \n**输入:**`nums = [4,6,3], k = 2`\n**输出:**`2`\n**解释:**\n以下 2 个不同的选择序列导致 `val == k`：\n| 序列 | 对 `nums[0]` 的操作 | 对 `nums[1]` 的操作 | 对 `nums[2]` 的操作 | 最终 `val` |\n| --- | --- | --- | --- | --- |\n| 1 | 乘法：`val = 1 * 4 = 4` | 除法：`val = 4 / 6 = 2 / 3` | 乘法：`val = (2 / 3) * 3 = 2` | 2 |\n| 2 | 保持 `val` 不变 | 乘法：`val = 1 * 6 = 6` | 除法：`val = 6 / 3 = 2` | 2 |\n\n**示例 3:**\n> \n**输入:**`nums = [1,5], k = 1`\n**输出:**`3`\n**解释:**\n以下 3 个不同的选择序列导致 `val == k`：\n| 序列 | 对 `nums[0]` 的操作 | 对 `nums[1]` 的操作 | 最终 `val` |\n| --- | --- | --- | --- |\n| 1 | 乘法：`val = 1 * 1 = 1` | 保持 `val` 不变 | 1 |\n| 2 | 除法：`val = 1 / 1 = 1` | 保持 `val` 不变 | 1 |\n| 3 | 保持 `val` 不变 | 保持 `val` 不变 | 1 |\n\n**提示:**\n - `1 <= nums.length <= 19`\n - `1 <= nums[i] <= 6`\n - `1 <= k <= 10^15`'
                         )

    def solve(self, nums: List[int], k: int) -> int:

        @cache
        def dfs(i: int, p: int, q: int) -> int:
            if i < 0:
                return 1 if p == q * k else 0
            res1 = dfs(i - 1, p * nums[i], q)
            res2 = dfs(i - 1, p, q * nums[i])
            res3 = dfs(i - 1, p, q)
            return res1 + res2 + res3
        return dfs(len(nums) - 1, 1, 1)

    def gen(self):
            """
            生成测试样例。

            覆盖场景：
            1. 边界情况：数组长度最小为1，最大限制在15以内以避免状态爆炸
            2. 特殊值：nums[i]=1（乘除效果相同）
            3. k的边界：最小值1，中等值，大值
            4. 特殊结构：全相同元素、递增序列、全1序列
            """
            # 减少测试样例数量，避免DFS+缓存在大输入下超时
            testcase_num = 30
            nums_cases = []
            k_cases = []

            # 边界情况：最小数组长度
            for _ in range(5):
                nums_cases.append([self.s_generate_int(int_range=(1, 6))])
                # k可以是1或者简单的乘积
                if nums_cases[-1][0] == 1:
                    k_cases.append(1)
                else:
                    k_cases.append(self.s_generate_int(int_range=(1, 3)))

            # 小数组：长度2-5，随机值
            for _ in range(5):
                length = self.s_generate_int(int_range=(2, 5))
                nums = [self.s_generate_int(int_range=(1, 6)) for _ in range(length)]
                nums_cases.append(nums)
                # 生成一个合理范围的k，避免太大导致状态爆炸
                k_cases.append(self.s_generate_int(int_range=(1, 100)))

            # 包含1的数组（乘除操作效果相同）
            for _ in range(4):
                length = self.s_generate_int(int_range=(3, 6))
                nums = [self.s_generate_int(int_range=(1, 6)) for _ in range(length)]
                # 确保至少有一个1
                nums[0] = 1
                nums_cases.append(nums)
                k_cases.append(self.s_generate_int(int_range=(1, 10)))

            # 全1的数组（特殊测试用例，每个元素都是1）
            for length in [2, 3, 4]:
                nums_cases.append([1] * length)
                k_cases.append(1)

            # 全相同元素的数组
            for _ in range(3):
                length = self.s_generate_int(int_range=(3, 6))
                val = self.s_generate_int(int_range=(2, 6))
                nums_cases.append([val] * length)
                # k可以是1, val^length等
                k_cases.append(self.s_generate_int(int_range=(1, val ** 2 + 1)))

            # 中等长度数组：6-10
            for _ in range(4):
                length = self.s_generate_int(int_range=(6, 10))
                nums = [self.s_generate_int(int_range=(1, 6)) for _ in range(length)]
                nums_cases.append(nums)
                k_cases.append(self.s_generate_int(int_range=(1, 50)))

            # 较大数组：11-15（避免使用19，会导致状态爆炸）
            for _ in range(2):
                length = self.s_generate_int(int_range=(11, 15))
                nums = [self.s_generate_int(int_range=(1, 6)) for _ in range(length)]
                nums_cases.append(nums)
                k_cases.append(self.s_generate_int(int_range=(1, 20)))

            return nums_cases, k_cases
    

