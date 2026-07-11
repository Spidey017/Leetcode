class Solution:
    def convertToTitle(self, n: int) -> str:
        ans=""

        while n!=0:
            n=n-1

            ans=chr(n%26+65)+ans
            n=n//26

        return ans
        