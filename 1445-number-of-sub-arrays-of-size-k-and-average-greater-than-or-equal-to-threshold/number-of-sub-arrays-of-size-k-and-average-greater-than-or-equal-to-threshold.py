class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        s=0
        
        i=0
        count=0

        for j in range(len(arr)):
            s=s+arr[j]

            if j-i+1==k:
                avg=s/k

                if avg>=threshold:
                    count=count+1

                s=s-arr[i]
                i=i+1

        return count




        