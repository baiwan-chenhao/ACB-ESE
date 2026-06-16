import string

from . import Problem as Testing, ProblemType
from ..testcase_sampler import _generate_int, _generate_string, _construct_graph_connected
from typing import List, Tuple


class Solution1(Testing):
    date = "2025-7-13"

    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3612,
                         types=[ProblemType.String, ProblemType.Simulation],
                         pass_rate=0.656,
                         description="给你一个字符串 `s`，它由小写英文字母和特殊字符：`*`、`#` 和 `%` 组成。\n\n请根据以下规则从左到右处理 `s` 中的字符，构造一个新的字符串 `result`：\n\n- 如果字符是 **小写** 英文字母，则将其添加到 `result` 中。\n- 字符 `'*'` 会 **删除** `result` 中的最后一个字符（如果存在）。\n- 字符 `'#'` 会 **复制** 当前的 `result` 并 **追加** 到其自身后面。\n- 字符 `'%'` 会 **反转** 当前的 `result`。\n\n在处理完 `s` 中的所有字符后，返回最终的字符串 `result`。\n\n \n\n**示例 1：**\n\n**输入：** s = \"a#b%*\"\n\n**输出：** \"ba\"\n\n**解释：**\n\n| `i`  | `s[i]` | 操作             | 当前 `result` |\n| ---- | ------ | ---------------- | ------------- |\n| 0    | `'a'`  | 添加 `'a'`       | `\"a\"`         |\n| 1    | `'#'`  | 复制 `result`    | `\"aa\"`        |\n| 2    | `'b'`  | 添加 `'b'`       | `\"aab\"`       |\n| 3    | `'%'`  | 反转 `result`    | `\"baa\"`       |\n| 4    | `'*'`  | 删除最后一个字符 | `\"ba\"`        |\n\n因此，最终的 `result` 是 `\"ba\"`。\n\n**示例 2：**\n\n**输入：** s = \"z*#\"\n\n**输出：** \"\"\n\n**解释：**\n\n| `i`  | `s[i]` | 操作             | 当前 `result` |\n| ---- | ------ | ---------------- | ------------- |\n| 0    | `'z'`  | 添加 `'z'`       | `\"z\"`         |\n| 1    | `'*'`  | 删除最后一个字符 | `\"\"`          |\n| 2    | `'#'`  | 复制字符串       | `\"\"`          |\n\n因此，最终的 `result` 是 `\"\"`。\n\n \n\n**提示:**\n\n- `1 <= s.length <= 20`\n- `s` 只包含小写英文字母和特殊字符 `*`、`#` 和 `%`。"
                         )

    def solve(self, s: str) -> str:
        ans = []
        for c in s:
            if c == '*':
                if ans:
                    ans.pop()
            elif c == '#':
                ans += ans
            elif c == '%':
                ans.reverse()
            else:
                ans.append(c)
        return ''.join(ans)

    def gen(self):
        return self.generate_string(vocab=string.ascii_lowercase + "*#%", length_range=(1, 100)),


class UnionFind:
    def __init__(self, n: int):
        # 一开始有 n 个集合 {0}, {1}, ..., {n-1}
        # 集合 i 的代表元是自己
        self._fa = list(range(n))  # 代表元
        self.cc = n  # 连通块个数

    # 返回 x 所在集合的代表元
    # 同时做路径压缩，也就是把 x 所在集合中的所有元素的 fa 都改成代表元
    def find(self, x: int) -> int:
        # 如果 fa[x] == x，则表示 x 是代表元
        if self._fa[x] != x:
            self._fa[x] = self.find(self._fa[x])  # fa 改成代表元
        return self._fa[x]

    # 把 from 所在集合合并到 to 所在集合中
    def merge(self, from_: int, to: int) -> None:
        x, y = self.find(from_), self.find(to)
        if x == y:  # from 和 to 在同一个集合，不做合并
            return
        self._fa[x] = y  # 合并集合。修改后就可以认为 from 和 to 在同一个集合了
        self.cc -= 1  # 成功合并，连通块个数减一


