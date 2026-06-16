import string
from . import Problem as Testing, ProblemType
from typing import List


class Solution1(Testing):
    date = "2025-9-7"
    def __init__(self):
        Testing.__init__(self,
                         degree=0,
                         idx=3674,
                         types=[ProblemType.Bit, ProblemType.Brainteasers, ProblemType.Array],
                         pass_rate=0.735,
                         description="给你一个长度为 `n` 的整数数组 `nums`。\n\n在一次操作中，可以选择任意子数组 `nums[l...r]` （`0 <= l <= r < n`），并将该子数组中的每个元素 **替换** 为所有元素的 **按位与（bitwise AND）**结果。\n\n返回使数组 `nums` 中所有元素相等所需的最小操作次数。\n\n**子数组** 是数组中连续的、非空的元素序列。\n\n \n\n**示例 1：**\n\n**输入：** nums = [1,2]\n\n**输出：** 1\n\n**解释：**\n\n选择 `nums[0...1]`：`(1 AND 2) = 0`，因此数组变为 `[0, 0]`，所有元素在一次操作后相等。\n\n**示例 2：**\n\n**输入：** nums = [5,5,5]\n\n**输出：** 0\n\n**解释：**\n\n`nums` 本身是 `[5, 5, 5]`，所有元素已经相等，因此不需要任何操作。\n\n \n\n**提示：**\n\n- `1 <= n == nums.length <= 100`\n- `1 <= nums[i] <= 10**5`"
                         )

    def solve(self, nums: list[int]) -> int:
        return int(any(x != nums[0] for x in nums))

    def gen(self):
        return self.generate_list_int(list_length_range=(1, 100), int_range=(1, 100000)),


class Solution2(Testing):
    date = "2025-9-7"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3675,
                         types=[ProblemType.Greedy, ProblemType.String],
                         pass_rate=0.618,
                         description="给你一个仅由小写英文字母组成的字符串 `s`。\n\n你可以执行以下操作任意次（包括零次）：\n\n- 选择字符串中出现的一个字符 `c`，并将 **每个** 出现的 `c` 替换为英文字母表中 **下一个** 小写字母。\n\n返回将 `s` 转换为仅由 `'a'` 组成的字符串所需的最小操作次数。\n\n**注意：**字母表是循环的，因此 `'z'` 的下一个字母是 `'a'`。\n\n \n\n**示例 1：**\n\n**输入：** s = \"yz\"\n\n**输出：** 2\n\n**解释：**\n\n- 将 `'y'` 变为 `'z'`，得到 `\"zz\"`。\n- 将 `'z'` 变为 `'a'`，得到 `\"aa\"`。\n- 因此，答案是 2。\n\n**示例 2：**\n\n**输入：** s = \"a\"\n\n**输出：** 0\n\n**解释：**\n\n- 字符串 `\"a\"` 已经由 `'a'` 组成。因此，答案是 0。\n\n \n\n**提示：**\n\n- `1 <= s.length <= 5 * 10**5`\n- `s` 仅由小写英文字母组成。"
                         )

    def solve(self, s: str) -> int:
        if 'b' in s:
            return 25
        # 'z' 的下一个字符是 '{'
        min_c = min((c for c in s if c != 'a'), default='{')
        return ord('{') - ord(min_c)

    def gen(self):
        return self.generate_string(vocab=string.ascii_lowercase, length_range=(1, 5000)),


