class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        h={}

        for i in nums:
            if i in h:
                h[i]=h[i]+1

            else:
                h[i]=1

        ans=[]

        for i in h:
            if h[i]>1:
                ans.append(i)

        
        nums1=set(nums)
        sum1=0
        n=len(nums)+1


        for i in range(0,n,1):
            sum1=sum1+i

        sum2=0

        for i in nums1:
            sum2=sum2+i

        ans1=sum1-sum2

        ans.append(ans1)

        return ans


        