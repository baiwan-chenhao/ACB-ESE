from heapq import nlargest
from . import Problem as Testing, ProblemType
from typing import List


class Solution1(Testing):
    date = "2025-9-14"
    def __init__(self):
        Testing.__init__(self,
                         degree=0,
                         idx=3683,
                         types=[],
                         pass_rate=0.868,
                         description="给你一个二维整数数组 `tasks`，其中 `tasks[i] = [si, ti]`。\n\n数组中的每个 `[si, ti]` 表示一个任务，该任务的开始时间为 `si`，完成该任务需要 `ti` 个时间单位。\n\n返回至少完成一个任务的最早时间。\n\n \n\n**示例 1：**\n\n**输入：** tasks = [[1,6],[2,3]]\n\n**输出：** 5\n\n**解释：**\n\n第一个任务从时间 `t = 1` 开始，并在 `1 + 6 = 7` 时完成。第二个任务在时间 `t = 2` 开始，并在 `2 + 3 = 5` 时完成。因此，最早完成的任务在时间 5。\n\n**示例 2：**\n\n**输入：** tasks = [[100,100],[100,100],[100,100]]\n\n**输出：** 200\n\n**解释：**\n\n三个任务都在时间 `100 + 100 = 200` 时完成。\n\n \n\n**提示：**\n\n- `1 <= tasks.length <= 100`\n- `tasks[i] = [si, ti]`\n- `1 <= si, ti <= 100`"
                         )

    def solve(self, tasks: List[List[int]]) -> int:
        return min(s + t for s, t in tasks)

    def gen(self):
        return self.generate_matrix(list_length_range1=(1, 100), list_length_range2=(2, 2), int_range=(1, 100)),


class Solution2(Testing):
    date = "2025-9-14"
    def __init__(self):
        Testing.__init__(self,
                         degree=0,
                         idx=3684,
                         types=[ProblemType.Greedy, ProblemType.Array, ProblemType.HashTable, ProblemType.Sorting],
                         pass_rate=0.700,
                         description="给你一个 **正整数** 数组 `nums` 和一个整数 `k`。\n\n从 `nums` 中选择最多 `k` 个元素，使它们的和最大化。但是，所选的数字必须 **互不相同** 。\n\n返回一个包含所选数字的数组，数组中的元素按 **严格递减** 顺序排序。\n\n \n\n**示例 1：**\n\n**输入：** nums = [84,93,100,77,90], k = 3\n\n**输出：** [100,93,90]\n\n**解释：**\n\n最大和为 283，可以通过选择 93、100 和 90 实现。将它们按严格递减顺序排列，得到 `[100, 93, 90]`。\n\n**示例 2：**\n\n**输入：** nums = [84,93,100,77,93], k = 3\n\n**输出：** [100,93,84]\n\n**解释：**\n\n最大和为 277，可以通过选择 84、93 和 100 实现。将它们按严格递减顺序排列，得到 `[100, 93, 84]`。不能选择 93、100 和另一个 93，因为所选数字必须互不相同。\n\n**示例 3：**\n\n**输入：** nums = [1,1,1,2,2,2], k = 6\n\n**输出：** [2,1]\n\n**解释：**\n\n最大和为 3，可以通过选择 1 和 2 实现。将它们按严格递减顺序排列，得到 `[2, 1]`。\n\n \n\n**提示：**\n\n- `1 <= nums.length <= 100`\n- `1 <= nums[i] <= 10*9`\n- `1 <= k <= nums.length`"
                         )

    def solve(self, nums: list[int], k: int) -> list[int]:
        return nlargest(k, set(nums))

    def _gen(self):
        nums = self.s_generate_list_int(list_length_range=(1, 100), int_range=(1, 1000000))
        k = self.s_generate_int(int_range=(1, len(nums)))
        return nums, k


