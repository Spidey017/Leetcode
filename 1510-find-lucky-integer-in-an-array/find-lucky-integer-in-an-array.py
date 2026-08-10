class Solution:
    def findLucky(self, arr: List[int]) -> int:

        h={}

        for i in arr:
            if i in h:
                h[i]=h[i]+1

            else:
                h[i]=1
        max=0

        for i in h:
            
            if i==h[i]:
                if i>max:
                    max=i

            
        if max==0:
            return -1

        return max

        