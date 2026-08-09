class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        h={}

        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1

        value=sorted(h)

        for i in range(1,len(h)):
            if h[value[0]]!=h[value[i]]:
                return [value[0],value[i]]


        return [-1,-1]

        

        