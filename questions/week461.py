import random
from . import Problem as Testing, ProblemType

from ..testcase_sampler import _generate_int, _generate_string, _generate_list_int
from typing import List


class Solution1(Testing):
    date = "2025-8-3"
    def __init__(self):
        Testing.__init__(self,
                         degree=0,
                         idx=3637,
                         types=[ProblemType.Array],
                         pass_rate=0.403,
                         description="给你一个长度为 `n` 的整数数组 `nums`。\n\n如果存在索引 `0 < p < q < n − 1`，使得数组满足以下条件，则称其为 **三段式数组（trionic）**：\n\n- `nums[0...p]` **严格** 递增，\n- `nums[p...q]` **严格** 递减，\n- `nums[q...n − 1]` **严格** 递增。\n\n如果 `nums` 是三段式数组，返回 `true`；否则，返回 `false`。\n\n \n\n**示例 1:**\n\n**输入:** nums = [1,3,5,4,2,6]\n\n**输出:** true\n\n**解释:**\n\n选择 `p = 2`, `q = 4`：\n\n- `nums[0...2] = [1, 3, 5]` 严格递增 (`1 < 3 < 5`)。\n- `nums[2...4] = [5, 4, 2]` 严格递减 (`5 > 4 > 2`)。\n- `nums[4...5] = [2, 6]` 严格递增 (`2 < 6`)。\n\n**示例 2:**\n\n**输入:** nums = [2,1,3]\n\n**输出:** false\n\n**解释:**\n\n无法选出能使数组满足三段式要求的 `p` 和 `q` 。\n\n \n\n**提示:**\n\n- `3 <= n <= 100`\n- `-1000 <= nums[i] <= 1000`"
                         )

    def solve(self, nums: List[int]) -> bool:
        n = len(nums)
        # 第一段
        i = 1
        while i < n and nums[i - 1] < nums[i]:
            i += 1
        if i == 1:  # 第一段至少要有两个数
            return False

        # 第二段
        i0 = i
        while i < n and nums[i - 1] > nums[i]:
            i += 1
        if i == i0 or i == n:  # 第二段至少要有两个数，第三段至少要有两个数
            return False

        # 第三段
        while i < n and nums[i - 1] < nums[i]:
            i += 1
        return i == n

    def gen(self):
        return self.generate_list_int(),


class Solution2(Testing):
    date = "2025-8-3"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3638,
                         types=[ProblemType.Stack, ProblemType.Greedy, ProblemType.Array, ProblemType.DynamicPlanning,
                                ProblemType.MonotonyStack],
                         pass_rate=0.599,
                         description="给你一个长度为 `n` 的整数数组 `weight`，表示按直线排列的 `n` 个包裹的重量。**装运** 定义为包裹的一个连续子数组。如果一个装运满足以下条件，则称其为 **平衡装运**：**最后一个包裹的重量** **严格小于** 该装运中所有包裹中 **最大重量** 。\n\n选择若干个 **不重叠** 的连续平衡装运，并满足 **每个包裹最多出现在一次装运中**（部分包裹可以不被装运）。\n\n返回 **可以形成的平衡装运的最大数量** 。\n\n \n\n**示例 1:**\n\n**输入:** weight = [2,5,1,4,3]\n\n**输出:** 2\n\n**解释:**\n\n我们可以形成最多两个平衡装运：\n\n- 装运 1:\n\n   \n\n  ```\n  [2, 5, 1]\n  ```\n\n  - 包裹的最大重量 = 5\n  - 最后一个包裹的重量 = 1，严格小于 5，因此这是平衡装运。\n\n- 装运 2:\n\n   \n\n  ```\n  [4, 3]\n  ```\n\n  - 包裹的最大重量 = 4\n  - 最后一个包裹的重量 = 3，严格小于 4，因此这是平衡装运。\n\n无法通过其他方式划分包裹获得超过两个平衡装运，因此答案是 2。\n\n**示例 2:**\n\n**输入:** weight = [4,4]\n\n**输出:** 0\n\n**解释:**\n\n在这种情况下无法形成平衡装运：\n\n- 装运 `[4, 4]` 的最大重量为 4，而最后一个包裹的重量也是 4，不严格小于最大重量，因此不是平衡的。\n- 单个包裹的装运 `[4]` 中，最后一个包裹的重量等于最大重量，因此也不是平衡的。\n\n由于无法形成任何平衡装运，答案是 0。\n\n \n\n**提示:**\n\n- `2 <= n <= 105`\n- `1 <= weight[i] <= 109`"
                         )

    def solve(self, weight: List[int]) -> int:
        n = len(weight)
        ans = 0
        i = 1
        while i < n:
            if weight[i - 1] > weight[i]:
                ans += 1
                i += 2  # 下个子数组至少要有两个数
            else:
                i += 1
        return ans

    def gen(self):
        return self.generate_list_int(),


