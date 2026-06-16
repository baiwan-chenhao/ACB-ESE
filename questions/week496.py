
import random
import string
from . import Problem
from collections import Counter
import re
from string import ascii_lowercase
from string import digits
from math import inf


class Solution1(Problem):
    date = "2026-4-5"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3889,
                         types=[],
                         pass_rate=0.65,
                         description='给你一个由小写英文字母和数字组成的字符串 `s`。\n对于每个字符，其**镜像字符**根据逆序定义其字符集合：\n - 对于字母，某字符的镜像字符是字母表中从末尾与其位置相同的字母。\n\t - 例如，`\'a\'` 的镜像字符是 `\'z\'`，`\'b\'` 的镜像字符是 `\'y\'`，以此类推。\n\n - 对于数字，某字符的镜像字符是范围 `\'0\'` 到 `\'9\'` 中从末尾与其位置相同的数字。\n\t - 例如，`\'0\'` 的镜像字符是 `\'9\'`，`\'1\'` 的镜像字符是 `\'8\'`，以此类推。\n\n对于字符串中每个**唯一**字符 `c`：\n - 设 `m` 为其**镜像字符**。\n - 设 `freq(x)` 表示字符 `x` 在字符串中出现的次数。\n - 计算其与镜像字符出现次数之间的**绝对差**，定义为：`|freq(c) - freq(m)|`\n\n镜像对 `(c, m)` 和 `(m, c)` 被视为相同，只能被计算**一次**。\n返回一个整数，表示所有这些**不同的镜像对**的绝对差之和。\n\n**示例 1：**\n> \n**输入：**`s = "ab1z9"`\n**输出：**`3`\n**解释：**\n对于每个镜像对：\n| `c` | `m` | `freq(c)` | `freq(m)` | `|freq(c) - freq(m)|` |\n| --- | --- | --- | --- | --- |\n| a | z | 1 | 1 | 0 |\n| b | y | 1 | 0 | 1 |\n| 1 | 8 | 1 | 0 | 1 |\n| 9 | 0 | 1 | 0 | 1 |\n\n因此，答案是 `0 + 1 + 1 + 1 = 3`。\n**示例 2：**\n> \n**输入：**`s = "4m7n"`\n**输出：**`2`\n**解释：**\n| `c` | `m` | `freq(c)` | `freq(m)` | `|freq(c) - freq(m)|` |\n| --- | --- | --- | --- | --- |\n| 4 | 5 | 1 | 0 | 1 |\n| m | n | 1 | 1 | 0 |\n| 7 | 2 | 1 | 0 | 1 |\n\n因此，答案是 `1 + 0 + 1 = 2`。\n**示例 3：**\n> \n`**输入：**s = "byby"`\n`**输出：**0`\n**解释：**\n| `c` | `m` | `freq(c)` | `freq(m)` | `|freq(c) - freq(m)|` |\n| --- | --- | --- | --- | --- |\n| b | y | 2 | 2 | 0 |\n\n因此，答案是 0 。\n\n**提示:**\n - `1 <= s.length <= 5 * 10^5`\n - `s`\xa0仅由小写英文字母和数字组成。'
                         )

    def solve(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        for i in range(13):
            ans += abs(cnt[ascii_lowercase[i]] - cnt[ascii_lowercase[-1 - i]])
        for i in range(5):
            ans += abs(cnt[digits[i]] - cnt[digits[-1 - i]])
        return ans

    def gen(self):
        """
        生成测试样例，用于测试镜像字符频率绝对差之和的计算。

        生成策略：
        1. 边界情况：短字符串（长度1-10）、长字符串
        2. 正常情况：随机混合字母和数字
        3. 特殊结构：只含字母、只含数字、同一字符重复、完美镜像配对

        为了避免测试时间过长，将字符串长度上限从5e5降至5000。
        """
        # 字符集：小写字母和数字
        vocab = ascii_lowercase + digits

        # 生成不同类型的测试用例
        testcases = []

        # 20% 边界短字符串（长度1-10）
        for _ in range(20):
            length = self.s_generate_int(int_range=(1, 10))
            s = ''.join(random.choice(vocab) for _ in range(length))
            testcases.append(s)

        # 10% 单字符重复（测试同一字符多次出现）
        for _ in range(10):
            char = random.choice(vocab)
            length = self.s_generate_int(int_range=(5, 100))
            s = char * length
            testcases.append(s)

        # 10% 只含字母
        for _ in range(10):
            length = self.s_generate_int(int_range=(10, 100))
            s = ''.join(random.choice(ascii_lowercase) for _ in range(length))
            testcases.append(s)

        # 10% 只含数字
        for _ in range(10):
            length = self.s_generate_int(int_range=(10, 100))
            s = ''.join(random.choice(digits) for _ in range(length))
            testcases.append(s)

        # 10% 完美镜像配对（a和z出现次数相同，b和y出现次数相同等）
        for _ in range(10):
            length = self.s_generate_int(int_range=(10, 50)) // 2 * 2  # 确保偶数长度
            s = ''
            for _ in range(length // 2):
                # 随机选择一对镜像字符
                if random.random() < 0.5:
                    i = random.randint(0, 12)
                    c1 = ascii_lowercase[i]
                    c2 = ascii_lowercase[25 - i]
                else:
                    i = random.randint(0, 4)
                    c1 = digits[i]
                    c2 = digits[9 - i]
                s += c1 + c2
            random.seed(self.seed + _)
            testcases.append(s)

        # 30% 随机混合字符串
        for _ in range(30):
            length = self.s_generate_int(int_range=(20, 500))
            s = ''.join(random.choice(vocab) for _ in range(length))
            testcases.append(s)

        # 10% 较长随机字符串
        for _ in range(10):
            length = self.s_generate_int(int_range=(1000, 5000))
            s = ''.join(random.choice(vocab) for _ in range(length))
            testcases.append(s)

        return (testcases,)
    


from . import Problem
from typing import List
from collections import defaultdict
from bisect import bisect_right
import re
MX = 1000000000
cnt = defaultdict(int)
a = 1
while a * a * a * 2 <= MX:
    b = a
    while (s := (a * a * a + b * b * b)) <= MX:
        cnt[s] += 1
        b += 1
    a += 1
good_integers = sorted((x for x, c in cnt.items() if c > 1))

class Solution2(Problem):
    date = "2026-4-5"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3890,
                         types=[],
                         pass_rate=0.47,
                         description='给你一个整数 `n`。\n当存在**至少**两组不同的整数对 `(a, b)` 满足以下条件时，整数 `x` 被称为**好整数**：\n - `a` 和 `b` 是正整数。\n - `a <= b`\n - `x = a^3 + b^3`\n\n返回一个数组，其中包含所有小于等于 `n` 的好整数，并按升序排序。\n\n**示例 1：**\n> \n**输入：**`n = 4104`\n**输出：**`[1729,4104]`\n**解释：**\n在小于等于 4104 的整数中，好整数包括：\n - 1729：`1^3 + 12^3 = 1729`，以及 `9^3 + 10^3 = 1729`。\n - 4104：`2^3 + 16^3 = 4104`，以及 `9^3 + 15^3 = 4104`。\n\n因此，答案是 `[1729, 4104]`。\n**示例 2：**\n> \n**输入：**`n = 578`\n**输出：**`[]`\n**解释：**\n不存在小于等于 578 的好整数，因此答案是空数组。\n\n**提示：**\n - `1 <= n <= 10^9`'
                         )

    def solve(self, n: int) -> List[int]:
        i = bisect_right(good_integers, n)
        return good_integers[:i]

    def gen(self):
        """
        生成测试用例，覆盖好整数问题的各种边界情况。

        策略说明：
        1. 边界值测试：n的最小值、最大值
        2. 好整数边界：等于好整数、小于好整数、略大于好整数
        3. 关键测试点：第一个好整数1729、第二个好整数4104
        4. 随机分布：不同范围内的随机值

        由于好整数列表已预计算完成，本题主要测试二分查找的正确性，
        因此重点在于测试不同n值下过滤结果的准确性。
        """
        def n_generator():
            # 关键测试点：覆盖各种边界和特殊情况
            key_values = [
                1,           # 最小值，无好整数
                577,         # 小于第一个好整数1729，无好整数
                1728,        # 略小于第一个好整数
                1729,        # 刚好等于第一个好整数
                1730,        # 略大于第一个好整数
                4104,        # 等于第二个好整数
                4105,        # 略大于第二个好整数
                100000,      # 中等值
                1000000000   # 最大值，包含所有好整数
            ]

            for n in key_values:
                yield n

            # 补充随机测试用例，增加覆盖率
            for n in self.generate_int(int_range=(1, 1000000000)):
                yield n

        # 返回包含一个生成器的元组，对应solve函数的一个参数n
        return (n_generator(),)
    

import random
from . import Problem
from typing import List
import re


class Solution3(Problem):
    date = "2026-4-5"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3891,
                         types=[],
                         pass_rate=0.3,
                         description='给你一个长度为 `n` 的整数数组 `nums`。\n如果 `nums[i] > nums[i - 1]` 且 `nums[i] > nums[i + 1]`，则下标 `i` (`0 < i < n - 1`) 是**特殊的**。\n你可以执行操作，选择**任意**下标 `i` 并将 `nums[i]`**增加**1。\n你的目标是：\n\n- **最大化**特殊**下标**的数量。\n- **最小化**达到该**最大值**所需的总**操作**数。\n\n返回所需的**最小**总操作数。\n\n**示例 1：**\n\n> **输入：**`nums = [1,2,2]`\n**输出：**`1`\n**解释：**\n - 从 `nums = [1, 2, 2]` 开始。\n - 将 `nums[1]` 增加 1，数组变为 `[1, 3, 2]`。\n - 最终数组是 `[1, 3, 2]`，有 1 个特殊的下标，这是可达到的最大值。\n - 不可能用更少的操作达到这个数量的特殊的下标。因此，答案是 1。\n\n**示例 2：**\n> \n**输入：**`nums = [2,1,1,3]`\n**输出：**`2`\n**解释：**\n - 从 `nums = [2, 1, 1, 3]` 开始。\n - 在下标 1 处执行 2 次操作，数组变为 `[2, 3, 1, 3]`。\n - 最终数组是 `[2, 3, 1, 3]`，有 1 个特殊的下标，这是可达到的最大值。因此，答案是 2。\n\n**示例 3：**\n> \n**输入：**`nums = [5,2,1,4,3]`\n**输出：**`4`\n**解释：**\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\n - 从 `nums = [5, 2, 1, 4, 3]` 开始。\n - 在下标 1 处执行 4 次操作，数组变为 `[5, 6, 1, 4, 3]`。\n - 最终数组是 `[5, 6, 1, 4, 3]`，有 2 个特殊的下标，这是可达到的最大值。因此，答案是 4。\u200b\u200b\u200b\u200b\u200b\u200b\u200b\n\n**提示：**\n - `3 <= n <= 10^5`\n - `1 <= nums[i] <= 10^9`'
                         )

    def solve(self, nums: List[int]) -> int:
        n = len(nums)
        suf = [0] * (n + 1)
        for i in range(n - 2, 0, -2):
            suf[i] = suf[i + 2] + max(max(nums[i - 1], nums[i + 1]) - nums[i] + 1, 0)
        if n % 2 > 0:
            return suf[1]
        ans = suf[2]
        pre = 0
        for i in range(1, n - 1, 2):
            pre += max(max(nums[i - 1], nums[i + 1]) - nums[i] + 1, 0)
            ans = min(ans, pre + suf[i + 3])
        return ans

    def gen(self):
        """
        生成测试样例用于测试特殊下标最大化问题。

        策略：
        1. 边界情况：最小长度n=3，奇数长度和偶数长度
        2. 无需操作的情况：初始已满足最大特殊下标
        3. 需要大量操作的情况：递减或递增序列
        4. 特殊结构：全相同、严格递增/递减
        5. 随机情况：中等规模随机数组

        返回格式：(参数列表的元组)，每个元素对应函数的参数
        这里函数只有一个参数 nums，所以返回 ([nums1, nums2, ...],)
        """
        testcase_num = self.testcase_num
        nums_list = []

        # 分配测试用例数量
        num_edge = 20      # 边界情况
        num_special = 15   # 特殊结构
        num_random = 65    # 随机情况

        random.seed(self.seed)

        # ====== 边界情况 (n=3) ======
        for _ in range(num_edge // 2):
            n = 3
            # 最小长度，随机值
            nums = [self.s_generate_int(int_range=(1, 10)) for _ in range(n)]
            nums_list.append(nums)

        # 小规模奇偶长度
        for _ in range(num_edge // 2):
            n = random.choice([4, 5, 6, 7])
            nums = [self.s_generate_int(int_range=(1, 10)) for _ in range(n)]
            nums_list.append(nums)

        # ====== 特殊结构 ======
        # 全相同
        nums = [5] * 10
        nums_list.append(nums)

        nums = [1] * 5
        nums_list.append(nums)

        # 严格递增
        nums = [1, 2, 3, 4, 5, 6, 7]
        nums_list.append(nums)

        nums = [1, 2, 3, 4, 5, 6]
        nums_list.append(nums)

        # 严格递减
        nums = [10, 9, 8, 7, 6, 5, 4]
        nums_list.append(nums)

        nums = [8, 7, 6, 5, 4, 3]
        nums_list.append(nums)

        # 已经有最大特殊下标的情况（奇数位置都是峰值）
        nums = [1, 3, 1, 5, 1, 7, 1]
        nums_list.append(nums)

        nums = [2, 5, 2, 6, 2]
        nums_list.append(nums)

        # 偶数位置都是峰值
        nums = [3, 1, 5, 1, 7, 1, 9, 1]
        nums_list.append(nums)

        nums = [4, 1, 6, 1, 8, 1]
        nums_list.append(nums)

        # 需要大量操作的情况（递减序列）
        nums = [100, 50, 25, 12, 6, 3, 1]
        nums_list.append(nums)

        nums = [50, 40, 30, 20, 10]
        nums_list.append(nums)

        # 峰值交替
        nums = [1, 10, 1, 9, 1, 8, 1]
        nums_list.append(nums)

        # 示例中的情况
        nums_list.append([1, 2, 2])
        nums_list.append([2, 1, 1, 3])
        nums_list.append([5, 2, 1, 4, 3])

        # ====== 随机情况 ======
        for _ in range(num_random):
            n = self.s_generate_int(int_range=(3, 100))
            nums = [self.s_generate_int(int_range=(1, 100)) for _ in range(n)]
            nums_list.append(nums)

        return (nums_list,)
    

import random
from . import Problem
from typing import List
from functools import cache
import re


class Solution4(Problem):
    date = "2026-4-5"
    def __init__(self):
        Problem.__init__(self,
                         degree=2,
                         idx=3892,
                         types=[],
                         pass_rate=0.39,
                         description='给你一个长度为 `n` 的循环整数数组 `nums`。\n如果下标 `i`\xa0对应的值**严格大于**其相邻元素，则该下标是一个**峰值**：\n - 如果 `i > 0`，下标 `i` 的**前一个**相邻元素是 `nums[i - 1]`，否则是 `nums[n - 1]`。\n - 如果 `i < n - 1`，下标 `i` 的**后一个**相邻元素是 `nums[i + 1]`，否则是 `nums[0]`。\n\n你可以执行以下操作**任意**次数：\n - 选择任意下标 `i` 并将 `nums[i]`**增加**1。\n\n返回使数组包含**至少**`k` 个峰值所需的**最小**操作数。如果不可能，返回 -1。\n\n**示例 1：**\n> \n**输入：**`nums = [2,1,2], k = 1`\n**输出：**`1`\n**解释：**\n - 为了实现至少 `k = 1` 个峰值，我们可以将 `nums[2] = 2` 增加到 3。\n - 执行此操作后，`nums[2] = 3` 严格大于其相邻元素 `nums[0] = 2` 和 `nums[1] = 1`。\n - 因此，所需的最小操作数是 1。\n\n**示例 2：**\n> \n**输入：**`nums = [4,5,3,6], k = 2`\n**输出：**`0`\n**解释：**\n - 数组在零次操作下已经包含至少 `k = 2` 个峰值。\n - 下标 1：`nums[1] = 5` 严格大于其相邻元素 `nums[0] = 4` 和 `nums[2] = 3`。\n - 下标 3：`nums[3] = 6` 严格大于其相邻元素 `nums[2] = 3` 和 `nums[0] = 4`。\n - 因此，所需的最小操作数是 0。\n\n**示例 3：**\n> \n**输入：**`nums = [3,7,3], k = 2`\n**输出：**`-1`\n**解释：**\n在这个数组中不可能有至少 `k = 2` 个峰值。因此，答案是 -1。\n\n**提示：**\n - `2 <= n == nums.length <= 5000`\n - `-10^5 <= nums[i] <= 10^5`\n - `0 <= k <= n`'
                         )

    def solve0(self, a: List[int], k: int) -> int:

        @cache
        def dfs(left: int, i: int) -> int:
            if left == 0:
                return 0
            if left > (i + 1) // 2:
                return inf
            not_choose = dfs(left, i - 1)
            choose = dfs(left - 1, i - 2) + max(max(a[i - 1], a[i + 1]) - a[i] + 1, 0)
            return min(not_choose, choose)
        return dfs(k, len(a) - 2)

    def solve(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k > n // 2:
            return -1
        cnt = 0
        for i in range(n):
            if nums[i - 1] < nums[i] > nums[(i + 1) % n]:
                cnt += 1
        if cnt >= k:
            return 0
        ans1 = self.solve0([nums[-1]] + nums, k)
        ans2 = self.solve0(nums + [nums[0]], k)
        return min(ans1, ans2)

    def gen(self):
        """
        生成测试样例，覆盖边界值、特殊结构和一般情况。

        覆盖场景：
        1. 边界测试：最小长度n=2、k=0、k=n//2、k>n//2（返回-1）
        2. 特殊结构：全相等、严格递增、严格递减、已有足够峰值
        3. 一般情况：需要操作创造峰值

        为避免参考答案超时，数组长度限制为2-100。
        """
        # 由于最多只生成100个测试用例，手动构造以确保覆盖关键场景
        nums_list = []
        k_list = []

        # ========== 边界测试 ==========
        # n=2, k=0
        nums_list.append([5, 3])
        k_list.append(0)

        # n=2, k=1（最大可能）
        nums_list.append([1, 1])
        k_list.append(1)

        # n=2, k=2（不可能）
        nums_list.append([1, 1])
        k_list.append(2)

        # n=3, k=0
        nums_list.append([1, 2, 1])
        k_list.append(0)

        # n=3, k=1（最大可能）
        nums_list.append([1, 1, 1])
        k_list.append(1)

        # n=3, k=2（不可能）
        nums_list.append([1, 1, 1])
        k_list.append(2)

        # ========== 特殊结构测试 ==========
        # 全相等
        nums_list.append([5, 5, 5, 5])
        k_list.append(2)

        # 严格递增
        nums_list.append([1, 2, 3, 4, 5])
        k_list.append(2)

        # 严格递减
        nums_list.append([5, 4, 3, 2, 1])
        k_list.append(2)

        # 交替高低（已有很多峰值）
        nums_list.append([1, 5, 1, 5, 1, 5])
        k_list.append(1)
        k_list.append(3)

        # 单峰
        nums_list.append([1, 2, 1])
        k_list.append(1)

        # 双峰
        nums_list.append([1, 3, 1, 3, 1])
        k_list.append(2)

        # 示例1
        nums_list.append([2, 1, 2])
        k_list.append(1)

        # 示例2
        nums_list.append([4, 5, 3, 6])
        k_list.append(2)

        # 示例3
        nums_list.append([3, 7, 3])
        k_list.append(2)

        # ========== 循环边界测试 ==========
        # nums[-1]影响nums[0]的情况
        nums_list.append([1, 5, 1])
        k_list.append(2)  # 需要同时让nums[-1]和nums[0]成为峰值

        nums_list.append([5, 1, 5])
        k_list.append(1)

        # ========== 大k值测试（接近最大可能） ==========
        # n=6, k=3（最大可能）
        nums_list.append([1, 1, 1, 1, 1, 1])
        k_list.append(3)

        # n=10, k=5（最大可能）
        nums_list.append([0] * 10)
        k_list.append(5)

        # 不可能：n=10, k=6
        nums_list.append([0] * 10)
        k_list.append(6)

        # ========== 需要操作的测试 ==========
        # 需要少量操作
        nums_list.append([1, 2, 1, 2, 1])
        k_list.append(3)  # 需要让某些点成为峰值

        # 需要大量操作（数值很大）
        nums_list.append([1000, 999, 1000, 999, 1000])
        k_list.append(2)

        # 负数情况
        nums_list.append([-5, -3, -7, -2])
        k_list.append(2)

        # 混合正负
        nums_list.append([10, -5, 20, -10, 30])
        k_list.append(2)

        # 长数组（减少最大长度避免超时）
        long_arr1 = [i % 10 for i in range(50)]  # 重复模式
        nums_list.append(long_arr1)
        k_list.append(25)

        long_arr2 = [1] * 50
        nums_list.append(long_arr2)
        k_list.append(25)

        # 随机测试（较小规模）
        random.seed(42)
        for _ in range(20):
            n = random.randint(2, 20)
            arr = [random.randint(-100, 100) for _ in range(n)]
            k = random.randint(0, n // 2 + 1)  # 包含不可能的情况
            nums_list.append(arr)
            k_list.append(k)

        # 填充到100个测试用例
        while len(nums_list) < 100:
            n = random.randint(2, 20)
            arr = [random.randint(-50, 50) for _ in range(n)]
            k = random.randint(0, min(n, 5))  # 限制k值
            nums_list.append(arr)
            k_list.append(k)

        return nums_list, k_list


