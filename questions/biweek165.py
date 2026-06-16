from . import Problem as Testing, ProblemType
from typing import List


class Solution1(Testing):
    date = "2025-9-13"
    def __init__(self):
        Testing.__init__(self,
                         degree=0,
                         idx=3678,
                         types=[ProblemType.Array, ProblemType.HashTable],
                         pass_rate=0.384,
                         description="给你一个整数数组 `nums`。\n\n返回 `nums` 中 **严格大于** `nums` 中所有元素 **平均值** 的 **最小未出现正整数**。\n\n数组的 **平均值** 定义为数组中所有元素的总和除以元素的数量。\n\n \n\n**示例 1:**\n\n**输入:** nums = [3,5]\n\n**输出:** 6\n\n**解释:**\n\n- `nums` 的平均值是 `(3 + 5) / 2 = 8 / 2 = 4` 。\n- 大于 4 的最小未出现正整数是 6。\n\n**示例 2:**\n\n**输入:** nums = [-1,1,2]\n\n**输出:** 3\n\n**解释:**\n\n- `nums` 的平均值是 `(-1 + 1 + 2) / 3 = 2 / 3 = 0.667` 。\n- 大于 0.667 的最小未出现正整数是 3 。\n\n**示例 3:**\n\n**输入:** nums = [4,-1]\n\n**输出:** 2\n\n**解释:**\n\n- `nums` 的平均值是 `(4 + (-1)) / 2 = 3 / 2 = 1.50`。\n- 大于 1.50 的最小未出现正整数是 2。\n\n \n\n**提示:**\n\n- `1 <= nums.length <= 100`\n- `-100 <= nums[i] <= 100`"
                         )

    def solve(self, nums: list[int]) -> int:
        st = set(nums)
        ans = max(sum(nums) // len(nums) + 1, 1)  # 答案必须是正整数
        while ans in st:
            ans += 1
        return ans

    def gen(self):
        return self.generate_list_int(list_length_range=(1, 100), int_range=(-100, 100)),


class Solution2(Testing):
    date = "2025-9-13"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3679,
                         types=[ProblemType.Array, ProblemType.HashTable, ProblemType.Counting, ProblemType.SlideWindows, ProblemType.Simulation],
                         pass_rate=0.403,
                         description="给你两个整数 `w` 和 `m`，以及一个整数数组 `arrivals`，其中 `arrivals[i]` 表示第 `i` 天到达的物品类型（天数从 **1 开始编号**）。\n\n物品的管理遵循以下规则：\n\n- 每个到达的物品可以被 **保留** 或 **丢弃** ，物品只能在到达当天被丢弃。\n- 对于每一天i，考虑天数范围为 `[max(1, i - w + 1), i]`（也就是直到第 `i`天为止最近的`w`天）：\n  - 对于 **任何** 这样的时间窗口，在被保留的到达物品中，每种类型最多只能出现 `m` 次。\n  - 如果在第 `i` 天保留该到达物品会导致其类型在该窗口中出现次数 **超过** `m` 次，那么该物品必须被丢弃。\n\n返回为满足每个 `w` 天的窗口中每种类型最多出现 `m` 次，**最少** 需要丢弃的物品数量。\n\n \n\n**示例 1：**\n\n**输入：** arrivals = [1,2,1,3,1], w = 4, m = 2\n\n**输出：** 0\n\n**解释：**\n\n- 第 1 天，物品 1 到达；窗口中该类型不超过 `m` 次，因此保留。\n- 第 2 天，物品 2 到达；第 1 到第 2 天的窗口是可以接受的。\n- 第 3 天，物品 1 到达，窗口 `[1, 2, 1]` 中物品 1 出现两次，符合限制。\n- 第 4 天，物品 3 到达，窗口 `[1, 2, 1, 3]` 中物品 1 出现两次，仍符合。\n- 第 5 天，物品 1 到达，窗口 `[2, 1, 3, 1]` 中物品 1 出现两次，依然有效。\n\n没有任何物品被丢弃，因此返回 0。\n\n**示例 2：**\n\n**输入：** arrivals = [1,2,3,3,3,4], w = 3, m = 2\n\n**输出：** 1\n\n**解释：**\n\n- 第 1 天，物品 1 到达。我们保留它。\n- 第 2 天，物品 2 到达，窗口 `[1, 2]` 是可以的。\n- 第 3 天，物品 3 到达，窗口 `[1, 2, 3]` 中物品 3 出现一次。\n- 第 4 天，物品 3 到达，窗口 `[2, 3, 3]` 中物品 3 出现两次，允许。\n- 第 5 天，物品 3 到达，窗口 `[3, 3, 3]` 中物品 3 出现三次，超过限制，因此该物品必须被丢弃。\n- 第 6 天，物品 4 到达，窗口 `[3, 4]` 是可以的。\n\n第 5 天的物品 3 被丢弃，这是最少必须丢弃的数量，因此返回 1。\n\n \n\n**提示：**\n\n- `1 <= arrivals.length <= 10**5`\n- `1 <= arrivals[i] <= 10**5`\n- `1 <= w <= arrivals.length`\n- `1 <= m <= w`"
                         )

    def solve(self, arrivals: List[int], w: int, m: int) -> int:
        cnt = [0] * (max(arrivals) + 1)  # 或者用 defaultdict(int)
        ans = 0
        for i, x in enumerate(arrivals):
            # x 进入窗口
            if cnt[x] == m:  # x 的个数已达上限
                # 注意 x 在未来要离开窗口，但由于已经丢弃，不能计入
                # 这里直接置为 0，未来离开窗口就是 cnt[0]--，不影响答案
                arrivals[i] = 0
                ans += 1
            else:
                cnt[x] += 1

            # 左端点元素离开窗口，为下一个循环做准备
            left = i + 1 - w
            if left >= 0:
                cnt[arrivals[left]] -= 1
        return ans

    def _gen(self):
        arrivals = self.s_generate_list_int(int_range=(1, 1000), list_length_range=(1, 100))
        w = self.s_generate_int((1, len(arrivals)))
        m = self.s_generate_int((1, w))
        return arrivals, w, m