class Solution2(Testing):
    date = "2025-7-13"

    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3613,
                         pass_rate=0.428,
                         types=[ProblemType.Sorting, ProblemType.DisjointSet, ProblemType.Graph, ProblemType.Bisearch],
                         description="给你一个无向连通图，包含 `n` 个节点，节点编号从 0 到 `n - 1`，以及一个二维整数数组 `edges`，其中 `edges[i] = [ui, vi, wi]` 表示一条连接节点 `ui` 和节点 `vi` 的无向边，边权为 `wi`，另有一个整数 `k`。\n\n你可以从图中移除任意数量的边，使得最终的图中 **最多** 只包含 `k` 个连通分量。\n\n连通分量的 **成本** 定义为该分量中边权的 **最大值** 。如果一个连通分量没有边，则其代价为 0。\n\n请返回在移除这些边之后，在所有连通分量之中的 **最大成本** 的 **最小可能值** 。\n\n \n\n**示例 1：**\n\n**输入：** n = 5, edges = [[0,1,4],[1,2,3],[1,3,2],[3,4,6]], k = 2\n\n**输出：** 4\n\n**解释：**\n\n- 移除节点 3 和节点 4 之间的边（权值为 6）。\n- 最终的连通分量成本分别为 0 和 4，因此最大代价为 4。\n\n**示例 2：**\n\n**输入：** n = 4, edges = [[0,1,5],[1,2,5],[2,3,5]], k = 1\n\n**输出：** 5\n\n**解释：**\n\n- 无法移除任何边，因为只允许一个连通分量（`k = 1`），图必须保持完全连通。\n- 该连通分量的成本等于其最大边权，即 5。\n\n \n\n**提示：**\n\n- `1 <= n <= 5 * 104`\n- `0 <= edges.length <= 105`\n- `edges[i].length == 3`\n- `0 <= ui, vi < n`\n- `1 <= wi <= 106`\n- `1 <= k <= n`\n- 输入图是连通图。"
                         )

        self.unionFind = None
        self.count = None

    def solve(self, n: int, edges: list[list[int]], k: int) -> int:
        def findFather(n: int) -> int:
            curr = n
            while unionFind[curr] != curr:
                curr = unionFind[curr]

            ## 这里需要进行路径压缩，不然会导致后续的遍历非常耗时，从而超时
            f = curr
            curr = n
            while unionFind[curr] != curr:
                tmp = unionFind[curr]
                unionFind[curr] = f
                curr = tmp
            return f

        if k == n:
            return 0

        unionFind = [i for i in range(n)]
        count = n
        edges.sort(key=lambda e: e[2])

        for edge in edges:
            f1 = findFather(edge[0])
            f2 = findFather(edge[1])
            if f1 != f2:
                unionFind[f2] = f1
                count -= 1
            if count == k:
                return edge[2]

        return 0

    def _gen(self) -> Tuple[int, List[List[int]], int]:
        n = _generate_int(1, 100)
        edges = _construct_graph_connected(n)
        edges = [[e[0], e[1], _generate_int(1, 1000)] for e in edges]
        k = _generate_int(1, n)
        return n, edges, k


