class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                goal = target - nums[i] - nums[j]
                left = j + 1
                right = n - 1
                while left < right:
                    while left < right and left > j + 1 and nums[left - 1] == nums[left]:
                        left += 1
                    while left < right and right < n - 1 and nums[right + 1] == nums[right]:
                        right -= 1
                    if left == right:
                        break
                    if nums[left] + nums[right] > goal:
                        right -= 1
                    elif nums[left] + nums[right] == goal:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                    else:
                        left += 1
        return ans