class Solution3(Testing):
    date = "2025-9-14"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3685,
                         types=[ProblemType.Array, ProblemType.BiPoint, ProblemType.DynamicPlanning, ProblemType.Sorting],
                         pass_rate=0.293,
                         description="给你一个大小为 `n` 的整数数组 `nums` 和一个正整数 `k`。\n\n通过将每个元素 `nums[i]` 替换为 `min(nums[i], x)`，可以得到一个由值 `x` **限制**（capped）的数组。\n\n对于从 1 到 `n` 的每个整数 `x`，确定是否可以从由 `x` 限制的数组中选择一个 **子序列**，使所选元素的和 **恰好** 为 `k`。\n\n返回一个下标从 **0** 开始的布尔数组 `answer`，其大小为 `n`，其中 `answer[i]` 为 `true` 表示当 `x = i + 1` 时可以选出满足要求的子序列；否则为 `false`。\n\n**子序列** 是一个从数组中通过删除一些或不删除任何元素（且不改变剩余元素顺序）派生出来的 **非空** 数组。\n\n \n\n**示例 1：**\n\n**输入：** nums = [4,3,2,4], k = 5\n\n**输出：** [false,false,true,true]\n\n**解释：**\n\n- 对于 `x = 1`，限制后的数组为 `[1, 1, 1, 1]`。可能的和为 `1, 2, 3, 4`，因此无法选出和为 `5` 的子序列。\n- 对于 `x = 2`，限制后的数组为 `[2, 2, 2, 2]`。可能的和为 `2, 4, 6, 8`，因此无法选出和为 `5` 的子序列。\n- 对于 `x = 3`，限制后的数组为 `[3, 3, 2, 3]`。可以选择子序列 `[2, 3]`，其和为 `5`，能选出满足要求的子序列。\n- 对于 `x = 4`，限制后的数组为 `[4, 3, 2, 4]`。可以选择子序列 `[3, 2]`，其和为 `5`，能选出满足要求的子序列。\n\n**示例 2：**\n\n**输入：** nums = [1,2,3,4,5], k = 3\n\n**输出：** [true,true,true,true,true]\n\n**解释：**\n\n对于每个值 `x`，总是可以从限制后的数组中选择一个子序列，其和正好为 `3`。\n\n \n\n**提示：**\n\n- `1 <= n == nums.length <= 4000`\n- `1 <= nums[i] <= n`\n- `1 <= k <= 4000`"
                         )

    def solve(self, nums: List[int], k: int) -> List[bool]:
        nums.sort()

        n = len(nums)
        ans = [False] * n
        f = [False] * (k + 1)
        f[0] = True  # 不选元素，和为 0

        i = 0
        for x in range(1, n + 1):
            # 增量地考虑所有恰好等于 x 的数
            # 小于 x 的数在之前的循环中已计算完毕，无需重复计算
            while i < n and nums[i] == x:
                for j in range(k, nums[i] - 1, -1):
                    f[j] = f[j] or f[j - nums[i]]  # 0-1 背包：不选 or 选
                i += 1

            # 枚举（从大于 x 的数中）选了 j 个 x
            for j in range(min(n - i, k // x) + 1):
                if f[k - j * x]:
                    ans[x - 1] = True
                    break
        return ans


    def _gen(self):
        n = self.s_generate_int((1, 40))
        nums = self.s_generate_list_int(list_length_range=(n, n), int_range=(1, n))
        k = self.s_generate_int((1, 40))
        return nums, k




class Solution4(Testing):
    date = "2025-9-14"
    def __init__(self):
        Testing.__init__(self,
                         degree=2,
                         idx=3686,
                         types=[ProblemType.Array, ProblemType.DynamicPlanning],
                         pass_rate=0.573,
                         description="给你一个整数数组 `nums`。\n\n如果一个 **子序列** 中 **不存在连续三个** 元素奇偶性相同（**仅考虑该子序列内**），则称该子序列为**稳定子序列** 。\n\n请返回所有稳定子序列的数量。\n\n由于结果可能非常大，请将答案对 `109 + 7` 取余数后返回。\n\n**子序列** 是一个从数组中通过删除某些元素（或不删除任何元素），并保持剩余元素相对顺序不变的 **非空** 数组。\n\n \n\n**示例 1：**\n\n**输入：** nums = [1,3,5]\n\n**输出：** 6\n\n**解释：**\n\n- 稳定子序列为：`[1]`, `[3]`, `[5]`, `[1, 3]`, `[1, 5]`, 和 `[3, 5]`。\n- 子序列 `[1, 3, 5]` 不稳定，因为它包含三个连续的奇数。因此答案是 6。\n\n**示例 2：**\n\n**输入：** nums = [2,3,4,2]\n\n**输出：** 14\n\n**解释：**\n\n- 唯一一个不稳定子序列是 `[2, 4, 2]`，因为它包含三个连续的偶数。\n- 所有其他子序列都是稳定子序列。因此答案是 14。\n\n \n\n**提示：**\n\n- `1 <= nums.length <= 10**5`\n- `1 <= nums[i] <= 10**5`\n\n "
                         )

    def solve(self, nums: list[int]) -> int:
        MOD = 1_000_000_007
        f = [[0, 0], [0, 0]]
        for x in nums:
            x %= 2
            f[x][1] = (f[x][1] + f[x][0]) % MOD
            f[x][0] = (f[x][0] + f[x ^ 1][0] + f[x ^ 1][1] + 1) % MOD
        return (f[0][0] + f[0][1] + f[1][0] + f[1][1]) % MOD


    def gen(self):
        return self.generate_list_int(list_length_range=(2, 100), int_range=(0, 100)),

