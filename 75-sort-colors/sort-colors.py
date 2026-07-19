class Solution:
    def sortColors(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0,len(a)-1+1,1):
            for j in range(i+1,len(a)-1+1,1):
                if a[i]>a[j]:
                    a[i],a[j]=a[j],a[i]

                
        