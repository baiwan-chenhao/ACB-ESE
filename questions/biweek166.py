import string
from collections import defaultdict, Counter
from functools import cache
from . import Problem as Testing
from typing import List


class Solution1(Testing):
    date = "2025-9-27"
    def __init__(self):
        Testing.__init__(self,
                         degree=0,
                         idx=3692,
                         types=[],
                         pass_rate=0.666,
                         description="给你一个由小写英文字母组成的字符串 `s`。\n\n对于一个值 `k`，**频率组** 是在 `s` 中恰好出现 `k` 次的字符集合。\n\n**众数频率组** 是包含 **不同** 字符数量最多的频率组。\n\n返回一个字符串，包含众数频率组中的所有字符，字符的顺序 **不限** 。如果两个或多个频率组的大小并列最大，则选择其频率 `k` **较大** 的那个组。\n\n \n\n**示例 1:**\n\n**输入:** s = \"aaabbbccdddde\"\n\n**输出:** \"ab\"\n\n**解释:**\n\n| 频率 (k) | 组中不同字符 | 组大小 | 是否众数? |\n| -------- | ------------ | ------ | --------- |\n| 4        | {d}          | 1      | 否        |\n| 3        | {a, b}       | 2      | **是**    |\n| 2        | {c}          | 1      | 否        |\n| 1        | {e}          | 1      | 否        |\n\n字符 `'a'` 和 `'b'` 的频率相同，都为 3，它们在众数频率组中。\n\n**示例 2:**\n\n**输入:** s = \"abcd\"\n\n**输出:** \"abcd\"\n\n**解释:**\n\n| 频率 (k) | 组中不同字符 | 组大小 | 是否众数? |\n| -------- | ------------ | ------ | --------- |\n| 1        | {a, b, c, d} | 4      | **是**    |\n\n所有字符的频率都相同，都为 1，它们都在众数频率组中。\n\n**示例 3:**\n\n**输入:** s = \"pfpfgi\"\n\n**输出:** \"fp\"\n\n**解释:**\n\n| 频率 (k) | 组中不同字符 | 组大小 | 是否众数?                             |\n| -------- | ------------ | ------ | ------------------------------------- |\n| 2        | {p, f}       | 2      | **是**                                |\n| 1        | {g, i}       | 2      | 否 (组大小并列，选择频率更大的 k = 2) |\n\n字符 `'p'` 和 `'f'` 的频率相同，都为 2，它们在众数频率组中。频率为 1 的组大小并列，但我们选择频率更高的组 2。\n\n \n\n**提示:**\n\n- `1 <= s.length <= 100`\n- `s` 只包含小写英文字母。"
                         )

    def solve(self, s: str) -> str:
        cnt = Counter(s)
        groups = defaultdict(list)
        k = 0
        for ch, cnt in cnt.items():
            groups[cnt].append(ch)
            if (len(groups[cnt]), cnt) > (len(groups[k]), k):
                k = cnt
        return ''.join(groups[k])

    def gen(self):
        return self.generate_string(vocab=string.ascii_lowercase),


