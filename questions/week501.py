

from . import Problem


class Solution1(Problem):
    date = "2026-5-10"
    def __init__(self):
        Problem.__init__(self,
                         degree=0,
                         idx=3925,
                         types=[],
                         pass_rate=0.9,
                         description='给你一个长度为 `n` 的整数数组 `nums`。\n构造一个新的长度为 `2 * n` 的数组 `ans`，其中前 `n` 个元素与 `nums` 相同，后 `n` 个元素为 `nums` 的逆序。\n具体而言，对于 `0 <= i <= n - 1`：\n\n- `ans[i] = nums[i]`\n\n - `ans[i + n] = nums[n - i - 1]`\n\n返回整数数组 `ans`。\n\n**示例 1：**\n> \n**输入：**`nums = [1,2,3]`\n**输出：**`[1,2,3,3,2,1]`\n**解释：**\n`ans` 的前 `n` 个元素与 `nums` 相同。\n接下来的 `n = 3` 个元素按照 `nums` 的逆序填入： - `ans[3] = nums[2] = 3`\n - `ans[4] = nums[1] = 2`\n - `ans[5] = nums[0] = 1`\n\n因此，`ans = [1, 2, 3, 3, 2, 1]`。\n**示例 2：**\n> \n**输入：**`nums = [1]`\n**输出：**`[1,1]`\n**解释：**\n数组逆序后保持不变。因此，`ans = [1, 1]`。\n\n**提示：**\n\n- `1 <= nums.length <= 100`\n\n - `1 <= nums[i] <= 100`'
                         )

    def solve(self, nums: list[int]) -> list[int]:
        return nums + nums[::-1]

    def gen(self):
        """
        生成测试样例。

        该题目要求构造一个长度为2*n的数组，前n个元素与nums相同，后n个元素为nums的逆序。

        覆盖场景：
        1. 边界值：
           - 最小长度 n=1（单元素）
           - 最大长度 n=100
           - 最小元素值 nums[i]=1
           - 最大元素值 nums[i]=100
        2. 特殊结构：
           - 全相同元素数组
           - 严格递增数组
           - 严格递减数组
           - 回文数组（逆序后不变）
        3. 正常分布：
           - 随机长度和随机值的数组

        参数约束：
        - 1 <= nums.length <= 100
        - 1 <= nums[i] <= 100
        """
        testcase_num = self.testcase_num
        test_cases = []

        # 1. 边界值测试 - 约20个用例
        # 最小长度 n=1，各种值的单元素
        for _ in range(5):
            test_cases.append([self.s_generate_int(int_range=(1, 100))])

        # 最大长度 n=100，随机值
        test_cases.append([self.s_generate_int(int_range=(1, 100)) for _ in range(100)])
        test_cases.append([self.s_generate_int(int_range=(1, 100)) for _ in range(100)])

        # 最小值数组（全1）
        for length in [1, 50, 100]:
            test_cases.append([1] * length)

        # 最大值数组（全100）
        for length in [1, 50, 100]:
            test_cases.append([100] * length)

        # 2. 特殊结构测试 - 约30个用例
        # 全相同元素（各种值）
        for length in [2, 10, 50, 100]:
            val = self.s_generate_int(int_range=(1, 100))
            test_cases.append([val] * length)

        # 严格递增
        for length in [2, 10, 50, 100]:
            test_cases.append(list(range(1, min(length + 1, 100))))

        # 严格递减
        for length in [2, 10, 50, 100]:
            start = min(100, length)
            test_cases.append(list(range(start, 0, -1)))

        # 回文数组（逆序后不变）
        for length in [2, 5, 10, 20, 50, 100]:
            half = length // 2
            arr = [self.s_generate_int(int_range=(1, 100)) for _ in range(half)]
            if length % 2 == 1:
                arr = arr + [self.s_generate_int(int_range=(1, 100))] + arr[::-1]
            else:
                arr = arr + arr[::-1]
            test_cases.append(arr)

        # 3. 正常随机分布 - 剩余用例
        while len(test_cases) < testcase_num:
            length = self.s_generate_int(int_range=(1, 100))
            test_cases.append([self.s_generate_int(int_range=(1, 100)) for _ in range(length)])

        # 返回元组形式，第一个元素是nums参数的所有测试样例
        return (test_cases,)
    


