
import random
from itertools import count
from . import Problem
from typing import List
from collections import Counter
import re


class Solution1(Problem):
    date = "2026-2-28"
    def __init__(self):
        Problem.__init__(self,
                         degree=0,
                         idx=3852,
                         types=[],
                         pass_rate=0.76,
                         description='给你一个整数数组 `nums`。\n从 `nums` 中找出两个**互不相同**的值 `x` 和 `y`，使得：\n - `x < y`\n - `x` 和 `y` 在 `nums` 中的频率不同。\n\n在所有满足条件的数对中：\n - 选择 `x` 的值尽可能小的数对。\n - 如果存在多个 `x` 相同的数对，选择 `y` 的值尽可能小的那个。\n\n返回一个整数数组 `[x, y]`。如果不存在有效的数对，返回 `[-1, -1]`。\n一个值 `x` 的**频率**是指它在数组中出现的次数。\n\n**示例 1：**\n> \n**输入：**`nums = [1,1,2,2,3,4]`\n**输出：**`[1,3]`\n**解释：**\n最小的值是 1，频率为 2。比 1 大且频率与 1 不同的最小值是 3，其频率为 1。因此，答案是 `[1, 3]`。\n**示例 2：**\n> \n**输入：**`nums = [1,5]`\n**输出：**`[-1,-1]`\n**解释：**\n两个值的频率相同，因此不存在有效的数对。返回 `[-1, -1]`。\n**示例 3：**\n> \n**输入：**`nums = [7]`\n**输出：**`[-1,-1]`\n**解释：**\n数组中只有一个值，因此不存在有效的数对。返回 `[-1, -1]`。\n\n**提示：**\n - `1 <= nums.length <= 100`\n - `1 <= nums[i] <= 100`'
                         )

    def solve(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        mn = min(nums)
        cnt_min = cnt[mn]
        min_y = min((y for y, c in cnt.items() if c != cnt_min), default=None)
        if min_y is None:
            return [-1, -1]
        return [mn, min_y]

    def gen(self):
        """
        生成测试样例，覆盖以下场景：
        1. 边界值：长度为1的数组（返回[-1, -1]）
        2. 不存在解：所有元素频率相同、只有一个唯一值
        3. 存在有效数对：最小值频率与某个较大值不同
        4. 特殊结构：最小值有多个、元素频率完全不同

        约束条件：
        - 1 <= nums.length <= 100
        - 1 <= nums[i] <= 100

        生成策略：
        - 使用较小的范围生成测试样例，避免参考答案超时
        - 生成50个测试样例，确保测试时间合理
        """
        random.seed(self.seed)
        nums_list = []

        for _ in range(50):
            # 随机选择场景类型
            scenario = random.randint(1, 4)

            if scenario == 1:
                # 场景1：边界值 - 长度为1的数组
                nums = [self.s_generate_int(int_range=(1, 100))]

            elif scenario == 2:
                # 场景2：不存在解 - 所有元素频率相同
                len_num = random.randint(2, 20)
                unique_values = random.randint(1, 5)
                # 确保每个值出现相同次数
                freq = len_num // unique_values
                values = random.sample(range(1, 101), unique_values)
                nums = []
                for val in values:
                    nums.extend([val] * freq)
                # 如果有剩余，随机添加
                while len(nums) < len_num:
                    nums.append(random.choice(values))

            elif scenario == 3:
                # 场景3：存在有效数对
                len_num = random.randint(2, 30)
                # 最小值出现次数
                min_freq = random.randint(1, 5)
                # 另一个值的出现次数（确保与min_freq不同）
                other_freq = random.randint(1, 5)
                while other_freq == min_freq:
                    other_freq = random.randint(1, 5)

                min_val = self.s_generate_int(int_range=(1, 50))
                other_val = self.s_generate_int(int_range=(min_val + 1, 100))

                # 基础数组
                nums = [min_val] * min_freq + [other_val] * other_freq
                # 填充剩余位置（确保不干扰结果）
                remaining = len_num - len(nums)
                for _ in range(remaining):
                    nums.append(self.s_generate_int(int_range=(min_val + 1, 100)))

            else:
                # 场景4：特殊结构 - 元素频率完全不同
                len_num = random.randint(3, 20)
                # 确保元素个数不超过数组长度
                unique_count = min(len_num, random.randint(3, 8))
                values = sorted(random.sample(range(1, 101), unique_count))
                nums = []
                # 每个值出现不同次数（从1开始）
                for i, val in enumerate(values):
                    nums.extend([val] * (i + 1))
                # 截取或填充到目标长度
                if len(nums) > len_num:
                    nums = nums[:len_num]
                else:
                    while len(nums) < len_num:
                        nums.append(self.s_generate_int(int_range=(1, 100)))

            nums_list.append(nums)

        return (nums_list,)
    

import math
import random
from string import ascii_lowercase
from . import Problem
from collections import defaultdict
import re
from math import inf


class Solution2(Problem):
    date = "2026-2-28"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3853,
                         types=[],
                         pass_rate=0.62,
                         description='给你一个由小写英文字母组成的字符串 `s` 和一个整数 `k`。\n在**当前**字符串 `s` 中，如果两个**相同**字符之间的下标距离**至多**为 `k`，则认为它们是**靠近**的。\n当两个字符**靠近**时，右侧的字符会合并到左侧。合并操作**逐个**发生，每次合并后，字符串都会更新，直到无法再进行合并为止。\n返回执行所有可能合并后的最终字符串。\n**注意**：如果可以进行多次合并，请始终选择**左侧下标最小**的那一对进行合并。如果多对字符共享最小的左侧下标，请选择**右侧下标最小**的那一对。\n\n**示例 1：**\n> \n**输入：**`s = "abca", k = 3`\n**输出：**`"abc"`\n**解释：**\n - 下标\xa0`i = 0` 和 `i = 3` 处的字符 `\'a\'` 是靠近的，因为 `3 - 0 = 3 <= k`。\n - 将它们合并到左侧的 `\'a\'`，得到 `s = "abc"`。\n - 没有其他相同的字符是靠近的，因此不再发生合并。\n\n**示例 2：**\n> \n**输入：**`s = "aabca", k = 2`\n**输出：**`"abca"`\n**解释：**\n - 下标\xa0`i = 0` 和 `i = 1` 处的字符 `\'a\'` 是靠近的，因为 `1 - 0 = 1 <= k`。\n - 将它们合并到左侧的 `\'a\'`，得到 `s = "abca"`。\n - 现在剩余的字符 `\'a\'` 分别位于下标\xa0`i = 0` 和 `i = 3`，它们不再靠近，因为 `k < 3`，所以不再发生合并。\n\n**示例 3：**\n> \n**输入：**`s = "yybyzybz", k = 2`\n**输出：**`"ybzybz"`\n**解释：**\n - 下标\xa0`i = 0` 和 `i = 1` 处的字符 `\'y\'` 是靠近的，因为 `1 - 0 = 1 <= k`。\n - 将它们合并到左侧的 `\'y\'`，得到 `s = "ybyzybz"`。\n - 现在下标\xa0`i = 0` 和 `i = 2` 处的字符 `\'y\'` 是靠近的，因为 `2 - 0 = 2 <= k`。\n - 将它们合并到左侧的 `\'y\'`，得到 `s = "ybzybz"`。\n - 没有其他相同的字符是靠近的，因此不再发生合并。\n\n**提示：**\n - `1 <= s.length <= 100`\n - `1 <= k <= s.length`\n - `s` 由小写英文字母组成。'
                         )

    def solve(self, s: str, k: int) -> str:
        last = defaultdict(lambda: -inf)
        ans = []
        for ch in s:
            if len(ans) - last[ch] > k:
                last[ch] = len(ans)
                ans.append(ch)
        return ''.join(ans)

    def gen(self):
        import string
        from random import randint, seed

        random.seed(self.seed)

        # 辅助函数：生成指定长度的随机字符串
        def s_generate_string_with_length(vocab, length_range):
            length = randint(*length_range)
            return ''.join(vocab[randint(0, len(vocab) - 1)] for _ in range(length))

        def _generate_int(int_range):
            return randint(*int_range)

        # 字符表
        vocab = string.ascii_lowercase

        def generate_s():
            # 生成30个特殊设计的测试用例
            for i in range(30):
                if i == 0:  # 示例1
                    yield "abca"
                elif i == 1:  # 示例2
                    yield "aabca"
                elif i == 2:  # 示例3
                    yield "yybyzybz"
                elif i == 3:  # 最小长度
                    yield "a"
                elif i == 4:  # k = 1，连续重复字符
                    yield "aaaaa"
                elif i == 5:  # k = 5，连续重复字符（都保留）
                    yield "aaaaa"
                elif i == 6:  # 无重复字符
                    yield "abcdefghij"
                elif i == 7:  # 重复模式 aabbcc
                    yield "aabbcc"
                elif i == 8:  # 间隔刚好等于 k
                    yield "ababab"
                elif i == 9:  # 间隔刚好不等于 k
                    yield "ababab"
                elif i == 10:  # 交替合并：abacabad
                    yield "abacabad"
                elif i == 11:  # 靠近字符
                    yield "xyzxy"
                elif i == 12:  # 最大长度，k=1（大规模合并）
                    yield "a" * 50
                elif i == 13:  # 最大长度，k=50（不合并）
                    yield "a" * 50
                elif i == 14:  # abcabcabc 模式
                    yield "abcabcabc"
                elif i == 15:  # abcabcabc 模式，k较小
                    yield "abcabcabc"
                elif i == 16:  # 混合重复模式
                    yield "aabbccddeeff"
                elif i == 17:  # 单一字符，k = 1
                    yield "zzzzz"
                elif i == 18:  # 单一字符，k = 5
                    yield "zzzzz"
                elif i == 19:  # 字符间隔较远
                    yield "a" + "b" * 20 + "a"
                elif i == 20:  # 嵌套重复模式
                    yield "abaaba"
                elif i == 21:  # 长字符串，k=1
                    yield "abcdeabcdeabcde"
                elif i == 22:  # 长字符串，k=5
                    yield "abcdeabcdeabcde"
                elif i == 23:  # 全不同字符
                    yield "qwerty"
                elif i == 24:  # 少量重复
                    yield "ababa"
                elif i == 25:  # 紧凑重复
                    yield "aaabbbccc"
                elif i == 26:  # 分散重复
                    yield "abcabcabcabc"
                elif i == 27:  # 边界：k等于字符串长度
                    yield "test"
                elif i == 28:  # 边界：k等于1
                    yield "mississippi"
                elif i == 29:  # 边界：k等于1，连续重复
                    yield "aaaaabbbbbccccc"

            # 生成70个随机测试用例
            for i in range(70):
                # 随机字符串长度 1-20（缩小范围以避免超时）
                yield s_generate_string_with_length(vocab, (1, 20))

        def generate_k():
            # 生成30个特殊设计的测试用例的k值
            for i in range(30):
                if i == 0:
                    yield 3
                elif i == 1:
                    yield 2
                elif i == 2:
                    yield 2
                elif i == 3:
                    yield 1
                elif i == 4:
                    yield 1
                elif i == 5:
                    yield 5
                elif i == 6:
                    yield 3
                elif i == 7:
                    yield 2
                elif i == 8:
                    yield 2
                elif i == 9:
                    yield 1
                elif i == 10:
                    yield 2
                elif i == 11:
                    yield 1
                elif i == 12:
                    yield 1
                elif i == 13:
                    yield 50
                elif i == 14:
                    yield 3
                elif i == 15:
                    yield 2
                elif i == 16:
                    yield 2
                elif i == 17:
                    yield 1
                elif i == 18:
                    yield 5
                elif i == 19:
                    yield 5
                elif i == 20:
                    yield 3
                elif i == 21:
                    yield 1
                elif i == 22:
                    yield 5
                elif i == 23:
                    yield 10
                elif i == 24:
                    yield 3
                elif i == 25:
                    yield 1
                elif i == 26:
                    yield 3
                elif i == 27:
                    yield 4
                elif i == 28:
                    yield 1
                elif i == 29:
                    yield 1

            # 生成70个随机测试用例的k值
            for i in range(70):
                yield _generate_int((1, 20))

        return generate_s(), generate_k()
    

