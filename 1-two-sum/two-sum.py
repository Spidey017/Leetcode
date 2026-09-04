class Solution:
    def twoSum(self, nums, target):
        h={}

        for i in range(len(nums)):
            j=target-nums[i]

            if j in h:
                return [h[j],i]

            h[nums[i]]=i


        


            
           

        