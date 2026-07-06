class Solution:
    def searchInsert(self, a: List[int], x: int) -> int:
        i=0
        j=len(a)-1

        while i<=j:
            mid=i+j-i//2

            if a[mid]==x:
                return mid
            elif x>a[mid]:
                i=mid+1

            else:
                j=mid-1

        return i

            
         