import random
from . import Problem as Testing, ProblemType
from typing import List


class Solution1(Testing):
    date = "2025-8-10"
    def __init__(self):
        Testing.__init__(self,
                         degree=0,
                         idx=3643,
                         types=[ProblemType.Array, ProblemType.BiPoint, ProblemType.Matrix],
                         pass_rate=0.667,
                         description="给你一个 `m x n` 的整数矩阵 `grid`，以及三个整数 `x`、`y` 和 `k`。\n\n整数 `x` 和 `y` 表示一个 **正方形子矩阵** 的左上角下标，整数 `k` 表示该正方形子矩阵的边长。\n\n你的任务是垂直翻转子矩阵的行顺序。\n\n返回更新后的矩阵。\n\n \n\n**示例 1：**\n\n**输入：** grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], x = 1, y = 0, k = 3\n\n**输出：** [[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]\n\n**解释：**\n\n上图展示了矩阵在变换前后的样子。\n\n**示例 2：**\n\n**输入：** grid = [[3,4,2,3],[2,3,4,2]], x = 0, y = 2, k = 2\n\n**输出：** [[3,4,4,2],[2,3,2,3]]\n\n**解释：**\n\n上图展示了矩阵在变换前后的样子。\n\n \n\n**提示：**\n\n- `m == grid.length`\n- `n == grid[i].length`\n- `1 <= m, n <= 50`\n- `1 <= grid[i][j] <= 100`\n- `0 <= x < m`\n- `0 <= y < n`\n- `1 <= k <= min(m - x, n - y)`"
                         )

    def solve(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        l, r = x, x + k - 1
        while l < r:
            for j in range(y, y + k):
                grid[l][j], grid[r][j] = grid[r][j], grid[l][j]
            l += 1
            r -= 1
        return grid

    def _gen(self):
        matrix = self.s_generate_matrix(list_length_range1=(1, 50), list_length_range2=(1, 50), int_range=(1, 100))
        m = len(matrix)
        n = len(matrix[0])
        x = self.s_generate_int((0, m - 1))
        y = self.s_generate_int((0, n - 1))
        k = self.s_generate_int((1, min(m - x, n - y)))
        return matrix, x, y, k


class Solution2(Testing):
    date = "2025-8-10"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3644,
                         types=[ProblemType.Array],
                         pass_rate=0.372,
                         description="给你一个长度为 `n` 的整数数组 `nums`，其中 `nums` 是范围 `[0..n - 1]` 内所有数字的一个 **排列** 。\n\n你可以在满足条件 `nums[i] AND nums[j] == k` 的情况下交换下标 `i` 和 `j` 的元素，其中 `AND` 表示按位与操作，`k` 是一个**非负整数**。\n\n返回可以使数组按 **非递减** 顺序排序的最大值 `k`（允许进行任意次这样的交换）。如果 `nums` 已经是有序的，返回 0。\n\n**排列** 是数组所有元素的一种重新排列。\n\n \n\n**示例 1：**\n\n**输入：**nums = [0,3,2,1]\n\n**输出：**1\n\n**解释：**\n\n选择 `k = 1`。交换 `nums[1] = 3` 和 `nums[3] = 1`，因为 `nums[1] AND nums[3] == 1`，从而得到一个排序后的排列：`[0, 1, 2, 3]`。\n\n**示例 2：**\n\n**输入：**nums = [0,1,3,2]\n\n**输出：**2\n\n**解释：**\n\n选择 `k = 2`。交换 `nums[2] = 3` 和 `nums[3] = 2`，因为 `nums[2] AND nums[3] == 2`，从而得到一个排序后的排列：`[0, 1, 2, 3]`。\n\n**示例 3：**\n\n**输入：**nums = [3,2,1,0]\n\n**输出：**0\n\n**解释：**\n\n只有当 `k = 0` 时，才能进行排序，因为没有更大的 `k` 能够满足 `nums[i] AND nums[j] == k` 的交换条件。\n\n \n\n**提示：**\n\n- `1 <= n == nums.length <= 10**5`\n- `0 <= nums[i] <= n - 1`\n- `nums` 是从 `0` 到 `n - 1` 的一个排列。"
                         )

    def solve(self, nums: List[int]) -> int:
        if nums[0]:  # 小优化：此时 0 参与 AND，结果一定是 0
            return 0
        ans = -1  # 二进制全为 1
        for i, x in enumerate(nums):
            if i != x:
                ans &= x
        return max(ans, 0)

    def _gen(self):
        n = self.s_generate_int((1, 10000))

        nums = list(range(n))
        random.shuffle(nums)
        return nums,

