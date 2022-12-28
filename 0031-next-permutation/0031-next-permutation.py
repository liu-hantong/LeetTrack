from bisect import bisect_right
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, -1, -1):
            nextBig = inf
            nextPos = 0
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i] and nums[j] < nextBig:
                    nextBig, nextPos = nums[j], j
            if nextBig != inf:
                nums[nextPos], nums[i] = nums[i], nums[nextPos]
                nums[i+1:] = sorted(nums[i+1:])
                return
        nums.sort()