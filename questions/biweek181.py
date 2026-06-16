

from . import Problem
import re


class Solution1(Problem):
    date = "2026-4-25"
    def __init__(self):
        Problem.__init__(self,
                         degree=0,
                         idx=3908,
                         types=[],
                         pass_rate=0.79,
                         description='给你一个整数 `n` 和一个数字 `x`。\n如果一个数字满足以下条件，则认为它是**有效**的：\n - 它包含**至少一个**数字 `x`，并且\n - 它**不以**数字 `x` 开头。\n\n如果 `n` 是**有效**的，请返回 `true`，否则返回 `false`。\n\n**示例 1：**\n> \n**输入：**`n = 101, x = 0`\n**输出：**`true`\n**解释：**\n该数字在下标 1 处包含数字 0。它不以 0 开头，因此满足两个条件。所以，答案是 `true`。\n**示例 2：**\n> \n**输入：**`n = 232, x = 2`\n**输出：**`false`\n**解释：**\n该数字以 2 开头，违反了条件。所以，答案是 `false`。\n**示例 3：**\n> \n**输入：**`n = 5, x = 1`\n**输出：**`false`\n**解释：**\n该数字不包含数字 1。所以，答案是 `false`。\n\n**提示：**\n - `0 <= n <= 10^5`\n - `0 <= x <= 9`'
                         )

    def solve(self, n: int, x: int) -> bool:
        has_x = False
        while n >= 10:
            if n % 10 == x:
                has_x = True
            n //= 10
        return has_x and n != x

    def gen(self):
        """
        生成测试样例，覆盖各种边界情况和场景：
        - 边界值：n=0, n=1, n 的最大值
        - 不同 x 值：x=0（特殊）, x=1-9
        - x 在不同位置：开头、中间、结尾
        - 有效和无效的组合
        """
        import random
        random.seed(self.seed)

        # 固定测试用例：覆盖各种边界和特殊情况
        fixed_cases = [
            # n=0 边界情况
            (0, 0),   # 不包含0
            (0, 1),   # 不包含1
            (0, 9),   # 不包含9

            # n=1 单个数字
            (1, 0),   # 不包含0
            (1, 1),   # 以1开头，包含1（无效）
            (1, 9),   # 不包含9

            # x=0 特殊情况
            (101, 0),  # 有效：包含0，不以0开头
            (100, 0),  # 有效：包含0，不以0开头
            (10, 0),   # 有效：包含0，不以0开头
            (0, 0),    # 无效：不包含0（已覆盖）
            (1000, 0), # 有效

            # x=1 情况
            (101, 1),  # 无效：以1开头，包含1
            (21, 1),   # 有效：包含1，不以1开头
            (231, 1),  # 有效：包含1，不以1开头
            (1, 1),    # 无效：单个1

            # x=2 情况
            (232, 2),  # 无效：以2开头，包含2
            (322, 2),  # 有效：包含2，不以2开头
            (32, 2),   # 有效：包含2，不以2开头
            (2, 2),    # 无效：单个2

            # 较大的n值
            (99999, 9),   # 无效：全9，以9开头
            (89999, 9),   # 有效：包含9，不以9开头
            (98999, 9),   # 有效：包含9，不以9开头

            # n最大值附近
            (100000, 0),  # 有效：包含0，不以0开头
            (100000, 1),  # 有效：包含1，不以1开头
            (100000, 9),  # 无效：不包含9

            # 只在末尾包含x
            (10, 0),   # 有效
            (21, 1),   # 有效
            (32, 2),   # 有效
            (43, 3),   # 有效
            (54, 4),   # 有效

            # 只在开头包含x（无效）
            (10, 1),   # 无效：不包含1
            (21, 2),   # 无效：不包含2
            (100, 1),  # 有效：不以1开头

            # 多处包含x
            (10101, 0), # 有效：多处包含0
            (21212, 1), # 有效：不以1开头
            (21212, 2), # 无效：以2开头
        ]

        # 提取固定测试用例
        n_fixed = [case[0] for case in fixed_cases]
        x_fixed = [case[1] for case in fixed_cases]

        # 生成随机测试用例
        num_random = self.testcase_num - len(fixed_cases)

        # 随机n的范围（适当缩小以避免超时）
        n_random = []
        x_random = []

        for _ in range(num_random):
            n_val = random.randint(0, 100000)
            x_val = random.randint(0, 9)
            n_random.append(n_val)
            x_random.append(x_val)

        # 合并固定和随机测试用例
        n_cases = n_fixed + n_random
        x_cases = x_fixed + x_random

        return n_cases, x_cases
    

