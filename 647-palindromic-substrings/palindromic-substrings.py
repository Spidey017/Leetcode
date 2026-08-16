class Solution:
    def countSubstrings(self, s: str) -> int:
        sub=[]
        count=0

        for i in range(0,len(s)):
            x=""
            for j in range(i,len(s)):
                x=x+s[j]

                if x==x[::-1]:
                    sub.append(x)

        for i in sub:
            if i==i[::-1]:
                count=count+1

        return count
        