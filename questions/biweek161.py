from collections import deque
from . import Problem as Testing, ProblemType
from ..testcase_sampler import _generate_int
from typing import List
import math


MX = 100_000
is_prime = [False] * 2 + [True] * (MX - 2)  # 0 和 1 不是质数
for i in range(2, math.isqrt(MX) + 1):
    if is_prime[i]:
        for j in range(i * i, MX, i):
            is_prime[j] = False  # j 是质数 i 的倍数


class Solution1(Testing):
    date = "2025-7-19"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3618,
                         types=[ProblemType.Math, ProblemType.NumberTheory, ProblemType.Array],
                         pass_rate=0.559,
                         description="给你一个整数数组 `nums`。\n\n根据以下规则将 `nums` 分割成两个数组 `A` 和 `B`：\n\n- `nums` 中位于 **质数** 下标的元素必须放入数组 `A`。\n- 所有其他元素必须放入数组 `B`。\n\n返回两个数组和的 **绝对** 差值：`|sum(A) - sum(B)|`。\n\n**质数** 是一个大于 1 的自然数，它只有两个因子，1和它本身。\n\n**注意**：空数组的和为 0。\n\n \n\n**示例 1:**\n\n**输入:** nums = [2,3,4]\n\n**输出:** 1\n\n**解释:**\n\n- 数组中唯一的质数下标是 2，所以 `nums[2] = 4` 被放入数组 `A`。\n- 其余元素 `nums[0] = 2` 和 `nums[1] = 3` 被放入数组 `B`。\n- `sum(A) = 4`，`sum(B) = 2 + 3 = 5`。\n- 绝对差值是 `|4 - 5| = 1`。\n\n**示例 2:**\n\n**输入:** nums = [-1,5,7,0]\n\n**输出:** 3\n\n**解释:**\n\n- 数组中的质数下标是 2 和 3，所以 `nums[2] = 7` 和 `nums[3] = 0` 被放入数组 `A`。\n- 其余元素 `nums[0] = -1` 和 `nums[1] = 5` 被放入数组 `B`。\n- `sum(A) = 7 + 0 = 7`，`sum(B) = -1 + 5 = 4`。\n- 绝对差值是 `|7 - 4| = 3`。\n\n \n\n**提示:**\n\n- `1 <= nums.length <= 105`\n- `-109 <= nums[i] <= 109`"
                         )

    def solve(self, nums: List[int]) -> int:
        ans = sum(x if p else -x for x, p in zip(nums, is_prime))
        return abs(ans)

    def gen(self):
        return self.generate_list_int(list_length_range=(1, 10000), int_range=(-10000, 10000)),


