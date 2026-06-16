from math import degrees, acos

from . import Problem
from typing import List
import re


class Solution1(Problem):
    date = "2026-4-12"
    def __init__(self):
        Problem.__init__(self,
                         degree=0,
                         idx=3898,
                         types=[],
                         pass_rate=0.91,
                         description='给你一个大小为 `n x n` 的二维整数数组 `matrix`，以邻接矩阵形式表示一个**无向图**。该图包含 `n` 个顶点，编号从 0 到 `n - 1`。\n - `matrix[i][j] = 1` 表示顶点 `i` 与顶点 `j` 之间存在一条边。\n - `matrix[i][j] = 0` 表示顶点 `i` 与顶点 `j` 之间不存在边。\n\n顶点的**度（degree）**定义为与该顶点相连的边的数量。\n请返回一个长度为 `n` 的整数数组 `ans`，其中 `ans[i]` 表示顶点 `i` 的度。\n\n**示例 1：**\n\n> \n**输入：**`matrix = [[0,1,1],[1,0,1],[1,1,0]]`\n**输出：**`[2,2,2]`\n**解释：**\n - 顶点 0 与顶点 1 和 2 相连，因此其度为 2。\n - 顶点 1 与顶点 0 和 2 相连，因此其度为 2。\n - 顶点 2 与顶点 0 和 1 相连，因此其度为 2。\n\n因此，答案为 `[2, 2, 2]`。\n**示例 2：**\n\n> \n**输入：**`matrix = [[0,1,0],[1,0,0],[0,0,0]]`\n**输出：**`[1,1,0]`\n**解释：**\n - 顶点 0 与顶点 1 相连，因此其度为 1。\n - 顶点 1 与顶点 0 相连，因此其度为 1。\n - 顶点 2 没有与任何顶点相连，因此其度为 0。\n\n因此，答案为 `[1, 1, 0]`。\n**示例 3：**\n> \n**输入：**`matrix = [[0]]`\n**输出：**`[0]`\n**解释：**\n图中只有一个顶点，且没有任何边与其相连，因此答案为 `[0]`。\n\n**提示：**\n - `1 <= n == matrix.length == matrix[i].length <= 100`\n - `matrix[i][i] == 0`\n - `matrix[i][j]` 仅为 0 或 1\n - `matrix[i][j] == matrix[j][i]`'
                         )

    def solve(self, matrix: List[List[int]]) -> List[int]:
        return list(map(sum, matrix))

    def gen(self):
        """
        生成邻接矩阵测试样例。

        覆盖场景：
        1. 边界情况：n=1（单个顶点）
        2. 小规模图：n=2, 3, 4
        3. 中等规模图：n=10, 20
        4. 较大规模图：n=50（接近最大值100的一半）
        5. 特殊结构：完全图、空图（无边）、稀疏图、密集图

        生成策略：
        - 生成随机对称矩阵，满足邻接矩阵约束
        - 通过调整边概率控制图密度
        """
        import random
        random.seed(self.seed)

        # 生成单个对称邻接矩阵
        def generate_adj_matrix(n, edge_prob):
            """生成n x n的对称邻接矩阵，边概率为edge_prob"""
            matrix = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(i + 1, n):
                    if random.random() < edge_prob:
                        matrix[i][j] = 1
                        matrix[j][i] = 1
            # 对角线保持为0
            return matrix

        test_cases = []

        # 场景1：边界情况 - n=1（5个用例）
        for _ in range(5):
            test_cases.append([[0]])

        # 场景2：小规模图 - n=2, 3, 4（15个用例）
        for n in [2, 3, 4]:
            for _ in range(5):
                test_cases.append(generate_adj_matrix(n, 0.5))

        # 场景3：中等规模图 - n=10（20个用例）
        for _ in range(20):
            test_cases.append(generate_adj_matrix(10, 0.3))

        # 场景4：中等规模图 - n=20（20个用例）
        for _ in range(20):
            test_cases.append(generate_adj_matrix(20, 0.4))

        # 场景5：较大规模图 - n=50（15个用例）
        for _ in range(15):
            test_cases.append(generate_adj_matrix(50, 0.2))

        # 场景6：特殊结构 - 完全图（5个用例）
        for n in [3, 5, 7, 10, 15]:
            matrix = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(i + 1, n):
                    matrix[i][j] = 1
                    matrix[j][i] = 1
            test_cases.append(matrix)

        # 场景7：特殊结构 - 空图（无边，5个用例）
        for n in [3, 5, 10, 20, 30]:
            test_cases.append([[0] * n for _ in range(n)])

        # 场景8：稀疏图（边很少，10个用例）
        for _ in range(10):
            test_cases.append(generate_adj_matrix(30, 0.05))

        # 场景9：密集图（边很多，5个用例）
        for _ in range(5):
            test_cases.append(generate_adj_matrix(30, 0.9))

        return [test_cases]
    