import math
from . import Problem
from typing import List
import re
from math import inf


class Solution3(Problem):
    date = "2026-2-28"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3854,
                         types=[],
                         pass_rate=0.32,
                         description='给你一个整数数组 `nums`。\n如果对于每一个下标\xa0`i`（其中 `0 <= i < n - 1`），`nums[i]` 和 `nums[i + 1]` 具有不同的奇偶性（一个是偶数，另一个是奇数），则该数组被称为**奇偶交替**的。\n在一次操作中，你可以选择任意下标\xa0`i`，并将 `nums[i]` 增加 1 或减少 1。\n返回一个长度为 2 的整数数组 `answer`，其中：\n - `answer[0]` 是使数组变为奇偶交替所需的**最少**操作次数。\n - `answer[1]` 是在所有通过执行**恰好**`answer[0]` 次操作获得的奇偶交替数组中，`max(nums) - min(nums)` 的**最小**可能值。\n\n长度为 1 的数组被认为是奇偶交替的。\n\n**示例 1：**\n> \n**输入：**`nums = [-2,-3,1,4]`\n**输出：**`[2,6]`\n**解释：**\n执行以下操作：\n - 将 `nums[2]` 增加 1，得到 `nums = [-2, -3, 2, 4]`。\n - 将 `nums[3]` 减少 1，得到 `nums = [-2, -3, 2, 3]`。\n\n得到的数组是奇偶交替的，且 `max(nums) - min(nums) = 3 - (-3) = 6` 是所有使用恰好 2 次操作可获得的奇偶交替数组中的最小值。\n**示例 2：**\n> \n**输入：**`nums = [0,2,-2]`\n**输出：**`[1,3]`\n**解释：**\n执行以下操作：\n - 将 `nums[1]` 减少 1，得到 `nums = [0, 1, -2]`。\n\n得到的数组是奇偶交替的，且 `max(nums) - min(nums) = 1 - (-2) = 3` 是所有使用恰好 1 次操作可获得的奇偶交替数组中的最小值。\n**示例 3：**\n> \n**输入：**`nums = [7]`\n**输出：**`[0,0]`\n**解释：**\n不需要任何操作。数组已经是奇偶交替的，且 `max(nums) - min(nums) = 7 - 7 = 0`，这是可能的最小值。\n\n**提示：**\n - `1 <= nums.length <= 10^5`\n - `-10^9 <= nums[i] <= 10^9`'
                         )

    def solve(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0, 0]
        g_min = min(nums)
        g_max = max(nums)

        def calc(target: int) -> List[int]:
            op = 0
            mn, mx = (inf, -inf)
            for i, x in enumerate(nums):
                if x - i & 1 != target:
                    op += 1
                    if x == g_min:
                        x += 1
                    elif x == g_max:
                        x -= 1
                mn = min(mn, x)
                mx = max(mx, x)
            return [op, max(mx - mn, 1)]
        return min(calc(0), calc(1))

    def gen(self):
            """
            生成测试样例。

            测试场景分配（testcase_num = 100）：
            1. 边界长度测试（10个）：
               - 1个元素：5组（包括极值和普通值）
               - 2个元素：5组
            2. 特殊结构测试（25个）：
               - 已经奇偶交替：7组
               - 所有元素同奇偶：7组
               - 全相同元素：4组
               - 严格递增/递减：4组
               - 交替模式：3组
            3. 边界值测试（15个）：
               - 包含极大/极小值：7组
               - 0值密集区域：4组
               - 混合正负极值：4组
            4. 正常随机测试（50个）：
               - 中小规模随机数组

            考虑到参考代码的复杂度，限制：
               - 最大长度：1000（而非10^5）
               - 数值范围：-1000~1000（而非-10^9~10^9）
            """
            import random
            random.seed(self.seed)

            def generate_array(length_range=(1, 1000), value_range=(-1000, 1000)):
                """生成指定长度和值范围的随机数组"""
                length = random.randint(*length_range)
                return [random.randint(*value_range) for _ in range(length)]

            test_cases = []

            # 1. 边界长度测试（10个）
            # 1.1 单元素数组（5个）
            test_cases.append([0])          # 0值
            test_cases.append([1])          # 正奇数
            test_cases.append([-1])         # 负奇数
            test_cases.append([1000])       # 边界正值
            test_cases.append([-1000])      # 边界负值

            # 1.2 双元素数组（5个）
            test_cases.append([1, 2])       # 已经奇偶交替
            test_cases.append([2, 2])       # 同奇偶
            test_cases.append([1000, -1000]) # 边界值
            test_cases.append([0, 0])       # 相同0值
            test_cases.append([1, 1000])    # 小值和边界值

            # 2. 特殊结构测试（25个）
            # 2.1 已经奇偶交替的数组（7个）
            for i in range(7):
                length = random.randint(3, 50)
                arr = []
                if i % 2 == 0:
                    # 从偶数开始：偶、奇、偶、奇...
                    arr = [(0 if j % 2 == 0 else 1) + random.randint(0, 100) * 2 for j in range(length)]
                else:
                    # 从奇数开始：奇、偶、奇、偶...
                    arr = [(1 if j % 2 == 0 else 0) + random.randint(0, 100) * 2 for j in range(length)]
                test_cases.append(arr)

            # 2.2 所有元素同奇偶（7个）
            for i in range(7):
                length = random.randint(3, 50)
                is_even = (i % 2 == 0)
                base = 0 if is_even else 1
                arr = [base + random.randint(0, 50) * 2 for _ in range(length)]
                test_cases.append(arr)

            # 2.3 全相同元素（4个）
            test_cases.append([5] * 10)
            test_cases.append([8] * 20)
            test_cases.append([0] * 15)
            test_cases.append([-7] * 12)

            # 2.4 严格递增/递减（4个）
            test_cases.append(list(range(1, 21)))           # 递增，奇偶交替
            test_cases.append(list(range(2, 22)))           # 递增，同奇偶
            test_cases.append(list(range(20, 0, -1)))       # 递减
            test_cases.append([i * 2 for i in range(1, 16)])# 递增，全偶数

            # 2.5 特殊交替模式（3个）
            test_cases.append([i % 2 for i in range(20)])   # 0,1,0,1...
            test_cases.append([(i + 1) % 2 for i in range(20)]) # 1,0,1,0...
            test_cases.append([random.choice([i % 2, i % 2 + 2]) for i in range(15)])

            # 3. 边界值测试（15个）
            # 3.1 包含极大/极小值（7个）
            for i in range(7):
                length = random.randint(5, 30)
                arr = []
                for j in range(length):
                    if random.random() < 0.1:  # 10%概率生成极值
                        arr.append(random.choice([-1000, 1000, -999, 999]))
                    else:
                        arr.append(random.randint(-500, 500))
                test_cases.append(arr)

            # 3.2 0值密集区域（4个）
            for i in range(4):
                length = random.randint(10, 30)
                arr = [random.randint(-5, 5) for _ in range(length)]
                test_cases.append(arr)

            # 3.3 混合正负极值（4个）
            for i in range(4):
                arr = []
                for j in range(random.randint(10, 25)):
                    choice = random.choice(['large_pos', 'large_neg', 'small_pos', 'small_neg', 'zero'])
                    if choice == 'large_pos':
                        arr.append(random.randint(500, 1000))
                    elif choice == 'large_neg':
                        arr.append(random.randint(-1000, -500))
                    elif choice == 'small_pos':
                        arr.append(random.randint(1, 100))
                    elif choice == 'small_neg':
                        arr.append(random.randint(-100, -1))
                    else:
                        arr.append(0)
                test_cases.append(arr)

            # 4. 正常随机测试（50个）
            for i in range(50):
                if i < 10:
                    # 较小规模（3-20）
                    arr = generate_array((3, 20), (-100, 100))
                elif i < 25:
                    # 中等规模（20-100）
                    arr = generate_array((20, 100), (-500, 500))
                else:
                    # 较大规模（100-500，避免太大导致超时）
                    arr = generate_array((100, 500), (-1000, 1000))
                test_cases.append(arr)

            return (test_cases,)
    


