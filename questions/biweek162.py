from . import Problem as Testing, ProblemType
from ..testcase_sampler import _generate_int,_generate_list_int
from typing import List


class Solution1(Testing):
    date = "2025-8-2"
    def __init__(self):
        Testing.__init__(self,
                         degree=0,
                         idx=3633,
                         types=[ProblemType.Greedy, ProblemType.Array, ProblemType.BiPoint, ProblemType.Bisearch,
                                ProblemType.Sorting],
                         pass_rate=0.641,
                         description="给你两种类别的游乐园项目：**陆地游乐设施** 和 **水上游乐设施**。\n\n- 陆地游乐设施\n  - `landStartTime[i]` – 第 `i` 个陆地游乐设施最早可以开始的时间。\n  - `landDuration[i]` – 第 `i` 个陆地游乐设施持续的时间。\n- 水上游乐设施\n  - `waterStartTime[j]` – 第 `j` 个水上游乐设施最早可以开始的时间。\n  - `waterDuration[j]` – 第 `j` 个水上游乐设施持续的时间。\n\n一位游客必须从 **每个** 类别中体验 **恰好****一个** 游乐设施，顺序 **不限** 。\n\n- 游乐设施可以在其开放时间开始，或 **之后任意时间** 开始。\n- 如果一个游乐设施在时间 `t` 开始，它将在时间 `t + duration` 结束。\n- 完成一个游乐设施后，游客可以立即乘坐另一个（如果它已经开放），或者等待它开放。\n\n返回游客完成这两个游乐设施的 **最早可能时间** 。\n\n \n\n**示例 1:**\n\n**输入：**landStartTime = [2,8], landDuration = [4,1], waterStartTime = [6], waterDuration = [3]\n\n**输出：**9\n\n**解释：**\n\n- 方案 A（陆地游乐设施 0 → 水上游乐设施 0）：\n  - 在时间 `landStartTime[0] = 2` 开始陆地游乐设施 0。在 `2 + landDuration[0] = 6` 结束。\n  - 水上游乐设施 0 在时间 `waterStartTime[0] = 6` 开放。立即在时间 `6` 开始，在 `6 + waterDuration[0] = 9` 结束。\n- 方案 B（水上游乐设施 0 → 陆地游乐设施 1）：\n  - 在时间 `waterStartTime[0] = 6` 开始水上游乐设施 0。在 `6 + waterDuration[0] = 9` 结束。\n  - 陆地游乐设施 1 在 `landStartTime[1] = 8` 开放。在时间 `9` 开始，在 `9 + landDuration[1] = 10` 结束。\n- 方案 C（陆地游乐设施 1 → 水上游乐设施 0）：\n  - 在时间 `landStartTime[1] = 8` 开始陆地游乐设施 1。在 `8 + landDuration[1] = 9` 结束。\n  - 水上游乐设施 0 在 `waterStartTime[0] = 6` 开放。在时间 `9` 开始，在 `9 + waterDuration[0] = 12` 结束。\n- 方案 D（水上游乐设施 0 → 陆地游乐设施 0）：\n  - 在时间 `waterStartTime[0] = 6` 开始水上游乐设施 0。在 `6 + waterDuration[0] = 9` 结束。\n  - 陆地游乐设施 0 在 `landStartTime[0] = 2` 开放。在时间 `9` 开始，在 `9 + landDuration[0] = 13` 结束。\n\n方案 A 提供了最早的结束时间 9。\n\n**示例 2:**\n\n**输入：**landStartTime = [5], landDuration = [3], waterStartTime = [1], waterDuration = [10]\n\n**输出：**14\n\n**解释：**\n\n- 方案 A（水上游乐设施 0 → 陆地游乐设施 0）：\n  - 在时间 `waterStartTime[0] = 1` 开始水上游乐设施 0。在 `1 + waterDuration[0] = 11` 结束。\n  - 陆地游乐设施 0 在 `landStartTime[0] = 5` 开放。立即在时间 `11` 开始，在 `11 + landDuration[0] = 14` 结束。\n- 方案 B（陆地游乐设施 0 → 水上游乐设施 0）：\n  - 在时间 `landStartTime[0] = 5` 开始陆地游乐设施 0。在 `5 + landDuration[0] = 8` 结束。\n  - 水上游乐设施 0 在 `waterStartTime[0] = 1` 开放。立即在时间 `8` 开始，在 `8 + waterDuration[0] = 18` 结束。\n\n方案 A 提供了最早的结束时间 14。****\n\n \n\n**提示:**\n\n- `1 <= n, m <= 100`\n- `landStartTime.length == landDuration.length == n`\n- `waterStartTime.length == waterDuration.length == m`\n- `1 <= landStartTime[i], landDuration[i], waterStartTime[j], waterDuration[j] <= 1000`"
                         )

    def solve(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int],
                           waterDuration: List[int]) -> int:
        def solve_(landStartTime: List[int], landDuration: List[int], waterStartTime: List[int],
                   waterDuration: List[int]) -> int:
            min_finish = min(start + duration for start, duration in zip(landStartTime, landDuration))
            return min(max(start, min_finish) + duration for start, duration in zip(waterStartTime, waterDuration))

        land_water = solve_(landStartTime, landDuration, waterStartTime, waterDuration)
        water_land = solve_(waterStartTime, waterDuration, landStartTime, landDuration)
        return min(land_water, water_land)

    def _gen(self):
        n1 = _generate_list_int((1, 500), (1, 500000))
        n2 = _generate_list_int((len(n1), len(n1)), (1, 500000))

        n3 = _generate_list_int((1, 500), (1, 500000))
        n4 = _generate_list_int((len(n3), len(n3)), (1, 500000))
        return n1, n2, n3, n4


