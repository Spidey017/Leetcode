class Solution:
    def sortString(self, s: str) -> str:

        h={}

        for i in s:
            h[i]=h.get(i,0)+1

        ans=""

        while len(ans)<len(s):
            for i in sorted(h.keys()):
                if h[i]>0:
                    ans=ans+i
                    h[i]-=1

            for i in sorted(h.keys(),reverse=True):
                if h[i]>0:
                    ans=ans+i
                    h[i]-=1

        return ans


            