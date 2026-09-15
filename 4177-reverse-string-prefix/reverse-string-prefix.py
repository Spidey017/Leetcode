class Solution:
    def reversePrefix(self, s: str, k: int) -> str:

        ans=''

        for i in range(len(s)):
            if i==k-1:
                ans=s[:k][::-1]+s[k:]


        return ans
        