import random
from . import Problem as Testing, ProblemType
from typing import List


class Solution1(Testing):
    date = "2025-8-31"
    def __init__(self):
        Testing.__init__(self,
                         degree=0,
                         idx=3668,
                         types=[ProblemType.Array, ProblemType.HashTable],
                         pass_rate=0.877,
                         description="给你一个长度为 `n` 的整数数组 `order` 和一个整数数组 `friends`。\n\n- `order` 包含从 1 到 `n` 的每个整数，且 **恰好出现一次** ，表示比赛中参赛者按照 **完成顺序** 的 ID。\n- `friends` 包含你朋友们的 ID，按照 **严格递增** 的顺序排列。`friends` 中的每个 ID 都保证出现在 `order` 数组中。\n\n请返回一个数组，包含你朋友们的 ID，按照他们的 **完成顺序** 排列。\n\n \n\n**示例 1：**\n\n**输入：**order = [3,1,2,5,4], friends = [1,3,4]\n\n**输出：**[3,1,4]\n\n**解释：**\n\n完成顺序是 `[**3**, **1**, 2, 5, **4**]`。因此，你朋友的完成顺序是 `[3, 1, 4]`。\n\n**示例 2：**\n\n**输入：**order = [1,4,5,3,2], friends = [2,5]\n\n**输出：**[5,2]\n\n**解释：**\n\n完成顺序是 `[1, 4, **5**, 3, **2**]`。因此，你朋友的完成顺序是 `[5, 2]`。\n\n \n\n**提示：**\n\n- `1 <= n == order.length <= 100`\n- `order` 包含从 1 到 `n` 的每个整数，且恰好出现一次\n- `1 <= friends.length <= min(8, n)`\n- `1 <= friends[i] <= n`\n- `friends` 是严格递增的"
                         )

    def solve(self, order: List[int], friends: List[int]) -> List[int]:
        st = set(friends)
        return [x for x in order if x in st]

    def _gen(self):
        n = self.s_generate_int((1, 100))
        order = list(range(1, n + 1))
        random.shuffle(order)
        friends = self.s_generate_list_int(list_length_range=(1, min(8, n)), int_range=(min(order), max(order)))
        friends.sort()
        return order, friends



MX = 100001
divisors = [[] for _ in range(MX)]
for i in range(1, MX):
    for j in range(i, MX, i):  # 枚举 i 的倍数 j
        divisors[j].append(i)  # i 是 j 的因子

