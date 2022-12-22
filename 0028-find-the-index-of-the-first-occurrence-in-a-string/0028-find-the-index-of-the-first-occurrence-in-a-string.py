class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        i = 0
        for j in range(len(haystack)):
            for i in range(len(needle)):
                if j + i < len(haystack):
                    if needle[i] != haystack[j + i]:
                        break
                    if i == len(needle) - 1:
                        return j
        return -1