class Solution2(Testing):
    date = "2025-9-27"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3693,
                         types=[],
                         pass_rate=0.727,
                         description="你正在爬一个有 `n + 1` 级台阶的楼梯，台阶编号从 `0` 到 `n`。\n\n你还得到了一个长度为 `n` 的 **下标从 1 开始** 的整数数组 `costs`，其中 `costs[i]` 是第 `i` 级台阶的成本。\n\n从第 `i` 级台阶，你 **只能** 跳到第 `i + 1`、`i + 2` 或 `i + 3` 级台阶。从第 `i` 级台阶跳到第 `j` 级台阶的成本定义为： `costs[j] + (j - i)2`\n\n你从第 0 级台阶开始，初始 `cost = 0`。\n\n返回到达第 `n` 级台阶所需的 **最小** 总成本。\n\n \n\n***\\*示例 1:\\****\n\n**输入：**n = 4, costs = [1,2,3,4]\n\n**输出：**13\n\n**解释：**\n\n一个最优路径是 `0 → 1 → 2 → 4`\n\n| 跳跃  | 成本计算                      | 成本 |\n| ----- | ----------------------------- | ---- |\n| 0 → 1 | `costs[1] + (1 - 0)2 = 1 + 1` | 2    |\n| 1 → 2 | `costs[2] + (2 - 1)2 = 2 + 1` | 3    |\n| 2 → 4 | `costs[4] + (4 - 2)2 = 4 + 4` | 8    |\n\n因此，最小总成本为 `2 + 3 + 8 = 13`\n\n***\\*示例 2:\\****\n\n**输入：**n = 4, costs = [5,1,6,2]\n\n**输出：**11\n\n**解释：**\n\n一个最优路径是 `0 → 2 → 4`\n\n| 跳跃  | 成本计算                      | 成本 |\n| ----- | ----------------------------- | ---- |\n| 0 → 2 | `costs[2] + (2 - 0)2 = 1 + 4` | 5    |\n| 2 → 4 | `costs[4] + (4 - 2)2 = 2 + 4` | 6    |\n\n因此，最小总成本为 `5 + 6 = 11`\n\n***\\*示例 3:\\****\n\n**输入：**n = 3, costs = [9,8,3]\n\n**输出：**12\n\n**解释：**\n\n最优路径是 `0 → 3`，总成本 = `costs[3] + (3 - 0)2 = 3 + 9 = 12`\n\n \n\n**提示:**\n\n- `1 <= n == costs.length <= 10**5`\n- `1 <= costs[i] <= 10**4`"
                         )

    def solve(self, n: int, costs: List[int]) -> int:
        @cache
        def dfs(i: int) -> int:
            if i == 0:
                return 0
            return min(dfs(j) + (i - j) * (i - j) for j in range(max(i - 3, 0), i)) + costs[i - 1]

        return dfs(n)

    def _gen(self):
        n = self.s_generate_int((1, 100))
        costs = self.s_generate_list_int(list_length_range=(n, n), int_range=(1, 100))
        return n, costs


DIRS = {
    'L': (-1, 0),
    'R': (1, 0),
    'D': (0, -1),
    'U': (0, 1),
}


class Solution3(Testing):
    date = "2025-9-27"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3694,
                         types=[],
                         pass_rate=0.573,
                         description="给你一个由字符 `'U'`、`'D'`、`'L'` 和 `'R'` 组成的字符串 `s`，表示在无限的二维笛卡尔网格上的移动。\n\n- `'U'`: 从 `(x, y)` 移动到 `(x, y + 1)`。\n- `'D'`: 从 `(x, y)` 移动到 `(x, y - 1)`。\n- `'L'`: 从 `(x, y)` 移动到 `(x - 1, y)`。\n- `'R'`: 从 `(x, y)` 移动到 `(x + 1, y)`。\n\n你还得到了一个正整数 `k`。\n\n你 **必须** 选择并移除 **恰好一个** 长度为 `k` 的连续子字符串 `s`。然后，从坐标 `(0, 0)` 开始，按顺序执行剩余的移动。\n\n返回可到达的 **不同** 最终坐标的数量。\n\n \n\n***\\*示例 1:\\****\n\n**输入：**s = \"LUL\", k = 1\n\n**输出：**2\n\n**解释：**\n\n移除长度为 1 的子字符串后，`s` 可以是 `\"UL\"`、`\"LL\"` 或 `\"LU\"`。执行这些移动后，最终坐标将分别是 `(-1, 1)`、`(-2, 0)` 和 `(-1, 1)`。有两个不同的点 `(-1, 1)` 和 `(-2, 0)`，因此答案是 2。\n\n***\\*示例 2:\\****\n\n**输入：**s = \"UDLR\", k = 4\n\n**输出：**1\n\n**解释：**\n\n移除长度为 4 的子字符串后，`s` 只能是空字符串。最终坐标将是 `(0, 0)`。只有一个不同的点 `(0, 0)`，因此答案是 1。\n\n***\\*示例 3:\\****\n\n**输入：**s = \"UU\", k = 1\n\n**输出：**1\n\n**解释：**\n\n移除长度为 1 的子字符串后，`s` 变为 `\"U\"`，它总是以 `(0, 1)` 结束，因此只有一个不同的最终坐标。\n\n \n\n**提示:**\n\n- `1 <= s.length <= 10**5`\n- `s` 只包含 `'U'`、`'D'`、`'L'` 和 `'R'`。\n- `1 <= k <= s.length`"
                         )

    def solve(self, s: str, k: int) -> int:
        st = {(0, 0)}  # 第一个窗口
        x = y = 0
        for i in range(k, len(s)):
            in_x, in_y = DIRS[s[i]]
            out_x, out_y = DIRS[s[i - k]]
            x += in_x - out_x
            y += in_y - out_y
            st.add((x, y))
        return len(st)


    def _gen(self):
        n = self.s_generate_int((1, 1000))
        s = self.s_generate_string(vocab="UDLR", length_range=(n, n))
        k = self.s_generate_int((1, n))
        return s, k