class Solution2(Testing):
    date = "2025-8-31"
    def __init__(self):
        Testing.__init__(self,
                         testcase_num=5,
                         degree=1,
                         idx=3669,
                         types=[ProblemType.Math, ProblemType.BackDating, ProblemType.NumberTheory],
                         pass_rate=0.381,
                         description="给你两个整数 `n` 和 `k`，将数字 `n` 恰好分割成 `k` 个正整数，使得这些整数的 **乘积** 等于 `n`。\n\n返回一个分割方案，使得这些数字中 **最大值** 和 **最小值** 之间的 **差值** 最小化。返回分割方案的和。\n\n \n\n**示例 1：**\n\n**输入：**n = 100, k = 2\n\n**输出：**20\n\n**解释：**\n\n分割方案 `[10, 10]` 的结果是 `10 * 10 = 100`，且最大值与最小值的差值为 0，这是最小可能值。\n\n**示例 2：**\n\n**输入：**n = 44, k = 3\n\n**输出：**15\n\n**解释：**\n\n- 分割方案 `[1, 1, 44]` 的差值为 43\n- 分割方案 `[1, 2, 22]` 的差值为 21\n- 分割方案 `[1, 4, 11]` 的差值为 10\n- 分割方案 `[2, 2, 11]` 的差值为 9\n\n因此，`[2, 2, 11]` 是最优分割方案，其差值最小，为 9。\n\n \n\n**提示：**\n\n- `4 <= n <= 10**5`\n- `2 <= k <= 5`\n- `k` 严格小于 `n` 的正因数的总数。"                         )

    def solve(self, n: int, k: int) -> int:
        min_diff = inf
        path = [0] * k
        ans = None

        def dfs(i: int, n: int) -> None:
            if i == k - 1:
                nonlocal min_diff, ans
                # path[0] 最小，n 最大
                if n - path[0] < min_diff:
                    min_diff = n - path[0]
                    path[i] = n
                    ans = path.copy()  # path[:]
                return
            for d in divisors[n]:  # 枚举 n 的因子 d
                if d * d > n or i > 0 and d - path[0] >= min_diff:
                    break
                if i == 0 or d >= path[i - 1]:
                    path[i] = d  # 直接覆盖，无需恢复现场
                    dfs(i + 1, n // d)

        dfs(0, n)
        return sum(ans)

    def gen(self):
        return self.generate_int(int_range=(4, 100)), self.generate_int(int_range=(2, 5))

from math import inf
class Solution3(Testing):
    date = "2025-8-31"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3670,
                         types=[ProblemType.Bit, ProblemType.Array, ProblemType.DynamicPlanning],
                         pass_rate=0.235,
                         description="给你一个整数数组 `nums`。\n\n请你找到两个 **不同** 的下标 `i` 和 `j`，使得 `nums[i] * nums[j]` 的 **乘积最大化** ，并且 `nums[i]` 和 `nums[j]` 的二进制表示中没有任何公共的置位 (set bit)。\n\n返回这样一对数的 **最大** 可能乘积。如果不存在这样的数对，则返回 0。\n\n \n\n**示例 1：**\n\n**输入：**nums = [1,2,3,4,5,6,7]\n\n**输出：**12\n\n**解释：**\n\n最佳数对为 3 (011) 和 4 (100)。它们没有公共的置位，并且 `3 * 4 = 12`。\n\n**示例 2：**\n\n**输入：**nums = [5,6,4]\n\n**输出:** 0\n\n**解释：**\n\n每一对数字都有至少一个公共置位。因此，答案是 0。\n\n**示例 3：**\n\n**输入：**nums = [64,8,32]\n\n**输出：**2048\n\n**解释：**\n\n没有任意一对数字共享公共置位，因此答案是两个最大元素的乘积：64 和 32 (`64 * 32 = 2048`)。\n\n \n\n**提示：**\n\n- `2 <= nums.length <= 10**5`\n- `1 <= nums[i] <= 10**6`"
                         )

    def solve(self, nums: List[int]) -> int:
        w = max(nums).bit_length()
        u = 1 << w
        f = [0] * u
        for x in nums:
            f[x] = x

        for s in range(u):
            t = s
            while t:
                lb = t & -t
                v = f[s ^ lb]
                if v > f[s]:
                    f[s] = v
                t ^= lb

        return max(x * f[(u - 1) ^ x] for x in nums)


    def gen(self):
        return self.generate_list_int(list_length_range=(2, 100), int_range=(1, 1000)),


MOD = 1_000_000_007

# 预处理每个数的因子
MX = 70_001
divisors = [[] for _ in range(MX)]
for i in range(1, MX):
    for j in range(i, MX, i):  # 枚举 i 的倍数 j
        divisors[j].append(i)  # i 是 j 的因子


# 完整模板见 https://leetcode.cn/circle/discuss/mOr1u6/
class FenwickTree:
    def __init__(self, n: int):
        self.tree = [0] * (n + 1)  # 使用下标 1 到 n

    # a[i] 增加 val
    # 1 <= i <= n
    # 时间复杂度 O(log n)
    def update(self, i: int, val: int) -> None:
        t = self.tree
        while i < len(t):
            t[i] += val
            i += i & -i

    # 计算前缀和 a[1] + ... + a[i]
    # 1 <= i <= n
    # 时间复杂度 O(log n)
    def pre(self, i: int) -> int:
        t = self.tree
        res = 0
        while i > 0:
            res += t[i]
            i &= i - 1
        return res % MOD


