class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans=[]
        compare=words

        for i in words:
            for j in compare:
                if i!=j and i in j:
                    ans.append(i)
                    break
        return ans
        

               
        