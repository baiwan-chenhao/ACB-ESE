from . import Problem as Testing, ProblemType
from ..testcase_sampler import _generate_int, _generate_string, _generate_bool, _construct_graph
from typing import List, Tuple
import random
from .tool_class import UnionFind


class Solution1(Testing):
    date = "2025-7-6"
    def __init__(self):
        Testing.__init__(self,
                         degree=0,
                         idx=3606,
                         types=[ProblemType.Array, ProblemType.HashTable, ProblemType.String, ProblemType.Sorting],
                         pass_rate=0.549,
                         problem_slug="add-two-numbers",
                         callable_name="validateCoupons",
                         description="给你三个长度为 `n` 的数组，分别描述 `n` 个优惠券的属性：`code`、`businessLine` 和 `isActive`。其中，第 `i` 个优惠券具有以下属性：\n\n- `code[i]`：一个 **字符串**，表示优惠券的标识符。\n- `businessLine[i]`：一个 **字符串**，表示优惠券所属的业务类别。\n- `isActive[i]`：一个 **布尔值**，表示优惠券是否当前有效。\n\n当以下所有条件都满足时，优惠券被认为是 **有效的** ：\n\n1. `code[i]` 不能为空，并且仅由字母数字字符（a-z、A-Z、0-9）和下划线（`_`）组成。\n2. `businessLine[i]` 必须是以下四个类别之一：`\"electronics\"`、`\"grocery\"`、`\"pharmacy\"`、`\"restaurant\"`。\n3. `isActive[i]` 为 **true** 。\n\n返回所有 **有效优惠券的标识符** 组成的数组，按照以下规则排序：\n\n- 先按照其 **businessLine** 的顺序排序：`\"electronics\"`、`\"grocery\"`、`\"pharmacy\"`、`\"restaurant\"`。\n- 在每个类别内，再按照 **标识符的字典序（升序）**排序。\n\n \n\n**示例 1：**\n\n**输入：** code = [\"SAVE20\",\"\",\"PHARMA5\",\"SAVE@20\"], businessLine = [\"restaurant\",\"grocery\",\"pharmacy\",\"restaurant\"], isActive = [true,true,true,true]\n\n**输出：** [\"PHARMA5\",\"SAVE20\"]\n\n**解释：**\n\n- 第一个优惠券有效。\n- 第二个优惠券的标识符为空（无效）。\n- 第三个优惠券有效。\n- 第四个优惠券的标识符包含特殊字符 `@`（无效）。\n\n**示例 2：**\n\n**输入：** code = [\"GROCERY15\",\"ELECTRONICS_50\",\"DISCOUNT10\"], businessLine = [\"grocery\",\"electronics\",\"invalid\"], isActive = [false,true,true]\n\n**输出：** [\"ELECTRONICS_50\"]\n\n**解释：**\n\n- 第一个优惠券无效，因为它未激活。\n- 第二个优惠券有效。\n- 第三个优惠券无效，因为其业务类别无效。\n\n \n\n**提示：**\n\n- `n == code.length == businessLine.length == isActive.length`\n- `1 <= n <= 100`\n- `0 <= code[i].length, businessLine[i].length <= 100`\n- `code[i]` 和 `businessLine[i]` 由可打印的 ASCII 字符组成。\n- `isActive[i]` 的值为 `true` 或 `false`。"
                         )

    def solve(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        BUSINESS_LINE_TO_CATEGORY = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3,
        }

        groups: list[list[str]] = [[] for _ in range(4)]
        for s, bus, active in zip(code, businessLine, isActive):
            category = BUSINESS_LINE_TO_CATEGORY.get(bus, -1)
            if s and category >= 0 and active and \
                    all(c == '_' or c.isalnum() for c in s):
                groups[category].append(s)  # 相同类别的优惠码分到同一组

        ans = []
        for g in groups:
            g.sort()  # 每一组内部排序
            ans += g
        return ans

    def _gen(self) -> Tuple[List[str], List[str], List[bool]]:
        n = _generate_int(1, 100)  # 数组长度 1~100

        # 合法的业务类别
        valid_business_lines = ["electronics", "grocery", "pharmacy", "restaurant"]
        # 字母数字 + 下划线，用于生成合法的 code
        alphanumeric_underscore = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
        # 包含一些非法字符（如 @、空格等），用于生成非法 code
        printable_ascii_but_invalid = alphanumeric_underscore + "!@#$%^&*()-+=[]{}|;:,.<>?"

        code = []
        businessLine = []
        isActive = []

        for _ in range(n):
            # 随机决定是否生成一个有效的优惠券（控制整体有效性分布）
            is_valid_coupon = random.random() < 0.6  # 60% 概率尝试构造有效优惠券

            # === 生成 code[i] ===
            if is_valid_coupon and random.random() < 0.8:  # 大概率给有效优惠券一个合法 code
                if random.random() < 0.3:  # 30% 概率为空（但只在不追求有效时才允许）
                    c = ""
                else:
                    c = _generate_string(alphanumeric_underscore, (1, 20))
            else:
                # 生成可能非法的 code：空、含特殊字符、或合法但配合其他条件无效
                choice = random.random()
                if choice < 0.3:
                    c = ""
                elif choice < 0.6:
                    c = _generate_string("!@#$%^&*", (1, 20))  # 特殊字符为主
                elif choice < 0.8:
                    c = _generate_string(alphanumeric_underscore, (0, 1))  # 可能为空
                else:
                    # 生成一个看似合法的 code（字母数字下划线），但通过其他字段使其整体无效
                    c = _generate_string(alphanumeric_underscore, (1, 20))
            code.append(c)

            # === 生成 businessLine[i] ===
            if is_valid_coupon and random.random() < 0.8:
                b = random.choice(valid_business_lines)
            else:
                # 70% 概率使用非法类别
                if random.random() < 0.7:
                    invalid_choices = ["fashion", "travel", "invalid", "books", ""]
                    b = random.choice(invalid_choices)
                else:
                    b = random.choice(valid_business_lines)
            businessLine.append(b)

            # === 生成 isActive[i] ===
            if is_valid_coupon and random.random() < 0.8:
                a = True
            else:
                a = _generate_bool()
            isActive.append(a)

        return code, businessLine, isActive