class Solution4(Testing):
    date = "2025-8-31"
    def __init__(self):
        Testing.__init__(self,
                         testcase_num=5,
                         degree=2,
                         idx=3671,
                         types=[ProblemType.Tree, ProblemType.Array, ProblemType.Math, ProblemType.NumberTheory],
                         pass_rate=0.351,
                         description="给你一个长度为 `n` 的整数数组 `nums`。\n\n对于每个 **正整数** `g`，定义 `g` 的 **美丽值** 为 `g` 与 `nums` 中符合要求的子序列数量的乘积，子序列需要 **严格递增** 且最大公约数（GCD）恰好为 `g` 。\n\n请返回所有正整数 `g` 的 **美丽值** 之和。\n\n由于答案可能非常大，请返回结果对 `109 + 7` 取模后的值。\n\n**子序列** 是一个 **非空** 数组，可以通过从另一个数组中删除某些元素（或不删除任何元素）而保持剩余元素顺序不变得到。\n\n \n\n**示例 1：**\n\n**输入：**nums = [1,2,3]\n\n**输出：**10\n\n**解释：**\n\n所有严格递增子序列及其 GCD 如下：\n\n| 子序列  | GCD  |\n| ------- | ---- |\n| [1]     | 1    |\n| [2]     | 2    |\n| [3]     | 3    |\n| [1,2]   | 1    |\n| [1,3]   | 1    |\n| [2,3]   | 1    |\n| [1,2,3] | 1    |\n\n计算每个 GCD 的美丽值：\n\n| GCD  | 子序列数量 | 美丽值 (GCD × 数量) |\n| ---- | ---------- | ------------------- |\n| 1    | 5          | 1 × 5 = 5           |\n| 2    | 1          | 2 × 1 = 2           |\n| 3    | 1          | 3 × 1 = 3           |\n\n美丽值总和为 `5 + 2 + 3 = 10`。\n\n**示例 2：**\n\n**输入：**nums = [4,6]\n\n**输出：**12\n\n**解释：**\n\n所有严格递增子序列及其 GCD 如下：\n\n| 子序列 | GCD  |\n| ------ | ---- |\n| [4]    | 4    |\n| [6]    | 6    |\n| [4,6]  | 2    |\n\n计算每个 GCD 的美丽值：\n\n| GCD  | 子序列数量 | 美丽值 (GCD × 数量) |\n| ---- | ---------- | ------------------- |\n| 2    | 1          | 2 × 1 = 2           |\n| 4    | 1          | 4 × 1 = 4           |\n| 6    | 1          | 6 × 1 = 6           |\n\n美丽值总和为 `2 + 4 + 6 = 12`。\n\n \n\n**提示：**\n\n- `1 <= n == nums.length <= 10**4`\n- `1 <= nums[i] <= 7 × 10**4`"
                         )

    def solve(self, nums: List[int]) -> int:
        m = max(nums)

        # 计算 b 的严格递增子序列的个数
        def count_increasing_subsequence(b: List[int], g: int) -> int:
            t = FenwickTree(m // g)
            res = 0
            for x in b:
                x //= g
                # cnt 表示以 x 结尾的严格递增子序列的个数
                cnt = t.pre(x - 1) + 1  # +1 是因为 x 可以一个数组成一个子序列
                res += cnt
                t.update(x, cnt)  # 更新以 x 结尾的严格递增子序列的个数
            return res

        groups = [[] for _ in range(m + 1)]
        for x in nums:
            for d in divisors[x]:
                groups[d].append(x)

        f = [0] * (m + 1)
        ans = 0
        for i in range(m, 0, -1):
            f[i] = count_increasing_subsequence(groups[i], i)
            # 倍数容斥
            for j in range(i * 2, m + 1, i):
                f[i] -= f[j]
            ans += f[i] * i
        return ans % MOD

    def gen(self):
        return self.generate_list_int(list_length_range=(10, 20), int_range=(1, 100)),

