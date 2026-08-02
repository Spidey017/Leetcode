class Solution:
    def increasingTriplet(self, nums):
        n = len(nums)

        pre = [0] * n
        post = [0] * n

        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = min(pre[i - 1], nums[i])

        post[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            post[i] = max(nums[i], post[i + 1])

        for i in range(1, n - 1):
            if nums[i] > pre[i - 1] and nums[i] < post[i + 1]:
                return True

        return False