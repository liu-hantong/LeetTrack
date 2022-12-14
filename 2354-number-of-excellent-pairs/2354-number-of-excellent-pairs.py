class Solution:
    def countExcellentPairs(self, A: List[int], k: int) -> int:
        c = Counter(map(int.bit_count, set(A)))
        return sum(c[k1] * c[k2] for k1 in c for k2 in c if k1 + k2 >= k)
