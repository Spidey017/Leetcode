class Solution:
    def rob(self, nums: List[int]) -> int:
        
        ans = 0
        prev = 0

        for i in range(len(nums)):
            temp = ans
            ans = max(ans, prev + nums[i])
            prev = temp

        return ans