class Solution2(Testing):
    date = "2025-8-2"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3634,
                         types=[ProblemType.Array, ProblemType.Sorting, ProblemType.SlideWindows],
                         pass_rate=0.413,
                         description="给你一个整数数组 `nums` 和一个整数 `k`。\n\n如果一个数组的 **最大** 元素的值 **至多** 是其 **最小** 元素的 `k` 倍，则该数组被称为是 **平衡** 的。\n\n你可以从 `nums` 中移除 **任意** 数量的元素，但不能使其变为 **空** 数组。\n\n返回为了使剩余数组平衡，需要移除的元素的 **最小** 数量。\n\n**注意：**大小为 1 的数组被认为是平衡的，因为其最大值和最小值相等，且条件总是成立。\n\n \n\n**示例 1:**\n\n**输入：**nums = [2,1,5], k = 2\n\n**输出：**1\n\n**解释：**\n\n- 移除 `nums[2] = 5` 得到 `nums = [2, 1]`。\n- 现在 `max = 2`, `min = 1`，且 `max <= min * k`，因为 `2 <= 1 * 2`。因此，答案是 1。\n\n**示例 2:**\n\n**输入：**nums = [1,6,2,9], k = 3\n\n**输出：**2\n\n**解释：**\n\n- 移除 `nums[0] = 1` 和 `nums[3] = 9` 得到 `nums = [6, 2]`。\n- 现在 `max = 6`, `min = 2`，且 `max <= min * k`，因为 `6 <= 2 * 3`。因此，答案是 2。\n\n**示例 3:**\n\n**输入：**nums = [4,6], k = 2\n\n**输出：**0\n\n**解释：**\n\n- 由于 `nums` 已经平衡，因为 `6 <= 4 * 2`，所以不需要移除任何元素。\n\n \n\n**提示：**\n\n- `1 <= nums.length <= 105`\n- `1 <= nums[i] <= 109`\n- `1 <= k <= 105`"
                         )

    def solve(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_save = left = 0
        for i, mx in enumerate(nums):
            while nums[left] * k < mx:
                left += 1
            max_save = max(max_save, i - left + 1)
        return len(nums) - max_save

    def gen(self):
        return (self.generate_list_int((1, 1000), (1, 1000)),
                self.generate_int(int_range=(1, 1000)))


class Solution3(Testing):
    date = "2025-8-2"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3635,
                         types=[ProblemType.Greedy, ProblemType.Array, ProblemType.BiPoint, ProblemType.Sorting],
                         pass_rate=0.565,
                         description="给你两种类别的游乐园项目：**陆地游乐设施** 和 **水上游乐设施**。\n\n- 陆地游乐设施\n  - `landStartTime[i]` – 第 `i` 个陆地游乐设施最早可以开始的时间。\n  - `landDuration[i]` – 第 `i` 个陆地游乐设施持续的时间。\n- 水上游乐设施\n  - `waterStartTime[j]` – 第 `j` 个水上游乐设施最早可以开始的时间。\n  - `waterDuration[j]` – 第 `j` 个水上游乐设施持续的时间。\n\n一位游客必须从 **每个** 类别中体验 **恰好****一个** 游乐设施，顺序 **不限** 。\n\n- 游乐设施可以在其开放时间开始，或 **之后任意时间** 开始。\n- 如果一个游乐设施在时间 `t` 开始，它将在时间 `t + duration` 结束。\n- 完成一个游乐设施后，游客可以立即乘坐另一个（如果它已经开放），或者等待它开放。\n\n返回游客完成这两个游乐设施的 **最早可能时间** 。\n\n \n\n**示例 1:**\n\n**输入：**landStartTime = [2,8], landDuration = [4,1], waterStartTime = [6], waterDuration = [3]\n\n**输出：**9\n\n**解释：**\n\n- 方案 A（陆地游乐设施 0 → 水上游乐设施 0）：\n  - 在时间 `landStartTime[0] = 2` 开始陆地游乐设施 0。在 `2 + landDuration[0] = 6` 结束。\n  - 水上游乐设施 0 在时间 `waterStartTime[0] = 6` 开放。立即在时间 `6` 开始，在 `6 + waterDuration[0] = 9` 结束。\n- 方案 B（水上游乐设施 0 → 陆地游乐设施 1）：\n  - 在时间 `waterStartTime[0] = 6` 开始水上游乐设施 0。在 `6 + waterDuration[0] = 9` 结束。\n  - 陆地游乐设施 1 在 `landStartTime[1] = 8` 开放。在时间 `9` 开始，在 `9 + landDuration[1] = 10` 结束。\n- 方案 C（陆地游乐设施 1 → 水上游乐设施 0）：\n  - 在时间 `landStartTime[1] = 8` 开始陆地游乐设施 1。在 `8 + landDuration[1] = 9` 结束。\n  - 水上游乐设施 0 在 `waterStartTime[0] = 6` 开放。在时间 `9` 开始，在 `9 + waterDuration[0] = 12` 结束。\n- 方案 D（水上游乐设施 0 → 陆地游乐设施 0）：\n  - 在时间 `waterStartTime[0] = 6` 开始水上游乐设施 0。在 `6 + waterDuration[0] = 9` 结束。\n  - 陆地游乐设施 0 在 `landStartTime[0] = 2` 开放。在时间 `9` 开始，在 `9 + landDuration[0] = 13` 结束。\n\n方案 A 提供了最早的结束时间 9。\n\n**示例 2:**\n\n**输入：**landStartTime = [5], landDuration = [3], waterStartTime = [1], waterDuration = [10]\n\n**输出：**14\n\n**解释：**\n\n- 方案 A（水上游乐设施 0 → 陆地游乐设施 0）：\n  - 在时间 `waterStartTime[0] = 1` 开始水上游乐设施 0。在 `1 + waterDuration[0] = 11` 结束。\n  - 陆地游乐设施 0 在 `landStartTime[0] = 5` 开放。立即在时间 `11` 开始，在 `11 + landDuration[0] = 14` 结束。\n- 方案 B（陆地游乐设施 0 → 水上游乐设施 0）：\n  - 在时间 `landStartTime[0] = 5` 开始陆地游乐设施 0。在 `5 + landDuration[0] = 8` 结束。\n  - 水上游乐设施 0 在 `waterStartTime[0] = 1` 开放。立即在时间 `8` 开始，在 `8 + waterDuration[0] = 18` 结束。\n\n方案 A 提供了最早的结束时间 14。"
                         )


    def solve(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int],
                           waterDuration: List[int]) -> int:
        def solve_(landStartTime: List[int], landDuration: List[int], waterStartTime: List[int],
                   waterDuration: List[int]) -> int:
            min_finish = min(start + duration for start, duration in zip(landStartTime, landDuration))
            return min(max(start, min_finish) + duration for start, duration in zip(waterStartTime, waterDuration))

        land_water = solve_(landStartTime, landDuration, waterStartTime, waterDuration)
        water_land = solve_(waterStartTime, waterDuration, landStartTime, landDuration)
        return min(land_water, water_land)

    def _gen(self):
        n1 = _generate_list_int((1, 500), (1, 500000))
        n2 = _generate_list_int((len(n1), len(n1)), (1, 500000))

        n3 = _generate_list_int((1, 500), (1, 500000))
        n4 = _generate_list_int((len(n3), len(n3)), (1, 500000))
        return n1, n2, n3, n4

