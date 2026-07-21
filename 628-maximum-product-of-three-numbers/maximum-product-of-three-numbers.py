class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        ans=1
        ans= nums[-1]*nums[-2]*nums[-3]

        if nums[0] * nums[1] * nums[-1] > ans:
            ans = nums[0] * nums[1] * nums[-1]

        return ans
        
        return ans


        