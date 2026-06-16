from . import Problem as Testing, ProblemType
from ..testcase_sampler import _generate_int, _generate_list_int
from typing import List


class Solution1(Testing):
    date = "2025-8-3"
    def __init__(self):
        Testing.__init__(self,
                         degree=0,
                         idx=3622,
                         types=[ProblemType.Math],
                         pass_rate=0.645,
                         description="给你一个正整数 `n`。请判断 `n` 是否可以被以下两值之和 **整除**：\n\n- `n` 的 **数字和**（即其各个位数之和）。\n- `n` 的 **数字积**（即其各个位数之积）。\n\n如果 `n` 能被该和整除，返回 `true`；否则，返回 `false`。\n\n \n\n**示例 1：**\n\n**输入：** n = 99\n\n**输出：** true\n\n**解释：**\n\n因为 99 可以被其数字和 (9 + 9 = 18) 与数字积 (9 * 9 = 81) 之和 (18 + 81 = 99) 整除，因此输出为 true。\n\n**示例 2：**\n\n**输入：** n = 23\n\n**输出：** false\n\n**解释：**\n\n因为 23 无法被其数字和 (2 + 3 = 5) 与数字积 (2 * 3 = 6) 之和 (5 + 6 = 11) 整除，因此输出为 false。\n\n \n\n**提示：**\n\n- `1 <= n <= 106`"
                         )

    def solve(self, n: int) -> bool:
        s, m = 0, 1
        x = n
        while x:
            d = x % 10
            x = x // 10
            s += d
            m *= d
        return n % (s + m) == 0

    def gen(self):
        return self.generate_int(int_range=(1, 1000000)),

from collections import Counter
class Solution2(Testing):
    date = "2025-8-3"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3623,
                         types=[ProblemType.Geometry, ProblemType.Array, ProblemType.HashTable, ProblemType.Math],
                         pass_rate=0.323,
                         description="给你一个二维整数数组 `points`，其中 `points[i] = [xi, yi]` 表示第 `i` 个点在笛卡尔平面上的坐标。\n\n**水平梯形** 是一种凸四边形，具有 **至少一对** 水平边（即平行于 x 轴的边）。两条直线平行当且仅当它们的斜率相同。\n\n返回可以从 `points` 中任意选择四个不同点组成的 **水平梯形** 数量。\n\n由于答案可能非常大，请返回结果对 `10**9 + 7` 取余数后的值。\n\n \n\n**示例 1：**\n\n**输入：** points = [[1,0],[2,0],[3,0],[2,2],[3,2]]\n\n**输出：** 3\n\n**解释：**\n\n有三种不同方式选择四个点组成一个水平梯形：\n\n- 使用点 `[1,0]`、`[2,0]`、`[3,2]` 和 `[2,2]`。\n- 使用点 `[2,0]`、`[3,0]`、`[3,2]` 和 `[2,2]`。\n- 使用点 `[1,0]`、`[3,0]`、`[3,2]` 和 `[2,2]`。\n\n**示例 2：**\n\n**输入：** points = [[0,0],[1,0],[0,1],[2,1]]\n\n**输出：** 1\n\n**解释：**\n\n只有一种方式可以组成一个水平梯形。\n\n \n\n**提示：**\n\n- `4 <= points.length <= 10**5`\n- `–10**8 <= xi, yi <= 10**8`\n- 所有点两两不同。"
                         )

    def solve(self, points: List[List[int]]) -> int:
        MOD = 1_000_000_007
        cnt: Counter[int] = Counter(p[1] for p in points)  # 统计每一行（水平线）有多少个点
        ans = s = 0
        for c in cnt.values():
            k = c * (c - 1) // 2
            ans += s * k
            s += k
        return ans % MOD

    def _gen(self):
        points = list()
        num = _generate_int(4, 1000)
        while len(points) < num:
            point = _generate_list_int(list_length_range=(2, 2), int_range=(-10000000, 1000000))
            if point not in points:
                points.append(point)
        return points,


