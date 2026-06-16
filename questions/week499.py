

from . import Problem


class Solution1(Problem):
    date = "2026-4-26"
    def __init__(self):
        Problem.__init__(self,
                         degree=0,
                         idx=3912,
                         types=[],
                         pass_rate=0.6,
                         description='给你一个整数数组 `nums`。\n如果元素 `nums[i]` 满足以下\xa0**至少一个\xa0**条件，则认为它是\xa0**有效\xa0**元素：\n\n- 它**严格大于\xa0**其左侧的所有元素。\n\n - 它**严格大于**\xa0其右侧的所有元素。\n\n第一个元素和最后一个元素始终有效。\n返回所有有效元素组成的数组，顺序与它们在 `nums` 中出现的顺序相同。\n\n**示例 1：**\n> \n**输入：**`nums = [1,2,4,2,3,2]`\n**输出：**`[1,2,4,3,2]`\n**解释：** - `nums[0]` 和 `nums[5]` 始终有效。\n - `nums[1]` 和 `nums[2]` 都严格大于其左侧的所有元素。\n - `nums[4]` 严格大于其右侧的所有元素。\n - 因此，答案为 `[1, 2, 4, 3, 2]`。\n\n**示例 2：**\n> \n**输入：**`nums = [5,5,5,5]`\n**输出：**`[5,5]`\n**解释：** - 第一个元素和最后一个元素始终有效。\n - 其他元素既不严格大于其左侧的所有元素，也不严格大于其右侧的所有元素。\n - 因此，答案为 `[5, 5]`。\n\n**示例 3：**\n> \n**输入：**`nums = [1]`\n**输出：**`[1]`\n**解释：**\n由于数组中只有一个元素，它始终有效。因此，答案为 `[1]`。\n\n**提示：**\n\n- `1 <= nums.length <= 100`\n\n - `1 <= nums[i] <= 100`'
                         )

    def solve(self, nums: list[int]) -> list[int]:
        n = len(nums)
        right_valid = [False] * n
        mx = 0
        for i in range(n - 1, -1, -1):
            x = nums[i]
            right_valid[i] = x > mx
            mx = max(mx, x)
        ans = []
        mx = 0
        for valid, x in zip(right_valid, nums):
            if valid or x > mx:
                ans.append(x)
            mx = max(mx, x)
        return ans

    def gen(self):
        """生成测试样例。

        策略分配（共100个测试样例）：
        - 10% (10个): 边界值测试 - 最小长度1、最大长度100、单元素
        - 20% (20个): 特殊结构测试 - 全相同、严格递增、严格递减
        - 70% (70个): 正常随机测试 - 各种长度的随机数组

        Returns:
            tuple: 包含一个列表，列表中的每个元素是一个测试用的nums数组
        """
        test_cases = []

        # 边界值测试 - 10个测试样例
        # 单元素数组
        test_cases.append([1])
        test_cases.append([100])
        test_cases.append([50])

        # 最小有效长度但非单元素
        test_cases.append([1, 1])
        test_cases.append([100, 1])
        test_cases.append([1, 100])

        # 最大长度边界测试
        test_cases.append([1] * 100)  # 全1
        test_cases.append([100] * 100)  # 全100
        test_cases.append(list(range(1, 101)))  # 严格递增到最大长度
        test_cases.append(list(range(100, 0, -1)))  # 严格递减到最大长度

        # 特殊结构测试 - 20个测试样例
        # 全相同元素（仅首尾有效）
        for _ in range(5):
            val = self.s_generate_int(int_range=(1, 100))
            length = self.s_generate_int(int_range=(2, 20))
            test_cases.append([val] * length)

        # 严格递增（全部有效）
        for _ in range(5):
            length = self.s_generate_int(int_range=(2, 30))
            arr = []
            start = self.s_generate_int(int_range=(1, 70))
            for i in range(length):
                arr.append(start + i)
            test_cases.append(arr)

        # 严格递减（仅首尾有效）
        for _ in range(5):
            length = self.s_generate_int(int_range=(2, 30))
            arr = []
            start = self.s_generate_int(int_range=(31, 100))
            for i in range(length):
                arr.append(start - i)
            test_cases.append(arr)

        # 波峰结构（中间元素为峰值）
        for _ in range(5):
            length = self.s_generate_int(int_range=(3, 15))
            if length % 2 == 0:
                length += 1
            half = length // 2
            peak_val = self.s_generate_int(int_range=(70, 100))
            arr = list(range(1, half + 1)) + [peak_val] + list(range(half, 0, -1))
            test_cases.append(arr[:length])

        # 正常随机测试 - 70个测试样例
        for _ in range(70):
            test_cases.append(self.s_generate_list_int(list_length_range=(2, 100), int_range=(1, 100)))

        return (test_cases,)
    


