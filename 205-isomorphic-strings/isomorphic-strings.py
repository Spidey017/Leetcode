class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        h={}

        for i in range(len(s)):
            if s[i] in h and h[s[i]]!=t[i]:
                return False

            elif s[i] not in h and t[i] in h.values():
                return False

            h[s[i]]=t[i]

        return True