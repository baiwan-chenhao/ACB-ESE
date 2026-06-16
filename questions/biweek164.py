from functools import cache
import sortedcontainers
from . import Problem as Testing, ProblemType
from typing import List, Tuple


class Solution1(Testing):
    date = "2025-8-30"
    def __init__(self):
        Testing.__init__(self,
                         degree=0,
                         idx=3663,
                         types=[ProblemType.Array, ProblemType.HashTable, ProblemType.Math, ProblemType.Counting],
                         pass_rate=0.709,
                         description="给你一个整数 `n`，找出在其十进制表示中出现频率 **最低** 的数字。如果多个数字的出现频率相同，则选择 **最小** 的那个数字。\n\n以整数形式返回所选的数字。\n\n数字 `x` 的出现频率是指它在 `n` 的十进制表示中的出现次数。\n\n \n\n**示例 1:**\n\n**输入：** n = 1553322\n\n**输出：** 1\n\n**解释：**\n\n在 `n` 中，出现频率最低的数字是 1，它只出现了一次。所有其他数字都出现了两次。\n\n**示例 2:**\n\n**输入：** n = 723344511\n\n**输出：** 2\n\n**解释：**\n\n在 `n` 中，出现频率最低的数字是 7、2 和 5，它们都只出现了一次。\n\n \n\n**提示:**\n\n- `1 <= n <= 2**31 - 1`"
                         )

    def solve(self, n: int) -> int:
        cnt = Counter(str(n))
        min_ch = min((c, ch) for ch, c in cnt.items())[1]
        return int(min_ch)

    def gen(self):
        return self.generate_int(int_range=(1, 1000000)),


from collections import Counter