from bisect import bisect_left
from math import ceil, sqrt

class Solution4(Testing):
    date = "2025-8-2"
    def __init__(self):
        Testing.__init__(self,
                         degree=2,
                         idx=3636,
                         types=[ProblemType.Array, ProblemType.HashTable, ProblemType.Bisearch, ProblemType.DevideAndConquer,
                                ProblemType.Counting, ProblemType.PrefixSum],
                         pass_rate=0.399,
                         description="给你一个长度为 `n` 的整数数组 `nums` 和一个查询数组 `queries`，其中 `queries[i] = [li, ri, thresholdi]`。\n\n返回一个整数数组 `ans`，其中 `ans[i]` 等于子数组 `nums[li...ri]` 中出现 **至少** `thresholdi` 次的元素，选择频率 **最高** 的元素（如果频率相同则选择 **最小** 的元素），如果不存在这样的元素则返回 -1。\n\n \n\n**示例 1:**\n\n**输入：** nums = [1,1,2,2,1,1], queries = [[0,5,4],[0,3,3],[2,3,2]]\n\n**输出：** [1,-1,2]\n\n**解释：**\n\n| 查询      | 子数组             | 阈值 | 频率表       | 答案 |\n| :-------- | :----------------- | :--- | :----------- | :--- |\n| [0, 5, 4] | [1, 1, 2, 2, 1, 1] | 4    | 1 → 4, 2 → 2 | 1    |\n| [0, 3, 3] | [1, 1, 2, 2]       | 3    | 1 → 2, 2 → 2 | -1   |\n| [2, 3, 2] | [2, 2]             | 2    | 2 → 2        | 2    |\n\n \n\n**示例 2:**\n\n**输入：**nums = [3,2,3,2,3,2,3], queries = [[0,6,4],[1,5,2],[2,4,1],[3,3,1]]\n\n**输出：**[3,2,3,2]\n\n**解释：**\n\n| 查询      | 子数组                | 阈值 | 频率表       | 答案 |\n| :-------- | :-------------------- | :--- | :----------- | :--- |\n| [0, 6, 4] | [3, 2, 3, 2, 3, 2, 3] | 4    | 3 → 4, 2 → 3 | 3    |\n| [1, 5, 2] | [2, 3, 2, 3, 2]       | 2    | 2 → 3, 3 → 2 | 2    |\n| [2, 4, 1] | [3, 2, 3]             | 1    | 3 → 2, 2 → 1 | 3    |\n| [3, 3, 1] | [2]                   | 1    | 2 → 1        | 2    |\n\n \n\n**提示：**\n\n- `1 <= nums.length == n <= 104`\n- `1 <= nums[i] <= 109`\n- `1 <= queries.length <= 5 * 104`\n- `queries[i] = [li, ri, thresholdi]`\n- `0 <= li <= ri < n`\n- `1 <= thresholdi <= ri - li + 1`"
                         )

    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        m = len(queries)

        # 离散化
        a: list[int] = sorted(set(nums))
        index_to_value: list[int] = [bisect_left(a, x) for x in nums]

        cnt = [0] * (len(a) + 1)
        max_cnt = 0
        min_val = 0

        def add(i: int) -> None:
            nonlocal max_cnt, min_val
            v = index_to_value[i]
            cnt[v] += 1
            c = cnt[v]
            x = nums[i]
            if c > max_cnt:
                max_cnt, min_val = c, x
            elif c == max_cnt:
                min_val = min(min_val, x)

        ans = [-1] * m
        block_size: int = ceil(n / sqrt(m * 2))

        qs = []  # (bid, ql, qr, threshold, qid) 其中 bid 是块号，qid 是询问的编号
        i: int
        l: int
        r: int
        threshold: int
        for i, (l, r, threshold) in enumerate(queries):
            r += 1  # 左闭右开

            # 大区间离线（保证 l 和 r 不在同一个块中）
            if r - l > block_size:
                qs.append((l // block_size, l, r, threshold, i))
                continue

            # 小区间暴力
            for j in range(l, r):
                add(j)
            if max_cnt >= threshold:
                ans[i] = min_val

            # 重置数据
            for v in index_to_value[l: r]:
                cnt[v] -= 1
            max_cnt = 0

        qs.sort(key=lambda q: (q[0], q[2]))

        i: int
        bid: int
        ql: int
        qr:int
        threshold:int
        qid:int
        for i, (bid, ql, qr, threshold, qid) in enumerate(qs):
            l0 = (bid + 1) * block_size
            if i == 0 or bid > qs[i - 1][0]:  # 遍历到一个新的块
                r = l0  # 右端点移动的起点
                # 重置数据
                cnt = [0] * (len(a) + 1)
                max_cnt = 0

            # 右端点从 r 移动到 qr（qr 不计入）
            while r < qr:
                add(r)
                r += 1

            tmp_max_cnt = max_cnt
            tmp_min_val = min_val

            # 左端点从 l0 移动到 ql（l0 不计入）
            for j in range(ql, l0):
                add(j)
            if max_cnt >= threshold:
                ans[qid] = min_val

            # 回滚
            max_cnt = tmp_max_cnt
            min_val = tmp_min_val
            for v in index_to_value[ql: l0]:
                cnt[v] -= 1

        return ans

    def _gen(self):
        n = _generate_int(1, 100)
        nums = _generate_list_int((n, n), (1, 100000))
        queries_len = _generate_int(1, 100)
        queries = list()
        for _ in range(queries_len):
            r = _generate_int(0, n-1)
            l = _generate_int(0, r)
            threshold = _generate_int(1, r - l + 1)
            queries.append([l, r, threshold])
        return nums, queries