from math import inf

class Solution2(Testing):
    date = "2025-7-6"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3607,
                         types=[ProblemType.DeepFirstSearch, ProblemType.BreadthFirstSearch, ProblemType.DisjointSet,
                                ProblemType.Graph, ProblemType.Array, ProblemType.HashTable, ProblemType.OrderedSet,
                                ProblemType.Heap],
                         pass_rate=0.422,
                         problem_slug="power-grid-maintenance",
                         callable_name="processQueries",
                         description="给你一个整数 `c`，表示 `c` 个电站，每个电站有一个唯一标识符 `id`，从 1 到 `c` 编号。\n\n这些电站通过 `n` 条 **双向** 电缆互相连接，表示为一个二维数组 `connections`，其中每个元素 `connections[i] = [ui, vi]` 表示电站 `ui` 和电站 `vi` 之间的连接。直接或间接连接的电站组成了一个 **电网** 。\n\n最初，**所有** 电站均处于在线（正常运行）状态。\n\n另给你一个二维数组 `queries`，其中每个查询属于以下 **两种类型之一** ：\n\n- `[1, x]`：请求对电站 `x` 进行维护检查。如果电站 `x` 在线，则它自行解决检查。如果电站 `x` 已离线，则检查由与 `x` 同一 **电网** 中 **编号最小** 的在线电站解决。如果该电网中 **不存在** 任何 **在线** 电站，则返回 -1。\n- `[2, x]`：电站 `x` 离线（即变为非运行状态）。\n\n返回一个整数数组，表示按照查询中出现的顺序，所有类型为 `[1, x]` 的查询结果。\n\n**注意：**电网的结构是固定的；离线（非运行）的节点仍然属于其所在的电网，且离线操作不会改变电网的连接性。\n\n \n\n**示例 1：**\n\n**输入：** c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]\n\n**输出：** [3,2,3]\n\n**解释：**\n\n![img](https://assets.leetcode.com/uploads/2025/04/15/powergrid.jpg)\n\n- 最初，所有电站 `{1, 2, 3, 4, 5}` 都在线，并组成一个电网。\n- 查询 `[1,3]`：电站 3 在线，因此维护检查由电站 3 自行解决。\n- 查询 `[2,1]`：电站 1 离线。剩余在线电站为 `{2, 3, 4, 5}`。\n- 查询 `[1,1]`：电站 1 离线，因此检查由电网中编号最小的在线电站解决，即电站 2。\n- 查询 `[2,2]`：电站 2 离线。剩余在线电站为 `{3, 4, 5}`。\n- 查询 `[1,2]`：电站 2 离线，因此检查由电网中编号最小的在线电站解决，即电站 3。\n\n**示例 2：**\n\n**输入：** c = 3, connections = [], queries = [[1,1],[2,1],[1,1]]\n\n**输出：** [1,-1]\n\n**解释：**\n\n- 没有连接，因此每个电站是一个独立的电网。\n- 查询 `[1,1]`：电站 1 在线，且属于其独立电网，因此维护检查由电站 1 自行解决。\n- 查询 `[2,1]`：电站 1 离线。\n- 查询 `[1,1]`：电站 1 离线，且其电网中没有其他电站，因此结果为 -1。\n\n \n\n**提示：**\n\n- `1 <= c <= 105`\n- `0 <= n == connections.length <= min(105, c * (c - 1) / 2)`\n- `connections[i].length == 2`\n- `1 <= ui, vi <= c`\n- `ui != vi`\n- `1 <= queries.length <= 2 * 105`\n- `queries[i].length == 2`\n- `queries[i][0]` 为 1 或 2。\n- `1 <= queries[i][1] <= c`"
                         )

    def solve(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        g: list[list[int]] = [[] for _ in range(c + 1)]
        x: int
        y: int
        for x, y in connections:
            g[x].append(y)
            g[y].append(x)

        belong = [-1] * (c + 1)
        cc = 0  # 连通块编号

        def dfs(x: int) -> None:
            belong[x] = cc  # 记录节点 x 在哪个连通块
            for y in g[x]:
                if belong[y] < 0:
                    dfs(y)

        for i in range(1, c + 1):
            if belong[i] < 0:
                dfs(i)
                cc += 1

        # 记录每个节点的离线时间，初始为无穷大（始终在线）
        offline_time = [inf] * (c + 1)
        for i in range(len(queries) - 1, -1, -1):
            t, x = queries[i]
            if t == 2:
                offline_time[x] = i  # 记录离线时间

        # 每个连通块中仍在线的电站的最小编号
        mn = [inf] * cc
        for i in range(1, c + 1):
            if offline_time[i] == inf:  # 最终仍在线
                j = belong[i]
                mn[j] = min(mn[j], i)

        ans = []
        for i in range(len(queries) - 1, -1, -1):
            t, x = queries[i]
            j = belong[x]
            if t == 2:
                if offline_time[x] == i:
                    mn[j] = min(mn[j], x)  # 变回在线
            elif i < offline_time[x]:  # 已经在线（写 < 或者 <= 都可以）
                ans.append(x)
            elif mn[j] != inf:
                ans.append(mn[j])
            else:
                ans.append(-1)
        ans.reverse()
        return ans

    def _gen(self) -> Tuple[int, List[List[int]], List[List[int]]]:
        # 第一步：生成电站数量 c
        c = _generate_int(1, 100)

        # 第二步：生成连接数 n
        max_possible_edges = c * (c - 1) // 2
        n = _generate_int(0, min(100, max_possible_edges))  # 实际生成的边数

        # === 修复：生成所有可能的边，再随机选 n 条 ===
        all_edges = []
        for u in range(1, c + 1):
            for v in range(u + 1, c + 1):
                all_edges.append([u, v])

        random.shuffle(all_edges)
        selected_edges = all_edges[:n]

        # 使用并查集来构建 connections（可选：是否保持连通性？这里直接返回 selected_edges）
        # 但注意：题目不要求图连通，所以可以直接返回
        connections = selected_edges

        # 第三步：生成 queries
        num_queries = _generate_int(1, 200)
        queries = []
        for _ in range(num_queries):
            op_type = _generate_int(1, 2)
            x = _generate_int(1, c)
            queries.append([op_type, x])

        return c, connections, queries


class Solution3(Testing):
    date = "2025-7-6"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3608,
                         types=[ProblemType.DisjointSet, ProblemType.Graph, ProblemType.Bisearch, ProblemType.Sorting],
                         pass_rate=0.535,
                         description="给你一个整数 `n`，表示一个包含 `n` 个节点（从 0 到 `n - 1` 编号）的无向图。该图由一个二维数组 `edges` 表示，其中 `edges[i] = [ui, vi, timei]` 表示一条连接节点 `ui` 和节点 `vi` 的无向边，该边会在时间 `timei` 被移除。\n\n同时，另给你一个整数 `k`。\n\n最初，图可能是连通的，也可能是非连通的。你的任务是找到一个 **最小** 的时间 `t`，使得在移除所有满足条件 `time <= t` 的边之后，该图包含 **至少** `k` 个连通分量。\n\n返回这个 **最小** 时间 `t`。\n\n**连通分量** 是图的一个子图，其中任意两个顶点之间都存在路径，且子图中的任意顶点均不与子图外的顶点共享边。\n\n \n\n**示例 1：**\n\n**输入：** n = 2, edges = [[0,1,3]], k = 2\n\n**输出：** 3\n\n**解释：**\n\n\n- 最初，图中有一个连通分量 `{0, 1}`。\n- 在 `time = 1` 或 `2` 时，图保持不变。\n- 在 `time = 3` 时，边 `[0, 1]` 被移除，图中形成 `k = 2` 个连通分量：`{0}` 和 `{1}`。因此，答案是 3。\n\n**示例 2：**\n\n**输入：** n = 3, edges = [[0,1,2],[1,2,4]], k = 3\n\n**输出：** 4\n\n**解释：**\n\n- 最初，图中有一个连通分量 `{0, 1, 2}`。\n- 在 `time = 2` 时，边 `[0, 1]` 被移除，图中形成两个连通分量：`{0}` 和 `{1, 2}`。\n- 在 `time = 4` 时，边 `[1, 2]` 被移除，图中形成 `k = 3` 个连通分量：`{0}`、`{1}` 和 `{2}`。因此，答案是 4。\n\n**示例 3：**\n\n**输入：** n = 3, edges = [[0,2,5]], k = 2\n\n**输出：** 0\n\n**解释：**\n\n- 由于图中已经存在 `k = 2` 个连通分量 `{1}` 和 `{0, 2}`，无需移除任何边。因此，答案是 0。\n\n \n\n**提示：**\n\n- `1 <= n <= 105`\n- `0 <= edges.length <= 105`\n- `edges[i] = [ui, vi, timei]`\n- `0 <= ui, vi < n`\n- `ui != vi`\n- `1 <= timei <= 109`\n- `1 <= k <= n`\n- 不存在重复的边。"
                         )

    def solve(self, n: int, edges: List[List[int]], k: int) -> int:
        edges.sort(key=lambda e: -e[2])  # 按照 time 降序排列

        u = UnionFind(n)
        x: int
        y: int
        t: int
        for x, y, t in edges:
            u.merge(x, y)
            if u.cc < k:  # 这条边不能留，即移除所有 time <= t 的边
                return t
        return 0  # 无需移除任何边

    def _gen(self) -> Tuple[int, list[int, int, int], int]:
        n = _generate_int(int_min=1)
        edges = _construct_graph(n, _generate_int(0, n * (n - 1) // 2))
        edges = [[edge[0], edge[1], _generate_int()] for edge in edges]
        k = _generate_int(1, n)
        return n, edges, k


class Solution4(Testing):
    date = "2025-7-6"
    def __init__(self):
        Testing.__init__(self,
                         degree=2,
                         idx=3609,
                         types=[ProblemType.Math],
                         pass_rate=0.294,
                         description="给你四个整数 `sx`、`sy`、`tx` 和 `ty`，表示在一个无限大的二维网格上的两个点 `(sx, sy)` 和 `(tx, ty)`。\n\n你的起点是 `(sx, sy)`。\n\n在任何位置 `(x, y)`，定义 `m = max(x, y)`。你可以执行以下两种操作之一：\n\n- 移动到 `(x + m, y)`，或者\n- 移动到 `(x, y + m)`。\n\n返回到达 `(tx, ty)` 所需的 **最小** 移动次数。如果无法到达目标点，则返回 -1。\n\n \n\n**示例 1：**\n\n**输入：** sx = 1, sy = 2, tx = 5, ty = 4\n\n**输出：** 2\n\n**解释：**\n\n最优路径如下：\n\n- 移动 1：`max(1, 2) = 2`。增加 y 坐标 2，从 `(1, 2)` 移动到 `(1, 2 + 2) = (1, 4)`。\n- 移动 2：`max(1, 4) = 4`。增加 x 坐标 4，从 `(1, 4)` 移动到 `(1 + 4, 4) = (5, 4)`。\n\n因此，到达 `(5, 4)` 的最小移动次数是 2。\n\n**示例 2：**\n\n**输入：** sx = 0, sy = 1, tx = 2, ty = 3\n\n**输出：** 3\n\n**解释：**\n\n最优路径如下：\n\n- 移动 1：`max(0, 1) = 1`。增加 x 坐标 1，从 `(0, 1)` 移动到 `(0 + 1, 1) = (1, 1)`。\n- 移动 2：`max(1, 1) = 1`。增加 x 坐标 1，从 `(1, 1)` 移动到 `(1 + 1, 1) = (2, 1)`。\n- 移动 3：`max(2, 1) = 2`。增加 y 坐标 2，从 `(2, 1)` 移动到 `(2, 1 + 2) = (2, 3)`。\n\n因此，到达 `(2, 3)` 的最小移动次数是 3。\n\n**示例 3：**\n\n**输入：** sx = 1, sy = 1, tx = 2, ty = 2\n\n**输出：** -1\n\n**解释：**\n\n- 无法通过题中允许的移动方式从 `(1, 1)` 到达 `(2, 2)`。因此，答案是 -1。\n\n \n\n**提示：**\n\n- `0 <= sx <= tx <= 109`\n- `0 <= sy <= ty <= 109`"
                         )

    def solve(self, sx: int, sy: int, x: int, y: int) -> int:
        ans = 0
        while x != sx or y != sy:
            if x < sx or y < sy:
                return -1
            ans += 1
            if x == y:
                if sy > 0:
                    x = 0
                else:
                    y = 0
                continue
            # 保证 x > y
            if x < y:
                x, y = y, x
                sx, sy = sy, sx
            if x > y * 2:
                if x % 2 > 0:
                    return -1
                x //= 2
            else:
                x -= y
        return ans

    def _gen(self) -> Tuple[int, int, int, int]:
        sx = _generate_int()
        sy = _generate_int()
        tx = _generate_int(int_min=sx)
        ty = _generate_int(int_min=sy)
        return sx, sy, tx, ty