class Solution2(Testing):
    date = "2025-7-19"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3619,
                         types=[ProblemType.DeepFirstSearch, ProblemType.BreadthFirstSearch, ProblemType.DisjointSet,
                                ProblemType.Array, ProblemType.Matrix],
                         pass_rate=0.625,
                         description="给你一个 `m x n` 的矩阵 `grid` 和一个正整数 `k`。一个 **岛屿** 是由 **正** 整数（表示陆地）组成的，并且陆地间 **四周** 连通（水平或垂直）。\n\n一个岛屿的总价值是该岛屿中所有单元格的值之和。\n\n返回总价值可以被 `k` **整除** 的岛屿数量。\n\n \n\n**示例 1:**\n\n**输入:** grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5\n\n**输出:** 2\n\n**解释:**\n\n网格中包含四个岛屿。蓝色高亮显示的岛屿的总价值可以被 5 整除，而红色高亮显示的岛屿则不能。\n\n**示例 2:**\n\n**输入:** grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3\n\n**输出:** 6\n\n**解释:**\n\n网格中包含六个岛屿，每个岛屿的总价值都可以被 3 整除。\n\n \n\n**提示:**\n\n- `m == grid.length`\n- `n == grid[i].length`\n- `1 <= m, n <= 1000`\n- `1 <= m * n <= 105`\n- `0 <= grid[i][j] <= 106`\n- `1 <= k < = 106`"
                         )

    def solve(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> int:
            res = grid[i][j]
            grid[i][j] = 0  # 标记 (i,j) 访问过
            for x, y in (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j):
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    res += dfs(x, y)
            return res

        ans = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x and dfs(i, j) % k == 0:
                    ans += 1
        return ans


    def gen(self):
        return (self.generate_matrix(list_length_range1=(1, 20), list_length_range2=(1, 20), int_range=(0, 100000)),
                self.generate_int(int_range=(1, 1000)))


from ..testcase_sampler import _construct_graph_connected, _generate_choice
from bisect import bisect_left

class Solution3(Testing):
    date = "2025-7-19"
    def __init__(self):
        Testing.__init__(self,
                         degree=2,
                         idx=3620,
                         types=[ProblemType.Graph, ProblemType.TopologySorting, ProblemType.Array, ProblemType.Bisearch,
                                ProblemType.DynamicPlanning, ProblemType.ShortestPath, ProblemType.Heap],
                         pass_rate=0.368,
                         description="给你一个包含 `n` 个节点（编号从 0 到 `n - 1`）的有向无环图。图由长度为 `m` 的二维数组 `edges` 表示，其中 `edges[i] = [ui, vi, costi]` 表示从节点 `ui` 到节点 `vi` 的单向通信，恢复成本为 `costi`。\n\n一些节点可能处于离线状态。给定一个布尔数组 `online`，其中 `online[i] = true` 表示节点 `i` 在线。节点 0 和 `n - 1` 始终在线。\n\n从 0 到 `n - 1` 的路径如果满足以下条件，那么它是 **有效** 的：\n\n- 路径上的所有中间节点都在线。\n- 路径上所有边的总恢复成本不超过 `k`。\n\n对于每条有效路径，其 **分数** 定义为该路径上的最小边成本。\n\n返回所有有效路径中的 **最大** 路径分数（即最大 **最小** 边成本）。如果没有有效路径，则返回 -1。\n\n \n\n**示例 1:**\n\n**输入:** edges = [[0,1,5],[1,3,10],[0,2,3],[2,3,4]], online = [true,true,true,true], k = 10\n\n**输出:** 3\n\n**解释:**\n\n![img](https://assets.leetcode.com/uploads/2025/06/06/graph-10.png)\n\n- 图中有两条从节点 0 到节点 3 的可能路线：\n  1. 路径 `0 → 1 → 3`\n     - 总成本 = `5 + 10 = 15`，超过了 k (`15 > 10`)，因此此路径无效。\n  2. 路径 `0 → 2 → 3`\n     - 总成本 = `3 + 4 = 7 <= k`，因此此路径有效。\n     - 此路径上的最小边成本为 `min(3, 4) = 3`。\n- 没有其他有效路径。因此，所有有效路径分数中的最大值为 3。\n\n**示例 2:**\n\n**输入:** edges = [[0,1,7],[1,4,5],[0,2,6],[2,3,6],[3,4,2],[2,4,6]], online = [true,true,true,false,true], k = 12\n\n**输出:** 6\n\n**解释:**\n\n![img](https://assets.leetcode.com/uploads/2025/06/06/graph-11.png)\n\n- 节点 3 离线，因此任何通过 3 的路径都是无效的。\n- 考虑从 0 到 4 的其余路线：\n  1. 路径 `0 → 1 → 4`\n     - 总成本 = `7 + 5 = 12 <= k`，因此此路径有效。\n     - 此路径上的最小边成本为 `min(7, 5) = 5`。\n  2. 路径 `0 → 2 → 3 → 4`\n     - 节点 3 离线，因此无论成本多少，此路径无效。\n  3. 路径 `0 → 2 → 4`\n     - 总成本 = `6 + 6 = 12 <= k`，因此此路径有效。\n     - 此路径上的最小边成本为 `min(6, 6) = 6`。\n- 在两条有效路径中，它们的分数分别为 5 和 6。因此，答案是 6。\n\n \n\n**提示:**\n\n- `n == online.length`\n- `2 <= n <= 5 * 104`\n- `0 <= m == edges.length <= min(105, n * (n - 1) / 2)`\n- `edges[i] = [ui, vi, costi]`\n- `0 <= ui, vi < n`\n- `ui != vi`\n- `0 <= costi <= 109`\n- `0 <= k <= 5 * 1013`\n- `online[i]` 是 `true` 或 `false`，且 `online[0]` 和 `online[n - 1]` 均为 `true`。\n- 给定的图是一个有向无环图。"
                         )

    def solve(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        deg = [0] * n
        max_wt = -1
        x: int
        y: int
        wt: int
        for x, y, wt in edges:
            if online[x] and online[y]:
                g[x].append((y, wt))
                deg[y] += 1
                if x == 0:
                    max_wt = max(max_wt, wt)

        # 先清理无法从 0 到达的边
        q: deque[int] = deque(i for i in range(1, n) if deg[i] == 0)
        while q:
            x = q.popleft()
            for y, _ in g[x]:
                deg[y] -= 1
                if y and deg[y] == 0:
                    q.append(y)

        def check(lower: int) -> bool:
            deg_copy = deg.copy()
            f = [math.inf] * n
            f[0] = 0

            q: deque[int] = deque([0])
            while q:
                x = q.popleft()
                if x == n - 1:
                    return f[x] > k
                y: int
                wt: int
                for y, wt in g[x]:
                    if wt >= lower:
                        f[y] = min(f[y], f[x] + wt)
                    deg_copy[y] -= 1
                    if deg_copy[y] == 0:
                        q.append(y)
            return True

        # 二分无法到达 n-1 的最小 lower，那么减一后，就是可以到达 n-1 的最大 lower
        return bisect_left(range(max_wt + 1), True, key=check) - 1

    def _gen(self):
        n = _generate_int(2, 100)
        edges = _construct_graph_connected(n)
        edges = [[i, j, _generate_int(0, 1000)] for i, j in edges]
        online = [_generate_choice([True, False]) for _ in range(n)]
        online[0] = True
        online[-1] = True
        k = _generate_int(0, 10000)
        return edges, online, k


from functools import cache
class Solution4(Testing):
    date = "2025-7-19"
    def __init__(self):
        Testing.__init__(self,
                         degree=2,
                         idx=3621,
                         pass_rate=0.41,
                         types=[ProblemType.Math, ProblemType.DynamicPlanning, ProblemType.Combination],
                         description="给你两个整数 `n` 和 `k`。\n\n对于任意正整数 `x`，定义以下序列：\n\n- $p_0$ = x\n- $p_{i+1} = popcount(p_i)$，对于所有 `i >= 0`，其中 `popcount(y)` 是 `y` 的二进制表示中 1 的数量。\n\n这个序列最终会达到值 1。\n\n`x` 的 **popcount-depth** （位计数深度）定义为使得 `pd = 1` 的 **最小** 整数 `d >= 0`。\n\n例如，如果 `x = 7`（二进制表示 `\"111\"`）。那么，序列是：`7 → 3 → 2 → 1`，所以 7 的 popcount-depth 是 3。\n\n你的任务是确定范围 `[1, n]` 中 popcount-depth **恰好** 等于 `k` 的整数数量。\n\n返回这些整数的数量。\n\n \n\n**示例 1:**\n\n**输入:** n = 4, k = 1\n\n**输出:** 2\n\n**解释:**\n\n在范围 `[1, 4]` 中，以下整数的 popcount-depth 恰好等于 1：\n\n|  x   | 二进制  | 序列    |\n| :--: | :-----: | :------ |\n|  2   | `\"10\"`  | `2 → 1` |\n|  4   | `\"100\"` | `4 → 1` |\n\n因此，答案是 2。\n\n**示例 2:**\n\n**输入:** n = 7, k = 2\n\n**输出:** 3\n\n**解释:**\n\n在范围 `[1, 7]` 中，以下整数的 popcount-depth 恰好等于 2：\n\n| x    | 二进制  | 序列        |\n| ---- | ------- | ----------- |\n| 3    | `\"11\"`  | `3 → 2 → 1` |\n| 5    | `\"101\"` | `5 → 2 → 1` |\n| 6    | `\"110\"` | `6 → 2 → 1` |\n\n因此，答案是 3。\n\n \n\n**提示:**\n\n- `1 <= n <= 1015`\n- `0 <= k <= 5`"
                         )

    def solve(self, n: int, k: int) -> int:
        if k == 0:
            return 1

        # 注：也可以不转成字符串，下面 dfs 用位运算取出 n 的第 i 位
        # 但转成字符串的通用性更好
        s = list(map(int, bin(n)[2:]))
        m = len(s)
        if k == 1:
            return m - 1

        @cache
        def dfs(i: int, left1: int, is_limit: bool) -> int:
            if i == m:
                return 0 if left1 else 1
            up = s[i] if is_limit else 1
            res = 0
            for d in range(min(up, left1) + 1):
                res += dfs(i + 1, left1 - d, is_limit and d == up)
            return res

        ans = 0
        f = [0] * (m + 1)
        for i in range(1, m + 1):
            f[i] = f[i.bit_count()] + 1
            if f[i] == k:
                # 计算有多少个二进制数恰好有 i 个 1
                ans += dfs(0, i, True)
        return ans

    def gen(self):
        return self.generate_int(int_range=(1, 100000)), self.generate_int(int_range=(0, 5))