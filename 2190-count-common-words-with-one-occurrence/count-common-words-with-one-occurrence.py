class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:

        h1={}

        for i in words1:
            if i in h1:
                h1[i]=h1[i]+1

            else:
                h1[i]=1

        h2={}

        for i in words2:
            if i in h2:
                h2[i]=h2[i]+1

            else:
                h2[i]=1

        count=0
        for i in h1:
            if h1[i]==1 and  i in h2 and h2[i]==1 :
                count=count+1

        return count
            
        