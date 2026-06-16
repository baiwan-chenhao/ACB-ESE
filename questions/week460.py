import string
from . import Problem as Testing, ProblemType
from ..testcase_sampler import _generate_int, _generate_list_int
from typing import List


class Solution1(Testing):
    date = "2025-7-27"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3627,
                         types=[ProblemType.Array],
                         pass_rate=0.649,
                         description="给你一个整数数组 `nums`，其长度可以被 3 整除。\n\n你需要通过多次操作将数组清空。在每一步操作中，你可以从数组中选择任意三个元素，计算它们的 **中位数** ，并将这三个元素从数组中移除。\n\n奇数长度数组的 **中位数** 定义为数组按非递减顺序排序后位于中间的元素。\n\n返回通过所有操作得到的 **中位数之和的最大值** 。\n\n \n\n**示例 1：**\n\n**输入：** nums = [2,1,3,2,1,3]\n\n**输出：** 5\n\n**解释：**\n\n- 第一步，选择下标为 2、4 和 5 的元素，它们的中位数是 3。移除这些元素后，`nums` 变为 `[2, 1, 2]`。\n- 第二步，选择下标为 0、1 和 2 的元素，它们的中位数是 2。移除这些元素后，`nums` 变为空数组。\n\n因此，中位数之和为 `3 + 2 = 5`。\n\n**示例 2：**\n\n**输入：** nums = [1,1,10,10,10,10]\n\n**输出：** 20\n\n**解释：**\n\n- 第一步，选择下标为 0、2 和 3 的元素，它们的中位数是 10。移除这些元素后，`nums` 变为 `[1, 10, 10]`。\n- 第二步，选择下标为 0、1 和 2 的元素，它们的中位数是 10。移除这些元素后，`nums` 变为空数组。\n\n因此，中位数之和为 `10 + 10 = 20`。\n\n \n\n**提示：**\n\n- `1 <= nums.length <= 5 * 105`\n- `nums.length % 3 == 0`\n- `1 <= nums[i] <= 109`"
                         )

    def solve(self, piles: List[int]) -> int:
        piles.sort()
        return sum(piles[len(piles) // 3::2])

    def _gen(self):
        l = _generate_int(int_min=1, int_max=3333)
        nums = _generate_list_int((l, l), (1, 10000))
        return nums,


class Solution2(Testing):
    date = "2025-7-27"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3628,
                         types=[ProblemType.Greedy, ProblemType.String, ProblemType.DynamicPlanning, ProblemType.PrefixSum],
                         pass_rate=0.339,
                         description="给你一个由大写英文字母组成的字符串 `s`。\n\n你可以在字符串的 **任意** 位置（包括字符串的开头或结尾）**最多插入一个** 大写英文字母。\n\n返回在 **最多插入一个字母** 后，字符串中可以形成的 `\"LCT\"` 子序列的 **最大** 数量。\n\n**子序列** 是从另一个字符串中删除某些字符（可以不删除）且不改变剩余字符顺序后得到的一个 **非空** 字符串。\n\n \n\n**示例 1：**\n\n**输入：** s = \"LMCT\"\n\n**输出：** 2\n\n**解释：**\n\n可以在字符串 `s` 的开头插入一个 `\"L\"`，变为 `\"LLMCT\"`，其中包含 2 个子序列，分别位于下标 [0, 3, 4] 和 [1, 3, 4]。\n\n**示例 2：**\n\n**输入：** s = \"LCCT\"\n\n**输出：** 4\n\n**解释：**\n\n可以在字符串 `s` 的开头插入一个 `\"L\"`，变为 `\"LLCCT\"`，其中包含 4 个子序列，分别位于下标 [0, 2, 4]、[0, 3, 4]、[1, 2, 4] 和 [1, 3, 4]。\n\n**示例 3：**\n\n**输入：** s = \"L\"\n\n**输出：** 0\n\n**解释：**\n\n插入一个字母无法获得子序列 `\"LCT\"`，结果为 0。\n\n \n\n**提示：**\n\n- `1 <= s.length <= 105`\n- `s` 仅由大写英文字母组成。"
                         )

    # 115. 不同的子序列
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        if n < m:
            return 0

        f = [1] + [0] * m
        for i, x in enumerate(s):
            for j in range(min(i, m - 1), max(m - n + i, 0) - 1, -1):
                if x == t[j]:
                    f[j + 1] += f[j]
        return f[m]

    # 计算插入 C 额外产生的 LCT 子序列个数的最大值
    def calcInsertC(self, s: str) -> int:
        cnt_t = s.count('T')  # s[i+1] 到 s[n-1] 的 'T' 的个数
        cnt_l = 0  # s[0] 到 s[i] 的 'L' 的个数
        res = 0
        for c in s:
            if c == 'T':
                cnt_t -= 1
            if c == 'L':
                cnt_l += 1
            res = max(res, cnt_l * cnt_t)
        return res

    def solve(self, s: str) -> int:
        extra = max(self.numDistinct(s, "CT"), self.numDistinct(s, "LC"), self.calcInsertC(s))
        return self.numDistinct(s, "LCT") + extra

    def gen(self):
        return self.generate_string(vocab=string.ascii_uppercase, length_range=(1, 10000)),


from collections import defaultdict


class Solution3(Testing):
    date = "2025-7-27"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3629,
                         types=[ProblemType.BreadthFirstSearch, ProblemType.Array, ProblemType.HashTable, ProblemType.Math,
                                ProblemType.NumberTheory],
                         pass_rate=0.242,
                         description="给你一个长度为 `n` 的整数数组 `nums`。\n\n你从下标 0 开始，目标是到达下标 `n - 1`。\n\n在任何下标 `i` 处，你可以执行以下操作之一：\n\n- **移动到相邻格子**：跳到下标 `i + 1` 或 `i - 1`，如果该下标在边界内。\n- **质数传送**：如果 `nums[i]` 是一个**质数** `p`，你可以立即跳到任何满足 `nums[j] % p == 0` 的下标 `j` 处，且下标 `j != i` 。\n\n返回到达下标 `n - 1` 所需的 **最少** 跳跃次数。\n\n**质数** 是一个大于 1 的自然数，只有两个因子，1 和它本身。\n\n \n\n**示例 1:**\n\n**输入:** nums = [1,2,4,6]\n\n**输出:** 2\n\n**解释:**\n\n一个最优的跳跃序列是：\n\n- 从下标 `i = 0` 开始。向相邻下标 1 跳一步。\n- 在下标 `i = 1`，`nums[1] = 2` 是一个质数。因此，我们传送到索引 `i = 3`，因为 `nums[3] = 6` 可以被 2 整除。\n\n因此，答案是 2。\n\n**示例 2:**\n\n**输入:** nums = [2,3,4,7,9]\n\n**输出:** 2\n\n**解释:**\n\n一个最优的跳跃序列是：\n\n- 从下标 `i = 0` 开始。向相邻下标 `i = 1` 跳一步。\n- 在下标 `i = 1`，`nums[1] = 3` 是一个质数。因此，我们传送到下标 `i = 4`，因为 `nums[4] = 9` 可以被 3 整除。\n\n因此，答案是 2。\n\n**示例 3:**\n\n**输入:** nums = [4,6,5,8]\n\n**输出:** 3\n\n**解释:**\n\n- 由于无法进行传送，我们通过 `0 → 1 → 2 → 3` 移动。因此，答案是 3。\n\n \n\n**提示:**\n\n- `1 <= n == nums.length <= 105`\n- `1 <= nums[i] <= 106`"
                         )

    def solve(self, nums: List[int]) -> int:
        MX = 1_000_001
        prime_factors: list[list[int]] = [[] for _ in range(MX)]
        for i in range(2, MX):
            if not prime_factors[i]:  # i 是质数
                for j in range(i, MX, i):  # i 的倍数有质因子 i
                    prime_factors[j].append(i)

        n = len(nums)
        groups: dict[int, list[int]] = defaultdict(list)
        for i, x in enumerate(nums):
            if len(prime_factors[x]) == 1:  # x 是质数
                groups[x].append(i)

        ans = 0
        vis = [False] * n
        vis[-1] = True
        q = [n - 1]

        while True:
            tmp = q
            q = []
            for i in tmp:
                if i == 0:
                    return ans
                if not vis[i - 1]:
                    vis[i - 1] = True
                    q.append(i - 1)
                if i < n - 1 and not vis[i + 1]:
                    vis[i + 1] = True
                    q.append(i + 1)
                # 逆向思维：从 i 倒着跳到 nums[i] 的质因子 p 的下标 j
                for p in prime_factors[nums[i]]:
                    idx = groups[p]
                    for j in idx:
                        if not vis[j]:
                            vis[j] = True
                            q.append(j)
                    idx.clear()  # 避免重复访问下标列表
            ans += 1


    def gen(self):
        return self.generate_list_int(list_length_range=(1, 10000), int_range=(1, 100000)),