class Solution2(Testing):
    date = "2025-8-30"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3664,
                         types=[ProblemType.Array, ProblemType.HashTable, ProblemType.String, ProblemType.Counting, ProblemType.Enum],
                         pass_rate=0.20,
                         description="给你一副由字符串数组 `cards` 表示的牌，每张牌上都显示两个小写字母。\n\n同时给你一个字母 `x`。你按照以下规则进行游戏：\n\n- 从 0 分开始。\n- 在每一轮中，你必须从牌堆中找到两张 **兼容的** 牌，这两张牌对应的字符串都包含字母 `x`。\n- 移除这对牌并获得 **1 分**。\n- 当你再也找不到兼容的牌对时，游戏结束。\n\n返回在最优策略下你能获得的 **最大** 分数。\n\n如果两张牌的字符串在 **恰好** 1 个位置上不同，则它们是**兼容的**。\n\n \n\n**示例 1:**\n\n**输入：** cards = [\"aa\",\"ab\",\"ba\",\"ac\"], x = \"a\"\n\n**输出：** 2\n\n**解释：**\n\n- 第一轮，选择并移除 `\"ab\"` 和 `\"ac\"`，它们是兼容的，因为仅在下标 1 处不同。\n- 第二轮，选择并移除 `\"aa\"` 和 `\"ba\"`，它们是兼容的，因为仅在下标 0 处不同。\n\n因为没有更多兼容的牌对，总分为 2。\n\n**示例 2:**\n\n**输入：** cards = [\"aa\",\"ab\",\"ba\"], x = \"a\"\n\n**输出：** 1\n\n**解释：**\n\n- 第一轮，选择并移除 `\"aa\"` 和 `\"ba\"`。\n\n因为没有更多兼容的牌对，总分为 1。\n\n**示例 3:**\n\n**输入：** cards = [\"aa\",\"ab\",\"ba\",\"ac\"], x = \"b\"\n\n**输出：** 0\n\n**解释：**\n\n唯一包含字符 `'b'` 的牌是 `\"ab\"` 和 `\"ba\"`。然而，它们在两个下标上都不同，所以它们不兼容。因此，输出为 0。\n\n \n\n**提示:**\n\n- `2 <= cards.length <= 10**5`\n- `cards[i].length == 2`\n- 每个 `cards[i]` 仅由 `'a'` 到 `'j'` 之间的小写英文字母组成。\n- `x` 是一个 `'a'` 到 `'j'` 之间的小写英文字母。"
                         )

    # 计算除了 x 以外的出现次数之和 sum_cnt，出现次数最大值 max_cnt
    def get_sum_and_max(self, cnt: dict[str, int]) -> Tuple[int, int]:
        sum_cnt = sum(cnt.values())
        max_cnt = max(cnt.values(), default=0)
        return sum_cnt, max_cnt

    # 计算这一组在得到 k 个 xx 后的得分
    def calc_score(self, s: int, mx: int, k: int) -> int:
        s += k
        mx = max(mx, k)
        return min(s // 2, s - mx)

    def solve(self, cards: List[str], x: str) -> int:
        cnt = Counter(cards)
        cnt_xx = cnt.pop(x + x, 0)
        cnt1: dict[str, str] = {b: c for (a, b), c in cnt.items() if a == x}  # 统计 "x?" 中的 ? 的出现次数
        cnt2: dict[str, int] = {a: c for (a, b), c in cnt.items() if b == x}  # 统计 "?x" 中的 ? 的出现次数

        sum1, max1 = self.get_sum_and_max(cnt1)
        sum2, max2 = self.get_sum_and_max(cnt2)

        ans = 0
        # 枚举分配 k 个 xx 给第一组，其余的 xx 给第二组
        for k in range(cnt_xx + 1):
            score1 = self.calc_score(sum1, max1, k)
            score2 = self.calc_score(sum2, max2, cnt_xx - k)
            ans = max(ans, score1 + score2)
        return ans

    def gen(self):
        return self.generate_list_string(vocab="abcdefj", length_range=(1, 1000), str_length_range=(2, 2)), self.generate_string(vocab="abcdefj")


class Solution3(Testing):
    date = "2025-8-30"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3665,
                         types=[ProblemType.Array, ProblemType.DynamicPlanning, ProblemType.Matrix],
                         pass_rate=0.576,
                         description="给你一个 `m x n` 的二进制网格 `grid`，其中：\n\n- `grid[i][j] == 0` 表示一个空格子。\n- `grid[i][j] == 1` 表示一面镜子。\n\n一个机器人从网格的左上角 `(0, 0)` 出发，想要到达右下角 `(m - 1, n - 1)`。它只能向 **右** 或向 **下** 移动。如果机器人试图移入一个有镜子的格子，它会在进入该格子前被 **反射**：\n\n- 如果它试图向 **右** 移动进入镜子，它会被转向 **下** 方，并移动到镜子正下方的格子里。\n- 如果它试图向 **下** 移动进入镜子，它会被转向 **右** 方，并移动到镜子正右方的格子里。\n\n如果这次反射会导致机器人移动到网格边界之外，则该路径被视为无效，不应被计数。\n\n返回从 `(0, 0)` 到 `(m - 1, n - 1)` 不同的有效路径数量。\n\n由于答案可能非常大，请将其返回对 `10**9 + 7` **取模** 的结果。\n\n**注意**：如果一次反射将机器人移动到一个有镜子的格子，机器人会立即再次被反射。这次反射的方向取决于它进入该镜子的方向：如果它是向右移动进入的，它将被转向下方；如果它是向下移动进入的，它将被转向右方。\n\n \n\n**示例 1:**\n\n**输入：** grid = [[0,1,0],[0,0,1],[1,0,0]]\n\n**输出：** 5\n\n**解释：**\n\n| 编号 | 完整路径                                           |\n| :--: | :------------------------------------------------- |\n|  1   | (0, 0) → (0, 1) [M] → (1, 1) → (1, 2) [M] → (2, 2) |\n|  2   | (0, 0) → (0, 1) [M] → (1, 1) → (2, 1) → (2, 2)     |\n|  3   | (0, 0) → (1, 0) → (1, 1) → (1, 2) [M] → (2, 2)     |\n|  4   | (0, 0) → (1, 0) → (1, 1) → (2, 1) → (2, 2)         |\n|  5   | (0, 0) → (1, 0) → (2, 0) [M] → (2, 1) → (2, 2)     |\n\n- `[M]` 表示机器人试图进入一个有镜子的格子但被反射了。\n\n**示例 2:**\n\n**输入：** grid = [[0,0],[0,0]]\n\n**输出：** 2\n\n**解释：**\n\n| 编号 | 完整路径                 |\n| :--: | :----------------------- |\n|  1   | (0, 0) → (0, 1) → (1, 1) |\n|  2   | (0, 0) → (1, 0) → (1, 1) |\n\n**示例 3:**\n\n**输入：** grid = [[0,1,1],[1,1,0]]\n\n**输出：** 1\n\n**解释：**\n\n| 编号 | 完整路径                                  |\n| :--: | :---------------------------------------- |\n|  1   | (0, 0) → (0, 1) [M] → (1, 1) [M] → (1, 2) |\n\n`(0, 0) → (1, 0) [M] → (1, 1) [M] → (2, 1)` 超出边界，因此是无效路径。\n\n \n\n**提示:**\n\n- `m == grid.length`\n- `n == grid[i].length`\n- `2 <= m, n <= 500`\n- `grid[i][j]` 的值为 `0` 或 `1`。\n- `grid[0][0] == grid[m - 1][n - 1] == 0`"
                         )

    def solve(self, grid: List[List[int]]) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs（一行代码实现记忆化）
        def dfs(i: int, j: int, k: int) -> int:
            if i < 0 or j < 0:  # 出界
                return 0
            if i == 0 and j == 0:  # 到达起点
                return 1
            if grid[i][j] == 0:  # 没有镜子，随便走
                return (dfs(i, j - 1, 0) + dfs(i - 1, j, 1)) % 1_000_000_007
            if k == 0:  # 从右边过来
                return dfs(i - 1, j, 1)  # 反射到上边
            # 从下边过来
            return dfs(i, j - 1, 0)  # 反射到左边

        m, n = len(grid), len(grid[0])
        return dfs(m - 1, n - 1, 0)  # 从终点出发


    def _gen(self):
        grid = self.s_generate_matrix(list_length_range1=(2, 10), list_length_range2=(2, 10), int_range=(0, 1))
        grid[0][0] = 0
        grid[-1][-1] = 0
        return grid,