from collections import defaultdict

class Solution3(Testing):
    date = "2025-8-10"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3645,
                         types=[ProblemType.Greedy, ProblemType.Array, ProblemType.BiPoint, ProblemType.Sorting, ProblemType.Heap],
                         pass_rate=0.514,
                         description="给你两个长度为 `n` 的整数数组 `value` 和 `limit`。\n\n初始时，所有元素都是 **非活跃** 的。你可以按任意顺序激活它们。\n\n- 要激活一个非活跃元素 `i`，**当前** 活跃元素的数量必须 **严格小于** `limit[i]`。\n- 当你激活元素 `i` 时，它的 `value[i]` 会被加到 **总和** 中（即所有进行过激活操作的元素 `value[i]` 之和）。\n- 每次激活后，如果 **当前** 活跃元素的数量变为 `x`，那么 **所有** 满足 `limit[j] <= x` 的元素 `j` 都会永久变为非活跃状态，即使它们已经处于活跃状态。\n\n返回通过最优选择激活顺序可以获得的 **最大总和** 。\n\n \n\n**示例 1:**\n\n**输入:** value = [3,5,8], limit = [2,1,3]\n\n**输出:** 16\n\n**解释:**\n\n一个最优的激活顺序是:\n\n| 步骤 | 激活的 `i` | `value[i]` | 激活 `i` 前的活跃数 | 激活 `i` 后的活跃数 |      变为非活跃的 `j`       | 非活跃元素 | 总和 |\n| :--: | :--------: | :--------: | :-----------------: | :-----------------: | :-------------------------: | :--------: | :--: |\n|  1   |     1      |     5      |          0          |          1          | `j = 1` 因为 `limit[1] = 1` |    [1]     |  5   |\n|  2   |     0      |     3      |          0          |          1          |              -              |    [1]     |  8   |\n|  3   |     2      |     8      |          1          |          2          | `j = 0` 因为 `limit[0] = 2` |   [0, 1]   |  16  |\n\n因此，可能的最大总和是 16。\n\n**示例 2:**\n\n**输入:** value = [4,2,6], limit = [1,1,1]\n\n**输出:** 6\n\n**解释:**\n\n一个最优的激活顺序是:\n\n| 步骤 | 激活的 `i` | `value[i]` | 激活 `i` 前的活跃数 | 激活 `i` 后的活跃数 |         变为非活跃的 `j`          | 非活跃元素 | 总和 |\n| :--: | :--------: | :--------: | :-----------------: | :-----------------: | :-------------------------------: | :--------: | :--: |\n|  1   |     2      |     6      |          0          |          1          | `j = 0, 1, 2` 因为 `limit[j] = 1` | [0, 1, 2]  |  6   |\n\n因此，可能的最大总和是 6。\n\n**示例 3:**\n\n**输入:** value = [4,1,5,2], limit = [3,3,2,3]\n\n**输出:** 12\n\n**解释:**\n\n一个最优的激活顺序是:\n\n| 步骤 | 激活的 `i` | `value[i]` | 激活 `i` 前的活跃数 | 激活 `i` 后的活跃数 |         变为非活跃的 `j`          |  非活跃元素  | 总和 |\n| :--: | :--------: | :--------: | :-----------------: | :-----------------: | :-------------------------------: | :----------: | :--: |\n|  1   |     2      |     5      |          0          |          1          |                 -                 |     [ ]      |  5   |\n|  2   |     0      |     4      |          1          |          2          |    `j = 2` 因为 `limit[2] = 2`    |     [2]      |  9   |\n|  3   |     1      |     1      |          1          |          2          |                 -                 |     [2]      |  10  |\n|  4   |     3      |     2      |          2          |          3          | `j = 0, 1, 3` 因为 `limit[j] = 3` | [0, 1, 2, 3] |  12  |\n\n因此，可能的最大总和是 12。\n\n \n\n**提示:**\n\n- `1 <= n == value.length == limit.length <= 105`\n- `1 <= value[i] <= 105`\n- `1 <= limit[i] <= n`"
                         )

    def solve(self, value: List[int], limit: List[int]) -> int:
        groups: dict[int, list[int]] = defaultdict(list)
        for lim, v in zip(limit, value):
            groups[lim].append(v)

        ans = 0
        for lim, a in groups.items():
            # 取最大的 lim 个数。更快写法见【Python3 优化】
            a.sort()
            ans += sum(a[-lim:])
        return ans


    def _gen(self):
        n = self.s_generate_int((1, 10000))
        value = self.s_generate_list_int((n, n), (1, 100000))
        limit = self.s_generate_list_int((n, n), (1, n))
        return value, limit


