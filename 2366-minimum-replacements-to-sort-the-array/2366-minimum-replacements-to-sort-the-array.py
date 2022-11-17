class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        m = nums[-1]
        for num in reversed(nums):
            count = ceil(num / m) - 1
            res += count
            m = num // (count + 1)
        return res