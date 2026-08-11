class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        h={}

        for i in s:
            if i in h:
                h[i]=h[i]+1
            else:
                h[i]=1
        
        freq=0
        for i in h.values():
            freq=i
            break

        for i in h.values():
            if i!=freq:
                return False
            
        return True
            




        