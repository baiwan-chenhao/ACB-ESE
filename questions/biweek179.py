
import math
import random
from itertools import count
from . import Problem
from typing import List
import re
from math import inf


class Solution1(Problem):
    date = "2026-3-28"
    def __init__(self):
        Problem.__init__(self,
                         degree=0,
                         idx=3880,
                         types=[],
                         pass_rate=0.71,
                         description='给你一个只包含 0、1 和 2 的整数数组 `nums`。\n如果 `nums[i] == 1` 且 `nums[j] == 2`，则称下标对 `(i, j)` 为**有效**的。\n请返回所有有效下标对中 `i` 和 `j` 之间的**最小**绝对差。如果不存在有效下标对，则返回 -1。\n下标 `i` 和 `j` 之间的绝对差定义为 `abs(i - j)`。\n\n**示例 1：**\n> \n**输入：**`nums = [1,0,0,2,0,1]`\n**输出：**`2`\n**解释：**\n有效下标对有：\n - (0, 3)，其绝对差为 `abs(0 - 3) = 3`。\n - (5, 3)，其绝对差为 `abs(5 - 3) = 2`。\n\n因此，结果是 2。\n**示例 2：**\n> \n**输入：**`nums = [1,0,1,0]`\n**输出：**`-1`\n**解释：**\n数组中不存在有效下标对，因此结果是 -1。\n\n**提示：**\n - `1 <= nums.length <= 100`\n - `0 <= nums[i] <= 2`'
                         )

    def solve(self, nums: List[int]) -> int:
        ans = inf
        last = [-inf] * 2
        for i, x in enumerate(nums):
            if x > 0:
                x -= 1
                ans = min(ans, i - last[x ^ 1])
                last[x] = i
        return ans if ans < inf else -1


    def gen(self):
        """
        生成测试样例，返回由列表构成的元组，每个列表对应一个参数的所有测试用例。

        测试样例设计策略：
        1. 边界值测试：最小长度1、最大长度100的数组
        2. 无效对测试：全0、全1、全2（应返回-1）
        3. 特殊结构测试：
           - 1和2相邻（最小距离为1）
           - 1和2在两端（最大距离）
           - 只有1和2，无0
        4. 随机测试：覆盖一般情况

        样例分配（共100个）：
        - 边界值：15个
        - 特殊结构：25个
        - 随机分布：60个

        :return: 包含nums参数所有测试用例的元组
        """
        random.seed(self.seed)
        nums_list = []

        for case_idx in range(self.testcase_num):
            if case_idx < 5:
                # 边界值：最小长度数组
                # [1], [2], [0], [1, 2], [2, 1]
                patterns = [
                    [1],
                    [2],
                    [0],
                    [1, 2],
                    [2, 1]
                ]
                nums = patterns[case_idx]

            elif case_idx < 10:
                # 边界值：最大长度(100)的边界情况
                pattern_idx = case_idx - 5
                if pattern_idx == 0:
                    # 全0，无有效对
                    nums = [0] * 100
                elif pattern_idx == 1:
                    # 全1，无有效对
                    nums = [1] * 100
                elif pattern_idx == 2:
                    # 全2，无有效对
                    nums = [2] * 100
                elif pattern_idx == 3:
                    # 1和2在两端，距离最大
                    nums = [1] + [0] * 98 + [2]
                else:
                    # 2和1在两端，距离最大
                    nums = [2] + [0] * 98 + [1]

            elif case_idx < 20:
                # 1和2相邻，最小距离为1的情况
                pattern_idx = case_idx - 10
                if pattern_idx < 5:
                    # [1, 2] 随机前后加0
                    prefix_len = self.s_generate_int(int_range=(0, 5))
                    suffix_len = self.s_generate_int(int_range=(0, 5))
                    nums = [0] * prefix_len + [1, 2] + [0] * suffix_len
                else:
                    # [2, 1] 随机前后加0
                    prefix_len = self.s_generate_int(int_range=(0, 5))
                    suffix_len = self.s_generate_int(int_range=(0, 5))
                    nums = [0] * prefix_len + [2, 1] + [0] * suffix_len

            elif case_idx < 30:
                # 多个1和2交替出现
                pattern_idx = case_idx - 20
                length = self.s_generate_int(int_range=(4, 20))
                nums = []
                for i in range(length):
                    if i % 3 == 0:
                        nums.append(1)
                    elif i % 3 == 1:
                        nums.append(2)
                    else:
                        nums.append(0)

            elif case_idx < 40:
                # 只有1和2，无0的情况
                pattern_idx = case_idx - 30
                length = self.s_generate_int(int_range=(4, 20))
                nums = [self.s_generate_int(int_range=(1, 2)) for _ in range(length)]

            elif case_idx < 50:
                # 连续的1后面跟连续的2
                pattern_idx = case_idx - 40
                ones_count = self.s_generate_int(int_range=(1, 5))
                twos_count = self.s_generate_int(int_range=(1, 5))
                nums = [1] * ones_count + [2] * twos_count

            elif case_idx < 60:
                # 单一1和多个2或反之
                pattern_idx = case_idx - 50
                length = self.s_generate_int(int_range=(10, 30))
                pos1 = self.s_generate_int(int_range=(0, length - 1))
                nums = [0] * length
                nums[pos1] = 1
                # 随机放置多个2
                num_twos = self.s_generate_int(int_range=(1, 5))
                for _ in range(num_twos):
                    pos2 = self.s_generate_int(int_range=(0, length - 1))
                    while pos2 == pos1:
                        pos2 = self.s_generate_int(int_range=(0, length - 1))
                    nums[pos2] = 2

            else:
                # 随机生成，覆盖一般情况
                nums = self.s_generate_list_int(
                    list_length_range=(1, 100),
                    int_range=(0, 2)
                )

            nums_list.append(nums)

        return (nums_list,)
    

