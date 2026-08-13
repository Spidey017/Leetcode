class Solution:
    def repeatedCharacter(self, s: str) -> str:

        h={}

        for i in s:
            if i in h:
                return i
            else:
                h[i]=1

        return ""
        