class Solution3(Testing):
    date = "2025-9-13"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3680,
                         types=[ProblemType.Greedy, ProblemType.Array, ProblemType.Math],
                         pass_rate=0.432,
                         description="给你一个整数 `n`，表示 `n` 支队伍。你需要生成一个赛程，使得：\n\n- 每支队伍与其他队伍 **正好比赛两次**：一次在主场，一次在客场。\n- 每天 **只有一场** 比赛；赛程是一个 **连续的** 天数列表，`schedule[i]` 表示第 `i` 天的比赛。\n- 没有队伍在 **连续** 两天内进行比赛。\n\n返回一个bool值，True表示问题有解，Fasle表示问题无解。\n\n \n\n**示例 1：**\n\n**输入：** n = 3\n\n**输出：**False\n\n**解释：**\n\n因为每支队伍与其他队伍恰好比赛两次，总共需要进行 6 场比赛：`[0,1],[0,2],[1,2],[1,0],[2,0],[2,1]`。\n\n所有赛程都至少有一支队伍在连续两天比赛，所以无法创建一个赛程。\n\n**示例 2：**\n\n**输入：** n = 5\n\n**输出：** True\n\n**解释：**\n\n[[0,1],[2,3],[0,4],[1,2],[3,4],[0,2],[1,3],[2,4],[0,3],[1,4],[2,0],[3,1],[4,0],[2,1],[4,3],[1,0],[3,2],[4,1],[3,0],[4,2]]\n\n \n\n**提示：**\n\n- `2 <= n <= 50`"
                         )

    def solve(self, n: int) -> bool:
        return n > 4


    def gen(self):
        return self.generate_int(int_range=(1, 100)),


class XorBasis:
    # n 为值域最大值 U 的二进制长度，例如 U=1e9 时 n=30
    def __init__(self, n: int):
        self.b = [0] * n

    def insert(self, x: int) -> None:
        b = self.b
        # 从高到低遍历，保证计算 max_xor 的时候，参与 XOR 的基的最高位（或者说二进制长度）是互不相同的
        for i in range(len(b) - 1, -1, -1):
            if x >> i:  # 由于大于 i 的位都被我们异或成了 0，所以 x >> i 的结果只能是 0 或 1
                if b[i] == 0:  # x 和之前的基是线性无关的
                    b[i] = x  # 新增一个基，最高位为 i
                    return
                x ^= b[i]  # 保证每个基的二进制长度互不相同
        # 正常循环结束，此时 x=0，说明一开始的 x 可以被已有基表出，不是一个线性无关基

    def max_xor(self) -> int:
        b = self.b
        res = 0
        # 从高到低贪心：越高的位，越必须是 1
        # 由于每个位的基至多一个，所以每个位只需考虑异或一个基，若能变大，则异或之
        for i in range(len(b) - 1, -1, -1):
            if res ^ b[i] > res:  # 手写 max 更快
                res ^= b[i]
        return res


class Solution4(Testing):
    date = "2025-9-13"
    def __init__(self):
        Testing.__init__(self,
                         degree=2,
                         idx=3681,
                         types=[ProblemType.Greedy, ProblemType.Bit, ProblemType.Array, ProblemType.Math],
                         pass_rate=0.579,
                         description="给你一个长度为 `n` 的整数数组 `nums`，其中每个元素都是非负整数。\n\n选择 **两个** 子序列 `nums`（它们可以为空并且 **允许重叠**），每个子序列保留原始元素的顺序，并且定义：\n\n- `X` 是第一个子序列中所有元素的按位 XOR。\n- `Y` 是第二个子序列中所有元素的按位 XOR。\n\n返回 **最大** 的 `X XOR Y` 值。\n\n**子序列** 是通过删除某些或不删除任何元素，而不改变剩余元素的顺序，从另一个数组派生出的数组。\n\n**注意：**一个 **空** 子序列的 XOR 为 0。\n\n \n\n**示例 1：**\n\n**输入：** nums = [1,2,3]\n\n**输出：** 3\n\n**解释：**\n\n选择子序列：\n\n- 第一个子序列 `[2]`，其 XOR 为 2。\n- 第二个子序列 `[2,3]`，其 XOR 为 1。\n\n然后，两个子序列的 XOR 为 `2 XOR 1 = 3`。\n\n这是从任何两个子序列中可以得到的最大 XOR 值。\n\n**示例 2：**\n\n**输入：** nums = [5,2]\n\n**输出：** 7\n\n**解释：**\n\n选择子序列：\n\n- 第一个子序列 `[5]`，其 XOR 为 5。\n- 第二个子序列 `[2]`，其 XOR 为 2。\n\n然后，两个子序列的 XOR 为 `5 XOR 2 = 7`。\n\n这是从任何两个子序列中可以得到的最大 XOR 值。\n\n \n\n**提示：**\n\n- `2 <= nums.length <= 10**5`\n- `0 <= nums[i] <= 10**9`"                         )

    def solve(self, nums: list[int]) -> int:
        m = max(nums).bit_length()
        b = XorBasis(m)
        for x in nums:
            b.insert(x)
        return b.max_xor()


    def gen(self):
        return self.generate_list_int(list_length_range=(2, 1000), int_range=(0, 1000)),

