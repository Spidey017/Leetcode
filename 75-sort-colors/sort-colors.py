class Solution:
    def sortColors(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0,len(a)-1+1,1):
            for j in range(0,len(a)-2+1,1):
                if a[j]>a[j+1]:
                    a[j],a[j+1]=a[j+1],a[j]

                
        