from . import Problem as Testing
from typing import List


class Solution1(Testing):
    date = "2025-8-16"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3648,
                         types=[],
                         pass_rate=0.68,
                         description="给你一个 `n × m` 的网格和一个整数 `k`。\n\n一个放置在单元格 `(r, c)` 的传感器可以覆盖所有与 `(r, c)` 的 **切比雪夫距离****不超过** `k` 的单元格。\n\n两个单元格 `(r1, c1)` 和 `(r2, c2)` 之间的 **切比雪夫距离** 为 `max(|r1 − r2|,|c1 − c2|)`。\n\n你的任务是返回覆盖整个网格所需传感器的 **最少** 数量。\n\n \n\n**示例 1:**\n\n**输入:** n = 5, m = 5, k = 1\n\n**输出:** 4\n\n**解释:**\n\n在位置 `(0, 3)`、`(1, 0)`、`(3, 3)` 和 `(4, 1)` 放置传感器可以确保网格中的每个单元格都被覆盖。因此，答案是 4。\n\n**示例 2:**\n\n**输入:** n = 2, m = 2, k = 2\n\n**输出:** 1\n\n**解释:**\n\n当 `k = 2` 时，无论传感器放在哪个位置，单个传感器都可以覆盖整个 `2 * 2` 的网格。因此，答案是 1。\n\n \n\n**提示:**\n\n- `1 <= n <= 10**3`\n- `1 <= m <= 10**3`\n- `0 <= k <= 10**3`"
                         )

    def solve(self, n: int, m: int, k: int) -> int:
        size = k * 2 + 1
        return ((n - 1) // size + 1) * ((m - 1) // size + 1)

    def gen(self):
        return self.generate_int(int_range=(1, 1000)), self.generate_int(int_range=(1, 1000)), self.generate_int(int_range=(1, 1000))



class Solution2(Testing):
    date = "2025-8-16"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3649,
                         types=[],
                         pass_rate=0.413,
                         description="给你一个整数数组 `nums`。\n\n如果一对下标 `(i, j)` 满足以下条件，则称其为 **完美** 的：\n\n- `i < j`\n- 令a = nums[i]，b = nums[j]。那么：\n  - `min(|a - b|, |a + b|) <= min(|a|, |b|)`\n  - `max(|a - b|, |a + b|) >= max(|a|, |b|)`\n\n返回 **不同** 完美对 的数量。\n\n**注意：**绝对值 `|x|` 指的是 `x` 的 **非负** 值。\n\n \n\n**示例 1:**\n\n**输入:** nums = [0,1,2,3]\n\n**输出:** 2\n\n**解释:**\n\n有 2 个完美对：\n\n| `(i, j)` | `(a, b)` | `min(|a − b|, |a + b|)`     | `min(|a|, |b|)` | `max(|a − b|, |a + b|)`     | `max(|a|, |b|)` |\n| -------- | -------- | --------------------------- | --------------- | --------------------------- | --------------- |\n| (1, 2)   | (1, 2)   | `min(|1 − 2|, |1 + 2|) = 1` | 1               | `max(|1 − 2|, |1 + 2|) = 3` | 2               |\n| (2, 3)   | (2, 3)   | `min(|2 − 3|, |2 + 3|) = 1` | 2               | `max(|2 − 3|, |2 + 3|) = 5` | 3               |\n\n**示例 2:**\n\n**输入:** nums = [-3,2,-1,4]\n\n**输出:** 4\n\n**解释:**\n\n有 4 个完美对：\n\n| `(i, j)` | `(a, b)` | `min(|a − b|, |a + b|)`           | `min(|a|, |b|)` | `max(|a − b|, |a + b|)`           | `max(|a|, |b|)` |\n| -------- | -------- | --------------------------------- | --------------- | --------------------------------- | --------------- |\n| (0, 1)   | (-3, 2)  | `min(|-3 - 2|, |-3 + 2|) = 1`     | 2               | `max(|-3 - 2|, |-3 + 2|) = 5`     | 3               |\n| (0, 3)   | (-3, 4)  | `min(|-3 - 4|, |-3 + 4|) = 1`     | 3               | `max(|-3 - 4|, |-3 + 4|) = 7`     | 4               |\n| (1, 2)   | (2, -1)  | `min(|2 - (-1)|, |2 + (-1)|) = 1` | 1               | `max(|2 - (-1)|, |2 + (-1)|) = 3` | 2               |\n| (1, 3)   | (2, 4)   | `min(|2 - 4|, |2 + 4|) = 2`       | 2               | `max(|2 - 4|, |2 + 4|) = 6`       | 4               |\n\n**示例 3:**\n\n**输入:** nums = [1,10,100,1000]\n\n**输出:** 0\n\n**解释:**\n\n没有完美对。因此，答案是 0。\n\n \n\n**提示:**\n\n- `2 <= nums.length <= 10**5`\n- `-10**9 <= nums[i] <= 10**9`"
                         )

    def solve(self, nums: List[int]) -> int:
        nums.sort(key=abs)
        ans = left = 0
        for j, b in enumerate(nums):
            while abs(nums[left]) * 2 < abs(b):
                left += 1
            # a=nums[i]，其中 i 最小是 left，最大是 j-1，一共有 j-left 个
            ans += j - left
        return ans

    def gen(self):
        return self.generate_list_int(list_length_range=(2, 10000), int_range=(-1000_000_000, 1000_000_000)),


