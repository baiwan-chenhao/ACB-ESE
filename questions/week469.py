from . import Problem as Testing
from typing import List


class Solution1(Testing):
    date = "2025-9-27"
    def __init__(self):
        Testing.__init__(self,
                         degree=0,
                         idx=3697,
                         types=[],
                         pass_rate=0.666,
                         description="给你一个 **正整数** `n`。\n\n如果一个正整数可以表示为 1 到 9 的单个数字和 10 的非负整数次幂的乘积，则称这个整数是一个 **10 进制分量**。例如，500、30 和 7 是 **10 进制分量** ，而 537、102 和 11 则不是。\n\n请将 `n` 表示为若干 **仅由** 10 进制分量组成的和，且使用的 10 进制分量个数 **最少** 。\n\n返回一个包含这些 **10 进制分量** 的数组，并按分量大小 **降序** 排列。\n\n \n\n**示例 1：**\n\n**输入：**n = 537\n\n**输出：**[500,30,7]\n\n**解释：**\n\n我们可以将 537 表示为`500 + 30 + 7`。无法用少于 3 个 10 进制分量表示 537。\n\n**示例 2：**\n\n**输入：**n = 102\n\n**输出：**[100,2]\n\n**解释：**\n\n我们可以将 102 表示为`100 + 2`。102 不是一个 10 进制分量，因此需要 2 个 10 进制分量。\n\n**示例 3：**\n\n**输入：**n = 6\n\n**输出：**[6]\n\n**解释：**\n\n6 是一个 10 进制分量。\n\n \n\n**提示：**\n\n- `1 <= n <= 10**9`"
                         )

    def solve(self, n: int) -> List[int]:
        ans = []
        pow10 = 1
        while n:
            n, d = divmod(n, 10)
            if d:
                ans.append(d * pow10)
            pow10 *= 10
        ans.reverse()
        return ans

    def gen(self):
        return self.generate_int(int_range=(1, 10000)),



class Solution2(Testing):
    date = "2025-9-27"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3698,
                         types=[],
                         pass_rate=0.270,
                         description="给你一个整数数组 `nums`。\n\n将数组 **恰好** 分成两个子数组 `left` 和 `right` ，使得 `left` **严格递增** ，`right` **严格递减** 。\n\n返回 `left` 与 `right` 的元素和之间 **绝对差值的最小可能值** 。如果不存在有效的分割方案，则返回 `-1` 。\n\n**子数组** 是数组中连续的非空元素序列。\n\n当数组中每个元素都严格大于其前一个元素（如果存在）时，称该数组为严格递增。\n\n当数组中每个元素都严格小于其前一个元素（如果存在）时，称该数组为严格递减。\n\n \n\n**示例 1：**\n\n**输入：** nums = [1,3,2]\n\n**输出：** 2\n\n**解释：**\n\n| `i`  | `left` | `right` | 是否有效 | `left` 和 | `right` 和 | 绝对差值      |\n| ---- | ------ | ------- | -------- | --------- | ---------- | ------------- |\n| 0    | [1]    | [3, 2]  | 是       | 1         | 5          | `|1 - 5| = 4` |\n| 1    | [1, 3] | [2]     | 是       | 4         | 2          | `|4 - 2| = 2` |\n\n因此，最小绝对差值为 2。\n\n**示例 2：**\n\n**输入：** nums = [1,2,4,3]\n\n**输出：** 4\n\n**解释：**\n\n| `i`  | `left`    | `right`   | 是否有效 | `left` 和 | `right` 和 | 绝对差值      |\n| ---- | --------- | --------- | -------- | --------- | ---------- | ------------- |\n| 0    | [1]       | [2, 4, 3] | 否       | 1         | 9          | -             |\n| 1    | [1, 2]    | [4, 3]    | 是       | 3         | 7          | `|3 - 7| = 4` |\n| 2    | [1, 2, 4] | [3]       | 是       | 7         | 3          | `|7 - 3| = 4` |\n\n因此，最小绝对差值为 4。\n\n**示例 3：**\n\n**输入：** nums = [3,1,2]\n\n**输出：** -1\n\n**解释：**\n\n不存在有效的分割方案，因此答案为 -1。\n\n \n\n**提示：**\n\n- `2 <= nums.length <= 10**5`\n- `1 <= nums[i] <= 10**5`"
                         )

    def solve(self, nums: List[int]) -> int:
        n = len(nums)
        # 最长严格递增前缀
        pre = nums[0]
        i = 1
        while i < n and nums[i] > nums[i - 1]:
            pre += nums[i]
            i += 1

        # 最长严格递减后缀
        suf = nums[-1]
        j = n - 2
        while j >= 0 and nums[j] > nums[j + 1]:
            suf += nums[j]
            j -= 1

        # 情况一
        if i <= j:
            return -1

        d = pre - suf
        # 情况二
        if i - 1 == j:
            return abs(d)

        # 情况三，suf 多算了一个 nums[i-1]，或者 pre 多算了一个 nums[i-1]
        return min(abs(d + nums[i - 1]), abs(d - nums[i - 1]))

    def gen(self):
        return self.generate_list_int(list_length_range=(2, 1000), int_range=(1, 1000)),



