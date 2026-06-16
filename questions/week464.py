from bisect import bisect_left, bisect_right
from functools import cache
from itertools import accumulate

from . import Problem as Testing, ProblemType
from typing import List


class Solution1(Testing):
    date = "2025-8-24"
    def __init__(self):
        Testing.__init__(self,
                         degree=0,
                         idx=3658,
                         types=[ProblemType.Math, ProblemType.NumberTheory],
                         pass_rate=0.843,
                         description="给你一个整数 `n`。请你计算以下两个值的 **最大公约数**（GCD）：\n\n- `sumOdd`：前 `n` 个奇数的总和。\n- `sumEven`：前 `n` 个偶数的总和。\n\n返回 `sumOdd` 和 `sumEven` 的 GCD。\n\n \n\n**示例 1：**\n\n**输入：** n = 4\n\n**输出：** 4\n\n**解释：**\n\n- 前 4 个奇数的总和 `sumOdd = 1 + 3 + 5 + 7 = 16`\n- 前 4 个偶数的总和 `sumEven = 2 + 4 + 6 + 8 = 20`\n\n因此，`GCD(sumOdd, sumEven) = GCD(16, 20) = 4`。\n\n**示例 2：**\n\n**输入：** n = 5\n\n**输出：** 5\n\n**解释：**\n\n- 前 5 个奇数的总和 `sumOdd = 1 + 3 + 5 + 7 + 9 = 25`\n- 前 5 个偶数的总和 `sumEven = 2 + 4 + 6 + 8 + 10 = 30`\n\n因此，`GCD(sumOdd, sumEven) = GCD(25, 30) = 5`。\n\n \n\n**提示：**\n\n- `1 <= n <= 1000`"
                         )

    def solve(self, n: int) -> int:
        return n

    def gen(self):
        return self.generate_int(int_range=(1, 1000)),


from collections import Counter


class Solution2(Testing):
    date = "2025-8-24"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3659,
                         types=[ProblemType.Array, ProblemType.HashTable, ProblemType.Counting],
                         pass_rate=0.459,
                         description="给你一个整数数组 `nums` 和一个整数 `k`。\n\n请你判断是否可以将 `nums` 中的所有元素分成一个或多个组，使得：\n\n- 每个组 **恰好** 包含 `k` 个元素。\n- 每组中的元素 **互不相同**。\n- `nums` 中的每个元素 **必须** 被分配到 **恰好一个** 组中。\n\n如果可以完成这样的分组，返回 `true`；否则，返回 `false`。\n\n \n\n**示例 1：**\n\n**输入：** nums = [1,2,3,4], k = 2\n\n**输出：** true\n\n**解释：**\n\n一种可能的分组方式是分成 2 组：\n\n- 组 1：`[1, 2]`\n- 组 2：`[3, 4]`\n\n每个组包含 `k = 2` 个不同的元素，并且所有元素都被恰好使用一次。\n\n**示例 2：**\n\n**输入：** nums = [3,5,2,2], k = 2\n\n**输出：** true\n\n**解释：**\n\n一种可能的分组方式是分成 2 组：\n\n- 组 1：`[2, 3]`\n- 组 2：`[2, 5]`\n\n每个组包含 `k = 2` 个不同的元素，并且所有元素都被恰好使用一次。\n\n**示例 3：**\n\n**输入：** nums = [1,5,2,3], k = 3\n\n**输出：** false\n\n**解释：**\n\n无法用所有值恰好一次性组成含有 `k = 3` 个不同元素的组。\n\n \n\n**提示：**\n\n- `1 <= nums.length <= 10**5`\n- `1 <= nums[i] <= 10**5`\n- `1 <= k <= nums.length`"
                         )

    def solve(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k:
            return False
        mx = max(Counter(nums).values())
        return mx * k <= n

    def _gen(self):
        nums = self.s_generate_list_int(int_range=(1, 10000), list_length_range=(1, 1000))
        k = self.s_generate_int(int_range=(1, len(nums)))
        return nums, k

from math import inf
class Solution3(Testing):
    date = "2025-8-24"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3660,
                         types=[ProblemType.Array, ProblemType.DynamicPlanning],
                         pass_rate=0.26,
                         description="给你一个整数数组 `nums` 和一个整数 `k`。\n\n你可以 **多次** 选择 **连续** 子数组 `nums`，其元素和可以被 `k` 整除，并将其删除；每次删除后，剩余元素会填补空缺。\n\n返回在执行任意次数此类删除操作后，`nums` 的最小可能 **和**。\n\n \n\n**示例 1：**\n\n**输入：** nums = [1,1,1], k = 2\n\n**输出：** 1\n\n**解释：**\n\n- 删除子数组 `nums[0..1] = [1, 1]`，其和为 2（可以被 2 整除），剩余 `[1]`。\n- 剩余数组的和为 1。\n\n**示例 2：**\n\n**输入：** nums = [3,1,4,1,5], k = 3\n\n**输出：** 5\n\n**解释：**\n\n- 首先删除子数组 `nums[1..3] = [1, 4, 1]`，其和为 6（可以被 3 整除），剩余数组为 `[3, 5]`。\n- 然后删除子数组 `nums[0..0] = [3]`，其和为 3（可以被 3 整除），剩余数组为 `[5]`。\n- 剩余数组的和为 5。\n\n \n\n**提示：**\n\n- `1 <= nums.length <= 10**5`\n- `1 <= nums[i] <= 10**6`\n- `1 <= k <= 10**5`"
                         )

    def solve(self, nums: list[int]) -> list[int]:
        n = len(nums)
        pre_max = list(accumulate(nums, max))  # nums 的前缀最大值

        ans = [0] * n
        suf_min = inf
        for i in range(n - 1, -1, -1):
            ans[i] = pre_max[i] if pre_max[i] <= suf_min else ans[i + 1]
            suf_min = min(suf_min, nums[i])
        return ans


    def gen(self):
        return self.generate_list_int(list_length_range=(1, 100), int_range=(1, 10000)),


