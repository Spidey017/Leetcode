class Solution:
    def findNumbers(self, a: List[int]) -> int:
        count=0
        
        for i in a:
            if len(str(i))%2==0:
                count+=1

        return count