class Solution4(Testing):
    date = "2025-8-30"
    def __init__(self):
        Testing.__init__(self,
                         degree=2,
                         idx=3666,
                         types=[ProblemType.BreadthFirstSearch, ProblemType.HashTable, ProblemType.Math, ProblemType.String],
                         pass_rate=0.26,
                         description="给你一个二进制字符串 `s` 和一个整数 `k`。\n\n在一次操作中，你必须选择 **恰好** `k` 个 **不同的** 下标，并将每个 `'0'` **翻转** 为 `'1'`，每个 `'1'` 翻转为 `'0'`。\n\n返回使字符串中所有字符都等于 `'1'` 所需的 **最少** 操作次数。如果不可能，则返回 -1。\n\n \n\n**示例 1:**\n\n**输入：** s = \"110\", k = 1\n\n**输出：** 1\n\n**解释：**\n\n- `s` 中有一个 `'0'`。\n- 由于 `k = 1`，我们可以直接在一次操作中翻转它。\n\n**示例 2:**\n\n**输入：** s = \"0101\", k = 3\n\n**输出：** 2\n\n**解释：**\n\n每次操作选择 `k = 3` 个下标的一种最优操作方案是：\n\n- **操作 1**：翻转下标 `[0, 1, 3]`。`s` 从 `\"0101\"` 变为 `\"1000\"`。\n- **操作 2**：翻转下标 `[1, 2, 3]`。`s` 从 `\"1000\"` 变为 `\"1111\"`。\n\n因此，最少操作次数为 2。\n\n**示例 3:**\n\n**输入：** s = \"101\", k = 2\n\n**输出：** -1\n\n**解释：**\n\n由于 `k = 2` 且 `s` 中只有一个 `'0'`，因此不可能通过翻转恰好 `k` 个位来使所有字符变为 `'1'`。因此，答案是 -1。\n\n \n\n**提示:**\n\n- `1 <= s.length <= 10**5`\n- `s[i]` 的值为 `'0'` 或 `'1'`。\n- `1 <= k <= s.length`"
                         )

    def solve(self, s: str, k: int) -> int:
        n = len(s)
        not_vis: list[sortedcontainers.SortedList] = [sortedcontainers.SortedList(range(0, n + 1, 2)),
                                                      sortedcontainers.SortedList(range(1, n + 1, 2))]
        not_vis[0].add(n + 1)  # 哨兵，下面 sl[idx] <= mx 无需判断越界
        not_vis[1].add(n + 1)

        start = s.count('0')  # 起点
        not_vis[start % 2].discard(start)
        q = [start]
        ans = 0
        while q:
            tmp = q
            q = []
            for z in tmp:
                if z == 0:  # 没有 0，翻转完毕
                    return ans
                # not_vis[mn % 2] 中的从 mn 到 mx 都可以从 z 翻转到
                mn = z + k - 2 * min(k, z)
                mx = z + k - 2 * max(0, k - n + z)
                sl = not_vis[mn % 2]
                idx = sl.bisect_left(mn)
                while sl[idx] <= mx:
                    j = sl.pop(idx)  # 注意 pop(idx) 会使后续元素向左移，不需要写 idx += 1
                    q.append(j)
            ans += 1
        return -1

    def _gen(self):
        s = self.s_generate_string(vocab="01", length_range=(1, 1000))
        k = self.s_generate_int((1, len(s)))
        return s, k