class Solution4(Testing):
    date = "2025-8-24"
    def __init__(self):
        Testing.__init__(self,
                         degree=2,
                         idx=3661,
                         types=[ProblemType.Array, ProblemType.Bisearch, ProblemType.DynamicPlanning, ProblemType.Sorting],
                         pass_rate=0.441,
                         description="一条无限长的直线上分布着一些机器人和墙壁。给你整数数组 robots ，distance 和 walls：\n\nrobots[i] 是第 i 个机器人的位置。\ndistance[i] 是第 i 个机器人的子弹可以行进的 最大 距离。\nwalls[j] 是第 j 堵墙的位置。\n每个机器人有 一颗 子弹，可以向左或向右发射，最远距离为 distance[i] 米。\n\n子弹会摧毁其射程内路径上的每一堵墙。机器人是固定的障碍物：如果子弹在到达墙壁前击中另一个机器人，它会 立即 在该机器人处停止，无法继续前进。\n\n返回机器人可以摧毁墙壁的 最大 数量。\n\n注意：\n\n墙壁和机器人可能在同一位置；该位置的墙壁可以被该位置的机器人摧毁。\n机器人不会被子弹摧毁。\n\n\n示例 1:\n\n输入: robots = [4], distance = [3], walls = [1,10]\n\n输出: 1\n\n解释:\n\nrobots[0] = 4 向 左 发射，distance[0] = 3，覆盖范围 [1, 4]，摧毁了 walls[0] = 1。\n因此，答案是 1。\n示例 2:\n\n输入: robots = [10,2], distance = [5,1], walls = [5,2,7]\n\n输出: 3\n\n解释:\n\nrobots[0] = 10 向 左 发射，distance[0] = 5，覆盖范围 [5, 10]，摧毁了 walls[0] = 5 和 walls[2] = 7。\nrobots[1] = 2 向 左 发射，distance[1] = 1，覆盖范围 [1, 2]，摧毁了 walls[1] = 2。\n因此，答案是 3。\n示例 3:\n输入: robots = [1,2], distance = [100,1], walls = [10]\n\n输出: 0\n\n解释:\n\n在这个例子中，只有 robots[0] 能够到达墙壁，但它向 右 的射击被 robots[1] 挡住了，因此答案是 0。\n\n**提示:**\n\n- `1 <= robots.length == distance.length <= 10**5`\n- `1 <= walls.length <= 10**5`\n- `1 <= robots[i], walls[j] <= 10**9`\n- `1 <= distance[i] <= 10**5`\n- `robots` 中的所有值都是 **互不相同** 的\n- `walls` 中的所有值都是 **互不相同** 的"
                         )

    def solve(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        a = sorted(zip(robots, distance), key=lambda p: p[0])
        walls.sort()

        @cache  # 缓存装饰器，避免重复计算 dfs（一行代码实现记忆化）
        def dfs(i: int, j: int) -> int:
            if i < 0:
                return 0

            x, d = a[i]
            # 往左射，墙的坐标范围为 [left_x, x]
            left_x = x - d
            if i > 0:
                left_x = max(left_x, a[i - 1][0] + 1)  # +1 表示不能射到左边那个机器人
            left = bisect_left(walls, left_x)
            cur = bisect_right(walls, x)
            res_left = dfs(i - 1, 0) + cur - left  # 下标在 [left, cur-1] 中的墙都能摧毁

            # 往右射，墙的坐标范围为 [x, right_x]
            right_x = x + d
            if i + 1 < n:
                x2, d2 = a[i + 1]
                if j == 0:  # 右边那个机器人往左射
                    x2 -= d2
                right_x = min(right_x, x2 - 1)  # -1 表示不能射到右边那个机器人（或者它往左射到的墙）
            right = bisect_right(walls, right_x)
            cur = bisect_left(walls, x)
            res_right = dfs(i - 1, 1) + right - cur  # 下标在 [cur, right-1] 中的墙都能摧毁

            return max(res_left, res_right)

        return dfs(n - 1, 1)

    def _gen(self):
        length = self.s_generate_int(int_range=(1, 100))
        distance = self.s_generate_list_int(list_length_range=(length, length), int_range=(1, 100))
        robots = self.s_generate_list_int(list_length_range=(length, length), int_range=(1, 1000), different=True)

        walls = self.s_generate_list_int(list_length_range=(1, 1000), int_range=(1, 1000), different=True)

        return robots, distance, walls

