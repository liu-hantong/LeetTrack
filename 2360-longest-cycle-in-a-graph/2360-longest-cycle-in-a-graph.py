class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        time = [0] * n
        res = -1
        clock = 1
        for i in range(n):
            if time[i]:
                continue
            x = i
            start_time = clock
            while x != -1:
                if time[x]:
                    if time[x] >= start_time:
                        res = max(res, clock - time[x])
                        break
                    break
                time[x] = clock
                clock += 1
                x = edges[x]
        return res