class XorBasis:
    def __init__(self, n: int):
        self.b = [0] * n

    def insert(self, x: int) -> None:
        b = self.b
        while x:
            i = x.bit_length() - 1  # x 的最高位
            if b[i] == 0:  # x 和之前的基是线性无关的
                b[i] = x  # 新增一个基，最高位为 i
                return
            x ^= b[i]  # 保证参与 max_xor 的基的最高位是互不相同的，方便我们贪心
        # 正常循环结束，此时 x=0，说明一开始的 x 可以被已有基表出，不是一个线性无关基

    def max_xor(self) -> int:
        b = self.b
        res = 0
        # 从高到低贪心：越高的位，越必须是 1
        # 由于每个位的基至多一个，所以每个位只需考虑异或一个基，若能变大，则异或之
        for i in range(len(b) - 1, -1, -1):
            if res ^ b[i] > res:
                res ^= b[i]
        return res

class Solution4(Testing):
    date = "2025-7-27"
    def __init__(self):
        Testing.__init__(self,
                         degree=2,
                         idx=3630,
                         types=[ProblemType.Greedy, ProblemType.Array, ProblemType.Math, ProblemType.Enum],
                         pass_rate=0.366,
                         description="给你一个整数数组 `nums`。\n\n将数组划分为 **三** 个（可以为空）子序列 `A`、`B` 和 `C`，使得 `nums` 中的每个元素 **恰好** 属于一个子序列。\n\n你的目标是 **最大化** 以下值：`XOR(A) + AND(B) + XOR(C)`\n\n其中：\n\n- `XOR(arr)` 表示 `arr` 中所有元素的按位异或结果。如果 `arr` 为空，结果定义为 0。\n- `AND(arr)` 表示 `arr` 中所有元素的按位与结果。如果 `arr` 为空，结果定义为 0。\n\n返回可实现的最 **大** 值。\n\n**注意:** 如果有多种划分方式得到相同的 **最大** 和，你可以按其中任何一种划分。\n\n**子序列** 是指一个数组通过删除一些或不删除任何元素，不改变剩余元素的顺序得到的元素序列。\n\n \n\n**示例 1:**\n\n**输入:** nums = [2,3]\n\n**输出:** 5\n\n**解释:**\n\n一个最优划分是：\n\n- `A = [3], XOR(A) = 3`\n- `B = [2], AND(B) = 2`\n- `C = [], XOR(C) = 0`\n\n最大值为: `XOR(A) + AND(B) + XOR(C) = 3 + 2 + 0 = 5`。因此，答案是 5。\n\n**示例 2:**\n\n**输入:** nums = [1,3,2]\n\n**输出:** 6\n\n**解释:**\n\n一个最优划分是：\n\n- `A = [1], XOR(A) = 1`\n- `B = [2], AND(B) = 2`\n- `C = [3], XOR(C) = 3`\n\n最大值为: `XOR(A) + AND(B) + XOR(C) = 1 + 2 + 3 = 6`。因此，答案是 6。\n\n**示例 3:**\n\n**输入:** nums = [2,3,6,7]\n\n**输出:** 15\n\n**解释:**\n\n一个最优划分是：\n\n- `A = [7], XOR(A) = 7`\n- `B = [2,3], AND(B) = 2`\n- `C = [6], XOR(C) = 6`\n\n最大值为: `XOR(A) + AND(B) + XOR(C) = 7 + 2 + 6 = 15`。因此，答案是 15。\n\n \n\n**提示:**\n\n- `1 <= nums.length <= 19`\n- `1 <= nums[i] <= 109`"
                         )

    def solve(self, nums: List[int]) -> int:
        n = len(nums)
        sz: int = max(nums).bit_length()

        # 多算一个子集 OR，用于剪枝
        u = 1 << n
        sub_and = [0] * u
        sub_xor = [0] * u
        sub_or = [0] * u
        sub_and[0] = -1
        for i, x in enumerate(nums):
            high_bit = 1 << i
            for mask in range(high_bit):
                sub_and[high_bit | mask] = sub_and[mask] & x
                sub_xor[high_bit | mask] = sub_xor[mask] ^ x
                sub_or[high_bit | mask] = sub_or[mask] | x
        sub_and[0] = 0

        def max_xor2(sub: int) -> int:
            b = XorBasis(sz)
            xor = sub_xor[sub]
            for i, x in enumerate(nums):
                if sub >> i & 1:
                    b.insert(x & ~xor)
            return xor + b.max_xor() * 2

        ans = 0
        for i in range(u):
            j = (u - 1) ^ i
            if sub_and[i] + sub_or[j] * 2 - sub_xor[j] > ans:  # 有机会让 ans 变得更大
                ans = max(ans, sub_and[i] + max_xor2(j))
        return ans

    def _gen(self):
        return _generate_list_int(((1, 19)), (1, 1000_000_000)),