class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unqiue=sorted(set(arr))

        rank={}
        
        r=1
        for i in unqiue:
            rank[i]=r
            r=r+1


        ans=[]
        for i in arr:
            ans.append(rank[i])

        return ans