class Solution3(Testing):
    date = "2025-8-3"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3639,
                         types=[ProblemType.Array, ProblemType.Bisearch],
                         pass_rate=0.405,
                         description="给你一个长度为 `n` 的字符串 `s` 和一个整数数组 `order`，其中 `order` 是范围 `[0, n - 1]` 内数字的一个 **排列**。\n\n从时间 `t = 0` 开始，在每个时间点，将字符串 `s` 中下标为 `order[t]` 的字符替换为 `'*'`。\n\n如果 **子字符串** 包含 **至少** 一个 `'*'` ，则认为该子字符串有效。\n\n如果字符串中 **有效子字符串** 的总数大于或等于 `k`，则称该字符串为 **活跃** 字符串。\n\n返回字符串 `s` 变为 **活跃** 状态的最小时间 `t`。如果无法变为活跃状态，返回 -1。\n\n \n\n**示例 1:**\n\n**输入:** s = \"abc\", order = [1,0,2], k = 2\n\n**输出:** 0\n\n**解释:**\n\n| `t`  | `order[t]` | 修改后的 `s` | 有效子字符串                   | 计数 | 激活状态 (计数 >= k) |\n| ---- | ---------- | ------------ | ------------------------------ | ---- | -------------------- |\n| 0    | 1          | `\"a*c\"`      | `\"*\"`, `\"a*\"`, `\"*c\"`, `\"a*c\"` | 4    | 是                   |\n\n字符串 `s` 在 `t = 0` 时变为激活状态。因此，答案是 0。\n\n**示例 2:**\n\n**输入:** s = \"cat\", order = [0,2,1], k = 6\n\n**输出:** 2\n\n**解释:**\n\n| `t`  | `order[t]` | 修改后的 `s` | 有效子字符串                          | 计数 | 激活状态 (计数 >= k) |\n| ---- | ---------- | ------------ | ------------------------------------- | ---- | -------------------- |\n| 0    | 0          | `\"*at\"`      | `\"*\"`, `\"*a\"`, `\"*at\"`                | 3    | 否                   |\n| 1    | 2          | `\"*a*\"`      | `\"*\"`, `\"*a\"`, `\"*a*\"`, `\"a*\"`, `\"*\"` | 5    | 否                   |\n| 2    | 1          | `\"***\"`      | 所有子字符串(包含 `'*'`)              | 6    | 是                   |\n\n字符串 `s` 在 `t = 2` 时变为激活状态。因此，答案是 2。\n\n**示例 3:**\n\n**输入:** s = \"xy\", order = [0,1], k = 4\n\n**输出:** -1\n\n**解释:**\n\n即使完成所有替换，也无法得到 `k = 4` 个有效子字符串。因此，答案是 -1。\n\n \n\n**提示:**\n\n- `1 <= n == s.length <= 105`\n- `order.length == n`\n- `0 <= order[i] <= n - 1`\n- `s` 由小写英文字母组成。\n- `order` 是从 0 到 `n - 1` 的整数排列。\n- `1 <= k <= 109`"
                         )

    def solve(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        if n * (n + 1) // 2 < k:
            return -1

        star = [0] * n  # 避免在二分内部反复创建/初始化列表

        def check(m: int) -> bool:
            m += 1
            for j in range(m):
                star[order[j]] = m
            cnt = 0
            last = -1  # 上一个 '*' 的位置
            for i, x in enumerate(star):
                if x == m:  # s[i] 是 '*'
                    last = i
                cnt += last + 1
                if cnt >= k:  # 提前退出循环
                    return True
            return False

        left, right = -1, n - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right


    def _gen(self):
        s = _generate_string()
        ordeer = list(range(len(s)))
        random.shuffle(ordeer)
        k = _generate_int()

        return s, ordeer, k

from math import inf

class Solution4(Testing):
    date = "2025-8-3"
    def __init__(self):
        Testing.__init__(self,
                         degree=2,
                         idx=3640,
                         types=[ProblemType.Array, ProblemType.DynamicPlanning],
                         pass_rate=0.43,
                         description="给你一个长度为 `n` 的整数数组 `nums`。\n\n**三段式子数组** 是一个连续子数组 `nums[l...r]`（满足 `0 <= l < r < n`），并且存在下标 `l < p < q < r`，使得：\n\n- `nums[l...p]` **严格** 递增，\n- `nums[p...q]` **严格** 递减，\n- `nums[q...r]` **严格** 递增。\n\n请你从数组 `nums` 的所有三段式子数组中找出和最大的那个，并返回其 **最大** 和。\n\n \n\n**示例 1：**\n\n**输入：**nums = [0,-2,-1,-3,0,2,-1]\n\n**输出：**-4\n\n**解释：**\n\n选择 `l = 1`, `p = 2`, `q = 3`, `r = 5`：\n\n- `nums[l...p] = nums[1...2] = [-2, -1]` 严格递增 (`-2 < -1`)。\n- `nums[p...q] = nums[2...3] = [-1, -3]` 严格递减 (`-1 > -3`)。\n- `nums[q...r] = nums[3...5] = [-3, 0, 2]` 严格递增 (`-3 < 0 < 2`)。\n- 和 = `(-2) + (-1) + (-3) + 0 + 2 = -4`。\n\n**示例 2:**\n\n**输入:** nums = [1,4,2,7]\n\n**输出:** 14\n\n**解释:**\n\n选择 `l = 0`, `p = 1`, `q = 2`, `r = 3`：\n\n- `nums[l...p] = nums[0...1] = [1, 4]` 严格递增 (`1 < 4`)。\n- `nums[p...q] = nums[1...2] = [4, 2]` 严格递减 (`4 > 2`)。\n- `nums[q...r] = nums[2...3] = [2, 7]` 严格递增 (`2 < 7`)。\n- 和 = `1 + 4 + 2 + 7 = 14`。\n\n \n\n**提示:**\n\n- `4 <= n = nums.length <= 10e5`\n- `-10e9 <= nums[i] <= 10e9`\n- 保证至少存在一个三段式子数组。"
                         )

    def solve(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -inf
        i = 0
        while i < n:
            # 第一段
            start = i
            i += 1
            while i < n and nums[i - 1] < nums[i]:
                i += 1
            if i == start + 1:  # 第一段至少要有两个数
                continue

            # 第二段
            peak = i - 1
            res = nums[peak - 1] + nums[peak]  # 第一段的最后两个数必选
            while i < n and nums[i - 1] > nums[i]:
                res += nums[i]  # 第二段的所有元素必选
                i += 1
            if i == peak + 1 or i == n or nums[i - 1] == nums[i]:  # 第二段至少要有两个数，第三段至少要有两个数
                continue

            # 第三段
            bottom = i - 1
            res += nums[i]  # 第三段的前两个数必选（第一个数在上面的循环中加了）
            # 从第三段的第三个数往右，计算最大元素和
            max_s = s = 0
            i += 1
            while i < n and nums[i - 1] < nums[i]:
                s += nums[i]
                max_s = max(max_s, s)
                i += 1
            res += max_s

            # 从第一段的倒数第三个数往左，计算最大元素和
            max_s = s = 0
            for j in range(peak - 2, start - 1, -1):
                s += nums[j]
                max_s = max(max_s, s)
            res += max_s
            ans = max(ans, res)

            i = bottom  # 第三段的起点也是下一个极大三段式子数组的第一段的起点
        return ans

    def _gen(self):
        return _generate_list_int(((4, 10000)), (-1000000000, 1000000000)),