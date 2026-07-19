class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = {}

        for i in nums1:
            if i in h:
                h[i]=h[i]+1
            else:
                h[i]=1



        ans = []

        for i in nums2:
            if i in h and h[i]>0:
                ans.append(i)
                h[i] -=1
       

        return ans