class FenwickTree:
    def __init__(self, n: int):
        self.tree = [0] * (n + 1)  # 使用下标 1 到 n

    # a[i] 增加 val
    # 1 <= i <= n
    # 时间复杂度 O(log n)
    def update(self, i: int, val: int) -> None:
        while i < len(self.tree):
            self.tree[i] += val
            i += i & -i

    # 计算前缀和 a[1] + ... + a[i]
    # 1 <= i <= n
    # 时间复杂度 O(log n)
    def pre(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.tree[i]
            i &= i - 1
        return res

    # 计算区间和 a[l] + ... + a[r]
    # 1 <= l <= r <= n
    # 时间复杂度 O(log n)
    def query(self, l: int, r: int) -> int:
        return self.pre(r) - self.pre(l - 1)

# 不写记忆化，直接迭代
def pop_depth(x: int) -> int:
    res = 0
    while x > 1:
        res += 1
        x = x.bit_count()
    return res

class Solution3(Testing):
    date = "2025-8-3"
    def __init__(self):
        Testing.__init__(self,
                         degree=2,
                         idx=3624,
                         types=[ProblemType.TreeArray, ProblemType.SegmentTree, ProblemType.Array, ProblemType.DevideAndConquer],
                         pass_rate=0.445,
                         description="给你一个整数数组 `nums`。\n\n对于任意正整数 `x`，定义以下序列：\n\n- $p_0 = x$\n- $p_{i+1} = popcount(p_i)$，对于所有 `i >= 0`，其中 `popcount(y)` 表示整数 `y` 的二进制表示中 1 的个数。\n\n这个序列最终会收敛到值 1。\n\n**popcount-depth**（位计数深度）定义为满足 $p_d = 1$ 的最小整数 `d >= 0`。\n\n例如，当 `x = 7`（二进制表示为 `\"111\"`）时，该序列为：`7 → 3 → 2 → 1`，因此 7 的 popcount-depth 为 3。\n\n此外，给定一个二维整数数组 `queries`，其中每个 `queries[i]` 可以是以下两种类型之一：\n\n- `[1, l, r, k]` - **计算**在区间 `[l, r]` 中，满足 `nums[j]` 的 **popcount-depth** 等于 `k` 的索引 `j` 的数量。\n- `[2, idx, val]` - **将** `nums[idx]` 更新为 `val`。\n\n返回一个整数数组 `answer`，其中 `answer[i]` 表示第 `i` 个类型为 `[1, l, r, k]` 的查询的结果。\n\n \n\n**示例 1：**\n\n**输入：** nums = [2,4], queries = [[1,0,1,1],[2,1,1],[1,0,1,0]]\n\n**输出：** [2,1]\n\n**解释：**\n\n| `i`  | `queries[i]` | `nums` | binary(`nums`) | popcount- depth | `[l, r]` | `k`  | 有效 `nums[j]` | 更新后的 `nums` | 答案 |\n| ---- | ------------ | ------ | -------------- | --------------- | -------- | ---- | -------------- | --------------- | ---- |\n| 0    | [1,0,1,1]    | [2,4]  | [10, 100]      | [1, 1]          | [0, 1]   | 1    | [0, 1]         | —               | 2    |\n| 1    | [2,1,1]      | [2,4]  | [10, 100]      | [1, 1]          | —        | —    | —              | [2,1]           | —    |\n| 2    | [1,0,1,0]    | [2,1]  | [10, 1]        | [1, 0]          | [0, 1]   | 0    | [1]            | —               | 1    |\n\n因此，最终 `answer` 为 `[2, 1]`。\n\n**示例 2：**\n\n**输入：**nums = [3,5,6], queries = [[1,0,2,2],[2,1,4],[1,1,2,1],[1,0,1,0]]\n\n**输出：**[3,1,0]\n\n**解释：**\n\n| `i`  | `queries[i]` | `nums`    | binary(`nums`) | popcount- depth | `[l, r]` | `k`  | 有效 `nums[j]` | 更新后的 `nums` | 答案 |\n| ---- | ------------ | --------- | -------------- | --------------- | -------- | ---- | -------------- | --------------- | ---- |\n| 0    | [1,0,2,2]    | [3, 5, 6] | [11, 101, 110] | [2, 2, 2]       | [0, 2]   | 2    | [0, 1, 2]      | —               | 3    |\n| 1    | [2,1,4]      | [3, 5, 6] | [11, 101, 110] | [2, 2, 2]       | —        | —    | —              | [3, 4, 6]       | —    |\n| 2    | [1,1,2,1]    | [3, 4, 6] | [11, 100, 110] | [2, 1, 2]       | [1, 2]   | 1    | [1]            | —               | 1    |\n| 3    | [1,0,1,0]    | [3, 4, 6] | [11, 100, 110] | [2, 1, 2]       | [0, 1]   | 0    | []             | —               | 0    |\n\n因此，最终 `answer` 为 `[3, 1, 0]` 。\n\n**示例 3：**\n\n**输入：**nums = [1,2], queries = [[1,0,1,1],[2,0,3],[1,0,0,1],[1,0,0,2]]\n\n**输出：**[1,0,1]\n\n**解释：**\n\n| `i`  | `queries[i]` | `nums` | binary(`nums`) | popcount- depth | `[l, r]` | `k`  | 有效 `nums[j]` | 更新后的 `nums` | 答案 |\n| ---- | ------------ | ------ | -------------- | --------------- | -------- | ---- | -------------- | --------------- | ---- |\n| 0    | [1,0,1,1]    | [1, 2] | [1, 10]        | [0, 1]          | [0, 1]   | 1    | [1]            | —               | 1    |\n| 1    | [2,0,3]      | [1, 2] | [1, 10]        | [0, 1]          | —        | —    | —              | [3, 2]          |      |\n| 2    | [1,0,0,1]    | [3, 2] | [11, 10]       | [2, 1]          | [0, 0]   | 1    | []             | —               | 0    |\n| 3    | [1,0,0,2]    | [3, 2] | [11, 10]       | [2, 1]          | [0, 0]   | 2    | [0]            | —               | 1    |\n\n因此，最终 `answer` 为 `[1, 0, 1]` 。\n\n \n\n**提示：**\n\n- `1 <= n == nums.length <= 10**5`\n\n- `1 <= nums[i] <= 10**15`\n\n- `1 <= queries.length <= 10**5`\n\n- ```\n  queries[i].length == 3 or 4\n  ```\n\n  - `queries[i] == [1, l, r, k]` 或`queries[i] == [2, idx, val]`\n  - `0 <= l <= r <= n - 1`\n  - `0 <= k <= 5`\n  - `0 <= idx <= n - 1`\n  - `1 <= val <= 10**15`\n\n"
                         )

    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        f = [FenwickTree(n + 1) for _ in range(6)]

        def update(i: int, delta: int) -> None:
            d = pop_depth(nums[i])
            f[d].update(i + 1, delta)

        for i in range(n):
            update(i, 1)  # 添加

        ans = []
        for q in queries:
            if q[0] == 1:
                ans.append(f[q[3]].query(q[1] + 1, q[2] + 1))
            else:
                i = q[1]
                update(i, -1)  # 撤销旧的
                nums[i] = q[2]
                update(i, 1)  # 添加新的
        return ans


    def _gen(self):
        nums = _generate_list_int(list_length_range=(1, 1000), int_range=(1, 10000))
        n = len(nums)
        queries = list()
        for i in range(_generate_int(1, 100)):
            if _generate_int(1, 2) == 1:
                r = _generate_int(0, n - 1)
                l = _generate_int(0, r)
                k = _generate_int(0, 5)
                queries.append(
                    [1, l, r, k]
                )
            else:
                idx = _generate_int(0, n - 1)
                val = _generate_int(1, 100000)
                queries.append([
                    2, idx, val
                ])

        return nums, queries

from collections import defaultdict
from math import inf

class Solution4(Testing):
    date = "2025-8-3"
    def __init__(self):
        Testing.__init__(self,
                         degree=2,
                         idx=3625,
                         types=[ProblemType.Geometry, ProblemType.Array, ProblemType.HashTable, ProblemType.Math],
                         pass_rate=0.281,
                         description="给你一个二维整数数组 `points`，其中 `points[i] = [xi, yi]` 表示第 `i` 个点在笛卡尔平面上的坐标。\n\n返回可以从 `points` 中任意选择四个不同点组成的梯形的数量。\n\n**梯形** 是一种凸四边形，具有 **至少一对** 平行边。两条直线平行当且仅当它们的斜率相同。\n\n**示例 1：**\n\n**输入：** points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]\n\n**输出：** 2\n\n**解释：**\n\n有两种不同方式选择四个点组成一个梯形：\n\n- 点 `[-3,2], [2,3], [3,2], [2,-3]` 组成一个梯形。\n- 点 `[2,3], [3,2], [3,0], [2,-3]` 组成另一个梯形。\n\n**示例 2：**\n\n**输入：** points = [[0,0],[1,0],[0,1],[2,1]]\n\n**输出：** 1\n\n**解释：**\n\n只有一种方式可以组成一个梯形。\n\n**提示：**\n\n- `4 <= points.length <= 500`\n- `–1000 <= xi, yi <= 1000`\n- 所有点两两不同。"
                         )

    def solve(self, points: List[List[int]]) -> int:
        groups: dict[float, list[int]] = defaultdict(list)  # 斜率 -> [截距]
        groups2: dict[tuple[int, int], list[float]] = defaultdict(list)  # 中点 -> [斜率]

        for i, (x, y) in enumerate(points):
            for x2, y2 in points[:i]:
                dy = y - y2
                dx = x - x2
                k = dy / dx if dx else inf
                b = (y * dx - x * dy) / dx if dx else x
                groups[k].append(b)
                groups2[(x + x2, y + y2)].append(k)

        ans = 0
        for g in groups.values():
            if len(g) == 1:
                continue
            s = 0
            for c in Counter(g).values():
                ans += s * c
                s += c

        for g in groups2.values():
            if len(g) == 1:
                continue
            s = 0
            for c in Counter(g).values():
                ans -= s * c  # 平行四边形会统计两次，减去多统计的一次
                s += c

        return ans

    def _gen(self):
        points = list()
        num = _generate_int(4, 200)
        while len(points) < num:
            point = _generate_list_int(list_length_range=(2, 2), int_range=(-100, 100))
            if point not in points:
                points.append(point)
        return points,