class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        h={}

        for i in arr:
            if i in h:
                h[i]=h[i]+1
            else:
                h[i]=1

        ans=[]
        for i in h:
            if h[i]==1:
                ans.append(i)

        
        
        ans1=''

        for i in range(0,len(ans)):
            if i==k-1:
                ans1=ans1+ans[i]


        return ans1
                
        