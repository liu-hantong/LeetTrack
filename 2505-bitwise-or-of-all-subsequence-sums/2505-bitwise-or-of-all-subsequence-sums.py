class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        bit = 0
        for i in range(64):
            for j, num in enumerate(nums):
                bit += num & 1
                nums[j] >>= 1
            if bit:
                ans |= 1 << i
                bit >>= 1
        return ans