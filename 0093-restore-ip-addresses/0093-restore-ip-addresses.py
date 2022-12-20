class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        ip = []
        n = len(s)
        def dfs(si, ri, num):
            if si == n and ri == 4:
                ans.append('.'.join(ip))
                return
            if si == n or ri == 4:
                return
            if num and int(num) > 255:
                return
            num = num + s[si]
            dfs(si + 1, ri, num)
            if num and int(num) <= 255:
                if len(num) > 1 and num[0] == '0':
                    return
                ip.append(num)
                dfs(si + 1, ri + 1, '')
                ip.pop()
        dfs(0, 0, '')
        return ans