from . import Problem
from typing import List
import re


class Solution2(Problem):
    date = "2026-4-12"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3899,
                         types=[],
                         pass_rate=0.62,
                         description='给你一个长度为 3 的正整数数组 `sides`。\n判断是否能够由 `sides` 中的三个元素作为边长，构成一个**面积为正**的三角形。\n如果可以构成这样的三角形，返回一个包含 3 个浮点数的数组，表示该三角形的三个**内角**（单位为**度**），并按**非递减顺序**排序。否则，返回一个空数组。\n与真实答案的误差在 `10^-5` 以内的结果都将被视为正确。\n\n**示例 1：**\n> \n**输入：**`sides = [3,4,5]`\n**输出：**`[36.86990,53.13010,90.00000]`\n**解释：**\n边长为 3、4、5 时，可以构成一个直角三角形。该三角形的三个内角分别约为 36.869897646°、53.130102354° 和 90°。\n**示例 2：**\n> \n**输入：**`sides = [2,4,2]`\n**输出：**`[]`\n**解释：**\n边长为 2、4、2 时，无法构成一个面积为正的三角形。\n\n**提示：**\n - `sides.length == 3`\n - `1 <= sides[i] <= 1000`'
                         )

    def solve(self, sides: List[int]) -> List[float]:
        sides.sort()
        a, b, c = sides
        if a + b <= c:
            return []
        A = degrees(acos((b * b + c * c - a * a) / (b * c * 2)))
        B = degrees(acos((a * a + c * c - b * b) / (a * c * 2)))
        return [A, B, 180 - A - B]

    def gen(self):
            """
            生成测试样例，覆盖各种三角形边长组合场景。

            覆盖场景：
            1. 能构成三角形的情况：
               - 等边三角形
               - 等腰三角形
               - 直角三角形
               - 锐角三角形
               - 钝角三角形
               - 边界值（最小和最大边长）

            2. 不能构成三角形的情况：
               - 两边之和等于第三边（面积为0）
               - 两边之和小于第三边

            3. 特殊值和随机值
            """
            import random
            sides_list = []

            # 固定测试用例：覆盖关键场景（约占50%）
            fixed_cases = []

            # 1. 能构成三角形 - 等边三角形
            fixed_cases.append([1, 1, 1])
            fixed_cases.append([100, 100, 100])
            fixed_cases.append([500, 500, 500])
            fixed_cases.append([1000, 1000, 1000])

            # 2. 能构成三角形 - 等腰三角形（锐角）
            fixed_cases.append([3, 3, 4])
            fixed_cases.append([5, 5, 8])
            fixed_cases.append([100, 100, 150])
            fixed_cases.append([200, 200, 300])

            # 3. 能构成三角形 - 直角三角形
            fixed_cases.append([3, 4, 5])
            fixed_cases.append([5, 12, 13])
            fixed_cases.append([6, 8, 10])
            fixed_cases.append([60, 80, 100])

            # 4. 能构成三角形 - 钝角三角形
            fixed_cases.append([3, 4, 6])
            fixed_cases.append([5, 6, 10])
            fixed_cases.append([100, 150, 240])

            # 5. 能构成三角形 - 锐角三角形
            fixed_cases.append([4, 5, 6])
            fixed_cases.append([7, 8, 9])
            fixed_cases.append([100, 120, 150])

            # 6. 不能构成三角形 - 两边之和等于第三边（面积为0）
            fixed_cases.append([1, 1, 2])
            fixed_cases.append([2, 3, 5])
            fixed_cases.append([100, 200, 300])

            # 7. 不能构成三角形 - 两边之和小于第三边
            fixed_cases.append([1, 1, 3])
            fixed_cases.append([2, 3, 6])
            fixed_cases.append([50, 100, 200])

            # 8. 边界值测试
            fixed_cases.append([1, 500, 500])
            fixed_cases.append([400, 600, 950])
            fixed_cases.append([1, 2, 2])
            fixed_cases.append([600, 800, 1000])
            fixed_cases.append([800, 900, 1000])
            fixed_cases.append([50, 60, 80])
            fixed_cases.append([200, 300, 400])
            fixed_cases.append([7, 10, 12])
            fixed_cases.append([20, 21, 29])
            fixed_cases.append([1, 2, 5])
            fixed_cases.append([10, 20, 50])
            fixed_cases.append([2, 2, 3])
            fixed_cases.append([2, 3, 4])
            fixed_cases.append([700, 900, 1000])
            fixed_cases.append([100, 150, 200])

            # 9. 接近边界的非三角形
            fixed_cases.append([1, 500, 501])
            fixed_cases.append([400, 500, 901])
            fixed_cases.append([500, 500, 1000])

            # 10. 更多直角三角形变体
            fixed_cases.append([8, 15, 17])
            fixed_cases.append([9, 40, 41])
            fixed_cases.append([12, 16, 20])

            # 11. 混合场景
            fixed_cases.append([333, 444, 555])
            fixed_cases.append([123, 456, 789])
            fixed_cases.append([111, 222, 333])

            # 添加固定用例（取前50个）
            for case in fixed_cases[:50]:
                sides_list.append(case)

            # 生成随机测试用例（剩余50个）
            random.seed(self.seed)
            while len(sides_list) < self.testcase_num:
                a = random.randint(1, 1000)
                b = random.randint(1, 1000)
                c = random.randint(1, 1000)
                sides_list.append([a, b, c])

            # 返回格式：元组的第i个列表对应第i个参数
            return (sides_list,)
    

