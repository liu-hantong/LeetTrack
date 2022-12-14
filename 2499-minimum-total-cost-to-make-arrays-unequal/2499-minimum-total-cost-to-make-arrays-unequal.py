class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        ans = same_cnt = mode_cnt = mode = 0
        cnt = [0] * (len(nums1) + 1)
        for i, (x, y) in enumerate(zip(nums1, nums2)):
            if x == y:
                ans += i
                same_cnt += 1
                cnt[x] += 1
                if cnt[x] > mode_cnt:
                    mode_cnt, mode = cnt[x], x
        for i, (x, y) in enumerate(zip(nums1, nums2)):
            if mode_cnt * 2 <= same_cnt: break
            if x != y and x != mode and y != mode:
                ans += i
                same_cnt += 1
        return ans if mode_cnt * 2 <= same_cnt else -1