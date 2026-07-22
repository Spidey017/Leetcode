class Solution:
    def threeConsecutiveOdds(self, a: List[int]) -> bool:

        for i in range(0,len(a)-2):
            if a[i]%2!=0 and a[i+1]%2!=0 and a[i+2]%2!=0:
                return True

        return False

        