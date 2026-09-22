class Solution:
    def reverseWords(self, s: str) -> str:

        a=s.split()

        ans=""

        for i in a:
            ans=ans+i[::-1]+" "


        return ans.strip()

        