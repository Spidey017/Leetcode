class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        a=s.split(" ")
        ans=""
        for i in range(0,k,1):
            ans=ans+a[i]+" "

        return ans.strip()
            

        