from typing import Tuple
from . import Problem
import re


class Solution2(Problem):
    date = "2026-4-25"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3909,
                         types=[],
                         pass_rate=0.68,
                         description='给你一个长度为 `n` 的**双调**数组 `nums`。\n将数组分为**两**部分：\n -**递增部分**：从下标 0 到峰值元素（包含）。\n -**递减部分**：从峰值元素到下标 `n - 1`（包含）。\n\n峰值元素同时属于这两部分。\n返回：\n - 如果**递增**部分的和更大，返回 0。\n - 如果**递减**部分的和更大，返回 1。\n - 如果两部分的和**相等**，返回 -1。\n\n**注意**：\n -**双调**数组是指在达到**单个峰值**元素之前**严格递增**，然后**严格递减**的数组。\n - 如果一个数组的每个元素都**严格大于**它的**前一个**元素（如果存在），则称该数组是**严格递增**的。\n - 如果一个数组的每个元素都**严格小于**它的**前一个**元素（如果存在），则称该数组是**严格递减**的。\n\n**示例 1：**\n> \n**输入：**`nums = [1,3,2,1]`\n**输出：**`1`\n**解释：**\n - 峰值元素是 `nums[1] = 3`\n - 递增部分 = `[1, 3]`，和为 `1 + 3 = 4`\n - 递减部分 = `[3, 2, 1]`，和为 `3 + 2 + 1 = 6`\n - 因为递减部分的和更大，返回 1。\n\n**示例 2：**\n> \n**输入：**`nums = [2,4,5,2]`\n**输出：**`0`\n**解释：**\n - 峰值元素是 `nums[2] = 5`\n - 递增部分 = `[2, 4, 5]`，和为 `2 + 4 + 5 = 11`\n - 递减部分 = `[5, 2]`，和为 `5 + 2 = 7`\n - 因为递增部分的和更大，返回 0。\n\n**示例 3：**\n> \n**输入：**`nums = [1,2,4,3]`\n**输出：**`-1`\n**解释：**\n - 峰值元素是 `nums[2] = 4`\n - 递增部分 = `[1, 2, 4]`，和为 `1 + 2 + 4 = 7`\n - 递减部分 = `[4, 3]`，和为 `4 + 3 = 7`\n - 因为两部分的和相等，返回 -1。\n\n**提示：**\n - `3 <= n == nums.length <= 10^5`\n - `1 <= nums[i] <= 10^9`\n - `nums` 是一个双调数组。'
                         )

    def solve(self, nums: list[int]) -> int:
        diff = 0
        inc = True
        for i, x in enumerate(nums):
            if i > 0 and nums[i - 1] < x > nums[i + 1]:
                inc = False
            else:
                diff += x if inc else -x
        return -1 if diff == 0 else int(diff < 0)

    def s_generate_bitonic_array(self, peak_pos, decr_range, incr_range):
        """
        Generate a strictly bitonic array with peak at specified position.

        :param peak_pos: Index of the peak element (0-indexed)
        :param decr_range: Tuple (min_val, max_val) for decreasing part (left of peak, excluding peak)
        :param incr_range: Tuple (min_val, max_val) for increasing part (right of peak, excluding peak)
        :return: A list representing the bitonic array
        """
        import random
        random.seed(self.seed)

        # Calculate lengths
        decr_len = peak_pos
        incr_len = self.testcase_num - peak_pos - 1

        # Generate decreasing part (left side, strictly decreasing towards peak)
        if decr_len > 0:
            left = random.sample(range(decr_range[0], decr_range[1] + 1), decr_len)
            left.sort(reverse=True)  # Strictly decreasing from left to right
        else:
            left = []

        # Peak value
        peak_val = random.randint(1, 10**9)

        # Generate increasing part (right side, strictly decreasing from peak)
        if incr_len > 0:
            right = random.sample(range(incr_range[0], incr_range[1] + 1), incr_len)
            right.sort(reverse=True)  # Strictly decreasing from left to right
        else:
            right = []

        return left + [peak_val] + right

    def gen(self):
        import random
        random.seed(self.seed)

        test_cases = []

        # Case 1: Equal sums (return -1)
        # Peak at middle with balanced ranges
        n_cases = 30
        for i in range(n_cases):
            self.testcase_num = random.randint(5, 20)
            peak_pos = random.randint(1, self.testcase_num - 2)
            # Use balanced ranges to achieve equal sums
            cases = self.s_generate_bitonic_array(peak_pos, (1, 50), (1, 50))
            test_cases.append(cases)

        # Case 2: Increasing sum > Decreasing sum (return 0)
        # Peak near end, left elements have larger values
        for i in range(35):
            self.testcase_num = random.randint(5, 20)
            peak_pos = random.randint(1, self.testcase_num - 2)
            # Left range > Right range
            cases = self.s_generate_bitonic_array(peak_pos, (50, 100), (1, 30))
            test_cases.append(cases)

        # Case 3: Decreasing sum > Increasing sum (return 1)  
        # Peak near start, right elements have larger values
        for i in range(35):
            self.testcase_num = random.randint(5, 20)
            peak_pos = random.randint(1, self.testcase_num - 2)
            # Left range < Right range
            cases = self.s_generate_bitonic_array(peak_pos, (1, 30), (50, 100))
            test_cases.append(cases)

        return (test_cases,)
    

