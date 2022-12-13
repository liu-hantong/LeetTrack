class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        fa = list(range(n))
        def find(x):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]
        def merge(f, to):
            f = find(f)
            to = find(to)
            if f != to:
                fa[f] = to
        ans = [0] * len(queries)
        edgeList.sort(key=lambda x : x[2])
        queries = sorted(enumerate(queries), key=lambda x : x[1][2])
        j = 0
        for i, (p, q, limit) in queries:
            while j < len(edgeList) and edgeList[j][2] < limit:
                merge(edgeList[j][0], edgeList[j][1])
                j += 1
            if find(q) == find(p):
                ans[i] = True
            else:
                ans[i] = False
        return ans