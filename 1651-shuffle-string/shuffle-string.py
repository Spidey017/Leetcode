class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans=[""]*len(s)      
        for i in range(0,len(s)):
            ans[indices[i]]=s[i]

        return "".join(ans)