import random
import string
from . import Problem
from collections import defaultdict
import re


class Solution3(Problem):
    date = "2026-4-12"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3900,
                         types=[],
                         pass_rate=0.24,
                         description='给你一个仅由字符 `\'0\'` 和 `\'1\'` 组成的二进制字符串 `s`。\n如果一个字符串中 `0` 和 `1` 的数量**相等**，则称该字符串是**平衡**字符串。\n你最多可以让\xa0`s` 中任意两个字符进行**一次**交换。之后，从 `s` 中选出一个**平衡**子串。\n返回一个整数，表示你能够选取的**平衡**子串的**最大**长度。\n**子串**是字符串中的一个连续字符序列。\n\n**示例 1：**\n> \n**输入：**`s = "100001"`\n**输出：**`4`\n**解释：**\n - 交换 `"10**0**00**1**"` 中标出的两个字符，字符串变为 `"101000"`。\n - 选择子串 `"**1010**00"`，它是平衡的，因为其中包含两个 `\'0\'` 和两个 `\'1\'`。\n\n**示例 2：**\n> \n**输入：**`s = "111"`\n**输出：**`0`\n**解释：**\n - 可以选择不进行任何交换。\n - 选择空子串。空子串也是平衡的，因为它包含 0 个 `\'0\'` 和 0 个 `\'1\'`。\n\n**提示：**\n - `1 <= s.length <= 10^5`\n - `s` 仅由字符 `\'0\'` 和 `\'1\'` 组成。'
                         )

    def solve(self, s: str) -> int:
        total0 = s.count('0')
        total1 = len(s) - total0
        pos = defaultdict(list)
        pos[0] = [-1]
        ans = 0
        pre = 0
        for i, ch in enumerate(s):
            pre += 1 if ch == '1' else -1
            if len(pos[pre]) < 2:
                pos[pre].append(i)
            ans = max(ans, i - pos[pre][0])
            if pre - 2 in pos:
                p = pos[pre - 2]
                if (i - p[0] - 2) // 2 < total0:
                    ans = max(ans, i - p[0])
                elif len(p) > 1:
                    ans = max(ans, i - p[1])
            if pre + 2 in pos:
                p = pos[pre + 2]
                if (i - p[0] - 2) // 2 < total1:
                    ans = max(ans, i - p[0])
                elif len(p) > 1:
                    ans = max(ans, i - p[1])
        return ans

    def gen(self):
        """
        生成二进制字符串s的测试样例。

        覆盖策略：
        1. 小规模边界测试：长度1-10，包括单字符、最小平衡等
        2. 特殊结构：全0、全1、交替、连续0或1等
        3. 不同0/1比例：0远多于1、1远多于0、接近平衡等
        4. 需要交换的情况：交换后能平衡、交换后仍不平衡
        5. 随机测试：中等到大规模随机字符串

        注意：题目限制字符串长度可达10^5，但为避免超时，测试时将最大长度控制在1000以内
        """
        # === 边界和特殊用例 ===
        special_cases = []

        # 单字符情况
        special_cases.extend(["0", "1"])

        # 最小平衡和接近平衡
        special_cases.extend(["01", "10", "001", "010", "100"])

        # 全0和全1（不同长度）
        special_cases.extend(["00", "11", "000", "111", "0000", "1111", "00000", "11111"])

        # 已经平衡的字符串
        special_cases.extend(["0011", "0101", "1010", "1100", "000111", "111000"])

        # 交替模式
        special_cases.extend(["010101", "101010", "01010101"])

        # 集中0或1（交换可能有用）
        special_cases.extend(["00001111", "11110000", "0000011111", "1111100000"])

        # 极端不平衡（0远多于1）
        special_cases.extend(["00001", "000001", "0000001"])

        # 极端不平衡（1远多于0）
        special_cases.extend(["11110", "111110", "1111110"])

        # 示例和变体
        special_cases.extend(["100001", "100000001", "000000011111111"])

        # 0和1数量相等但需要交换
        special_cases.extend(["001011", "110100", "00011011", "11100100"])

        # 需要交换才能达到最佳平衡
        special_cases.extend(["000010111", "111101000", "00000101111"])

        # === 随机生成的测试用例 ===
        random_cases = []

        # 小规模随机（长度2-20）
        for _ in range(15):
            random_cases.append(self.s_generate_string(vocab='01', length_range=(2, 20)))

        # 中小规模（长度20-100）
        for _ in range(15):
            random_cases.append(self.s_generate_string(vocab='01', length_range=(20, 100)))

        # 中等规模（长度100-300）
        for _ in range(10):
            random_cases.append(self.s_generate_string(vocab='01', length_range=(100, 300)))

        # 较大规模（长度300-800）
        for _ in range(8):
            random_cases.append(self.s_generate_string(vocab='01', length_range=(300, 800)))

        # 大规模（长度800-1000，接近但不超过1000）
        for _ in range(5):
            random_cases.append(self.s_generate_string(vocab='01', length_range=(800, 1000)))

        # 合并所有测试用例
        all_cases = special_cases + random_cases

        # 返回单列表（因为只有一个参数s）
        return [all_cases]
    

