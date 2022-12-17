class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n) * (n + 1) // 2
        count = 0
        for num in nums:
            if num % 2 == 1:
                count += 1
            else:
                total -= (count) * (count + 1) // 2
                count = 0
        total -= (count) * (count + 1) // 2
        return total
    