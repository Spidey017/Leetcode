class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:

        e_sum=0

        for i in nums:
            e_sum=e_sum+i

        d_sum=0

        for i in nums:

            while i>0:
                r=i%10
                d_sum=d_sum+r
                i=i//10


                   


        return abs(e_sum-d_sum)




        