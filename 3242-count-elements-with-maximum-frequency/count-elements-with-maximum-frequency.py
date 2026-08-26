class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        h = {}

        for i in nums:
            if i in h:
                h[i] = h[i] + 1
            else:
                h[i] = 1

        max_freq = max(h.values())

        ans = 0

        for i in h:
            if h[i] == max_freq:
                ans = ans + h[i]

        return ans