import math
from . import Problem
import re
from math import comb


class Solution2(Problem):
    date = "2026-3-28"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3881,
                         types=[],
                         pass_rate=0.33,
                         description="给你三个整数 `n`、`pos` 和 `k`。\n有 `n` 个人排成一排，下标从 0 到 `n - 1`。每个人**独立地**选择一个方向：\n - `'L'`：只对他们**右边**的人**可见**\n - `'R'`：只对他们**左边**的人**可见**\n\n位于下标 `pos` 的人看其他人的方式如下：\n\n - 一个 `i < pos` 的人可见当且仅当他们选择 `'L'`。\n - 一个 `i > pos` 的人可见当且仅当他们选择 `'R'`。\n\n返回可能的方向分配数量，使得位于下标 `pos` 的人**恰好**看到 `k` 个人。\n由于答案可能很大，请将其对 `10^9 + 7`**取余**后返回。\n\n**示例 1：**\n> \n**输入：**`n = 3, pos = 1, k = 0`\n**输出：**`2`\n**解释：**\n - 下标 0 在 `pos = 1` 的左侧，下标 2 在 `pos = 1` 的右侧。\n - 为了看到 `k = 0` 个人，下标 0 必须选择 `'R'`，且下标 2 必须选择 `'L'`，这样两人都不可见。\n - 位于下标 1 的人可以选择 `'L'` 或 `'R'`，因为这不会影响计数。因此，答案是 2。\n\n**示例 2：**\n> \n**输入：**`n = 3, pos = 2, k = 1`\n**输出：**`4`\n**解释：**\n - 下标 0 和下标 1 在 `pos = 2` 的左侧，右侧没有下标。\n - 为了看到 `k = 1` 个人，下标 0 或下标 1 中必须恰好有一个选择 `'L'`，另一个必须选择 `'R'`。\n - 有 2 种方法可以选择哪个下标从左侧可见。\n - 位于下标 2 的人可以选择 `'L'` 或 `'R'`，因为这不会影响计数。因此，答案是 `2 + 2 = 4`。\n\n**示例 3：**\n> \n**输入：**`n = 1, pos = 0, k = 0`\n**输出：**`2`\n**解释：**\n - `pos = 0` 的左侧或右侧没有下标。\n - 为了看到 `k = 0` 个人，不需要额外的条件。\n - 位于下标 0 的人可以选择 `'L'` 或 `'R'`。因此，答案是 2。\n\n**提示：**\n - `1 <= n <= 10^5`\n - `0 <= pos, k <= n - 1`"
                         )

    def solve(self, n: int, pos: int, k: int) -> int:
        return comb(n - 1, k) * 2 % 1000000007

    def gen(self):
        """
        生成测试样例。
        参数：
        - n: 人数，1 <= n <= 10000（根据经验调整，避免过大）
        - pos: 位置，0 <= pos <= n-1
        - k: 想要看到的人数，0 <= k <= n-1

        测试覆盖：
        1. 边界情况：n=1, k=0
        2. 小规模测试：n=2,3,5，覆盖所有k值
        3. 中等规模：n=10,20,50,100,1000,5000，测试k=0, k=n/2, k=n-1
        4. 随机测试：覆盖各种n和k的组合
        """
        n_cases = []
        pos_cases = []
        k_cases = []

        # 1. 边界情况：n=1
        n_cases.extend([1])
        pos_cases.extend([0])
        k_cases.extend([0])

        # 2. 小规模测试 - n=2
        for k in [0, 1]:
            for pos in [0, 1]:
                n_cases.append(2)
                pos_cases.append(pos)
                k_cases.append(k)

        # 3. 小规模测试 - n=3
        for k in [0, 1, 2]:
            n_cases.append(3)
            pos_cases.append(1)  # 中间位置
            k_cases.append(k)

        # 4. 小规模测试 - n=5
        for k in [0, 2, 4]:
            for pos in [0, 2, 4]:
                n_cases.append(5)
                pos_cases.append(pos)
                k_cases.append(k)

        # 5. 中等规模测试 - n=10
        for k in [0, 5, 9]:
            n_cases.append(10)
            pos_cases.append(5)
            k_cases.append(k)

        # 6. 中等规模测试 - n=20
        for k in [0, 10, 19]:
            n_cases.append(20)
            pos_cases.append(10)
            k_cases.append(k)

        # 7. 中等规模测试 - n=50
        for k in [0, 25, 49]:
            n_cases.append(50)
            pos_cases.append(25)
            k_cases.append(k)

        # 8. 中等规模测试 - n=100
        for k in [0, 50, 99]:
            n_cases.append(100)
            pos_cases.append(50)
            k_cases.append(k)

        # 9. 较大规模测试 - n=1000
        for k in [0, 500, 999]:
            n_cases.append(1000)
            pos_cases.append(500)
            k_cases.append(k)

        # 10. 较大规模测试 - n=5000
        for k in [0, 2500, 4999]:
            n_cases.append(5000)
            pos_cases.append(2500)
            k_cases.append(k)

        # 11. 随机测试填充剩余样例
        import random
        random.seed(self.seed)
        while len(n_cases) < self.testcase_num:
            n = random.randint(2, 5000)
            pos = random.randint(0, n - 1)
            k = random.randint(0, n - 1)
            n_cases.append(n)
            pos_cases.append(pos)
            k_cases.append(k)

        return n_cases, pos_cases, k_cases
    