class Solution3(Testing):
    date = "2025-7-13"

    def __init__(self):
        Testing.__init__(self,
                         degree=2,
                         idx=3614,
                         pass_rate=0.351,
                         types=[ProblemType.String, ProblemType.Simulation],
                         description="给你一个字符串 `s`，由小写英文字母和特殊字符：`'*'`、`'#'` 和 `'%'` 组成。\n\n同时给你一个整数 `k`。\n\n请根据以下规则从左到右处理 `s` 中每个字符，构造一个新的字符串 `result`：\n\n- 如果字符是 **小写** 英文字母，则将其添加到 `result` 中。\n- 字符 `'*'` 会 **删除** `result` 中的最后一个字符（如果存在）。\n- 字符 `'#'` 会 **复制** 当前的 `result` 并**追加**到其自身后面。\n- 字符 `'%'` 会 **反转** 当前的 `result`。\n\n返回最终字符串 `result` 中第 `k` 个字符（下标从 0 开始）。如果 `k` 超出 `result` 的下标索引范围，则返回 `'.'`。\n\n \n\n**示例 1：**\n\n**输入：** s = \"a#b%*\", k = 1\n\n**输出：** \"a\"\n\n**解释：**\n\n| `i`  | `s[i]` | 操作             | 当前 `result` |\n| ---- | ------ | ---------------- | ------------- |\n| 0    | `'a'`  | 添加 `'a'`       | `\"a\"`         |\n| 1    | `'#'`  | 复制 `result`    | `\"aa\"`        |\n| 2    | `'b'`  | 添加 `'b'`       | `\"aab\"`       |\n| 3    | `'%'`  | 反转 `result`    | `\"baa\"`       |\n| 4    | `'*'`  | 删除最后一个字符 | `\"ba\"`        |\n\n最终的 `result` 是 `\"ba\"`。下标为 `k = 1` 的字符是 `'a'`。\n\n**示例 2：**\n\n**输入：** s = \"cd%#*#\", k = 3\n\n**输出：** \"d\"\n\n**解释：**\n\n| `i`  | `s[i]` | 操作             | 当前 `result` |\n| ---- | ------ | ---------------- | ------------- |\n| 0    | `'c'`  | 添加 `'c'`       | `\"c\"`         |\n| 1    | `'d'`  | 添加 `'d'`       | `\"cd\"`        |\n| 2    | `'%'`  | 反转 `result`    | `\"dc\"`        |\n| 3    | `'#'`  | 复制 `result`    | `\"dcdc\"`      |\n| 4    | `'*'`  | 删除最后一个字符 | `\"dcd\"`       |\n| 5    | `'#'`  | 复制 `result`    | `\"dcddcd\"`    |\n\n最终的 `result` 是 `\"dcddcd\"`。下标为 `k = 3` 的字符是 `'d'`。\n\n**示例 3：**\n\n**输入：** s = \"z*#\", k = 0\n\n**输出：** \".\"\n\n**解释：**\n\n| `i`  | `s[i]` | 操作             | 当前 `result` |\n| ---- | ------ | ---------------- | ------------- |\n| 0    | `'z'`  | 添加 `'z'`       | `\"z\"`         |\n| 1    | `'*'`  | 删除最后一个字符 | `\"\"`          |\n| 2    | `'#'`  | 复制字符串       | `\"\"`          |\n\n最终的 `result` 是 `\"\"`。由于下标 `k = 0` 越界，输出为 `'.'`。\n\n \n\n**提示:**\n\n- `1 <= s.length <= 105`\n- `s` 只包含小写英文字母和特殊字符 `'*'`、`'#'` 和 `'%'`。\n- `0 <= k <= 1015`\n- 处理 `s` 后得到的 `result` 的长度不超过 `1015`。"
                         )

    def solve(self, s: str, k: int) -> str:
        n = len(s)
        size = [0] * n
        sz = 0
        for i, c in enumerate(s):
            if c == '*':
                sz = max(sz - 1, 0)
            elif c == '#':
                sz *= 2
            elif c != '%':  # c 是字母
                sz += 1
            size[i] = sz

        if k >= size[-1]:  # 下标越界
            return '.'

        # 迭代
        for i in range(n - 1, -1, -1):
            c = s[i]
            sz = size[i]
            if c == '#':
                if k >= sz // 2:  # k 在复制后的右半边
                    k -= sz // 2
            elif c == '%':
                k = sz - 1 - k  # 反转前的下标为 sz-1-k 的字母就是答案
            elif c != '*' and k == sz - 1:  # 找到答案
                return c

    def gen(self):
        return self.generate_string(vocab=string.ascii_lowercase + "*#%", length_range=(1, 100)), self.generate_int()


from collections import Counter
from functools import cache