from . import Problem


class Solution2(Problem):
    date = "2026-4-26"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3913,
                         types=[],
                         pass_rate=0.64,
                         description='给你一个由小写英文字母组成的字符串 `s`。\n仅重新排列字符串中的**元音字母**，使它们按照出现频率的\xa0**非递增\xa0**顺序排列。\n如果多个元音字母的\xa0**出现频率\xa0**相同，则按照它们在 `s` 中\xa0**首次出现\xa0**的位置排序。\n返回修改后的字符串。\n元音字母为 `\'a\'`、`\'e\'`、`\'i\'`、`\'o\'` 和 `\'u\'`。\n字母的\xa0**出现频率\xa0**是指它在字符串中出现的次数。\n\n**示例 1：**\n\n> \n**输入：**`s = "leetcode"`\n**输出：**`"leetcedo"`\n**解释：** - 字符串中的元音字母为 `[\'e\', \'e\', \'o\', \'e\']`，其出现频率为：`e = 3`，`o = 1`。\n - 按出现频率非递增排序后，再放回原来的元音位置，得到 `"leetcedo"`。\n\n**示例 2：**\n> \n**输入：**`s = "aeiaaioooa"`\n**输出：**`"aaaaoooiie"`\n**解释：** - 字符串中的元音字母为 `[\'a\', \'e\', \'i\', \'a\', \'a\', \'i\', \'o\', \'o\', \'o\', \'a\']`，其出现频率为：`a = 4`，`o = 3`，`i = 2`，`e = 1`。\n - 按出现频率非递增排序后，再放回原来的元音位置，得到 `"aaaaoooiie"`。\n\n**示例 3：**\n> \n**输入：**`s = "baeiou"`\n**输出：**`"baeiou"`\n**解释：** - 每个元音字母都恰好出现一次，因此它们的出现频率相同。\n - 所以它们会按照首次出现的位置保持相对顺序，字符串保持不变。\n\n**提示：\n\n- `1 <= s.length <= 10<sup>5</sup>`\n\n - `s` 由小写英文字母组成'
                         )

    def solve(self, s: str) -> str:
        cnt = {}
        vowels = []
        for ch in s:
            if ch not in 'aeiou':
                continue
            if ch not in cnt:
                cnt[ch] = 1
                vowels.append(ch)
            else:
                cnt[ch] += 1
        vowels.sort(key=lambda ch: -cnt[ch])
        t = list(s)
        j = 0
        for i, ch in enumerate(t):
            if ch not in 'aeiou':
                continue
            t[i] = c = vowels[j]
            cnt[c] -= 1
            if cnt[c] == 0:
                j += 1
        return ''.join(t)

    def gen(self):
        """
        生成测试样例，覆盖以下场景：
        1. 边界值：长度为1的字符串（单个元音或辅音）
        2. 特殊结构：无元音（纯辅音）、全是元音
        3. 频率分布：所有元音频率相同、频率递减排列
        4. 随机字符串：中等长度的随机字符串
        5. 首次出现顺序：测试相同频率下的首次出现位置排序

        测试覆盖策略：
        - 边界值覆盖：最小长度1
        - 特殊结构覆盖：纯元音、纯辅音（边界情况）
        - 频率相同场景：每个元音出现次数相同，验证首次出现位置排序
        - 频率递减场景：a最多，e次之，验证频率降序排序
        - 随机场景：模拟一般情况
        """
        import random

        testcase_num = self.testcase_num
        cases_per_type = testcase_num // 5

        vowels = 'aeiou'

        # 类型1: 边界值 - 长度为1的字符串（单个元音或辅音）
        boundary_small = []
        for _ in range(cases_per_type):
            if random.random() < 0.5:
                boundary_small.append(random.choice(vowels))
            else:
                boundary_small.append(random.choice('bcdfghjklmnpqrstvwxyz'))

        # 类型2: 特殊结构 - 无元音（纯辅音）
        no_vowels = []
        for _ in range(cases_per_type // 2):
            length = random.randint(1, 5000)
            s_list = [random.choice('bcdfghjklmnpqrstvwxyz') for _ in range(length)]
            no_vowels.append(''.join(s_list))

        # 类型2续: 特殊结构 - 全是元音
        all_vowels = []
        for _ in range(cases_per_type // 2):
            length = random.randint(1, 5000)
            s_list = [random.choice(vowels) for _ in range(length)]
            all_vowels.append(''.join(s_list))

        # 类型3: 频率相同 - 每个元音出现相同次数
        # 验证当频率相同时，按首次出现位置排序
        same_freq = []
        for _ in range(cases_per_type):
            k = random.randint(1, 15)
            vowel_chars = [v for v in vowels for _ in range(k)]
            random.shuffle(vowel_chars)
            # 添加辅音增加测试复杂度
            consonants = [random.choice('bcdfghjklmnpqrstvwxyz') for _ in range(len(vowel_chars))]
            result = []
            for v, c in zip(vowel_chars, consonants):
                result.append(v)
                result.append(c)
            result.extend(vowel_chars[len(consonants):])
            same_freq.append(''.join(result))

        # 类型4: 频率递减 - a最多，e次之，o最少
        # 验证频率降序排序的正确性
        decreasing_freq = []
        for _ in range(cases_per_type):
            parts = []
            for i, v in enumerate(vowels):
                count = (5 - i) * random.randint(1, 8)
                parts.append(v * count)
            vowel_part = ''.join(parts)
            consonant_part = ''.join([random.choice('bcdfghjklmnpqrstvwxyz') for _ in range(len(vowel_part) // 2)])
            result = []
            v_idx = c_idx = 0
            while v_idx < len(vowel_part) or c_idx < len(consonant_part):
                if v_idx < len(vowel_part) and (c_idx >= len(consonant_part) or random.random() < 0.6):
                    result.append(vowel_part[v_idx])
                    v_idx += 1
                else:
                    result.append(consonant_part[c_idx])
                    c_idx += 1
            decreasing_freq.append(''.join(result))

        # 类型5: 随机字符串 - 中等长度
        # 模拟一般情况下的输入
        random_cases = []
        for _ in range(cases_per_type):
            length = random.randint(100, 20000)
            s_list = []
            for _ in range(length):
                if random.random() < 0.38:  # 元音约占38%
                    s_list.append(random.choice(vowels))
                else:
                    s_list.append(random.choice('bcdfghjklmnpqrstvwxyz'))
            random_cases.append(''.join(s_list))

        # 合并所有测试用例
        all_cases = (boundary_small + no_vowels + all_vowels + 
                     same_freq + decreasing_freq + random_cases)

        return (all_cases[:testcase_num],)
    

import random
from . import Problem
from itertools import pairwise


class Solution3(Problem):
    date = "2026-4-26"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3914,
                         types=[],
                         pass_rate=0.62,
                         description='给你一个长度为 `n` 的整数数组 `nums`。\n一次操作中，你可以选择任意一个**子数组**`nums[l..r]`，并将该\xa0**子数组\xa0**中的每个元素都增加 `x`，其中 `x` 可以是任意**正**整数。\n返回使数组变为**非递减**所需的所有操作中，所选 `x` 的值之和可能达到的\xa0**最小值**。\n如果对于所有 `0 <= i < n - 1`，都有 `nums[i] <= nums[i + 1]`，则称数组是\xa0**非递减\xa0**的。\n**子数组**\xa0是数组中一个连续**、\xa0非空** 的元素序列。\n\n**示例 1：**\n\n> **输入：**`nums = [3,3,2,1]`\n**输出：**`2`\n**解释：**\n一种最优操作方案为： - 选择子数组 `[2..3]`，并增加 `x = 1`，得到 `[3, 3, 3, 2]`\n - 选择子数组 `[3..3]`，并增加 `x = 1`，得到 `[3, 3, 3, 3]`\n\n数组变为非递减，所选 `x` 的总和为 `1 + 1 = 2`。\n**示例 2：**\n> \n**输入：**`nums = [5,1,2,3]`\n**输出：**`4`\n**解释：**\n一种最优操作方案为： - 选择子数组 `[1..3]`，并增加 `x = 4`，得到 `[5, 5, 6, 7]`\n\n数组变为非递减，所选 `x` 的总和为 `4`。\n\n**提示：** - `1 <= n == nums.length <= 10**5`\n\n - `1 <= nums[i] <= 10<sup>9</sup>`'
                         )

    def solve(self, nums: list[int]) -> int:
        return sum((max(x - y, 0) for x, y in pairwise(nums)))

    def gen(self):
        """生成测试样例，覆盖各种边界和特殊情况

        覆盖场景：
        1. 最小长度 (n=1)
        2. 边界值测试
        3. 严格递减数组（最大需要修正）
        4. 严格递增数组（无需修正）
        5. 全相同元素（无需修正）
        6. 单一下降点
        7. 交替递减模式
        8. 随机数组（不同规模）
        9. 大值测试（接近10^9）
        10. 长数组（接近10^5）
        """
        testcase_num = self.testcase_num
        random.seed(self.seed)

        nums_list = []

        # 1. 最小长度：单个元素，答案为0
        nums_list.append([self.s_generate_int(int_range=(1, 10**9))])

        # 2. 边界值测试：两个元素，后小于前
        nums_list.append([10**9, 1])
        nums_list.append([1, 10**9])  # 无需修正

        # 3. 严格递减数组（最大需要修正）
        # 短版本
        nums_list.append(list(range(5, 0, -1)))
        # 中等版本
        nums_list.append(list(range(10, 0, -1)))

        # 4. 严格递增数组（无需修正，答案为0）
        nums_list.append(list(range(1, 11)))
        nums_list.append([10**9 - i for i in range(10)])  # 大值递增

        # 5. 全相同元素（无需修正，答案为0）
        nums_list.append([1] * 10)
        nums_list.append([10**9] * 20)

        # 6. 单一下降点
        nums_list.append([1, 2, 3, 2, 4, 5])  # 需要修正1
        nums_list.append([10**9, 10**9-1, 10**9])  # 大值下降

        # 7. 交替递减模式
        nums_list.append([5, 4, 5, 4, 5, 4])
        nums_list.append([10, 1, 10, 1, 10, 1])

        # 8. 随机数组 - 不同规模
        # 小规模随机
        for _ in range(10):
            length = self.s_generate_int(int_range=(2, 20))
            nums = self.s_generate_list_int(
                list_length_range=(length, length),
                int_range=(1, 1000)
            )
            nums_list.append(nums)

        # 中等规模随机
        for _ in range(8):
            length = self.s_generate_int(int_range=(100, 1000))
            nums = self.s_generate_list_int(
                list_length_range=(length, length),
                int_range=(1, 10000)
            )
            nums_list.append(nums)

        # 9. 大值测试（接近10^9）
        for _ in range(5):
            length = self.s_generate_int(int_range=(5, 50))
            nums = self.s_generate_list_int(
                list_length_range=(length, length),
                int_range=(10**9 - 1000, 10**9)
            )
            nums_list.append(nums)

        # 10. 长数组（接近10^5）
        for _ in range(3):
            length = self.s_generate_int(int_range=(10000, 50000))
            nums = self.s_generate_list_int(
                list_length_range=(length, length),
                int_range=(1, 100000)
            )
            nums_list.append(nums)

        # 填充剩余的测试用例为随机数组
        remaining = testcase_num - len(nums_list)
        for _ in range(remaining):
            length = self.s_generate_int(int_range=(2, 10000))
            nums = self.s_generate_list_int(
                list_length_range=(length, length),
                int_range=(1, 10**9)
            )
            nums_list.append(nums)

        return (nums_list,)
    


from . import Problem
from bisect import bisect_left
class Fenwick:

    def __init__(self, n: int):
        self.f = [0] * n

    def update(self, i: int, val: int) -> None:
        f = self.f
        while i < len(f):
            f[i] = max(f[i], val)
            i += i & -i

    def pre_max(self, i: int) -> int:
        f = self.f
        res = 0
        while i > 0:
            res = max(res, f[i])
            i &= i - 1
        return res

class Solution4(Problem):
    date = "2026-4-26"
    def __init__(self):
        Problem.__init__(self,
                         degree=2,
                         idx=3915,
                         types=[],
                         pass_rate=0.51,
                         description='给你一个长度为 `n` 的整数数组 `nums` 和一个整数 `k`。\n选择一个下标满足 `0 <= i1 < i2 < ... < im < n` 的**\xa0子序列**，并满足： - 对于每个 `1 <= t < m`，都有 `it+1 - it >= k`。\n\n - 所选的值构成一个**严格交替\xa0**序列。换句话说，满足以下两种形式之一：\n\t - `nums[i1] < nums[i2] > nums[i3] < ...`，或\n - `nums[i1] > nums[i2] < nums[i3] > ...`\n\n长度为 1 的\xa0**子序列\xa0**也被认为符合\xa0**严格交替\xa0**。一个**有效\xa0**子序列的得分为其所选元素值的**总和**。\n返回一个整数，表示有效子序列可能取得的**最大得分**。\n\n**子序列\xa0**是指通过删除原数组中的某些元素或不删除任何元素，并且不改变剩余元素相对顺序后得到的数组。\n\n**示例 1：**\n\n> \n**输入：**`nums = [5,4,2], k = 2`\n**输出：**`7`\n**解释：**\n一种最优选择是下标 `[0, 2]`，对应的值为 `[5, 2]`。 - 距离条件成立，因为 `2 - 0 = 2 >= k`。\n - 这些值严格交替，因为 `5 > 2`。\n\n得分为 `5 + 2 = 7`。\n**示例 2：**\n> \n**输入：**`nums = [3,5,4,2,4], k = 1`\n**输出：**`14`\n**解释：**\n一种最优选择是下标 `[0, 1, 3, 4]`，对应的值为 `[3, 5, 2, 4]`。 - 距离条件成立，因为任意两个相邻选中下标之差都至少为 `k = 1`。\n - 这些值严格交替，因为 `3 < 5 > 2 < 4`。\n\n得分为 `3 + 5 + 2 + 4 = 14`。\n**示例 3：**\n> \n**输入：**`nums = [5], k = 1`\n**输出：**`5`\n**解释：**\n唯一的有效子序列是 `[5]`。长度为 1 的子序列始终是严格交替的，因此得分为 5。\n\n**提示：**\n\n- `1 <= n == nums.length <= 10**5>`\n\n - `1 <= nums[i] <= 10**5`\n - `1 <= k <= n`'
                         )

    def solve(self, nums: list[int], k: int) -> int:
        sorted_nums = sorted(set(nums))
        n = len(nums)
        f_inc = [0] * n
        f_dec = [0] * n
        m = len(sorted_nums)
        inc = Fenwick(m + 1)
        dec = Fenwick(m + 1)
        for i, x in enumerate(nums):
            if i >= k:
                j = nums[i - k]
                inc.update(m - j, f_inc[i - k])
                dec.update(j + 1, f_dec[i - k])
            j = bisect_left(sorted_nums, x)
            nums[i] = j
            f_inc[i] = dec.pre_max(j) + x
            f_dec[i] = inc.pre_max(m - 1 - j) + x
        return max(max(f_inc), max(f_dec))

    def gen(self):
        # 分配测试用例：共100个测试样例
        # 边界值测试(15%): 单元素、最小/最大k、全相同、严格递增/递减
        # 正常分布测试(65%): 随机数组、各种规模
        # 特殊结构测试(20%): 完美交替序列、周期性序列、锯齿状序列、大k值

        testcase_num = self.testcase_num
        result_nums = []
        result_k = []

        # ============== 边界值测试 (15个用例) ==============

        # Case 1-2: 单元素数组（最小n=1）
        for _ in range(2):
            val = self.s_generate_int(int_range=(1, 100000))
            result_nums.append([val])
            result_k.append(1)

        # Case 3: k=1（最小间隔，允许相邻元素）
        n = self.s_generate_int(int_range=(2, 10))
        result_nums.append(self.s_generate_list_int(list_length_range=(2, 10), int_range=(1, 100)))
        result_k.append(1)

        # Case 4: k=n（最大间隔，只能选一个元素）
        n = self.s_generate_int(int_range=(2, 5))
        nums = self.s_generate_list_int(list_length_range=(2, 5), int_range=(1, 100))
        result_nums.append(nums)
        result_k.append(len(nums))

        # Case 5-7: 全相同元素（无法形成交替，只能选一个）
        for _ in range(3):
            n = self.s_generate_int(int_range=(1, 20))
            val = self.s_generate_int(int_range=(1, 100))
            result_nums.append([val] * n)
            result_k.append(self.s_generate_int(int_range=(1, min(n, 5))))

        # Case 8-9: 严格递增序列（只能选一个或相邻大间隔）
        for _ in range(2):
            n = self.s_generate_int(int_range=(5, 20))
            start = self.s_generate_int(int_range=(1, 50))
            k = self.s_generate_int(int_range=(1, min(n, 5)))
            nums = [start + i for i in range(n)]
            result_nums.append(nums)
            result_k.append(k)

        # Case 10-11: 严格递减序列
        for _ in range(2):
            n = self.s_generate_int(int_range=(5, 20))
            start = self.s_generate_int(int_range=(50, 100))
            k = self.s_generate_int(int_range=(1, min(n, 5)))
            nums = [start - i for i in range(n)]
            result_nums.append(nums)
            result_k.append(k)

        # Case 12-13: 两个元素（最小交替序列）
        for _ in range(2):
            if self.s_generate_int(int_range=(0, 1)) == 0:
                nums = [self.s_generate_int(int_range=(1, 100)), self.s_generate_int(int_range=(101, 200))]
            else:
                nums = [self.s_generate_int(int_range=(101, 200)), self.s_generate_int(int_range=(1, 100))]
            result_nums.append(nums)
            result_k.append(self.s_generate_int(int_range=(1, 2)))

        # Case 14-15: 最小值和最大值边界
        result_nums.append([1] * self.s_generate_int(int_range=(1, 10)))
        result_k.append(1)
        result_nums.append([100000] * self.s_generate_int(int_range=(1, 10)))
        result_k.append(1)

        # ============== 特殊结构测试 (20个用例) ==============

        # Case 16-18: 完美交替序列（低高低高...）
        for _ in range(3):
            n = self.s_generate_int(int_range=(10, 30))
            low_base = self.s_generate_int(int_range=(1, 10))
            high_base = self.s_generate_int(int_range=(100, 200))
            nums = []
            for i in range(n):
                if i % 2 == 0:
                    nums.append(low_base + self.s_generate_int(int_range=(0, 5)))
                else:
                    nums.append(high_base + self.s_generate_int(int_range=(0, 5)))
            result_nums.append(nums)
            result_k.append(1)

        # Case 19-21: 完美交替序列（高低高低...）
        for _ in range(3):
            n = self.s_generate_int(int_range=(10, 30))
            low_base = self.s_generate_int(int_range=(1, 10))
            high_base = self.s_generate_int(int_range=(100, 200))
            nums = []
            for i in range(n):
                if i % 2 == 0:
                    nums.append(high_base + self.s_generate_int(int_range=(0, 5)))
                else:
                    nums.append(low_base + self.s_generate_int(int_range=(0, 5)))
            result_nums.append(nums)
            result_k.append(1)

        # Case 22-25: 大k值的交替序列（需要跳过元素）
        for _ in range(4):
            n = self.s_generate_int(int_range=(20, 50))
            k = self.s_generate_int(int_range=(3, 10))
            low_base = self.s_generate_int(int_range=(1, 10))
            high_base = self.s_generate_int(int_range=(100, 200))
            nums = []
            for i in range(n):
                if i % 2 == 0:
                    nums.append(low_base + self.s_generate_int(int_range=(0, 5)))
                else:
                    nums.append(high_base + self.s_generate_int(int_range=(0, 5)))
            result_nums.append(nums)
            result_k.append(k)

        # Case 26-28: 周期性序列
        for _ in range(3):
            period = self.s_generate_int(int_range=(2, 5))
            n = period * self.s_generate_int(int_range=(3, 10))
            base_vals = [self.s_generate_int(int_range=(1, 100)) for _ in range(period)]
            nums = base_vals * (n // period)
            result_nums.append(nums)
            result_k.append(self.s_generate_int(int_range=(1, 3)))

        # Case 29-30: 锯齿状序列（有利于最大化交替子序列）
        for _ in range(2):
            n = self.s_generate_int(int_range=(20, 50))
            nums = []
            for i in range(n):
                if i % 2 == 0:
                    nums.append(i + 1)
                else:
                    nums.append(n * 2 - i)
            result_nums.append(nums)
            result_k.append(1)

        # Case 31-32: 小规模大k值
        for _ in range(2):
            n = self.s_generate_int(int_range=(5, 15))
            k = self.s_generate_int(int_range=(n // 2, n))
            result_nums.append(self.s_generate_list_int(list_length_range=(5, 15), int_range=(1, 1000)))
            result_k.append(k)

        # Case 33-35: 大值数组（接近10^5边界）
        for _ in range(3):
            n = self.s_generate_int(int_range=(10, 30))
            nums = [self.s_generate_int(int_range=(90000, 100000)) for _ in range(n)]
            result_nums.append(nums)
            result_k.append(self.s_generate_int(int_range=(1, 5)))

        # ============== 正常分布测试 (65个用例) ==============

        # Case 36-60: 小规模随机 (n <= 100)
        for _ in range(25):
            n = self.s_generate_int(int_range=(2, 100))
            nums = self.s_generate_list_int(list_length_range=(2, 100), int_range=(1, 10000))
            k = self.s_generate_int(int_range=(1, min(n, 20)))
            result_nums.append(nums)
            result_k.append(k)

        # Case 61-80: 中等规模随机 (100 < n <= 1000)
        for _ in range(20):
            n = self.s_generate_int(int_range=(101, 1000))
            nums = self.s_generate_list_int(list_length_range=(101, 1000), int_range=(1, 100000))
            k = self.s_generate_int(int_range=(1, min(n, 50)))
            result_nums.append(nums)
            result_k.append(k)

        # Case 81-95: 大规模随机 (1000 < n <= 10000)
        for _ in range(15):
            n = self.s_generate_int(int_range=(1001, 10000))
            nums = self.s_generate_list_int(list_length_range=(1001, 10000), int_range=(1, 100000))
            k = self.s_generate_int(int_range=(1, min(n, 100)))
            result_nums.append(nums)
            result_k.append(k)

        # Case 96-100: 超大规模随机 (接近n=10^5)
        for _ in range(5):
            n = self.s_generate_int(int_range=(10001, 50000))
            nums = self.s_generate_list_int(list_length_range=(10001, 50000), int_range=(1, 100000))
            k = self.s_generate_int(int_range=(1, min(n, 500)))
            result_nums.append(nums)
            result_k.append(k)

        return result_nums, result_k
    