from math import inf
from heapq import heappop, heappush


class Solution3(Testing):
    date = "2025-8-16"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3650,
                         types=[],
                         pass_rate=0.565,
                         description="给你一个包含 `n` 个节点的有向带权图，节点编号从 `0` 到 `n - 1`。同时给你一个数组 `edges`，其中 `edges[i] = [ui, vi, wi]` 表示一条从节点 `ui` 到节点 `vi` 的有向边，其成本为 `wi`。\n\n\n\n每个节点 `ui` 都有一个 **最多可使用一次** 的开关：当你到达 `ui` 且尚未使用其开关时，你可以对其一条入边 `vi` → `ui` 激活开关，将该边反转为 `ui` → `vi` 并 **立即** 穿过它。\n\n反转仅对那一次移动有效，使用反转边的成本为 `2 * wi`。\n\n返回从节点 `0` 到达节点 `n - 1` 的 **最小** 总成本。如果无法到达，则返回 -1。\n\n \n\n**示例 1:**\n\n**输入:** n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]\n\n**输出:** 5\n\n**解释:**\n\n**![img](https://assets.leetcode.com/uploads/2025/05/07/e1drawio.png)**\n\n- 使用路径 `0 → 1` (成本 3)。\n- 在节点 1，将原始边 `3 → 1` 反转为 `1 → 3` 并穿过它，成本为 `2 * 1 = 2`。\n- 总成本为 `3 + 2 = 5`。\n\n**示例 2:**\n\n**输入:** n = 4, edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]\n\n**输出:** 3\n\n**解释:**\n\n- 不需要反转。走路径 `0 → 2` (成本 1)，然后 `2 → 1` (成本 1)，再然后 `1 → 3` (成本 1)。\n- 总成本为 `1 + 1 + 1 = 3`。\n\n \n\n**提示:**\n\n- `2 <= n <= 5 * 10**4`\n- `1 <= edges.length <= 10**5`\n- `edges[i] = [ui, vi, wi]`\n- `0 <= ui, vi <= n - 1`\n- `1 <= wi <= 1000`"
                         )

    def solve(self, n: int, edges: List[List[int]]) -> int:
        g: list[list[tuple[int, int]]] = [[] for _ in range(n)]  # 邻接表
        for x, y, wt in edges:
            g[x].append((y, wt))
            g[y].append((x, wt * 2))

        dis = [inf] * n
        dis[0] = 0  # 起点到自己的距离是 0
        h = [(0, 0)]  # 堆中保存 (起点到节点 x 的最短路长度，节点 x)

        while h:
            dis_x, x = heappop(h)
            if dis_x > dis[x]:  # x 之前出堆过
                continue
            if x == n - 1:  # 到达终点
                return dis_x
            for y, wt in g[x]:
                new_dis_y = dis_x + wt
                if new_dis_y < dis[y]:
                    dis[y] = new_dis_y  # 更新 x 的邻居的最短路
                    # 懒更新堆：只插入数据，不更新堆中数据
                    # 相同节点可能有多个不同的 new_dis_y，除了最小的 new_dis_y，其余值都会触发上面的 continue
                    heappush(h, (new_dis_y, y))

        return -1

    def _gen(self):
        n, edges = self.s_generate_graph(v_num_range=(2, 5000), edges_length_range=(1, 1000), weigth_range=(1, 1000))
        return n, edges