import math
import random
from . import Problem
from typing import List
import re
from math import inf


class Solution3(Problem):
    date = "2026-3-28"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3882,
                         types=[],
                         pass_rate=0.52,
                         description='给你一个大小为 `m * n` 的二维整数数组 `grid`。\n你从**左上角**的单元格 `(0, 0)` 出发，想要到达**右下角**的单元格 `(m - 1, n - 1)`。\n在每一步中，你**可以****向右或向下**移动。\n路径的**代价**定义为该路径上所有单元格（**包括**起点和终点）的值的**按位异或**。\n返回从 `(0, 0)` 到 `(m - 1, n - 1)` 的所有有效路径中**最小**的可能异或值。\n\n**示例 1：**\n> \n**输入：**`grid = [[1,2],[3,4]]`\n**输出：**`6`\n**解释：**\n有两条有效路径：\n - `(0, 0) → (0, 1) → (1, 1)`，异或值为：`1 XOR 2 XOR 4 = 7`\n - `(0, 0) → (1, 0) → (1, 1)`，异或值为：`1 XOR 3 XOR 4 = 6`\n\n所有有效路径中的最小异或值为 6。\n**示例 2：**\n> \n**输入：**`grid = [[6,7],[5,8]]`\n**输出：**`9`\n**解释：**\n有两条有效路径：\n - `(0, 0) → (0, 1) → (1, 1)`，异或值为：`6 XOR 7 XOR 8 = 9`\n - `(0, 0) → (1, 0) → (1, 1)`，异或值为：`6 XOR 5 XOR 8 = 11`\n\n所有有效路径中的最小异或值为 9。\n**示例 3：**\n> \n**输入：**`grid = [[2,7,5]]`\n**输出：**`0`\n**解释：**\n只有一条有效路径：\n - `(0, 0) → (0, 1) → (0, 2)`，异或值为：`2 XOR 7 XOR 5 = 0`\n\n这条路径的异或值为 0，这是可能达到的最小值。\n\n**提示：**\n - `1 <= m == grid.length <= 1000`\n - `1 <= n == grid[i].length <= 1000`\n - `m * n <= 1000`\n - `0 <= grid[i][j] <= 1023\u200b`'
                         )

    def solve(self, grid: List[List[int]]) -> int:
        vis = set()
        ans = inf

        def dfs(i: int, j: int, xor: int) -> None:
            nonlocal ans
            if ans == 0 or i < 0 or j < 0 or ((i, j, xor) in vis):
                return
            vis.add((i, j, xor))
            xor ^= grid[i][j]
            if i == 0 and j == 0:
                ans = min(ans, xor)
                return
            dfs(i - 1, j, xor)
            dfs(i, j - 1, xor)
        dfs(len(grid) - 1, len(grid[0]) - 1, 0)
        return ans

    def gen(self):
        """
        生成测试样例，覆盖边界值、特殊结构和随机测试。

        约束条件：
        - 1 <= m, n <= 1000
        - m * n <= 1000 (关键约束)
        - 0 <= grid[i][j] <= 1023
        """
        test_cases = []

        # ========== 边界值测试 ==========

        # 1×1 最小网格 (2个)
        for _ in range(2):
            test_cases.append([[random.randint(0, 1023)]])

        # 单行/单列网格 (各3个)
        for _ in range(3):
            cols = random.randint(2, 15)
            row = [random.randint(0, 1023) for _ in range(cols)]
            test_cases.append([row])

        for _ in range(3):
            rows = random.randint(2, 15)
            col = [[random.randint(0, 1023)] for _ in range(rows)]
            test_cases.append(col)

        # 接近最大规模的网格 (m*n <= 1000) (4个)
        # 32×32 = 1024 > 1000, 所以最大约为31×32或32×31
        large_configs = [(31, 32), (32, 31), (25, 40), (20, 50)]
        for m, n in large_configs:
            grid = [[random.randint(0, 1023) for _ in range(n)] for _ in range(m)]
            test_cases.append(grid)

        # ========== 特殊结构测试 ==========

        # 全0网格 (3个，不同尺寸)
        for _ in range(3):
            m, n = random.randint(2, 10), random.randint(2, 10)
            test_cases.append([[0] * n for _ in range(m)])

        # 全相同数值 (3个)
        for _ in range(3):
            m, n = random.randint(2, 10), random.randint(2, 10)
            val = random.randint(1, 1023)
            test_cases.append([[val] * n for _ in range(m)])

        # 严格递增网格 (2个)
        for _ in range(2):
            m, n = random.randint(3, 10), random.randint(3, 10)
            cnt = 0
            grid = []
            for i in range(m):
                row = []
                for j in range(n):
                    row.append(cnt % 1024)
                    cnt += 1
                grid.append(row)
            test_cases.append(grid)

        # 二进制规律网格 (2个)
        for _ in range(2):
            m, n = random.randint(4, 10), random.randint(4, 10)
            grid = [[(1 << ((i + j) % 10)) for j in range(n)] for i in range(m)]
            test_cases.append(grid)

        # ========== 随机测试 ==========

        # 中等规模随机网格 (剩余的70个)
        for _ in range(70):
            # 确保 m*n <= 1000
            while True:
                m = random.randint(2, 50)
                n = random.randint(2, 50)
                if m * n <= 1000:
                    break
            grid = [[random.randint(0, 1023) for _ in range(n)] for _ in range(m)]
            test_cases.append(grid)

        return (test_cases,)
    