from . import Problem
from collections import defaultdict


class Solution2(Problem):
    date = "2026-5-10"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3926,
                         types=[],
                         pass_rate=0.41,
                         description='给你一个字符串数组 `chunks`。按顺序将这些字符串拼接起来，形成一个字符串 `s`。\n另给定一个字符串数组 `queries`。\n**单词**定义为 `s` 的一个**子串**，并满足：\n - 由小写英文字母（`\'a\'` 到 `\'z\'`）组成；\n - 可以包含连字符（`\'-\'`），但仅当每个连字符两侧都被小写英文字母包围时才允许；\n - 它不是某个同样满足上述条件更长子串的一部分。\n\n任何不是小写英文字母或合法连字符的字符都会作为分隔符。\n返回一个整数数组 `ans`，其中 `ans[i]` 表示 `queries[i]` 作为单词在 `s` 中出现的次数。\n**子串**是字符串中一个连续的**非空**字符序列。\n\n**示例 1：**\n> \n**输入：**`chunks = ["hello wor","ld hello"], queries = ["hello","world","wor"]`\n**输出：**`[2,1,0]`\n**解释：**\n - 将 `chunks` 中的所有字符串拼接后，得到 `s = "hello world hello"`。\n - `s` 中的有效单词为 `"hello"`（出现两次）和 `"world"`（出现一次）。\n - 因此，`ans = [2, 1, 0]`。\n\n**示例 2：**\n> \n**输入：**`chunks = ["a--b a-","-c"], queries = ["a","b","c"]`\n**输出：**`[2,1,1]`\n**解释：**\n - 将 `chunks` 中的所有字符串拼接后，得到 `s = "a--b a--c"`。\n - `s` 中的有效单词为 `"a"`（出现两次）、`"b"`（出现一次）和 `"c"`（出现一次）。\n - 因此，`ans = [2, 1, 1]`。\n\n**示例 3：**\n> \n**输入：**`chunks = ["hello"], queries = ["hello","ell"]`\n**输出：**`[1,0]`\n**解释：**\n - `s` 中唯一的有效单词是 `"hello"`，出现一次。\n - 因此，`ans = [1, 0]`。\n\n**提示：**\n - `1 <= chunks.length <= 10^5`\n - `1 <= chunks[i].length <= 10^5`\n - `chunks[i]` 可以由小写英文字母、空格和连字符组成。\n - 所有 `chunks` 中字符串的总长度不超过 `10^5`\n - `1 <= queries.length <= 10^5`\n - `1 <= queries[i].length <= 10^5`\n - `queries[i]` 是一个有效单词\n - 所有 `queries` 中字符串的总长度不超过 `10^5`'
                         )

    def solve(self, chunks: list[str], queries: list[str]) -> list[int]:
        s = ''.join(chunks)
        cnt = defaultdict(int)
        for t in s.split():
            n = len(t)
            i = 0
            while i < n:
                if t[i] == '-':
                    i += 1
                    continue
                start = i
                while i < n and (t[i] != '-' or (i < n - 1 and t[i + 1] != '-')):
                    i += 1
                cnt[t[start:i]] += 1
        return [cnt[q] for q in queries]

    def gen(self):
        """
        生成测试样例用于测试单词计数功能。

        生成策略：
        1. 边界覆盖：chunks长度为1、单个字符、空格分隔、连续连字符等情况
        2. 随机场景：生成随机文本，提取有效单词作为query
        3. 特殊结构：含连字符的单词、重复单词、不存在的query等

        由于chunks总长度≤10^5，queries总长度≤10^5，使用较小testcase_num确保不超时
        """
        testcase_num = 50  # 减少测试样例数量以确保不超时
        chunks_list = []
        queries_list = []

        # === 边界测试用例 ===

        # Case 1: 单个chunk，简单空格分隔
        chunks_list.append(["hello world test"])
        queries_list.append(["hello", "world", "test"])

        # Case 2: 多个chunks拼接
        chunks_list.append(["hello", " world", " test"])
        queries_list.append(["hello", "world", "test"])

        # Case 3: 包含合法连字符
        chunks_list.append(["well-known co-operate"])
        queries_list.append(["well-known", "co-operate"])

        # Case 4: 连续连字符分隔
        chunks_list.append(["a--b"])
        queries_list.append(["a", "b", "a--b"])

        # Case 5: 前后连字符（不合法）
        chunks_list.append(["-abc def-"])
        queries_list.append(["abc", "def"])

        # Case 6: 重复单词
        chunks_list.append(["test test test"])
        queries_list.append(["test"])

        # Case 7: query不存在
        chunks_list.append(["hello world"])
        queries_list.append(["notexist"])

        # Case 8: 单字符
        chunks_list.append(["a b c"])
        queries_list.append(["a", "b", "c"])

        # Case 9: 混合空格和连字符
        chunks_list.append(["a-b c-d e--f"])
        queries_list.append(["a-b", "c-d", "e", "f"])

        # Case 10: 跨chunks的单词
        chunks_list.append(["hel", "lo wor", "ld"])
        queries_list.append(["hello", "world"])

        # Case 11: 空格作为唯一分隔符
        chunks_list.append(["abc  def   ghi"])
        queries_list.append(["abc", "def", "ghi"])

        # Case 12: 带连字符的长单词
        chunks_list.append(["state-of-the-art"])
        queries_list.append(["state-of-the-art"])

        # Case 13: chunks中空字符串（最小长度情况）
        chunks_list.append(["a"])
        queries_list.append(["a"])

        # Case 14: 多个连续空格和连字符混合
        chunks_list.append(["a  b--c --d"])
        queries_list.append(["a", "b", "c", "d"])

        # Case 15: 只有连字符
        chunks_list.append(["---"])
        queries_list.append(["test"])  # 应该返回0

        # Case 16: 大量重复单词
        chunks_list.append(["x " * 100])
        queries_list.append(["x"])

        # Case 17: chunk边界分割单词
        chunks_list.append(["ab", "c", "def"])
        queries_list.append(["abc", "def"])

        # Case 18: 混合大小写（不符合题意但测试鲁棒性）
        chunks_list.append(["Hello World"])
        queries_list.append(["hello", "world"])  # 应该都是0

        # Case 19: 包含特殊字符作为分隔符（虽然题目说只允许空格和连字符）
        chunks_list.append(["hello.world,test"])
        queries_list.append(["hello", "world", "test"])

        # Case 20: 复杂连字符模式
        chunks_list.append(["a-b-c de-f"])
        queries_list.append(["a-b-c", "de-f"])

        # === 随机生成测试用例 ===
        # 剩余测试用例随机生成
        import random
        random.seed(0)

        for i in range(testcase_num - 20):
            # 生成随机词汇表
            vocab_size = random.randint(5, 20)
            words = []
            for _ in range(vocab_size):
                # 生成无连字符的单词或带连字符的单词
                if random.random() < 0.3:
                    # 带连字符的单词
                    parts = []
                    num_parts = random.randint(2, 3)
                    for _ in range(num_parts):
                        part_len = random.randint(1, 5)
                        part = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(part_len))
                        parts.append(part)
                    word = '-'.join(parts)
                else:
                    # 普通单词
                    word_len = random.randint(1, 8)
                    word = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(word_len))
                words.append(word)

            # 生成chunks文本
            num_words = random.randint(10, 50)
            selected_words = [random.choice(words) for _ in range(num_words)]

            # 分配到chunks中，可能在chunk边界插入空格或连续连字符
            num_chunks = random.randint(1, 5)
            chunks = []
            chunk_words = [[] for _ in range(num_chunks)]
            for word in selected_words:
                chunk_idx = random.randint(0, num_chunks - 1)
                chunk_words[chunk_idx].append(word)

            for cw in chunk_words:
                # 在单词之间随机插入分隔符
                text_parts = []
                for idx, w in enumerate(cw):
                    text_parts.append(w)
                    if idx < len(cw) - 1:
                        sep_type = random.random()
                        if sep_type < 0.6:
                            text_parts.append(' ')
                        elif sep_type < 0.8:
                            text_parts.append('  ')
                        else:
                            text_parts.append('--')
                chunks.append(''.join(text_parts))

            # 提取有效单词
            s = ''.join(chunks)
            valid_words = []
            for token in s.split():
                n = len(token)
                j = 0
                while j < n:
                    if token[j] == '-':
                        j += 1
                        continue
                    start = j
                    while j < n and (token[j] != '-' or (j < n - 1 and token[j + 1] != '-')):
                        j += 1
                    word = token[start:j]
                    if word and word not in valid_words:
                        valid_words.append(word)

            # 选择queries
            num_queries = min(random.randint(2, 10), len(valid_words))
            if num_queries == 0:
                queries = ["nonexistent"]
            else:
                # 60%从有效单词中选，40%可能选不存在的
                queries = []
                for _ in range(num_queries):
                    if random.random() < 0.6 and valid_words:
                        queries.append(random.choice(valid_words))
                    else:
                        fake_len = random.randint(1, 5)
                        fake = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(fake_len))
                        queries.append(fake)

            chunks_list.append(chunks)
            queries_list.append(queries)

        return chunks_list, queries_list
    