class Solution4(Testing):
    date = "2025-8-16"
    def __init__(self):
        Testing.__init__(self,
                         degree=2,
                         idx=3651,
                         types=[],
                         pass_rate=0.399,
                         description="给你一个 `m x n` 的二维整数数组 `grid` 和一个整数 `k`。你从左上角的单元格 `(0, 0)` 出发，目标是到达右下角的单元格 `(m - 1, n - 1)`。\n\n有两种移动方式可用：\n\n- **普通移动**：你可以从当前单元格 `(i, j)` 向右或向下移动，即移动到 `(i, j + 1)`（右）或 `(i + 1, j)`（下）。成本为目标单元格的值。\n- **传送**：你可以从任意单元格 `(i, j)` 传送到任意满足 `grid[x][y] <= grid[i][j]` 的单元格 `(x, y)`；此移动的成本为 0。你最多可以传送 `k` 次。\n\n返回从 `(0, 0)` 到达单元格 `(m - 1, n - 1)` 的 **最小** 总成本。\n\n \n\n**示例 1:**\n\n**输入:** grid = [[1,3,3],[2,5,4],[4,3,5]], k = 2\n\n**输出:** 7\n\n**解释:**\n\n我们最初在 (0, 0)，成本为 0。\n\n| 当前位置 | 移动            | 新位置   | 总成本      |\n| -------- | --------------- | -------- | ----------- |\n| `(0, 0)` | 向下移动        | `(1, 0)` | `0 + 2 = 2` |\n| `(1, 0)` | 向右移动        | `(1, 1)` | `2 + 5 = 7` |\n| `(1, 1)` | 传送到 `(2, 2)` | `(2, 2)` | `7 + 0 = 7` |\n\n到达右下角单元格的最小成本是 7。\n\n**示例 2:**\n\n**输入:** grid = [[1,2],[2,3],[3,4]], k = 1\n\n**输出:** 9\n\n**解释:**\n\n我们最初在 (0, 0)，成本为 0。\n\n| 当前位置 | 移动     | 新位置   | 总成本      |\n| -------- | -------- | -------- | ----------- |\n| `(0, 0)` | 向下移动 | `(1, 0)` | `0 + 2 = 2` |\n| `(1, 0)` | 向右移动 | `(1, 1)` | `2 + 3 = 5` |\n| `(1, 1)` | 向下移动 | `(2, 1)` | `5 + 4 = 9` |\n\n到达右下角单元格的最小成本是 9。\n\n \n\n**提示:**\n\n- `2 <= m, n <= 80`\n- `m == grid.length`\n- `n == grid[i].length`\n- `0 <= grid[i][j] <= 10**4`\n- `0 <= k <= 10`"
                         )

    def solve(self, grid: List[List[int]], k: int) -> int:
        if k and grid[0][0] >= grid[-1][-1]:
            return 0

        n = len(grid[0])
        mx = max(map(max, grid))

        suf_min_f = [inf] * (mx + 2)
        for _ in range(k + 1):
            min_f = [inf] * (mx + 1)

            # 64. 最小路径和（空间优化写法）
            f = [inf] * (n + 1)
            f[1] = -grid[0][0]  # 起点的成本不算
            for row in grid:
                for j, x in enumerate(row):
                    f[j + 1] = min(min(f[j], f[j + 1]) + x, suf_min_f[x])
                    min_f[x] = min(min_f[x], f[j + 1])

            tmp = suf_min_f.copy()
            # 计算 min_f 的后缀最小值
            for i in range(mx, -1, -1):
                suf_min_f[i] = min(suf_min_f[i + 1], min_f[i])
            if suf_min_f == tmp:
                # 收敛了：传送不改变 suf_min_f，那么无论再传送多少次都不会改变 suf_min_f
                break

        return f[n]


    def gen(self):
        return self.generate_matrix(list_length_range1=(2, 80), list_length_range2=(2, 80),
                                    int_range=(0, 10000)), self.generate_int(int_range=(0, 10))