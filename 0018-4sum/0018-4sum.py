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
                seen = set()
                added = set()
                for k in range(j + 1, n):
                    if goal - nums[k] in seen and nums[k] not in added:
                        ans.append([nums[i], nums[j], nums[k], goal - nums[k]])
                        added.add(nums[k])
                    seen.add(nums[k])
        return ans