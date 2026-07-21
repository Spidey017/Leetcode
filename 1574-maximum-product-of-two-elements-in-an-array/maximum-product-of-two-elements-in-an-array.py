class Solution:
    def maxProduct(self, a: List[int]) -> int:
        ans=0


        for i in range(0,len(a)):
            for j in range(i+1,len(a)):
                x=(a[i]-1)*(a[j]-1)
                if x>ans:
                    ans=x

        return ans
        