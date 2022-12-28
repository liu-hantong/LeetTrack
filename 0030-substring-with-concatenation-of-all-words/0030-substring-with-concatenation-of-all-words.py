class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []
        n = len(s)
        k = len(words[0])
        c = Counter(words)
        t = len(words)
        def slide_window(i):
            left = i
            cp = c.copy()
            for right in range(i + k, n + 1, k):
                nw = s[right-k:right]
                if nw in c:
                    print(nw)
                    cp[nw] -= 1
                else:
                    left = right
                    cp = c.copy()
                while cp[nw] < 0:
                    cp[s[left:left+k]] += 1
                    left += k
                if right - left == k * t:
                    ans.append(left)
                    cp[s[left:left+k]] += 1
                    left += k
                    
        for i in range(k):
            slide_window(i)
      
        return ans