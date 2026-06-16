
from string import ascii_lowercase
from . import Problem
import re


class Solution1(Problem):
    date = "2026-3-29"
    def __init__(self):
        Problem.__init__(self,
                         degree=0,
                         idx=3884,
                         types=[],
                         pass_rate=0.73,
                         description='给你一个长度为 `n` 的字符串 `s`，其中只包含小写英文字母。\n返回最小的下标 `i`，使得 `s[i] == s[n - i - 1]`。\n如果不存在这样的下标，返回 `-1`。\n\n**示例 1：**\n> \n**输入：**`s = "abcacbd"`\n**输出：**`1`\n**解释：**\n在下标 `i = 1` 处，`s[1]` 和 `s[5]` 的值均为 `\'b\'`。\n没有更小的下标满足条件，因此答案是 1。\n**示例 2：**\n> \n**输入：**`s = "abc"`\n**输出：**`1`\n**解释：**\n\u200b\u200b\u200b\u200b\u200b\u200b\u200b在下标 `i = 1` 处，左右对应位置重合，因此字符均为 `\'b\'`。\n没有更小的下标满足条件，因此答案是 1。\n**示例 3：**\n> \n**输入：**`s = "abcdab"`\n**输出：**`-1`\n**解释：**\n\u200b\u200b\u200b\u200b\u200b\u200b\u200b对于每个下标 `i`，位置 `i` 和 `n - i - 1` 的字符均不相同。\n因此，不存在有效下标，答案是 `-1`。\n\n**提示：**\n - `1 <= n == s.length <= 100`\n - `s` 仅包含小写英文字母。'
                         )

    def solve(self, s: str) -> int:
        for i in range(len(s) // 2 + 1):
            if s[i] == s[-1 - i]:
                return i
        return -1

    def gen(self):
        """
        生成测试样例，覆盖以下场景：
        1. 边界情况：最小长度、最大长度
        2. 特殊结构：全相同字符、对称字符串、不对称字符串、立即匹配、最晚匹配、无匹配
        3. 正常情况：随机生成的字符串
        """
        import random
        import string

        # 确保可重复性
        random.seed(self.seed)

        cases = []
        total_cases = self.testcase_num

        # 1. 边界情况 - 最小长度
        cases.append("a")  # n=1, i=0时s[0]==s[0]

        # 2. 边界情况 - 最大长度全相同
        cases.append("z" * 100)  # i=0即匹配

        # 3. 完全不对称 - 无匹配
        cases.append("abcdef")  # 长度6，s[0]!='f', s[1]!='e', s[2]!='d'

        # 4. 对称字符串 - 最晚匹配
        cases.append("abcba")  # 长度5，i=0,1不匹配，i=2匹配

        # 5. 立即匹配（i=0）
        cases.append("abac")  # 长度4，i=0时s[0]='a'==s[3]='a'

        # 6. 最大长度不对称
        cases.append(("abcdefghijklmnopqrstuvwxyz" + "0123456789" + "abcdefghij")[:100])

        # 7. 特殊：回文字符串 - i=0即匹配
        cases.append("abccba")  # 长度6

        # 8. 单字符重复
        cases.append("bb")

        # 9. 长度2不匹配
        cases.append("ab")

        # 10. 长度3中间匹配
        cases.append("aba")

        # 剩余用随机字符串填充
        for _ in range(total_cases - 10):
            # 随机长度1-20
            length = random.randint(1, 20)
            s = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
            cases.append(s)

        return (cases,)
    

from . import NotSuitQuestion
from . import Problem
from typing import List
from heapq import heappop
from heapq import heappush
from heapq import heapify
import re
class EventManager:

    def __init__(self, events: List[List[int]]):
        self.id_to_priority = {}
        self.h = []
        for eid, priority in events:
            self.id_to_priority[eid] = priority
            self.h.append((-priority, eid))
        heapify(self.h)

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.id_to_priority[eventId] = newPriority
        heappush(self.h, (-newPriority, eventId))

    def pollHighest(self) -> int:
        while self.h:
            priority, eid = heappop(self.h)
            if self.id_to_priority.get(eid, -1) == -priority:
                del self.id_to_priority[eid]
                return eid
        return -1

class Solution2(Problem):
    date = "2026-3-29"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3885,
                         types=[],
                         pass_rate=0.44,
                         description='给你一组初始事件列表，其中每个事件有一个唯一的 `eventId` 和一个 `priority`（优先级）。\n实现 `EventManager` 类：\n - `EventManager(int[][] events)` 使用给定事件初始化管理器，其中 `events[i] = [eventId_i, priority_i]`。\n - `void updatePriority(int eventId, int newPriority)` 更新具有 id 为 `eventId` 的**活跃**事件的优先级为 `newPriority`。\n - `int pollHighest()` 移除并返回具有**最高优先级**的**活跃事件**的 `eventId`。如果有多个活动事件具有相同的优先级，则返回 `eventId` 最小的事件。如果没有活跃事件，则返回 -1。\n\n如果一个事件没有被 `pollHighest()` 移除，则称其为**活跃事件**。\n\n**示例 1：**\n> \n**输入：**\n`["EventManager", "pollHighest", "updatePriority", "pollHighest", "pollHighest"]\n\n> [[[[5, 7], [2, 7], [9, 4]]], [], [9, 7], [], []]`\n**输出：**\n`[null, 2, null, 5, 9] `\n**解释**\n> EventManager eventManager = new EventManager([[5,7], [2,7], [9,4]]); // 使用三个事件初始化管理器\n\n> eventManager.pollHighest(); // 两个事件 5 和 2 的优先级均为 7，因此返回 id 最小的事件 2\n\n> eventManager.updatePriority(9, 7); // 将事件 9 的优先级更新为 7\n\n> eventManager.pollHighest(); // 剩下的优先级最高的事件是 5 和 9，返回 5\n\n> eventManager.pollHighest(); // 返回 9\n**示例 2：**\n> \n**输入：**\n`["EventManager", "pollHighest", "pollHighest", "pollHighest"]\n\n> [[[[4, 1], [7, 2]]], [], [], []]`\n**输出：**\n`[null, 7, 4, -1] `\n**解释**\n> EventManager eventManager = new EventManager([[4,1], [7,2]]); // 使用两个事件初始化管理器\n\n> eventManager.pollHighest(); // 返回 7\n\n> eventManager.pollHighest(); // 返回 4\n\n> eventManager.pollHighest(); // 没有剩余事件，返回 -1\n\n**提示：**\n - `1 <= events.length <= 10^5`\n - `events[i] = [eventId, priority]`\n - `1 <= eventId <= 10^9`\n - `1 <= priority <= 10^9`\n - `events` 中的所有 `eventId` 值都是**唯一的**。\n - `1 <= newPriority <= 10^9`\n - 对每次调用 `updatePriority`，`eventId` 都指向一个**活跃事件**。\n - 对 `updatePriority` 和 `pollHighest` 的总调用次数最多为 `10^5` 次。'
                         )



    def gen(self):
        raise NotSuitQuestion()
    

