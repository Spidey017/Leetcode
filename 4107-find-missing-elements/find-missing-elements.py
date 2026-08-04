class Solution:
    def findMissingElements(self, a: List[int]) -> List[int]:
        s=set(a)

        m=max(a)
        n=min(a)

        ans=[]
        for i in range(n,m+1,1):
            if i not in s:
                ans.append(i)

        return ans

        