from itertools import count
from . import Problem
import re


class Solution3(Problem):
    date = "2026-4-25"
    def __init__(self):
        Problem.__init__(self,
                         degree=2,
                         idx=3910,
                         types=[],
                         pass_rate=0.64,
                         description='给你一个无向图，有 `n` 个节点，编号从 0 到 `n - 1`。节点 `i` 的**值**为 `nums[i]`，可以是 0 或 1。图的边由一个二维数组 `edges` 给出，其中 `edges[i] = [u_i, v_i]` 表示节点 `u_i` 和节点 `v_i` 之间的一条边。\n对于图中节点的**非空子集**`s`，我们考虑由 `s` 生成的**诱导子图**如下：\n - 我们只保留 `s` 中的节点。\n - 我们只保留两个端点都在 `s` 中的边。\n\n返回一个整数，表示图中满足以下条件的节点的**非空**子集 `s` 的数量：\n - `s` 的**诱导子图**是**连通的**。\n - `s` 中节点**值**的**总和**是**偶数**。\n\n**示例 1：**\n> \n**输入：**`nums = [1,0,1], edges = [[0,1],[1,2]]`\n**输出：**`2`\n**解释：**\n| `s` | 是否连通？ | 节点值总和 | 和是否为偶数？ |\n| --- | --- | --- | --- |\n| `[0]` | 是 | 1 | 否 |\n| `[1]` | 是 | 0 | 是 |\n| `[2]` | 是 | 1 | 否 |\n| `[0,1]` | 是 | 1 | 否 |\n| `[0,2]` | 否，节点 0 和节点 2 不连通。 | 2 | 否 |\n| `[1,2]` | 是 | 1 | 否 |\n| `[0,1,2]` | 是 | 2 | 是 |\n\n**示例 2：**\n> \n**输入：**`nums = [1], edges = []`\n**输出：**`0`\n**解释：**\n| `s` | 是否连通？ | 节点值总和 | 和是否为偶数？ |\n| --- | --- | --- | --- |\n| `[0]` | 是 | 1 | 否 |\n\n**提示：**\n - `1 <= n == nums.length <= 13`\n - `nums[i]` 是 0 或 1。\n - `0 <= edges.length <= n * (n - 1) / 2`\n - `edges[i] = [u_i, v_i]`\n - `0 <= u_i < v_i < n`\n - 所有边都是**互不相同**的。'
                         )

    def solve(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        u = (1 << n) - 1
        ans = 0
        for sub in range(1, u + 1):
            xor_sum = 0
            for i, x in enumerate(nums):
                if sub >> i & 1:
                    xor_sum ^= x
            if xor_sum:
                continue

            def dfs(x: int) -> None:
                nonlocal vis
                vis |= 1 << x
                for y in g[x]:
                    if vis >> y & 1 == 0:
                        dfs(y)
            vis = u ^ sub
            dfs(sub.bit_length() - 1)
            if vis == u:
                ans += 1
        return ans

    def gen(self):
        # 由于n较小且需要枚举子集，减少测试用例数避免超时
        self.testcase_num = 40

        # 构建测试用例列表
        nums_list = []
        edges_list = []

        # ===== 边界情况测试 (10个用例) =====

        # n=1, 无边，节点值为1（示例2）
        nums_list.append([1])
        edges_list.append([])

        # n=1, 无边，节点值为0
        nums_list.append([0])
        edges_list.append([])

        # n=2, 无边，不同节点值组合
        nums_list.append([0, 0])
        edges_list.append([])

        nums_list.append([1, 0])
        edges_list.append([])

        nums_list.append([1, 1])
        edges_list.append([])

        # n=2, 完全图（1条边）
        nums_list.append([1, 0])
        edges_list.append([[0, 1]])

        nums_list.append([1, 1])
        edges_list.append([[0, 1]])

        nums_list.append([0, 0])
        edges_list.append([[0, 1]])

        # n=13, 无边
        nums_list.append([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])
        edges_list.append([])

        # n=13, 完全图（78条边）
        n = 13
        nums_list.append([0] * 7 + [1] * 6)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                edges.append([i, j])
        edges_list.append(edges)

        # ===== 特殊图结构测试 (10个用例) =====

        # 链形图: 0-1-2-3-4-5-6
        n = 7
        nums_list.append([0, 1, 0, 1, 0, 1, 0])
        edges = []
        for i in range(n - 1):
            edges.append([i, i + 1])
        edges_list.append(edges)

        # 链形图，全0节点值
        nums_list.append([0] * 7)
        edges_list.append(edges[:])

        # 链形图，全1节点值
        nums_list.append([1] * 7)
        edges_list.append(edges[:])

        # 环形图: 0-1-2-3-4-5-0
        n = 6
        nums_list.append([1, 0, 1, 0, 1, 0])
        edges = []
        for i in range(n):
            edges.append([i, (i + 1) % n])
        edges_list.append(edges)

        # 环形图，偶数个1
        nums_list.append([1, 1, 0, 0, 0, 0])
        edges_list.append(edges[:])

        # 星形图: 中心节点0连接其他节点
        n = 6
        nums_list.append([0, 1, 1, 1, 1, 1])
        edges = [[0, i] for i in range(1, n)]
        edges_list.append(edges)

        # 星形图，中心节点为1
        nums_list.append([1, 0, 0, 0, 0, 0])
        edges_list.append(edges[:])

        # 两个连通分量
        n = 6
        nums_list.append([0, 1, 1, 0, 1, 0])
        edges = [[0, 1], [0, 2], [3, 4]]
        edges_list.append(edges)

        # 三个连通分量（单节点）
        nums_list.append([0, 1, 0])
        edges_list.append([])

        # ===== 随机测试 (20个用例) =====
        import random

        # 随机小图
        for _ in range(10):
            n = random.randint(3, 8)
            max_edges = n * (n - 1) // 2
            edge_count = random.randint(0, max_edges)

            # 生成节点值（0或1）
            nums = [random.randint(0, 1) for _ in range(n)]

            # 生成不重复的边
            all_possible_edges = [[i, j] for i in range(n) for j in range(i + 1, n)]
            random.shuffle(all_possible_edges)
            edges = all_possible_edges[:edge_count]

            nums_list.append(nums)
            edges_list.append(edges)

        # 随机中等规模图
        for _ in range(10):
            n = random.randint(8, 12)
            max_edges = n * (n - 1) // 2
            # 限制边数，避免完全图过多
            edge_count = random.randint(0, min(max_edges, 30))

            nums = [random.randint(0, 1) for _ in range(n)]

            all_possible_edges = [[i, j] for i in range(n) for j in range(i + 1, n)]
            random.shuffle(all_possible_edges)
            edges = all_possible_edges[:edge_count]

            nums_list.append(nums)
            edges_list.append(edges)

        return nums_list, edges_list
    


from . import Problem
from bisect import bisect_left
from bisect import bisect_right
import re


class Solution4(Problem):
    date = "2026-4-25"
    def __init__(self):
        Problem.__init__(self,
                         degree=2,
                         idx=3911,
                         types=[],
                         pass_rate=0.44,
                         description='给你一个整数数组 `nums`，其中 `nums` 是**严格递增**的。\n另给你一个二维整数数组 `queries`，其中 `queries[i] = [l_i, r_i, k_i]`。\n对于每个查询 `[l_i, r_i, k_i]`：\n - 考虑**子数组**`nums[l_i..r_i]`\n - 从**无限**的所有**正偶数**序列中：`2, 4, 6, 8, 10, 12, 14, ...`\n -**移除**所有出现在**子数组**`nums[l_i..r_i]` 中的元素。\n - 找到移除后序列中剩余的第 `k_i` 个**最小整数**。\n\n返回一个整数数组 `ans`，其中 `ans[i]` 是第 `i` 个查询的结果。\n**子数组**是数组中连续的**非空**元素序列。\n如果数组中的每个元素都**严格大于**它的**前一个**元素（如果存在），则称该数组是**严格递增**的。\n\n**示例 1：**\n> \n**输入：**`nums = [1,4,7], queries = [[0,2,1],[1,1,2],[0,0,3]]`\n**输出：**`[2,6,6]`\n**解释：**\n| `i` | `queries[i]` | `nums[l_i..r_i]` | 移除的 > 偶数 | 剩余的 > 偶数 | `k_i` | `ans[i]` |\n| --- | --- | --- | --- | --- | --- | --- |\n| 0 | [0, 2, 1] | [1, 4, 7] | [4] | 2, 6, 8, ... | 1 | 2 |\n| 1 | [1, 1, 2] | [4] | [4] | 2, 6, 8, ... | 2 | 6 |\n| 2 | [0, 0, 3] | [1] | [] | 2, 4, 6, ... | 3 | 6 |\n\n因此，`ans = [2, 6, 6]`。\n**示例 2：**\n> \n**输入：**`nums = [2,5,8], queries = [[0,1,2],[1,2,1],[0,2,4]]`\n**输出：**`[6,2,12]`\n**解释：**\n| `i` | `queries[i]` | `nums[l_i..r_i]` | 移除的 > 偶数 | 剩余的 > 偶数 | `k_i` | `ans[i]` |\n| --- | --- | --- | --- | --- | --- | --- |\n| 0 | [0, 1, 2] | [2, 5] | [2] | 4, 6, 8, ... | 2 | 6 |\n| 1 | [1, 2, 1] | [5, 8] | [8] | 2, 4, 6, ... | 1 | 2 |\n| 2 | [0, 2, 4] | [2, 5, 8] | [2, 8] | 4, 6, 10, 12, ... | 4 | 12 |\n\n因此，`ans = [6, 2, 12]`。\n**示例 3：**\n> \n**输入：**`nums = [3,6], queries = [[0,1,1],[1,1,3]]`\n**输出：**`[2,8]`\n**解释：**\n| `i` | `queries[i]` | `nums[l_i..r_i]` | 移除的 > 偶数 | 剩余的 > 偶数 | `k_i` | `ans[i]` |\n| --- | --- | --- | --- | --- | --- | --- |\n| 0 | [0, 1, 1] | [3, 6] | [6] | 2, 4, 8, ... | 1 | 2 |\n| 1 | [1, 1, 3] | [6] | [6] | 2, 4, 8, ... | 3 | 8 |\n\n因此，`ans = [2, 8]`。\n\n**提示：**\n - `1 <= nums.length <= 10^5`\n - `1 <= nums[i] <= 10^9`\n - `nums` 是严格递增的\n - `1 <= queries.length <= 10^5`\n - `queries[i] = [l_i, r_i, k_i]`\n - `0 <= l_i <= r_i < nums.length`\n - `1 <= k_i <= 10^9`'
                         )

    def solve(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        even_pos = [i for i, x in enumerate(nums) if x % 2 == 0]
        ans = [0] * len(queries)
        for i, (l, r, k) in enumerate(queries):
            li = bisect_left(even_pos, l)
            ri = bisect_right(even_pos, r)

            def check(x: int) -> bool:
                j = bisect_right(range(ri), x * 2, lo=li, key=lambda i: nums[even_pos[i]]) - li
                return x - j >= k
            left, right = (k, k + ri - li)
            res = bisect_left(range(right), True, lo=left, key=check)
            ans[i] = res * 2
        return ans

    def gen(self):
        """
        生成测试样例，覆盖以下场景：
        1. 边界情况：全奇数、全偶数、单元素数组
        2. 查询边界：l=r、覆盖整个数组、覆盖单元素
        3. k的边界：小值、中等值、大值
        4. 偶数分布：密集、稀疏、均匀
        5. 数组规模：小、中、大（适当缩小范围）
        """
        # 分配测试样例：总共100个
        # 0-19: 小规模边界测试 (20个)
        # 20-49: 中规模随机测试 (30个)  
        # 50-69: 特殊结构测试 (20个)
        # 70-99: 混合场景测试 (30个)

        import random
        random.seed(self.seed)

        nums_list = []
        queries_list = []

        # === 0-19: 小规模边界测试 (20个) ===
        for i in range(20):
            n = random.randint(2, 10)

            # 偶数分布模式：0=全奇数, 1=全偶数, 2=混合
            pattern = i % 3

            if pattern == 0:  # 全奇数
                nums = [2 * j + 1 for j in range(n)]
            elif pattern == 1:  # 全偶数
                nums = [2 * (j + 1) for j in range(n)]
            else:  # 混合
                nums = list(range(1, 2 * n + 1))

            q_num = random.randint(1, 3)
            queries = []
            for j in range(q_num):
                l = random.randint(0, n - 1)
                r = random.randint(l, n - 1)
                k = random.randint(1, min(10, n * 2))
                queries.append([l, r, k])

            nums_list.append(nums)
            queries_list.append(queries)

        # === 20-49: 中规模随机测试 (30个) ===
        for i in range(30):
            n = random.randint(20, 100)

            # 随机生成严格递增数组
            nums = [random.randint(1, 200)]
            for j in range(1, n):
                next_val = nums[-1] + random.randint(1, 3)
                nums.append(next_val)

            q_num = random.randint(5, 15)
            queries = []
            for j in range(q_num):
                l = random.randint(0, n - 1)
                r = random.randint(l, min(n - 1, l + 20))
                k = random.randint(1, min(50, n * 2))
                queries.append([l, r, k])

            nums_list.append(nums)
            queries_list.append(queries)

        # === 50-69: 特殊结构测试 (20个) ===
        for i in range(20):
            n = 30

            if i < 5:  # 偶数密集：连续偶数
                nums = [2 * (j + 1) for j in range(n)]
            elif i < 10:  # 偶数稀疏：几乎全奇数，少量偶数
                nums = [2 * j + 1 for j in range(n)]
                for pos in [5, 15, 25]:
                    if pos < n:
                        nums[pos] = 2 * (pos + 1)
            elif i < 15:  # 偶数交替
                nums = [(2 * j + 1) if j % 2 == 0 else (2 * (j + 1)) for j in range(n)]
            else:  # 偶数集中在某个区间
                nums = [2 * j + 1 for j in range(n)]
                start = 10
                for j in range(start, min(start + 10, n)):
                    nums[j] = 2 * (j + 1)

            q_num = random.randint(3, 8)
            queries = []
            for j in range(q_num):
                l = random.randint(0, n - 1)
                r = random.randint(l, n - 1)
                k = random.randint(1, min(20, n * 2))
                queries.append([l, r, k])

            nums_list.append(nums)
            queries_list.append(queries)

        # === 70-99: 混合场景测试 (30个) ===
        for i in range(30):
            # 不同规模
            if i < 10:
                n = random.randint(50, 150)
            elif i < 20:
                n = random.randint(200, 300)
            else:
                n = random.randint(10, 50)

            # 随机偶数密度
            even_density = random.random()
            nums = []
            current = 1
            for j in range(n):
                if random.random() < even_density:
                    nums.append(current)
                else:
                    nums.append(current + 1)  # 偶数
                current += random.randint(1, 2)

            q_num = random.randint(5, 20)
            queries = []
            for j in range(q_num):
                l = random.randint(0, n - 1)
                r = random.randint(l, n - 1)
                k = random.randint(1, min(100, n * 3))
                queries.append([l, r, k])

            nums_list.append(nums)
            queries_list.append(queries)

        return nums_list, queries_list
    

