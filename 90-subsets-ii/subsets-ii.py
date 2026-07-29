class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        ans = [[]]
        start = 0
        end = 0

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                start = end + 1
            else:
                start = 0

            end = len(ans) - 1

            for j in range(start, end + 1):
                ans.append(ans[j] + [nums[i]])

        return ans
        