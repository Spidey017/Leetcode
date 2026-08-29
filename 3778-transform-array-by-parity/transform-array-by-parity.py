class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:

        for i in range(0,len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1

        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]

        return nums
        