import random
from heapq import heapreplace
from itertools import count
from . import Problem as Testing, ProblemType
import copy
from typing import List, Tuple


class Solution1(Testing):
    date = "2025-9-21"
    def __init__(self):
        Testing.__init__(self,
                         degree=0,
                         idx=3688,
                         types=[ProblemType.Bit, ProblemType.Array, ProblemType.Simulation],
                         pass_rate=0.842,
                         description="给你一个整数数组 `nums`。\n\n返回数组中所有 **偶数** 的按位 **或** 运算结果。\n\n如果 `nums` 中没有偶数，返回 0。\n\n \n\n**示例 1：**\n\n**输入：** nums = [1,2,3,4,5,6]\n\n**输出：** 6\n\n**解释：**\n\n偶数为 2、4 和 6。它们的按位或运算结果是 6。\n\n**示例 2：**\n\n**输入：** nums = [7,9,11]\n\n**输出：** 0\n\n**解释：**\n\n数组中没有偶数，因此结果为 0。\n\n**示例 3：**\n\n**输入：** nums = [1,8,16]\n\n**输出：** 24\n\n**解释：**\n\n偶数为 8 和 16。它们的按位或运算结果是 24。\n\n \n\n**提示：**\n\n- `1 <= nums.length <= 100`\n- `1 <= nums[i] <= 100`"
                         )

    def solve(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            if x % 2 == 0:
                ans |= x
        return ans

    def gen(self):
        return self.generate_list_int(list_length_range=(1, 100), int_range=(1, 100)),



class Solution2(Testing):
    date = "2025-9-21"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3689,
                         types=[ProblemType.Greedy, ProblemType.Array],
                         pass_rate=0.612,
                         description="给定一个长度为 `n` 的整数数组 `nums` 和一个整数 `k`。\n\n你必须从 `nums` 中选择 **恰好** `k` 个非空子数组 `nums[l..r]`。子数组可以重叠，同一个子数组（相同的 `l` 和 `r`）**可以** 被选择超过一次。\n\n子数组 `nums[l..r]` 的 **值** 定义为：`max(nums[l..r]) - min(nums[l..r])`。\n\n**总值** 是所有被选子数组的 **值** 之和。\n\n返回你能实现的 **最大** 可能总值。\n\n**子数组** 是数组中连续的 **非空** 元素序列。\n\n \n\n**示例 1:**\n\n**输入:** nums = [1,3,2], k = 2\n\n**输出:** 4\n\n**解释:**\n\n一种最优的方法是：\n\n- 选择 `nums[0..1] = [1, 3]`。最大值为 3，最小值为 1，得到的值为 `3 - 1 = 2`。\n- 选择 `nums[0..2] = [1, 3, 2]`。最大值仍为 3，最小值仍为 1，所以值也是 `3 - 1 = 2`。\n\n将它们相加得到 `2 + 2 = 4`。\n\n**示例 2:**\n\n**输入:** nums = [4,2,5,1], k = 3\n\n**输出:** 12\n\n**解释:**\n\n一种最优的方法是：\n\n- 选择 `nums[0..3] = [4, 2, 5, 1]`。最大值为 5，最小值为 1，得到的值为 `5 - 1 = 4`。\n- 选择 `nums[1..3] = [2, 5, 1]`。最大值为 5，最小值为 1，所以值也是 `4`。\n- 选择 `nums[2..3] = [5, 1]`。最大值为 5，最小值为 1，所以值同样是 `4`。\n\n将它们相加得到 `4 + 4 + 4 = 12`。\n\n \n\n**提示:**\n\n- `1 <= n == nums.length <= 5 * 10**4`\n- `0 <= nums[i] <= 10**9`\n- `1 <= k <= 10**5`"
                         )

    def solve(self, nums: List[int], k: int) -> int:
        return (max(nums) - min(nums)) * k

    def gen(self):
        return self.generate_list_int(list_length_range=(1, 500), int_range=(0, 1000)), self.generate_int(int_range=(1, 100))


