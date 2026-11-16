class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s,t=list(s),list(t)
        return sorted(s) == sorted(t)
        