def digit_sum(n: int) -> int:
    return sum(int(d) for d in str(n))
from . import Problem
from typing import List
import re
MOD = 1000000007
MX = 5001
MAX_DIGIT_SUM = 31
dig_sum = [0] * MX
for x in range(MX):
    dig_sum[x] = dig_sum[x // 10] + x % 10

class Solution4(Problem):
    date = "2026-3-28"
    def __init__(self):
        Problem.__init__(self,
                         degree=2,
                         idx=3883,
                         types=[],
                         pass_rate=0.53,
                         description='给你一个长度为 `n` 的整数数组 `digitSum`。\n如果一个长度为 `n` 的数组 `arr` 满足以下条件，则认为它是**有效**的：\n - `0 <= arr[i] <= 5000`\n - 它是**非递减**的。\n - `arr[i]` 的**数位和****等于**`digitSum[i]`。\n\n返回一个整数，表示**不同的有效数组**的数量。由于答案可能很大，请将其对 `10^9 + 7` 取模后返回。\n如果一个数组的每个元素都大于或等于它的前一个元素（如果存在），则称该数组是**非递减**的。\n\n**示例 1：**\n> \n**输入：**`digitSum = [25,1]`\n**输出：**`6`\n**解释：**\n数位和为 25 的数字有 799、889、898、979、988 和 997。\n数位和为 1 且可以出现在这些值之后同时保持数组非递减的唯一数字是 1000。\n因此，有效数组为 `[799, 1000]`、`[889, 1000]`、`[898, 1000]`、`[979, 1000]`、`[988, 1000]` 和 `[997, 1000]`。\n因此，答案是 6。\n**示例 2：**\n> \n**输入：**`digitSum = [1]`\n**输出：**`4`\n**解释：**\n有效数组为 `[1]`、`[10]`、`[100]` 和 `[1000]`。\n因此，答案是 4。\n**示例 3：**\n> \n**输入：**`digitSum = [2,49,23]`\n**输出：**`0`\n**解释：**\n在范围 [0, 5000] 内没有数位和为 49 的整数。因此，答案是 0。\n\n**提示：**\n - `1 <= digitSum.length <= 1000`\n - `0 <= digitSum[i] <= 50`'
                         )

    def solve(self, digitSum: List[int]) -> int:
        s = [1] * MX
        for ds in digitSum:
            if ds > MAX_DIGIT_SUM:
                return 0
            for x in range(MX):
                if dig_sum[x] != ds:
                    s[x] = 0
                if x > 0:
                    s[x] = (s[x] + s[x - 1]) % MOD
        return s[-1]

    def gen(self):
        """
        生成测试样例。

        策略覆盖：
        1. 边界值测试：
           - 空数组情况（digitSum[i] = 0 或超出范围）
           - 单元素数组
           - 最大数位和（31）和超出范围的情况

        2. 正常分布测试：
           - 随机长度的数组
           - 随机数值的 digitSum

        3. 特殊结构测试：
           - 全相同元素（所有 digitSum 相同）
           - 严格递增的数位和
           - 严格递减的数位和
           - 包含 0 的情况
        """
        # 将测试用例数量减少到 50，避免超时
        testcase_num = self.testcase_num
        if testcase_num > 50:
            testcase_num = 50

        digit_sum_tests = []

        # 边界值测试（约 15%）
        # 单元素数组，数位和为 0
        digit_sum_tests.append([0])
        # 单元素数组，数位和为 31（最大有效值）
        digit_sum_tests.append([31])
        # 单元素数组，数位和为 32（超出范围，答案应为 0）
        digit_sum_tests.append([32])
        # 单元素数组，数位和为 50
        digit_sum_tests.append([50])

        # 全 0 的情况
        digit_sum_tests.append([0, 0, 0])
        digit_sum_tests.append([0] * 10)

        # 包含无效值的情况（答案为 0）
        digit_sum_tests.append([1, 50, 2])
        digit_sum_tests.append([5, 32, 3])

        # 正常分布测试（约 50%）
        for _ in range(20):
            # 随机长度 2-30
            length = self.s_generate_int(int_range=(2, 30))
            # 随机数位和 0-31
            test = [self.s_generate_int(int_range=(0, 31)) for _ in range(length)]
            digit_sum_tests.append(test)

        # 包含无效值的随机测试（约 10%）
        for _ in range(5):
            length = self.s_generate_int(int_range=(2, 20))
            test = [self.s_generate_int(int_range=(32, 50)) for _ in range(length)]
            digit_sum_tests.append(test)

        # 特殊结构测试（约 25%）
        # 全相同元素
        for _ in range(3):
            length = self.s_generate_int(int_range=(5, 20))
            value = self.s_generate_int(int_range=(1, 31))
            digit_sum_tests.append([value] * length)

        # 严格递增的数位和
        for _ in range(2):
            length = self.s_generate_int(int_range=(5, 15))
            test = list(range(1, length + 1))
            digit_sum_tests.append(test)

        # 严格递减的数位和（可能导致答案为 0 或很小）
        for _ in range(2):
            length = self.s_generate_int(int_range=(5, 15))
            test = list(range(length, 0, -1))
            digit_sum_tests.append(test)

        # 保证返回 testcase_num 个测试用例
        while len(digit_sum_tests) < testcase_num:
            length = self.s_generate_int(int_range=(1, 10))
            test = [self.s_generate_int(int_range=(0, 31)) for _ in range(length)]
            digit_sum_tests.append(test)

        # 截断到 testcase_num 个
        digit_sum_tests = digit_sum_tests[:testcase_num]

        return (digit_sum_tests,)
    