class Solution4(Testing):
    date = "2025-7-13"

    def __init__(self):
        Testing.__init__(self,
                         testcase_num=14,
                         degree=2,
                         idx=3615,
                         pass_rate=0.392,
                         types=[ProblemType.Bit, ProblemType.Graph, ProblemType.String, ProblemType.DynamicPlanning,
                                ProblemType.StateCompression],
                         description="给你一个整数 `n` 和一个包含 `n` 个节点的 **无向图** ，节点编号从 0 到 `n - 1`，以及一个二维数组 `edges`，其中 `edges[i] = [ui, vi]` 表示节点 `ui` 和节点 `vi` 之间有一条边。\n\n同时给你一个长度为 `n` 的字符串 `label`，其中 `label[i]` 是与节点 `i` 关联的字符。\n\n你可以从任意节点开始，移动到任意相邻节点，每个节点 **最多** 访问一次。\n\n返回通过访问一条路径，路径中 **不包含重复** 节点，所能形成的 **最长回文串** 的长度。\n\n**回文串** 是指正着读和反着读相同的字符串。\n\n \n\n**示例 1：**\n\n**输入：** n = 3, edges = [[0,1],[1,2]], label = \"aba\"\n\n**输出：** 3\n\n**解释：**\n\n- 最长的回文路径是从节点 0 到节点 2，经过节点 1，路径为 `0 → 1 → 2`，形成字符串 `\"aba\"`。\n- 这是一个长度为 3 的回文串。\n\n**示例 2：**\n\n**输入：** n = 3, edges = [[0,1],[0,2]], label = \"abc\"\n\n**输出：** 1\n\n**解释：**\n\n- 没有超过一个节点的路径可以形成回文串。\n- 最好的选择是任意一个单独的节点，构成长度为 1 的回文串。\n\n**示例 3：**\n\n**输入：** n = 4, edges = [[0,2],[0,3],[3,1]], label = \"bbac\"\n\n**输出：** 3\n\n**解释：**\n\n- 最长的回文路径是从节点 0 到节点 1，经过节点 3，路径为 `0 → 3 → 1`，形成字符串 `\"bcb\"`。\n- 这是一个有效的回文串，长度为 3。\n\n \n\n**提示:**\n\n- `1 <= n <= 14`\n- `n - 1 <= edges.length <= n * (n - 1) / 2`\n- `edges[i] == [ui, vi]`\n- `0 <= ui, vi <= n - 1`\n- `ui != vi`\n- `label.length == n`\n- `label` 只包含小写英文字母。\n- 不存在重复边。"
                         )

    def solve(self, n: int, edges: list[list[int]], label: str) -> int:
        # 手写 max 更快
        max = lambda a, b: b if b > a else a
        # 计算理论最大值
        odd = sum(c % 2 for c in Counter(label).values())
        theoretical_max: int = n - max(odd - 1, 0)  # 奇数选一个放正中心，其余全弃

        if len(edges) == n * (n - 1) // 2:  # 完全图，可以达到理论最大值
            return theoretical_max

        g: list[list[int]] = [[] for _ in range(n)]
        x: int
        y: int
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        # 计算从 x 和 y 向两侧扩展，最多还能访问多少个节点（不算 x 和 y）
        @cache
        def dfs(x: int, y: int, vis: int) -> int:
            res = 0
            for v in g[x]:
                if vis >> v & 1:
                    continue
                for w in g[y]:
                    if vis >> w & 1 == 0 and v != w and label[w] == label[v]:
                        tv, tw = v, w  # 注意不能直接交换 v 和 w，否则下个循环的 v 就不是原来的 v 了
                        if tv > tw:  # 保证 tv < tw，减少状态个数和计算量
                            tv, tw = tw, tv
                        res = max(res, dfs(tv, tw, vis | 1 << v | 1 << w) + 2)
            return res

        ans = 0
        for x, to in enumerate(g):
            # 奇回文串，x 作为回文中心
            ans = max(ans, dfs(x, x, 1 << x) + 1)
            if ans == theoretical_max:
                return ans
            # 偶回文串，x 和 x 的邻居 y 作为回文中心
            for y in to:
                # 保证递归参数 x < y，减少状态个数和计算量
                if x < y and label[x] == label[y]:
                    ans = max(ans, dfs(x, y, 1 << x | 1 << y) + 2)
                    if ans == theoretical_max:
                        return ans
        return ans

    def _gen(self):
        n = _generate_int(1, 14)
        edges = _construct_graph_connected(n)
        label = _generate_string(length_range=(n, n))
        return n, edges, label