from itertools import permutations
ODD_MASK = 0x155
D = 9

special_numbers = []
for mask in range(1, 1 << D):
    t = mask & ODD_MASK
    if t & (t - 1):  # 至少有两个奇数
        continue

    # 构造排列 perm
    perm = []
    size = odd = 0
    for x in range(1, D + 1):
        if mask >> (x - 1) & 1:
            size += x
            perm.extend([x] * (x // 2))
            if x % 2:
                odd = x
    if size > 16:  # 回文串太长了
        continue

    # 枚举 perm 的所有排列 p，生成对应的回文数
    for p in permutations(perm):
        pal = 0
        for v in p:
            pal = pal * 10 + v
        v = pal
        if odd:
            pal = pal * 10 + odd
        # 反转 pal 的左半，拼在 pal 后面
        while v:
            v, d = divmod(v, 10)
            pal = pal * 10 + d
        special_numbers.append(pal)
special_numbers = sorted(set(special_numbers))

from bisect import bisect_right

class Solution4(Testing):
    date = "2025-8-10"
    def __init__(self):
        Testing.__init__(self,
                         degree=2,
                         idx=3646,
                         types=[ProblemType.BackDating],
                         pass_rate=0.413,
                         description="给你一个整数 `n`。\n\n如果一个数满足以下条件，那么它被称为 **特殊数** ：\n\n- 它是一个 **回文数** 。\n- 数字中每个数字 `k` 出现 **恰好** `k` 次。\n\n返回 **严格** 大于 `n` 的 **最小** 特殊数。\n\n如果一个整数正向读和反向读都相同，则它是 **回文数** 。例如，`121` 是回文数，而 `123` 不是。\n\n \n\n**示例 1:**\n\n**输入:** n = 2\n\n**输出:** 22\n\n**解释:**\n\n22 是大于 2 的最小特殊数，因为它是一个回文数，并且数字 2 恰好出现了 2 次。\n\n**示例 2:**\n\n**输入:** n = 33\n\n**输出:** 212\n\n**解释:**\n\n212 是大于 33 的最小特殊数，因为它是一个回文数，并且数字 1 和 2 恰好分别出现了 1 次和 2 次。\n\n \n\n**提示:**\n\n- `0 <= n <= 10**15`"
                         )

    def solve(self, n: int) -> int:
        i = bisect_right(special_numbers, n)
        return special_numbers[i]

    def gen(self):
        return self.generate_int(int_range=(0, 1000_000_000_000_000)),