import math
from . import Problem
from typing import List
import re
from math import isqrt


class Solution3(Problem):
    date = "2026-3-29"
    def __init__(self):
        Problem.__init__(self,
                         degree=2,
                         idx=3886,
                         types=[],
                         pass_rate=0.39,
                         description='给你一个长度为 `n` 的整数数组 `nums`。\n如果一个整数 `k` 满足以下条件，则称其为**可排序整数**：`k` 是 `n` 的**因数**，且可以通过依次执行以下操作将 `nums` 排序为**非递减顺序**：\n - 将 `nums` 划分为长度为 `k` 的**连续子数组**。\n - **独立地对每个子数组进行循环移动**（左移或右移任意次数）。\n\n返回所有可能的可排序整数 `k` 的和。**子数组**是数组中的一个连续、非空元素序列。\n\n**示例 1：**\n> \n**输入：**`nums = [3,1,2]`\n**输出：**`3`\n**解释：**\u200b\u200b\u200b\u200b\u200b\u200b\u200b\n - 对于 `n = 3`，可能的因数是 1 和 3。\n - 对于 `k = 1`：每个子数组都只有一个元素。无法通过移动使数组排序。\n - 对于 `k = 3`：单个子数组 `[3, 1, 2]` 可以通过左移一次得到 `[1, 2, 3]`，从而将数组排序。\n - 只有 `k = 3` 可排序，因此答案是 3。\n\n**示例 2：**\n> \n**输入：**`nums = [7,6,5]`\n**输出：**`0`\n**解释：**\n - 对于 `n = 3`，可能的因数是 1 和 3。\n - 对于 `k = 1`：每个子数组都只有一个元素。无法通过移动使数组排序。\n - 对于 `k = 3`：单个子数组 `[7, 6, 5]` 无法通过任何移动排序为非递减顺序。\n - 没有任何可排序的\xa0`k`，因此答案是 0。\n\n**示例 3：**\n> \n**输入：**`nums = [5,8]`\n**输出：**`3`\n**解释：**\u200b\u200b\u200b\u200b\u200b\u200b\u200b\n - 对于 `n = 2`，可能的因数是 1 和 2。\n - 由于 `[5, 8]` 本身已经有序，每个因数都可排序。\n - 因此答案是 `1 + 2 = 3`。\n\n**提示：**\n - `1 <= n == nums.length <= 10^5`\n - `1 <= nums[i] <= 10^5`'
                         )

    def solve(self, nums: List[int]) -> int:
        n = len(nums)
        next_dec = [0] * n
        next_dec[-1] = p = n
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                p = i
            next_dec[i] = p

        def solve(k: int) -> None:
            last_max = 0
            for r in range(k - 1, n, k):
                l = r - k + 1
                m = next_dec[l]
                if m >= r:
                    if nums[l] < last_max:
                        return
                    last_max = nums[r]
                else:
                    if next_dec[m + 1] < r or nums[m + 1] < last_max or nums[r] > nums[l]:
                        return
                    last_max = nums[m]
            nonlocal ans
            ans += k
        ans = 0
        for k in range(1, isqrt(n) + 1):
            if n % k == 0:
                solve(k)
                if k * k < n:
                    solve(n // k)
        return ans

    def gen(self):
        """
        生成测试样例，覆盖各种场景：
        1. 边界情况：n=1, n=2
        2. 特殊结构：全相同元素、严格递增、严格递减
        3. 随机数组：小规模、中等规模、较大规模
        4. 特殊可排序情况

        注意：题目约束 n <= 10^5，但为避免超时，实际测试中最大长度控制在 200
        """
        import random
        random.seed(self.seed)

        testcases = []

        # 边界情况：n = 1
        testcases.append([1])
        # 边界情况：n = 2，有序
        testcases.append([1, 2])
        # 边界情况：n = 2，无序
        testcases.append([2, 1])

        # 全相同元素数组（所有因数都可排序）
        testcases.append([5] * 12)

        # 严格递增数组（所有因数都可排序）
        testcases.append(list(range(1, 13)))

        # 严格递减数组（可能没有可排序k，或只有n可排序）
        testcases.append(list(range(12, 0, -1)))

        # 小规模随机数组 (n = 12)
        testcases.append([random.randint(1, 1000) for _ in range(12)])
        testcases.append([random.randint(1, 1000) for _ in range(12)])
        testcases.append([random.randint(1, 1000) for _ in range(12)])
        testcases.append([random.randint(1, 1000) for _ in range(12)])
        testcases.append([random.randint(1, 1000) for _ in range(12)])

        # 中等规模随机数组 (n = 50)
        testcases.append([random.randint(1, 10000) for _ in range(50)])
        testcases.append([random.randint(1, 10000) for _ in range(50)])
        testcases.append([random.randint(1, 10000) for _ in range(50)])

        # 较大规模随机数组 (n = 100)
        testcases.append([random.randint(1, 10000) for _ in range(100)])
        testcases.append([random.randint(1, 10000) for _ in range(100)])
        testcases.append([random.randint(1, 10000) for _ in range(100)])

        # 更大规模随机数组 (n = 200)
        testcases.append([random.randint(1, 10000) for _ in range(200)])
        testcases.append([random.randint(1, 10000) for _ in range(200)])
        testcases.append([random.randint(1, 10000) for _ in range(200)])

        # 补充随机用例达到100个
        for _ in range(100 - len(testcases)):
            length = random.randint(10, 100)
            testcases.append([random.randint(1, 10000) for _ in range(length)])

        return (testcases,)
    


from . import Problem
from typing import List
from typing import Union
import re
class UnionFind:

    def __init__(self, n: int):
        self.fa = list(range(n))
        self.dis = [0] * n

    def find(self, x: int) -> int:
        fa = self.fa
        if fa[x] != x:
            root = self.find(fa[x])
            self.dis[x] ^= self.dis[fa[x]]
            fa[x] = root
        return fa[x]

    def merge(self, from_: int, to: int, value: int) -> bool:
        x, y = (self.find(from_), self.find(to))
        dis = self.dis
        if x == y:
            return dis[from_] ^ dis[to] == value
        dis[x] = value ^ dis[to] ^ dis[from_]
        self.fa[x] = y
        return True

class Solution4(Problem):
    date = "2026-3-29"
    def __init__(self):
        Problem.__init__(self,
                         degree=2,
                         idx=3887,
                         types=[],
                         pass_rate=0.56,
                         description='给你一个正整数 `n`。\n有一个由 `n` 个节点组成的**无向图**，节点的编号从 0 到 `n - 1`。最初，这个图没有任何边。\n你还得到一个二维整数数组 `edges`，其中 `edges[i] = [u_i, v_i, w_i]` 表示一条连接节点 `u_i` 和 `v_i` 的边，边的权重为 `w_i`。权重 `w_i` 要么是 0，要么是 1。\n按照给定顺序处理 `edges` 中的每一条边。对于每条边，如果将其添加到图中后，图中的**每个环**的边权和依然是**偶数**，那么将这条边添加到图中。\n返回一个整数，表示最终成功添加到图中的边的数量。\n\n**示例 1：**\n> \n**输入：**`n = 3, edges = [[0,1,1],[1,2,1],[0,2,1]]`\n**输出：**`2`\n**解释：**\n - `[0, 1, 1]`：添加节点 0 和节点 1 之间的边，权重为 1。\n - `[1, 2, 1]`：添加节点 1 和节点 2 之间的边，权重为 1。\n - `[0, 2, 1]`：节点 0 和节点 2 之间的边（图中的虚线）不被添加，因为环 `0 - 1 - 2 - 0` 的边权和为 `1 + 1 + 1 = 3`（奇数）。\n\n**示例 2：**\n> \n**输入：**`n = 3, edges = [[0,1,1],[1,2,1],[0,2,0]]`\n**输出：**`3`\n**解释：**\n - `[0, 1, 1]`：添加节点 0 和节点 1 之间的边，权重为 1。\n - `[1, 2, 1]`：添加节点 1 和节点 2 之间的边，权重为 1。\n - `[0, 2, 0]`：添加节点 0 和节点 2 之间的边，权重为 0。\n - 注意，环 `0 - 1 - 2 - 0` 的边权和为 `1 + 1 + 0 = 2`（偶数）。\n\n**提示：**\n - `3 <= n <= 5 * 10^4`\n - `1 <= edges.length <= 5 * 10^4`\n - `edges[i] = [u_i, v_i, w_i]`\n - `0 <= u_i < v_i < n`\n - 所有边都是唯一的。\n - `w_i = 0` 或 `w_i = 1`'
                         )

    def solve(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        ans = 0
        for x, y, w in edges:
            if uf.merge(x, y, w):
                ans += 1
        return ans

    def gen(self):
        """
        生成测试样例，验证带权并查集求解偶数环问题的正确性。

        测试策略：
        1. 边界测试：最小节点、最小边数、全0/全1权重
        2. 树形结构：所有边都能成功添加
        3. 环结构测试：验证奇偶性约束
        4. 特殊结构：星形、链形图
        """
        # 由于题目规模较大（可达5*10^4），为避免超时，适当缩小规模
        # 保留边界测试含义，同时控制运行时间
        n_cases = self.testcase_num
        quarter = n_cases // 4
        eighth = n_cases // 8

        n_list = []
        edges_list = []

        # 1. 边界测试 - 最小规模
        for _ in range(eighth):
            n_list.append(3)
            edges_list.append([[0, 1, 0], [1, 2, 0], [0, 2, 0]])

        for _ in range(eighth):
            n_list.append(3)
            edges_list.append([[0, 1, 1], [1, 2, 1], [0, 2, 1]])

        # 2. 树形结构（所有边都能添加）
        for _ in range(quarter):
            n = self.s_generate_int(int_range=(3, 20))
            edges = []
            # 生成一棵树
            for i in range(1, n):
                parent = self.s_generate_int(int_range=(0, i - 1))
                w = self.s_generate_int(int_range=(0, 1))
                edges.append([parent, i, w] if parent < i else [i, parent, w])
            n_list.append(n)
            edges_list.append(edges)

        # 3. 环结构测试
        for _ in range(quarter):
            n = self.s_generate_int(int_range=(3, 30))
            edges = []
            # 先生成一棵树
            for i in range(1, n):
                parent = self.s_generate_int(int_range=(0, i - 1))
                w = self.s_generate_int(int_range=(0, 1))
                edges.append([parent, i, w] if parent < i else [i, parent, w])
            # 添加一些额外的边（可能形成环）
            extra_edges = self.s_generate_int(int_range=(1, min(n, 10)))
            existing_edges = set((e[0], e[1]) for e in edges)
            added = 0
            attempts = 0
            while added < extra_edges and attempts < 100:
                u = self.s_generate_int(int_range=(0, n - 2))
                v = self.s_generate_int(int_range=(u + 1, n - 1))
                if (u, v) not in existing_edges:
                    w = self.s_generate_int(int_range=(0, 1))
                    edges.append([u, v, w])
                    existing_edges.add((u, v))
                    added += 1
                attempts += 1
            n_list.append(n)
            edges_list.append(edges)

        # 4. 随机图结构
        remaining = n_cases - len(n_list)
        for _ in range(remaining):
            n = self.s_generate_int(int_range=(3, 50))
            max_edges = min(n * (n - 1) // 2, 100)
            num_edges = self.s_generate_int(int_range=(1, max_edges))
            edges = []
            existing_edges = set()
            attempts = 0
            while len(edges) < num_edges and attempts < 1000:
                u = self.s_generate_int(int_range=(0, n - 2))
                v = self.s_generate_int(int_range=(u + 1, n - 1))
                if (u, v) not in existing_edges:
                    w = self.s_generate_int(int_range=(0, 1))
                    edges.append([u, v, w])
                    existing_edges.add((u, v))
                attempts += 1
            n_list.append(n)
            edges_list.append(edges)

        return n_list, edges_list
    