class Solution3(Testing):
    date = "2025-9-21"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3690,
                         types=[],
                         pass_rate=0.595,
                         description="给你两个长度为 `n` 的整数数组 `nums1` 和 `nums2`。你可以对 `nums1` 执行任意次下述的 **拆分合并操作**：\n\n1. 选择一个子数组 `nums1[L..R]`。\n2. 移除该子数组，留下前缀 `nums1[0..L-1]`（如果 `L = 0` 则为空）和后缀 `nums1[R+1..n-1]`（如果 `R = n - 1` 则为空）。\n3. 将移除的子数组（按原顺序）重新插入到剩余数组的 **任意** 位置（即，在任意两个元素之间、最开始或最后面）。\n\n返回将 `nums1` 转换为 `nums2` 所需的 **最少拆分合并操作** 次数。\n\n \n\n**示例 1:**\n\n**输入:** nums1 = [3,1,2], nums2 = [1,2,3]\n\n**输出:** 1\n\n**解释:**\n\n- 拆分出子数组 `[3]` (`L = 0`, `R = 0`)；剩余数组为 `[1,2]`。\n- 将 `[3]` 插入到末尾；数组变为 `[1,2,3]`。\n\n**示例 2:**\n\n**输入:** nums1 = [1,1,2,3,4,5], nums2 = [5,4,3,2,1,1]\n\n**输出:** 3\n\n**解释:**\n\n- 移除下标 `0 - 2` 处的 `[1,1,2]`；剩余 `[3,4,5]`；将 `[1,1,2]` 插入到位置 `2`，得到 `[3,4,1,1,2,5]`。\n- 移除下标 `1 - 3` 处的 `[4,1,1]`；剩余 `[3,2,5]`；将 `[4,1,1]` 插入到位置 `3`，得到 `[3,2,5,4,1,1]`。\n- 移除下标 `0 - 1` 处的 `[3,2]`；剩余 `[5,4,1,1]`；将 `[3,2]` 插入到位置 `2`，得到 `[5,4,3,2,1,1]`。\n\n \n\n**提示:**\n\n- `2 <= n == nums1.length == nums2.length <= 6`\n- `-10**5 <= nums1[i], nums2[i] <= 10**5`\n- `nums2` 是 `nums1` 的一个 **排列**。"
                         )

    def solve(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1 == nums2:
            return 0

        n = len(nums1)
        mp = {x: i for i, x in enumerate(set(nums1))}  # 用于离散化的映射表
        val1 = sum(mp[x] << (i * 3) for i, x in enumerate(nums1))
        val2 = sum(mp[x] << (i * 3) for i, x in enumerate(nums2))

        vis = {val1}
        q = [val1]
        for ans in count(1):
            tmp = q
            q = []
            for a in tmp:
                for r in range(1, n + 1):  # 为方便实现，先枚举 r，再枚举 l
                    v = a & ((1 << (r * 3)) - 1)
                    for l in range(r):
                        sub = v >> (l * 3)
                        b = a & ((1 << (l * 3)) - 1) | a >> (r * 3) << (l * 3)  # 从 a 中移除 sub
                        for i in range(n - r + l + 1):
                            c = b & ((1 << (i * 3)) - 1) | sub << (i * 3) | b >> (i * 3) << ((i + r - l) * 3)
                            if c == val2:
                                return ans
                            if c not in vis:
                                vis.add(c)
                                q.append(c)


    def _gen(self):
        n = self.s_generate_int((2, 6))
        nums = self.s_generate_list_int(list_length_range=(n, n), int_range=(1, 1000))
        nums2 = copy.deepcopy(nums)
        random.shuffle(nums2)
        return nums, nums2


def op(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    return min(a[0], b[0]), max(a[1], b[1])

class ST:
    def __init__(self, a: List[int]):
        n = len(a)
        w = n.bit_length()
        st = [[None] * n for _ in range(w)]
        st[0] = [(x, x) for x in a]
        for i in range(1, w):
            for j in range(n - (1 << i) + 1):
                st[i][j] = op(st[i - 1][j], st[i - 1][j + (1 << (i - 1))])
        self.st = st

    # [l, r) 左闭右开
    def query(self, l: int, r: int) -> int:
        k = (r - l).bit_length() - 1
        mn, mx = op(self.st[k][l], self.st[k][r - (1 << k)])
        return mx - mn


class Solution4(Testing):
    date = "2025-9-21"
    def __init__(self):
        Testing.__init__(self,
                         testcase_num=10,
                         degree=2,
                         idx=3691,
                         types=[ProblemType.Greedy, ProblemType.SegmentTree, ProblemType.Array, ProblemType.Stack],
                         pass_rate=0.297,
                         description="给你一个长度为 `n` 的整数数组 `nums` 和一个整数 `k`。\n\n你必须从 `nums` 中选择 **恰好** `k` 个 **不同** 的非空子数组 `nums[l..r]`。子数组可以重叠，但同一个子数组（相同的 `l` 和 `r`）**不能** 被选择超过一次。\n\n子数组 `nums[l..r]` 的 **值** 定义为：`max(nums[l..r]) - min(nums[l..r])`。\n\n**总值** 是所有被选子数组的 **值** 之和。\n\n返回你能实现的 **最大** 可能总值。\n\n**子数组** 是数组中连续的 **非空** 元素序列。\n\n \n\n**示例 1:**\n\n**输入:** nums = [1,3,2], k = 2\n\n**输出:** 4\n\n**解释:**\n\n一种最优的方法是：\n\n- 选择 `nums[0..1] = [1, 3]`。最大值为 3，最小值为 1，得到的值为 `3 - 1 = 2`。\n- 选择 `nums[0..2] = [1, 3, 2]`。最大值仍为 3，最小值仍为 1，所以值也是 `3 - 1 = 2`。\n\n将它们相加得到 `2 + 2 = 4`。\n\n**示例 2:**\n\n**输入:** nums = [4,2,5,1], k = 3\n\n**输出:** 12\n\n**解释:**\n\n一种最优的方法是：\n\n- 选择 `nums[0..3] = [4, 2, 5, 1]`。最大值为 5，最小值为 1，得到的值为 `5 - 1 = 4`。\n- 选择 `nums[1..3] = [2, 5, 1]`。最大值为 5，最小值为 1，所以值也是 `4`。\n- 选择 `nums[2..3] = [5, 1]`。最大值为 5，最小值为 1，所以值同样是 `4`。\n\n将它们相加得到 `4 + 4 + 4 = 12`。\n\n \n\n**提示:**\n\n- `1 <= n == nums.length <= 5 * 10**4`\n- `0 <= nums[i] <= 10**9`\n- `1 <= k <= min(10**5, n * (n + 1) / 2)`"
                         )

    def solve(self, nums: List[int], k: int) -> int:
        n = len(nums)
        st = ST(nums)

        # 堆中保存 (子数组值，左端点，右端点加一)
        # 取负号变成最大堆
        h = [(-st.query(i, n), i, n) for i in range(n)]
        # 由于 h 是递减的，无需堆化

        ans = 0
        for _ in range(k):
            d, l, r = h[0]
            if d == 0:  # 堆中剩余元素全是 0
                break
            ans -= d
            heapreplace(h, (-st.query(l, r - 1), l, r - 1))
        return ans


    def _gen(self):
        n = self.s_generate_int((1, 1000))
        nums = self.s_generate_list_int(list_length_range=(n, n), int_range=(0, 100))
        k = self.s_generate_int((1, min(10, n * (n + 1) / 2)))
        return nums, k

