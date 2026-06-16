from itertools import accumulate
from . import Problem as Testing, ProblemType
from typing import List


class Solution1(Testing):
    date = "2025-8-17"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3652,
                         types=[ProblemType.Array, ProblemType.PrefixSum, ProblemType.SlideWindows],
                         pass_rate=0.41,
                         description="给你两个整数数组 `prices` 和 `strategy`，其中：\n\n- `prices[i]` 表示第 `i` 天某股票的价格。\n\n- ```\n  strategy[i]表示第i天的交易策略，其中：\n  ```\n\n  - `-1` 表示买入一单位股票。\n  - `0` 表示持有股票。\n  - `1` 表示卖出一单位股票。\n\n同时给你一个 **偶数** 整数 `k`，你可以对 `strategy` 进行 **最多一次** 修改。一次修改包括：\n\n- 选择 `strategy` 中恰好 `k` 个 **连续** 元素。\n- 将前 `k / 2` 个元素设为 `0`（持有）。\n- 将后 `k / 2` 个元素设为 `1`（卖出）。\n\n**利润** 定义为所有天数中 `strategy[i] * prices[i]` 的 **总和** 。\n\n返回你可以获得的 **最大** 可能利润。\n\n**注意：** 没有预算或股票持有数量的限制，因此所有买入和卖出操作均可行，无需考虑过去的操作。\n\n \n\n**示例 1：**\n\n**输入：** prices = [4,2,8], strategy = [-1,0,1], k = 2\n\n**输出：** 10\n\n**解释：**\n\n| 修改        | 策略       | 利润计算                                  | 利润 |\n| ----------- | ---------- | ----------------------------------------- | ---- |\n| 原始        | [-1, 0, 1] | (-1 × 4) + (0 × 2) + (1 × 8) = -4 + 0 + 8 | 4    |\n| 修改 [0, 1] | [0, 1, 1]  | (0 × 4) + (1 × 2) + (1 × 8) = 0 + 2 + 8   | 10   |\n| 修改 [1, 2] | [-1, 0, 1] | (-1 × 4) + (0 × 2) + (1 × 8) = -4 + 0 + 8 | 4    |\n\n因此，最大可能利润是 10，通过修改子数组 `[0, 1]` 实现。\n\n**示例 2：**\n\n**输入：** prices = [5,4,3], strategy = [1,1,0], k = 2\n\n**输出：** 9\n\n**解释：**\n\n| 修改        | 策略      | 利润计算                                | 利润 |\n| ----------- | --------- | --------------------------------------- | ---- |\n| 原始        | [1, 1, 0] | (1 × 5) + (1 × 4) + (0 × 3) = 5 + 4 + 0 | 9    |\n| 修改 [0, 1] | [0, 1, 0] | (0 × 5) + (1 × 4) + (0 × 3) = 0 + 4 + 0 | 4    |\n| 修改 [1, 2] | [1, 0, 1] | (1 × 5) + (0 × 4) + (1 × 3) = 5 + 0 + 3 | 8    |\n\n因此，最大可能利润是 9，无需任何修改即可达成。\n\n \n\n**提示：**\n\n- `2 <= prices.length == strategy.length <= 105`\n- `1 <= prices[i] <= 105`\n- `-1 <= strategy[i] <= 1`\n- `2 <= k <= prices.length`\n- `k` 是偶数"
                         )

    def solve(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        s = list(accumulate((p * s for p, s in zip(prices, strategy)), initial=0))
        s_sell = list(accumulate(prices, initial=0))

        # 修改一次
        ans = max(s[i - k] + s[n] - s[i] + s_sell[i] - s_sell[i - k // 2] for i in range(k, n + 1))
        return max(ans, s[n])  # 不修改

    def _gen(self):
        l = self.s_generate_int((2, 10000))
        prices = self.s_generate_list_int(list_length_range=(l, l), int_range=(1, 100000))
        strategy = self.s_generate_list_int(list_length_range=(l, l), int_range=(-1, 1))
        k = self.s_generate_int((2, l))
        return prices, strategy, k


from math import isqrt
from functools import reduce
from operator import xor


class Solution2(Testing):
    date = "2025-8-17"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3653,
                         types=[ProblemType.Array, ProblemType.DevideAndConquer, ProblemType.Simulation],
                         pass_rate=0.62,
                         description="给你一个长度为 `n` 的整数数组 `nums` 和一个大小为 `q` 的二维整数数组 `queries`，其中 `queries[i] = [li, ri, ki, vi]`。\n\n对于每个查询，按以下步骤执行操作：\n\n- 设定 `idx = li`。\n- 当idx <= ri时：\n  - 更新：`nums[idx] = (nums[idx] * vi) % (109 + 7)`\n  - 将 `idx += ki`。\n\n在处理完所有查询后，返回数组 `nums` 中所有元素的 **按位异或** 结果。\n\n \n\n**示例 1：**\n\n**输入：** nums = [1,1,1], queries = [[0,2,1,4]]\n\n**输出：** 4\n\n**解释：**\n\n- 唯一的查询 `[0, 2, 1, 4]` 将下标 0 到下标 2 的每个元素乘以 4。\n- 数组从 `[1, 1, 1]` 变为 `[4, 4, 4]`。\n- 所有元素的异或为 `4 ^ 4 ^ 4 = 4`。\n\n**示例 2：**\n\n**输入：** nums = [2,3,1,5,4], queries = [[1,4,2,3],[0,2,1,2]]\n\n**输出：** 31\n\n**解释：**\n\n- 第一个查询 `[1, 4, 2, 3]` 将下标 1 和 3 的元素乘以 3，数组变为 `[2, 9, 1, 15, 4]`。\n- 第二个查询 `[0, 2, 1, 2]` 将下标 0、1 和 2 的元素乘以 2，数组变为 `[4, 18, 2, 15, 4]`。\n- 所有元素的异或为 `4 ^ 18 ^ 2 ^ 15 ^ 4 = 31`。\n\n \n\n**提示：**\n\n- `1 <= n == nums.length <= 10**3`\n- `1 <= nums[i] <= 10**9`\n- `1 <= q == queries.length <= 10**3`\n- `queries[i] = [li, ri, ki, vi]`\n- `0 <= li <= ri < n`\n- `1 <= ki <= n`\n- `1 <= vi <= 10**5`"
                         )

    def solve(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        B = isqrt(len(queries))
        diff = [None] * B
        has = [None] * B

        for l, r, k, v in queries:
            if k < B:
                # 懒初始化
                if not diff[k]:
                    diff[k] = [1] * (n + k)
                    has[k] = [False] * k
                has[k][l % k] = True
                diff[k][l] = diff[k][l] * v % MOD
                r = r - (r - l) % k + k
                diff[k][r] = diff[k][r] * pow(v, -1, MOD) % MOD
            else:
                for i in range(l, r + 1, k):
                    nums[i] = nums[i] * v % MOD

        for k, d in enumerate(diff):
            if not d:
                continue
            for start, b in enumerate(has[k]):
                if not b:
                    continue
                mul_d = 1
                for i in range(start, n, k):
                    mul_d = mul_d * d[i] % MOD
                    nums[i] = nums[i] * mul_d % MOD

        return reduce(xor, nums)

    def _gen(self):
        length = self.s_generate_int((1, 1000))
        nums = self.s_generate_list_int(list_length_range=(length, length), int_range=(1, 1000_000_000))
        q = self.s_generate_int((1, 1000))
        queries = list()
        for i in range(q):
            r = self.s_generate_int((0, length - 1))
            l = self.s_generate_int((0, r))
            k = self.s_generate_int((1, length))
            v = self.s_generate_int((1, 100000))
            queries.append([
                l, r, k, v
            ])
        return nums, queries

from math import inf
class Solution3(Testing):
    date = "2025-8-17"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3654,
                         types=[ProblemType.Array],
                         pass_rate=0.38,
                         description="给你一个整数数组 `nums` 和一个整数 `k`。\n\n你可以 **多次** 选择 **连续** 子数组 `nums`，其元素和可以被 `k` 整除，并将其删除；每次删除后，剩余元素会填补空缺。\n\n返回在执行任意次数此类删除操作后，`nums` 的最小可能 **和**。\n\n \n\n**示例 1：**\n\n**输入：** nums = [1,1,1], k = 2\n\n**输出：** 1\n\n**解释：**\n\n- 删除子数组 `nums[0..1] = [1, 1]`，其和为 2（可以被 2 整除），剩余 `[1]`。\n- 剩余数组的和为 1。\n\n**示例 2：**\n\n**输入：** nums = [3,1,4,1,5], k = 3\n\n**输出：** 5\n\n**解释：**\n\n- 首先删除子数组 `nums[1..3] = [1, 4, 1]`，其和为 6（可以被 3 整除），剩余数组为 `[3, 5]`。\n- 然后删除子数组 `nums[0..0] = [3]`，其和为 3（可以被 3 整除），剩余数组为 `[5]`。\n- 剩余数组的和为 5。\n\n \n\n**提示：**\n\n- `1 <= nums.length <= 10**5`\n- `1 <= nums[i] <= 10**6`\n- `1 <= k <= 10**5`"
                         )

    def solve(self, nums: list[int], k: int) -> int:
        min_f = [inf] * k
        min_f[0] = 0  # s[0] = 0，对应的 f[0] = 0
        f = s = 0
        for x in nums:
            s = (s + x) % k
            # 不删除 x，那么转移来源为 f + x
            # 删除以 x 结尾的子数组，问题变成剩余前缀的最小和
            # 其中剩余前缀的元素和模 k 等于 s，对应的 f 值的最小值记录在 min_f[s] 中
            f = min(f + x, min_f[s])
            # 维护前缀和 s 对应的最小和，由于上面计算了 min，这里无需再计算 min
            min_f[s] = f
        return f


    def gen(self):
        return self.generate_list_int(list_length_range=(1, 10000), int_range=(1, 10000000)), self.generate_int(int_range=(1, 100000))


class Solution4(Testing):
    date = "2025-8-17"
    def __init__(self):
        Testing.__init__(self,
                         testcase_num=5,
                         degree=2,
                         idx=3655,
                         types=[ProblemType.Array, ProblemType.DevideAndConquer],
                         pass_rate=0.397,
                         description="给你一个长度为 `n` 的整数数组 `nums` 和一个大小为 `q` 的二维整数数组 `queries`，其中 `queries[i] = [li, ri, ki, vi]`。\n\n对于每个查询，需要按以下步骤依次执行操作：\n\n- 设定 `idx = li`。\n- 当idx <= ri时：\n  - 更新：`nums[idx] = (nums[idx] * vi) % (109 + 7)`。\n  - 将 `idx += ki`。\n\n在处理完所有查询后，返回数组 `nums` 中所有元素的 **按位异或** 结果。\n\n \n\n**示例 1：**\n\n**输入：** nums = [1,1,1], queries = [[0,2,1,4]]\n\n**输出：** 4\n\n**解释：**\n\n- 唯一的查询 `[0, 2, 1, 4]` 将下标 0 到下标 2 的每个元素乘以 4。\n- 数组从 `[1, 1, 1]` 变为 `[4, 4, 4]`。\n- 所有元素的异或为 `4 ^ 4 ^ 4 = 4`。\n\n**示例 2：**\n\n**输入：** nums = [2,3,1,5,4], queries = [[1,4,2,3],[0,2,1,2]]\n\n**输出：** 31\n\n**解释：**\n\n- 第一个查询 `[1, 4, 2, 3]` 将下标 1 和 3 的元素乘以 3，数组变为 `[2, 9, 1, 15, 4]`。\n- 第二个查询 `[0, 2, 1, 2]` 将下标 0、1 和 2 的元素乘以 2，数组变为 `[4, 18, 2, 15, 4]`。\n- 所有元素的异或为 `4 ^ 18 ^ 2 ^ 15 ^ 4 = 31`。\n\n \n\n**提示：**\n\n- `1 <= n == nums.length <= 10**5`\n- `1 <= nums[i] <= 109`\n- `1 <= q == queries.length <= 10**5`\n- `queries[i] = [li, ri, ki, vi]`\n- `0 <= li <= ri < n`\n- `1 <= ki <= n`\n- `1 <= vi <= 10**5`"
                         )

    def solve(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        B = isqrt(len(queries))
        diff = [None] * B
        has = [None] * B

        for l, r, k, v in queries:
            if k < B:
                # 懒初始化
                if not diff[k]:
                    diff[k] = [1] * (n + k)
                    has[k] = [False] * k
                has[k][l % k] = True
                diff[k][l] = diff[k][l] * v % MOD
                r = r - (r - l) % k + k
                diff[k][r] = diff[k][r] * pow(v, -1, MOD) % MOD
            else:
                for i in range(l, r + 1, k):
                    nums[i] = nums[i] * v % MOD

        for k, d in enumerate(diff):
            if not d:
                continue
            for start, b in enumerate(has[k]):
                if not b:
                    continue
                mul_d = 1
                for i in range(start, n, k):
                    mul_d = mul_d * d[i] % MOD
                    nums[i] = nums[i] * mul_d % MOD

        return reduce(xor, nums)

    def _gen(self):
        length = self.s_generate_int((1, 10000))
        nums = self.s_generate_list_int(list_length_range=(length, length), int_range=(1, 1000_000_000))
        q = self.s_generate_int((1, 100000))
        queries = list()
        for i in range(q):
            r = self.s_generate_int((0, length - 1))
            l = self.s_generate_int((0, r))
            k = self.s_generate_int((1, length))
            v = self.s_generate_int((1, 100000))
            queries.append([
                l, r, k, v
            ])
        return nums, queries