class Solution3(Testing):
    date = "2025-9-7"
    def __init__(self):
        Testing.__init__(self,
                         degree=1,
                         idx=3676,
                         types=[ProblemType.Stack, ProblemType.Array, ProblemType.MonotonyStack],
                         pass_rate=0.432,
                         description="给你一个整数数组 `nums`，包含 **互不相同** 的元素。\n\n`nums` 的一个子数组 `nums[l...r]` 被称为 **碗（bowl）**，如果它满足以下条件：\n\n- 子数组的长度至少为 3。也就是说，`r - l + 1 >= 3`。\n- 其两端元素的 **最小值** **严格大于** 中间所有元素的 **最大值**。也就是说，`min(nums[l], nums[r]) > max(nums[l + 1], ..., nums[r - 1])`。\n\n返回 `nums` 中 **碗** 子数组的数量。\n\n**子数组** 是数组中连续的元素序列。\n\n \n\n**示例 1:**\n\n**输入:** nums = [2,5,3,1,4]\n\n**输出:** 2\n\n**解释:**\n\n碗子数组是 `[3, 1, 4]` 和 `[5, 3, 1, 4]`。\n\n- `[3, 1, 4]` 是一个碗，因为 `min(3, 4) = 3 > max(1) = 1`。\n- `[5, 3, 1, 4]` 是一个碗，因为 `min(5, 4) = 4 > max(3, 1) = 3`。\n\n**示例 2:**\n\n**输入:** nums = [5,1,2,3,4]\n\n**输出:** 3\n\n**解释:**\n\n碗子数组是 `[5, 1, 2]`、`[5, 1, 2, 3]` 和 `[5, 1, 2, 3, 4]`。\n\n**示例 3:**\n\n**输入:** nums = [1000000000,999999999,999999998]\n\n**输出:** 0\n\n**解释:**\n\n没有子数组是碗。\n\n \n\n**提示:**\n\n- `3 <= nums.length <= 10**5`\n- `1 <= nums[i] <= 10**9`\n- `nums` 由不同的元素组成。"
                         )

    def solve(self, nums: List[int]) -> int:
        ans = 0
        st = []
        for i, x in enumerate(nums):
            while st and nums[st[-1]] < x:
                # j=st[-1] 右侧严格大于 nums[j] 的数的下标是 i
                if i - st.pop() > 1:  # 子数组的长度至少为 3
                    ans += 1
            # i 左侧大于等于 nums[i] 的数的下标是 st[-1]
            if st and i - st[-1] > 1:  # 子数组的长度至少为 3
                ans += 1
            st.append(i)
        return ans


    def gen(self):
        return self.generate_list_int(list_length_range=(3, 500), int_range=(1, 1000), different=True),



class Solution4(Testing):
    date = "2025-9-7"
    def __init__(self):
        Testing.__init__(self,
                         degree=2,
                         idx=3677,
                         types=[ProblemType.Bit, ProblemType.Math],
                         pass_rate=0.287,
                         description="给你一个 **非负** 整数 `n`。\n\n如果一个 **非负** 整数的二进制表示（不含前导零）正着读和倒着读都一样，则称该数为 **二进制回文数**。\n\n返回满足 `0 <= k <= n` 且 `k` 的二进制表示是回文数的整数 `k` 的数量。\n\n**注意：** 数字 0 被认为是二进制回文数，其表示为 `\"0\"`。\n\n \n\n**示例 1:**\n\n**输入:** n = 9\n\n**输出:** 6\n\n**解释:**\n\n在范围 `[0, 9]` 内，二进制表示为回文数的整数 `k` 有：\n\n- `0 → \"0\"`\n- `1 → \"1\"`\n- `3 → \"11\"`\n- `5 → \"101\"`\n- `7 → \"111\"`\n- `9 → \"1001\"`\n\n`[0, 9]` 中的所有其他值的二进制形式都不是回文。因此，计数为 6。\n\n**示例 2:**\n\n**输入:** n = 0\n\n**输出:** 1\n\n**解释:**\n\n由于 `\"0\"` 是一个回文数，所以计数为 1。\n\n**提示:**\n\n- `0 <= n <= 10**15`"
                         )

    def solve(self, n: int) -> int:
        if n == 0:
            return 1

        m = n.bit_length()  # n 的二进制长度

        # 对于二进制长度小于 m 的回文数，左半边随便填
        ans = 1  # 0 也是回文数
        # 枚举二进制长度，最高位填 1，回文数左半的其余位置随便填
        for i in range(1, m):
            ans += 1 << ((i - 1) // 2)

        # 最高位一定是 1，从次高位开始填
        for i in range(m - 2, m // 2 - 1, -1):
            if n >> i & 1:
                # 这一位可以填 0，那么回文数左半的剩余位置可以随便填
                ans += 1 << (i - m // 2)
            # 在后续循环中，这一位填 1

        pal = n >> (m // 2)
        # 左半反转到右半
        # 如果 m 是奇数，那么去掉回文中心再反转
        v = pal >> (m % 2)
        while v:
            pal = pal * 2 + v % 2
            v //= 2
        if pal <= n:
            ans += 1

        return ans


    def gen(self):
        return self.generate_int(int_range=(1, 100000)),

