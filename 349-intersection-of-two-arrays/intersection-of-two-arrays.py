class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        

        s=set()
        ans=set()

        for i in nums1:
            
            s.add(i)

        for i in nums2:
            if i in s:
                ans.add(i)

            

        return list(ans)
                

        

        
