class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        n = len(cardPoints)

        s = 0

        
        for i in range(k):
            s += cardPoints[i]

        maxx = s

        
        for i in range(k):
            s -= cardPoints[k - 1 - i]
            s += cardPoints[n - 1 - i]

            if s > maxx:
                maxx = s

        return maxx