import math
from . import Problem
from typing import List
import re
from math import gcd
class SegmentTree:

    def __init__(self, arr, target_gcd: int, default=0):
        if isinstance(arr, int):
            arr = [default] * arr
        n = len(arr)
        self._target_gcd = target_gcd
        self._n = n
        self._tree = [0] * (2 << (n - 1).bit_length())
        self._build(arr, 1, 0, n - 1)

    def _maintain(self, node: int) -> None:
        self._tree[node] = gcd(self._tree[node * 2], self._tree[node * 2 + 1])

    def _build(self, a: List[int], node: int, l: int, r: int) -> None:
        if l == r:
            self._tree[node] = a[l] if a[l] % self._target_gcd == 0 else 0
            return
        m = (l + r) // 2
        self._build(a, node * 2, l, m)
        self._build(a, node * 2 + 1, m + 1, r)
        self._maintain(node)

    def _update(self, node: int, l: int, r: int, i: int, val: int) -> None:
        if l == r:
            self._tree[node] = val if val % self._target_gcd == 0 else 0
            return
        m = (l + r) // 2
        if i <= m:
            self._update(node * 2, l, m, i, val)
        else:
            self._update(node * 2 + 1, m + 1, r, i, val)
        self._maintain(node)

    def _query(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql > qr:
            return 0
        if ql <= l and r <= qr:
            return self._tree[node]
        m = (l + r) // 2
        if qr <= m:
            return self._query(node * 2, l, m, ql, qr)
        if ql > m:
            return self._query(node * 2 + 1, m + 1, r, ql, qr)
        l_res = self._query(node * 2, l, m, ql, qr)
        r_res = self._query(node * 2 + 1, m + 1, r, ql, qr)
        return gcd(l_res, r_res)

    def update(self, i: int, val: int) -> None:
        self._update(1, 0, self._n - 1, i, val)

    def query(self, ql: int, qr: int) -> int:
        return self._query(1, 0, self._n - 1, ql, qr)

    def query_all(self) -> int:
        return self._tree[1]

    def check(self, n: int) -> bool:
        return any((gcd(self.query(0, i - 1), self.query(i + 1, n - 1)) == self._target_gcd for i in range(n)))

class Solution4(Problem):
    date = "2026-4-12"
    def __init__(self):
        Problem.__init__(self,
                         degree=2,
                         idx=3901,
                         types=[],
                         pass_rate=0.4,
                         description='给你一个长度为 `n` 的整数数组 `nums` 和一个整数 `p`。\n如果 `nums` 的一个**非空子序列**满足以下条件，则称其为**好子序列**：\n - 其长度**严格小于**`n`。\n - 其所有元素的**最大公约数（GCD）**恰好等于 `p`。\n\n另给定一个长度为 `q` 的二维整数数组 `queries`，其中 `queries[i] = [ind_i, val_i]` 表示你需要将 `nums[ind_i]` 更新为 `val_i`。\n在每次查询更新后，判断当前数组中是否存在**任意一个好子序列**。\n返回一个整数，表示使得数组中存在**好子序列**的查询**次数**。\n**子序列**是指通过删除原序列中的某些元素或不删除任何元素，并且不改变剩余元素相对顺序后得到的序列。\n`gcd(a, b)` 表示 `a` 和 `b` 的**最大公约数**。\n\n**示例 1：**\n> \n**输入：**`nums = [4,8,12,16], p = 2, queries = [[0,3],[2,6]]`\n**输出：**`1`\n**解释：**\n| i | `[ind_i, val_i]` | 操作 | 更新后的 `nums` | 是否存在好子序列 |\n| --- | --- | --- | --- | --- |\n| 0 | `[0, 3]` | 将 `nums[0]` 更新为 `3` | `[3, 8, 12, 16]` | 否，因为不存在最大公约数恰好为 `p = 2` 的子序列 |\n| 1 | `[2, 6]` | 将 `nums[2]` 更新为 `6` | `[3, 8, 6, 16]` | 是，子序列 `[8, 6]` 的最大公约数恰好为 `p = 2` |\n\n因此，答案是 1。\n**示例 2：**\n> \n**输入：**`nums = [4,5,7,8], p = 3, queries = [[0,6],[1,9],[2,3]]`\n**输出：**`2`\n**解释：**\n| i | `[ind_i, val_i]` | 操作 | 更新后的 `nums` | 是否存在好子序列 |\n| --- | --- | --- | --- | --- |\n| 0 | `[0, 6]` | 将 `nums[0]` 更新为 `6` | `[6, 5, 7, 8]` | 否，因为不存在最大公约数恰好为 `p = 3` 的子序列 |\n| 1 | `[1, 9]` | 将 `nums[1]` 更新为 `9` | `[6, 9, 7, 8]` | 是，子序列 `[6, 9]` 的最大公约数恰好为 `p = 3` |\n| 2 | `[2, 3]` | 将 `nums[2]` 更新为 `3` | `[6, 9, 3, 8]` | 是，子序列 `[6, 9, 3]` 的最大公约数恰好为 `p = 3` |\n\n因此，答案是 2。\n**示例 3：**\n> \n**输入：**`nums = [5,7,9], p = 2, queries = [[1,4],[2,8]]`\n**输出：**`0`\n**解释：**\n| i | `[ind_i, val_i]` | 操作 | 更新后的 `nums` | 是否存在好子序列 |\n| --- | --- | --- | --- | --- |\n| 0 | `[1, 4]` | 将 `nums[1]` 更新为 `4` | `[5, 4, 9]` | 否，因为不存在最大公约数恰好为 `p = 2` 的子序列 |\n| 1 | `[2, 8]` | 将 `nums[2]` 更新为 `8` | `[5, 4, 8]` | 否，因为不存在最大公约数恰好为 `p = 2` 的子序列 |\n\n因此，答案是 0。\n\n**提示：**\n - `2 <= n == nums.length <= 5 * 10^4`\n - `1 <= nums[i] <= 5 * 10^4`\n - `1 <= queries.length <= 5 * 10^4`\n - `queries[i] = [ind_i, val_i]`\n - `1 <= val_i, p <= 5 * 10^4`\n - `0 <= ind_i <= n - 1`'
                         )

    def solve(self, nums: List[int], p: int, queries: List[List[int]]) -> int:
        n = len(nums)
        cnt_p = sum((x % p == 0 for x in nums))
        t = SegmentTree(nums, p)
        ans = 0
        for i, x in queries:
            if nums[i] % p == 0:
                cnt_p -= 1
            if x % p == 0:
                cnt_p += 1
            nums[i] = x
            t.update(i, x)
            if t.query_all() == p and (cnt_p < n or n > 6 or t.check(n)):
                ans += 1
        return ans

    def gen(self):
        """
        生成测试样例：
        - nums: 整数数组，范围 [2, 15]
        - p: 目标 GCD，范围 [1, 20]
        - queries: 更新查询列表，范围 [3, 8]

        覆盖场景：
        1. 边界值：n=2, 最小/最大查询数
        2. 全部元素能被 p 整除
        3. 全部元素不能被 p 整除
        4. 混合情况
        5. 更新后 GCD 恰好为 p 的情况
        """
        import random
        from math import gcd

        # 减少测试用例数量以避免超时
        self.testcase_num = 30
        random.seed(self.seed)

        nums_list = []
        p_list = []
        queries_list = []

        # 场景1：边界值 - n=2, 最小查询数=3
        for _ in range(3):
            n = 2
            p = random.randint(2, 10)
            nums = [random.randint(1, 20) for _ in range(n)]
            q = random.randint(3, 5)
            queries = []
            for _ in range(q):
                idx = random.randint(0, n-1)
                val = random.randint(1, 20)
                queries.append([idx, val])
            nums_list.append(nums)
            p_list.append(p)
            queries_list.append(queries)

        # 场景2：全部元素能被 p 整除
        for _ in range(5):
            n = random.randint(3, 8)
            p = random.randint(2, 10)
            nums = [random.randint(1, 5) * p for _ in range(n)]
            q = random.randint(3, 6)
            queries = []
            for _ in range(q):
                idx = random.randint(0, n-1)
                val = random.randint(1, 5) * p
                queries.append([idx, val])
            nums_list.append(nums)
            p_list.append(p)
            queries_list.append(queries)

        # 场景3：全部元素不能被 p 整除
        for _ in range(5):
            n = random.randint(3, 8)
            p = random.randint(2, 10)
            nums = []
            for _ in range(n):
                val = random.randint(1, 30)
                while val % p == 0:
                    val = random.randint(1, 30)
                nums.append(val)
            q = random.randint(3, 6)
            queries = []
            for _ in range(q):
                idx = random.randint(0, n-1)
                val = random.randint(1, 30)
                while val % p == 0:
                    val = random.randint(1, 30)
                queries.append([idx, val])
            nums_list.append(nums)
            p_list.append(p)
            queries_list.append(queries)

        # 场景4：混合情况 - 部分元素能被 p 整除
        for _ in range(8):
            n = random.randint(4, 10)
            p = random.randint(2, 10)
            nums = []
            for _ in range(n):
                if random.random() < 0.5:
                    nums.append(random.randint(1, 5) * p)
                else:
                    val = random.randint(1, 30)
                    while val % p == 0:
                        val = random.randint(1, 30)
                    nums.append(val)
            q = random.randint(4, 8)
            queries = []
            for _ in range(q):
                idx = random.randint(0, n-1)
                if random.random() < 0.5:
                    val = random.randint(1, 5) * p
                else:
                    val = random.randint(1, 30)
                queries.append([idx, val])
            nums_list.append(nums)
            p_list.append(p)
            queries_list.append(queries)

        # 场景5：确保存在更新后 GCD 恰好为 p 的情况
        for _ in range(4):
            n = random.randint(4, 8)
            p = random.randint(2, 10)
            # 先生成一个整体 GCD 为 p 的数组
            nums = [p * random.randint(1, 3) for _ in range(n)]
            q = random.randint(4, 6)
            queries = []
            for _ in range(q):
                idx = random.randint(0, n-1)
                val = p * random.randint(1, 3)
                queries.append([idx, val])
            nums_list.append(nums)
            p_list.append(p)
            queries_list.append(queries)

        # 场景6：随机场景
        for _ in range(5):
            n = random.randint(5, 15)
            p = random.randint(1, 20)
            nums = [random.randint(1, 100) for _ in range(n)]
            q = random.randint(5, 8)
            queries = []
            for _ in range(q):
                idx = random.randint(0, n-1)
                val = random.randint(1, 100)
                queries.append([idx, val])
            nums_list.append(nums)
            p_list.append(p)
            queries_list.append(queries)

        return nums_list, p_list, queries_list
    

