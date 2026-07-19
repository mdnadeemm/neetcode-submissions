class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sor = "".join(sorted(s))
        tor = "".join(sorted(t))
        
        for i in range(len(sor)):
            if sor[i] != tor[i]:
                return False
        return True