class UnionFind:
    def __init__(self, n: int):
        # 一开始有 n 个集合 {0}, {1}, ..., {n-1}
        # 集合 i 的代表元是自己
        self._fa = list(range(n))  # 代表元
        self.odd = [i % 2 for i in range(n)]  # 集合中的奇数个数
        self.cc = n  # 连通块个数

    # 返回 x 所在集合的代表元
    # 同时做路径压缩，也就是把 x 所在集合中的所有元素的 fa 都改成代表元
    def find(self, x: int) -> int:
        # 如果 fa[x] == x，则表示 x 是代表元
        fa = self._fa
        if fa[x] != x:
            fa[x] = self.find(fa[x])  # fa 改成代表元
        return fa[x]

    # 把 from 所在集合合并到 to 所在集合中
    def merge(self, from_: int, to: int) -> None:
        x, y = self.find(from_), self.find(to)
        if x == y:  # from 和 to 在同一个集合，不做合并
            return
        self._fa[x] = y  # 合并集合
        self.odd[y] += self.odd[x]  # 更新集合中的奇数个数


class Solution4(Testing):
    date = "2025-9-27"
    def __init__(self):
        Testing.__init__(self,
                         degree=2,
                         idx=3695,
                         types=[],
                         pass_rate=0.693,
                         description="给你一个整数数组 `nums`。\n\n你希望最大化 `nums` 的 **交替和**：将偶数下标的元素 **相加** 并 **减去** 奇数索引的元素获得的值。即 `nums[0] - nums[1] + nums[2] - nums[3]...`\n\n同时给你一个二维整数数组 `swaps`，其中 `swaps[i] = [pi, qi]`。对于 `swaps` 中的每对 `[pi, qi]`，你可以交换索引 `pi` 和 `qi` 处的元素。这些交换可以进行任意次数和任意顺序。\n\n返回 `nums` 可能的最大 **交替和**。\n\n \n\n***\\*示例 1:\\****\n\n**输入：**nums = [1,2,3], swaps = [[0,2],[1,2]]\n\n**输出：**4\n\n**解释：**\n\n当 `nums` 为 `[2, 1, 3]` 或 `[3, 1, 2]` 时，可以实现最大交替和。例如，你可以通过以下方式得到 `nums = [2, 1, 3]`。\n\n- 交换 `nums[0]` 和 `nums[2]`。此时 `nums` 为 `[3, 2, 1]`。\n- 交换 `nums[1]` 和 `nums[2]`。此时 `nums` 为 `[3, 1, 2]`。\n- 交换 `nums[0]` 和 `nums[2]`。此时 `nums` 为 `[2, 1, 3]`。\n\n***\\*示例 2:\\****\n\n**输入：**nums = [1,2,3], swaps = [[1,2]]\n\n**输出：**2\n\n**解释：**\n\n不进行任何交换即可实现最大交替和。\n\n***\\*示例 3:\\****\n\n**输入：**nums = [1,1000000000,1,1000000000,1,1000000000], swaps = []\n\n**输出：**-2999999997\n\n**解释：**\n\n由于我们不能进行任何交换，因此不进行任何交换即可实现最大交替和。\n\n \n\n**提示:**\n\n- `2 <= nums.length <= 105`\n- `1 <= nums[i] <= 109`\n- `0 <= swaps.length <= 105`\n- `swaps[i] = [pi, qi]`\n- `0 <= pi < qi <= nums.length - 1`\n- `[pi, qi] != [pj, qj]`"
                         )

    def solve(self, nums: List[int], swaps: List[List[int]]) -> int:
        uf = UnionFind(len(nums))
        for p, q in swaps:
            uf.merge(p, q)

        g = defaultdict(list)
        for i, x in enumerate(nums):
            g[uf.find(i)].append(x)  # 相同集合的元素分到同一组

        ans = 0
        for i, a in g.items():
            a.sort()
            odd = uf.odd[i]
            # 小的取负号，大的取正号
            ans += sum(a[odd:]) - sum(a[:odd])
        return ans


    def _gen(self):
        l = self.s_generate_int((2, 100))
        nums = self.s_generate_list_int(list_length_range=(l, l), int_range=(1, 100))
        swaps = self.s_generate_matrix(list_length_range1=(0, 100), list_length_range2=(2, 2), int_range=(0, l - 1))
        return nums, swaps