import random
from . import Problem
from collections import Counter
MX = 100001
divisors = [[] for _ in range(MX)]
for i in range(1, MX):
    for j in range(i, MX, i):
        divisors[j].append(i)

class Solution3(Problem):
    date = "2026-5-10"
    def __init__(self):
        Problem.__init__(self,
                         degree=1,
                         idx=3927,
                         types=[],
                         pass_rate=0.41,
                         description='给你一个整数数组 `nums`。\n你可以执行以下操作任意多次：\n - 选择两个下标 `a` 和 `b`，且满足\xa0`nums[a] % nums[b] == 0`。\n - 将 `nums[a]` 替换为 `nums[b]`。\n\n返回执行任意次操作后，数组可能得到的\xa0**最小\xa0**元素和。\n\n**示例 1：**\n> \n**输入：**`nums = [3,6,2]`\n**输出：**`7`\n**解释：**\n - 选择 `a = 1`、`b = 2`，此时 `nums[a] = 6`，`nums[b] = 2`。由于 `6 % 2 == 0`，将 `nums[1]` 替换为 `nums[2]`。\n - 数组变为 `[3, 2, 2]`。\n - 之后无法再通过操作减少元素和。因此，最终元素和为 `3 + 2 + 2 = 7`。\n\n**示例 2：**\n> \n**输入：**`nums = [4,2,8,3]`\n**输出：**`9`\n**解释：**\n - 选择 `a = 0`、`b = 1`，此时 `nums[a] = 4`，`nums[b] = 2`。由于 `4 % 2 == 0`，将 `nums[0]` 替换为 `nums[1]`。\n - 选择 `a = 2`、`b = 1`，此时 `nums[a] = 8`，`nums[b] = 2`。由于 `8 % 2 == 0`，将 `nums[2]` 替换为 `nums[1]`。\n - 数组变为 `[2, 2, 2, 3]`。\n - 之后无法再通过操作减少元素和。因此，最终元素和为 `2 + 2 + 2 + 3 = 9`。\n\n**示例 3：**\n> \n**输入：**`nums = [7,5,9]`\n**输出：**`21`\n**解释：**\n - 不存在满足 `nums[a] % nums[b] == 0` 的下标对 `(a, b)`。\n - 因此，无法执行任何操作。元素和保持为 `7 + 5 + 9 = 21`。\n\n**提示：**\n - `1 <= nums.length <= 10**5`\n - `1 <= nums[i] <= 10**5`'
                         )

    def solve(self, nums: list[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for x, c in cnt.items():
            for d in divisors[x]:
                if d in cnt:
                    ans += d * c
                    break
        return ans

    def gen(self):
        """生成测试样例，覆盖各种边界情况和正常分布场景。

        测试策略：
        1. 边界测试：最小长度数组、全相同元素、包含1的数组
        2. 特殊结构：互不相同元素、小范围数值、大数值元素
        3. 正常分布：中等规模和较大规模的随机数组

        考虑到 nums.length <= 10^5 且参考算法复杂度较高，
        将最大数组长度控制在 1000 以内，避免超时。

        Returns:
            tuple: 包含一个元素，为 nums 参数的测试样例列表
        """
        # 使用约 40 个测试用例，平衡覆盖率和运行时间
        cases = []

        # 边界测试：最小长度为 1 的数组
        cases.append([self.s_generate_int(int_range=(1, 100000))])

        # 边界测试：长度为 2 的数组
        cases.append(self.s_generate_list_int(list_length_range=(2, 2), int_range=(1, 100000)))

        # 边界测试：长度为 3 的数组
        cases.append(self.s_generate_list_int(list_length_range=(3, 3), int_range=(1, 100000)))

        # 边界测试：长度为 5 的数组
        cases.append(self.s_generate_list_int(list_length_range=(5, 5), int_range=(1, 100000)))

        # 边界测试：全部元素为 1（1 可以整除任何数，关键测试点）
        cases.append([1] * self.s_generate_int(int_range=(1, 100)))

        # 边界测试：全部元素为 2
        cases.append([2] * self.s_generate_int(int_range=(1, 100)))

        # 特殊结构：元素互不相同的数组（测试去重逻辑）
        cases.append(self.s_generate_list_int(list_length_range=(5, 20), int_range=(1, 1000), different=True))

        # 特殊结构：包含 1 的数组（1 是整除关系的关键）
        arr_with_1 = self.s_generate_list_int(list_length_range=(10, 50), int_range=(1, 100))
        arr_with_1[0] = 1  # 确保 1 存在
        random.shuffle(arr_with_1)
        cases.append(arr_with_1)

        # 特殊结构：由 1 和 2 组成的数组
        len_1_2 = self.s_generate_int(int_range=(5, 50))
        cases.append([self.s_generate_int(int_range=(1, 2)) for _ in range(len_1_2)])

        # 特殊结构：元素范围在 1-10 之间的小数值数组（测试小整数的整除关系）
        cases.append(self.s_generate_list_int(list_length_range=(10, 50), int_range=(1, 10)))

        # 正常分布：中等规模随机数组
        for _ in range(10):
            cases.append(self.s_generate_list_int(list_length_range=(5, 100), int_range=(1, 10000)))

        # 正常分布：较大规模随机数组
        for _ in range(8):
            cases.append(self.s_generate_list_int(list_length_range=(100, 500), int_range=(1, 100000)))

        # 边界测试：接近最大长度的数组（控制在 1000 以内避免超时）
        for _ in range(3):
            cases.append(self.s_generate_list_int(list_length_range=(800, 1000), int_range=(1, 100000)))

        # 边界测试：包含大元素的数组（接近约束上限）
        cases.append(self.s_generate_list_int(list_length_range=(10, 30), int_range=(99990, 100000)))

        # 边界测试：元素集中在某个范围（重复元素多，测试去重效果）
        center = self.s_generate_int(int_range=(1000, 50000))
        cases.append([self.s_generate_int(int_range=(center, center + 10)) for _ in range(50)])

        # 返回参数列表：只有一个参数 nums
        return (cases,)
    

from heapq import heappop
from heapq import heappush
import re
def dijkstra(g: list[list[tuple[int, int]]], start: int, price: int) -> list[int]:
    dis = [price] * len(g)
    dis[start] = 0
    h = [(0, start)]
    while h:
        dis_x, x = heappop(h)
        if dis_x > dis[x]:
            continue
        for y, wt in g[x]:
            new_dis_y = dis_x + wt
            if new_dis_y < dis[y]:
                dis[y] = new_dis_y
                heappush(h, (new_dis_y, y))
    return dis

class Solution4(Problem):
    date = "2026-5-10"
    def __init__(self):
        Problem.__init__(self,
                         degree=2,
                         idx=3928,
                         types=[],
                         pass_rate=0.45,
                         description='给你一个整数 `n` 和一个长度为 `n` 的整数数组 `prices`，其中 `prices[i]` 表示商店 `i` 中苹果的价格。\n另给定一个二维整数数组 `roads`，其中 `roads[i] = [u_i, v_i, cost_i, tax_i]` 表示一条**双向**道路：\n - `u_i` 和 `v_i` 是该道路连接的两个商店。\n - `cost_i` 表示在**不携带苹果**时通过该道路的花费。\n - `tax_i` 表示在**携带苹果**时，该道路费用相对于 `cost_i` 的乘数。\n\n对于每个商店 `i`，你可以选择其中之一：\n - 直接在商店 `i` 购买苹果，花费为 `prices[i]`。\n - 以**空手**状态，通过**任意数量**的道路前往任意一家商店 `j`，以 `prices[j]` 的价格购买苹果，然后携带苹果返回商店 `i`。返回途中，每条道路的费用为 `cost * tax`。\n\n前往商店时（空手）和返回时（携带苹果）所经过的路径可以**不同**。\n返回一个长度为 `n` 的整数数组 `ans`，其中 `ans[i]` 表示从商店 `i` 出发购买到苹果所需的**最小**总花费。\n\n**示例 1：**\n> \n**输入：**`n = 2, prices = [8,3], roads = [[0,1,1,2]]`\n**输出：**`[6,3]`\n**解释：**\n\n| 商店 `i` | `prices[i]` | 商店 `j` | `prices[j]` | `cost_i` | `tax_i` | 去程花费 | 返程花费 | 总花费 | 最小值 |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n| 0 | 8 | 1 | 3 | 1 | 2 | 1 | `1 * 2 = 2` | `1 + 2 + 3 = 6` | `min(8, 6) = 6` |\n| 1 | 3 | 0 | 8 | 1 | 2 | 1 | `1 * 2 = 2` | `1 + 2 + 8 = 11` | `min(3, 11) = 3` |\n\n因此，答案为 `[6, 3]`。\n**示例 2：**\n> \n**输入：**`n = 3, prices = [9,4,6], roads = [[0,1,1,3],[1,2,4,2]]`\n**输出：**`[8,4,6]`\n**解释：**\n\n| 商店 `i` | `prices[i]` | 商店 `j` | `prices[j]` | `cost_i` | `tax_i` | 去程花费 | 返程花费 | 总花费 | 最小值 |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n| 0 | 9 | 1 | 4 | 1 | 3 | 1 | `1 * 3 = 3` | `1 + 3 + 4 = 8` | `min(9, 8) = 8` |\n| 1 | 4 | 2 | 6 | 4 | 2 | 4 | `4 * 2 = 8` | `4 + 8 + 6 = 18` | `min(4, 18) = 4` |\n| 2 | 6 | 1 | 4 | 4 | 2 | 4 | `4 * 2 = 8` | `4 + 8 + 4 = 16` | `min(6, 16) = 6` |\n\n因此，答案为 `[8, 4, 6]`。\n**示例 3：**\n> \n**输入：**`n = 3, prices = [10,11,1], roads = [[0,2,1,3],[1,2,3,4],[0,1,5,2]]`\n**输出：**`[5,11,1]`\n**解释：**\n\n| 商店 `i` | `prices[i]` | 商店 `j` | `prices[j]` | `cost_i` | `tax_i` | 去程花费 | 返程花费 | 总花费 | 最小值 |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n| 0 | 10 | 2 | 1 | 1 | 3 | 1 | `1 * 3 = 3` | `1 + 3 + 1 = 5` | `min(10, 5) = 5` |\n| 1 | 11 | 2 | 1 | 3 | 4 | 3 | `3 * 4 = 12` | `3 + 12 + 1 = 16` | `min(11, 16) = 11` |\n| 2 | 1 | 0 | 10 | 1 | 3 | 1 | `1 * 3 = 3` | `1 + 3 + 10 = 14` | `min(1, 14) = 1` |\n\n因此，答案为 `[5, 11, 1]`。\n\n**提示：**\n - `1 <= n <= 1000`\n - `prices.length == n`\n - `1 <= prices[i] <= 10^9`\n - `0 <= roads.length <= min(n × (n - 1) / 2, 2000)`\n - `roads[i] = [u_i, v_i, cost_i, tax_i]`\n - `0 <= u_i, v_i <= n - 1`\n - `u_i != v_i`\n - `1 <= cost_i <= 10^9`\n - `1 <= tax_i <= 100`\n - 不存在重复边。'
                         )

    def solve(self, n: int, prices: list[int], roads: list[list[int]]) -> list[int]:
        g1 = [[] for _ in range(n)]
        g2 = [[] for _ in range(n)]
        for x, y, cost, tax in roads:
            g1[x].append((y, cost))
            g1[y].append((x, cost))
            g2[x].append((y, cost * tax))
            g2[y].append((x, cost * tax))
        ans = [0] * n
        for i, price in enumerate(prices):
            dis1 = dijkstra(g1, i, price)
            dis2 = dijkstra(g2, i, price)
            ans[i] = min((p + d1 + d2 for p, d1, d2 in zip(prices, dis1, dis2)))
        return ans

    def gen(self):
        """Generate test cases for the apple purchasing problem.

        Coverage strategy:
        - Boundary cases: n=1, n=2, no roads, single road
        - Small graphs (5-15 nodes): sparse, dense, special structures
        - Medium graphs (50-200 nodes): various densities
        - Large graphs (200-400 nodes): sparse graphs to avoid timeout
        - Special structures: linear chain, star, tree, cycle
        - Extreme values: prices, costs, tax multipliers
        - Disconnected graphs: isolated components
        """
        results = []

        # Boundary: n=1, single node (5 cases)
        for _ in range(5):
            n = 1
            prices = [self.s_generate_int(int_range=(1, 1000000000))]
            roads = []
            results.append((n, prices, roads))

        # Boundary: n=2, no roads (3 cases)
        for _ in range(3):
            n = 2
            prices = [self.s_generate_int(int_range=(1, 100)), self.s_generate_int(int_range=(1, 100))]
            roads = []
            results.append((n, prices, roads))

        # Boundary: n=2, single road (5 cases)
        for _ in range(5):
            n = 2
            prices = [self.s_generate_int(int_range=(1, 100)), self.s_generate_int(int_range=(1, 100))]
            cost = self.s_generate_int(int_range=(1, 50))
            tax = self.s_generate_int(int_range=(1, 5))
            roads = [[0, 1, cost, tax]]
            results.append((n, prices, roads))

        # Small graphs with various structures (10 cases)
        for _ in range(10):
            n = self.s_generate_int(int_range=(5, 15))
            prices = [self.s_generate_int(int_range=(1, 1000)) for _ in range(n)]
            num_roads = min(n * (n - 1) // 2, self.s_generate_int(int_range=(n - 1, n + 10)))
            roads = self._s_generate_connected_graph(n, num_roads, cost_range=(1, 100), tax_range=(1, 10))
            results.append((n, prices, roads))

        # Linear chain graphs (5 cases)
        for _ in range(5):
            n = self.s_generate_int(int_range=(10, 30))
            prices = [self.s_generate_int(int_range=(1, 500)) for _ in range(n)]
            roads = []
            for i in range(n - 1):
                cost = self.s_generate_int(int_range=(1, 20))
                tax = self.s_generate_int(int_range=(1, 3))
                roads.append([i, i + 1, cost, tax])
            results.append((n, prices, roads))

        # Star graphs (5 cases)
        for _ in range(5):
            n = self.s_generate_int(int_range=(10, 20))
            prices = [self.s_generate_int(int_range=(1, 500)) for _ in range(n)]
            center = 0
            roads = []
            for i in range(1, n):
                cost = self.s_generate_int(int_range=(1, 30))
                tax = self.s_generate_int(int_range=(1, 5))
                roads.append([center, i, cost, tax])
            results.append((n, prices, roads))

        # Tree structures (5 cases)
        for _ in range(5):
            n = self.s_generate_int(int_range=(20, 50))
            prices = [self.s_generate_int(int_range=(1, 1000)) for _ in range(n)]
            roads = []
            for i in range(1, n):
                parent = self.s_generate_int(int_range=(0, i - 1))
                cost = self.s_generate_int(int_range=(1, 50))
                tax = self.s_generate_int(int_range=(1, 5))
                roads.append([parent, i, cost, tax])
            results.append((n, prices, roads))

        # Medium sparse graphs (10 cases)
        for _ in range(10):
            n = self.s_generate_int(int_range=(50, 200))
            prices = [self.s_generate_int(int_range=(1, 10000)) for _ in range(n)]
            num_roads = min(n * (n - 1) // 2, self.s_generate_int(int_range=(n, min(n * 2, 500))))
            roads = self._s_generate_connected_graph(n, num_roads, cost_range=(1, 500), tax_range=(1, 20))
            results.append((n, prices, roads))

        # Large sparse graphs - reduced size to avoid timeout (10 cases)
        for _ in range(10):
            n = self.s_generate_int(int_range=(200, 400))
            prices = [self.s_generate_int(int_range=(1, 100000)) for _ in range(n)]
            num_roads = min(n - 1, self.s_generate_int(int_range=(50, 150)))
            roads = self._s_generate_connected_graph(n, num_roads, cost_range=(1, 1000), tax_range=(1, 30))
            results.append((n, prices, roads))

        # Extreme prices (5 cases)
        for _ in range(5):
            n = self.s_generate_int(int_range=(5, 10))
            prices = []
            for _ in range(n):
                if random.random() < 0.4:
                    prices.append(self.s_generate_int(int_range=(1, 10)))
                elif random.random() < 0.7:
                    prices.append(self.s_generate_int(int_range=(100000000, 1000000000)))
                else:
                    prices.append(self.s_generate_int(int_range=(100, 1000)))
            num_roads = min(n * (n - 1) // 2, self.s_generate_int(int_range=(n - 1, n * 2)))
            roads = self._s_generate_connected_graph(n, num_roads, cost_range=(1, 50), tax_range=(1, 10))
            results.append((n, prices, roads))

        # Extreme tax values (5 cases)
        for _ in range(5):
            n = self.s_generate_int(int_range=(5, 15))
            prices = [self.s_generate_int(int_range=(100, 1000)) for _ in range(n)]
            num_roads = min(n * (n - 1) // 2, self.s_generate_int(int_range=(n - 1, min(n * 3, 30))))
            edges = self._s_generate_connected_graph_edges(n, num_roads)
            roads = []
            for u, v in edges:
                cost = self.s_generate_int(int_range=(1, 20))
                tax = self.s_generate_int(int_range=(50, 100))
                roads.append([u, v, cost, tax])
            results.append((n, prices, roads))

        # Disconnected graphs (5 cases)
        for _ in range(5):
            n = self.s_generate_int(int_range=(10, 30))
            prices = [self.s_generate_int(int_range=(1, 500)) for _ in range(n)]
            connected_nodes = max(3, n // 2)
            num_roads = min(connected_nodes * (connected_nodes - 1) // 2, 
                           self.s_generate_int(int_range=(connected_nodes - 1, connected_nodes * 2)))
            roads = self._s_generate_connected_graph(connected_nodes, num_roads, cost_range=(1, 50), tax_range=(1, 5))
            results.append((n, prices, roads))

        # Transform to gen() format
        n_list = [r[0] for r in results]
        prices_list = [r[1] for r in results]
        roads_list = [r[2] for r in results]

        return (n_list, prices_list, roads_list)

    def _s_generate_connected_graph(self, n: int, num_roads: int, cost_range: tuple = (1, 100), 
                                     tax_range: tuple = (1, 10)) -> list:
        """Generate a connected graph with n nodes and num_roads edges.

        Args:
            n: Number of nodes
            num_roads: Number of edges
            cost_range: Range for cost values (inclusive)
            tax_range: Range for tax values (inclusive)

        Returns:
            List of roads [u, v, cost, tax]
        """
        edges = self._s_generate_connected_graph_edges(n, num_roads)
        roads = []
        for u, v in edges:
            cost = self.s_generate_int(int_range=cost_range)
            tax = self.s_generate_int(int_range=tax_range)
            roads.append([u, v, cost, tax])
        return roads

    def _s_generate_connected_graph_edges(self, n: int, num_roads: int) -> list:
        """Generate edges for a connected graph.

        First ensures connectivity with a spanning tree, then adds random edges.

        Args:
            n: Number of nodes
            num_roads: Number of edges to generate

        Returns:
            List of edge tuples (u, v)
        """
        max_roads = n * (n - 1) // 2
        num_roads = min(num_roads, max_roads)

        if n == 1:
            return []

        # Create a spanning tree to ensure connectivity
        edges = []
        for i in range(1, n):
            parent = self.s_generate_int(int_range=(0, i - 1))
            edges.append((parent, i))

        # Add remaining edges randomly
        all_possible = set()
        for i in range(n):
            for j in range(i + 1, n):
                all_possible.add((i, j))

        # Remove already used edges
        for e in list(edges):
            if e in all_possible:
                all_possible.remove(e)
            elif (e[1], e[0]) in all_possible:
                all_possible.remove((e[1], e[0]))

        # Add random remaining edges
        remaining = list(all_possible)
        import random
        while len(edges) < num_roads and remaining:
            idx = self.s_generate_int(int_range=(0, len(remaining) - 1))
            edges.append(remaining.pop(idx))

        return edges
    