class Solution3(Testing):
    date = "2025-9-27"
    def __init__(self):
        Testing.__init__(self,
                         degree=2,
                         idx=3699,
                         types=[],
                         pass_rate=0.363,
                         description="给你 三个整数 `n`、`l` 和 `r`。\n\n长度为 `n` 的锯齿形数组定义如下：\n\n- 每个元素的取值范围为 `[l, r]`。\n- 任意 **两个** 相邻的元素都不相等。\n- 任意 **三个** 连续的元素不能构成一个 **严格递增** 或 **严格递减** 的序列。\n\n返回满足条件的锯齿形数组的总数。\n\n由于答案可能很大，请将结果对 `10**9 + 7` 取余数。\n\n**序列** 被称为 **严格递增** 需要满足：当且仅当每个元素都严格大于它的前一个元素（如果存在）。\n\n**序列** 被称为 **严格递减** 需要满足，当且仅当每个元素都严格小于它的前一个元素（如果存在）。\n\n \n\n**示例 1：**\n\n**输入：**n = 3, l = 4, r = 5\n\n**输出：**2\n\n**解释：**\n\n在取值范围 `[4, 5]` 内，长度为 `n = 3` 的锯齿形数组只有 2 种：\n\n- `[4, 5, 4]`\n- `[5, 4, 5]`\n\n**示例 2：**\n\n**输入：**n = 3, l = 1, r = 3\n\n**输出：**10\n\n**解释：**\n\n在取值范围 `[1, 3]` 内，长度为 `n = 3` 的锯齿形数组共有 10 种：\n\n- `[1, 2, 1]`, `[1, 3, 1]`, `[1, 3, 2]`\n- `[2, 1, 2]`, `[2, 1, 3]`, `[2, 3, 1]`, `[2, 3, 2]`\n- `[3, 1, 2]`, `[3, 1, 3]`, `[3, 2, 3]`\n\n所有数组均符合锯齿形条件。\n\n \n\n**提示：**\n\n- `3 <= n <= 2000`\n- `1 <= l < r <= 2000`"
                         )

    def solve(self, n: int, l: int, r: int) -> int:
        MOD = 1_000_000_007
        k = r - l + 1
        f = [1] * k

        for i in range(1, n):
            if i % 2:  # 增
                pre = 0
                for j, v in enumerate(f):
                    f[j] = pre % MOD
                    pre += v
            else:  # 减
                suf = 0
                for j in range(k - 1, -1, -1):
                    v = f[j]
                    f[j] = suf % MOD
                    suf += v

        return sum(f) * 2 % MOD


    def _gen(self):
        n = self.s_generate_int((3, 100))
        r = self.s_generate_int((1, 100))
        l = self.s_generate_int((1, r))
        return n, l, r

MOD = 1_000_000_007

# a @ b，其中 @ 是矩阵乘法
# 更快的写法见另一份代码【NumPy】
def mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    return [[sum(x * y for x, y in zip(row, col)) % MOD for col in zip(*b)]
            for row in a]

# a^n @ f1
def pow_mul(a: List[List[int]], n: int, f1: List[List[int]]) -> List[List[int]]:
    res = f1
    while n:
        if n & 1:
            res = mul(a, res)
        a = mul(a, a)
        n >>= 1
    return res

Solution4 = Solution3