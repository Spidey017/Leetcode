class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        h={}

        for i in s:
            if i in h.keys():
                h[i]=h[i]+1

            else:
                h[i]=1

        for i in t:
            if i in h.keys():
                h[i]=h[i]-1

            else:
                return i


        for i in h.keys():
            if h[i]<0:
                return i
        