from . import Problem
import re


class Solution4(Problem):
    date = "2026-2-28"
    def __init__(self):
        Problem.__init__(self,
                         degree=2,
                         idx=3855,
                         types=[],
                         pass_rate=0.51,
                         description='给你三个整数 `l`、`r` 和 `k`。\n考虑所有由**恰好**`k` 位数字组成的整数里，每一位数字都是从整数范围 `[l, r]`（闭区间）中独立选择的。如果该范围内包含 0，则允许出现前导零。\n返回一个整数，代表**所有此类数字之和**。由于答案可能很大，请将其对 `10^9 + 7`**取模**后返回。\n\n**示例 1：**\n> \n**输入：**`l = 1, r = 2, k = 2`\n**输出：**`66`\n**解释：**\n - 使用范围 `[1, 2]` 内的 `k = 2` 位数字形成的所有数字为 `11, 12, 21, 22`。\n - 总和为 `11 + 12 + 21 + 22 = 66`。\n\n**示例 2：**\n> \n**输入：**`l = 0, r = 1, k = 3`\n**输出：**`444`\n**解释：**\n - 使用范围 `[0, 1]` 内的 `k = 3` 位数字形成的所有数字为 `000, 001, 010, 011, 100, 101, 110, 111`。\n - 这些去掉前导零后的数字为 `0, 1, 10, 11, 100, 101, 110, 111`。\n - 总和为 444。\n\n**示例 3：**\n> \n**输入：**`l = 5, r = 5, k = 10`\n**输出：**`555555520`\n**解释：**\n - 5555555555 是唯一一个由范围 `[5, 5]` 内 `k = 10` 位数字组成的有效数字。\n - 总和为 `5555555555 % (10^9 + 7) = 555555520`。\n\n**提示：**\n - `0 <= l <= r <= 9`\n - `1 <= k <= 10^9`'
                         )

    def solve(self, l: int, r: int, k: int) -> int:
        MOD = 1000000007
        m = r - l + 1
        return (l + r) * m * (pow(10, k, MOD) - 1) * pow(18, -1, MOD) * pow(m, k - 1, MOD) % MOD

    def gen(self):
        """
        生成测试样例。

        参数约束：
        - 0 <= l <= r <= 9
        - 1 <= k <= 10^9

        为了避免超时，将k的上限调整为10000（足以测试逻辑正确性）

        测试场景分配：
        1. 边界值 (15个):
           - l=r=0, k=1 (最小值，全0)
           - l=r=9, k=1 (最大单数字)
           - l=0, r=9, k=1 (最大范围)
           - l=r=5, k=10 (示例3情况)
           - l=1, r=1, k=5 (单非零数字)
           - l=0, r=0, k=5 (全零)
           - l=1, r=2, k=2 (示例1)
           - l=0, r=1, k=3 (示例2)
           - l=1, r=9, k=2
           - l=0, r=5, k=2
           - l=2, r=7, k=1
           - l=3, r=4, k=3
           - l=1, r=1, k=100 (单数字大k)
           - l=0, r=9, k=100 (最大范围大k)
           - l=4, r=4, k=1

        2. 正常随机 (15个):
           - 随机生成l, r, k，覆盖各种组合
        """
        testcase_num = 30

        # 减小k的最大值以避免超时，同时足够测试正确性
        k_max = 10000

        l_cases = []
        r_cases = []
        k_cases = []

        # 边界值测试用例
        boundary_cases = [
            # (l, r, k, description)
            (0, 0, 1, "min l=r=0, k=1"),
            (9, 9, 1, "max l=r=9, k=1"),
            (0, 9, 1, "max range, k=1"),
            (5, 5, 10, "example 3: single digit"),
            (1, 1, 5, "single non-zero digit"),
            (0, 0, 5, "all zeros"),
            (1, 2, 2, "example 1"),
            (0, 1, 3, "example 2"),
            (1, 9, 2, "wide range no zero"),
            (0, 5, 2, "mid range with zero"),
            (2, 7, 1, "k=1 range"),
            (3, 4, 3, "small range k=3"),
            (1, 1, 100, "single digit large k"),
            (0, 9, 100, "max range large k"),
            (4, 4, 1, "single digit mid"),
        ]

        # 添加边界用例
        for l, r, k, _ in boundary_cases:
            l_cases.append(l)
            r_cases.append(r)
            k_cases.append(k)

        # 随机用例
        import random
        random.seed(self.seed)

        for _ in range(testcase_num - len(boundary_cases)):
            # 随机生成l和r，确保l <= r
            l = random.randint(0, 8)
            r = random.randint(l, 9)

            # 随机生成k，覆盖不同数量级
            rand_val = random.random()
            if rand_val < 0.3:
                # 30%概率生成小k (1-10)
                k = random.randint(1, 10)
            elif rand_val < 0.7:
                # 40%概率生成中等k (11-100)
                k = random.randint(11, 100)
            elif rand_val < 0.9:
                # 20%概率生成较大k (101-1000)
                k = random.randint(101, 1000)
            else:
                # 10%概率生成大k (1001-10000)
                k = random.randint(1001, k_max)

            l_cases.append(l)
            r_cases.append(r)
            k_cases.append(k)

        return l_cases, r_cases, k_cases
    

