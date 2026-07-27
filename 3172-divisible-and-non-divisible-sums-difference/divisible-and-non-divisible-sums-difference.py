class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nums1=0
        nums2=0

        for i in range(0,n+1,1):
            if i%m!=0:
                nums1=nums1+i

        for i in range(0,n+1,1):
            if i%m==0:
                nums2=nums2+i
        return nums1-nums2
        

            
        