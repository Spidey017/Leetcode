class Solution:
    def frequencySort(self, a: List[int]) -> List[int]:
        h={}
        ans=[]

        for  i in a:
            if i in h:
                h[i]=h[i]+1
            else:
                h[i]=1


        a.sort(key=lambda x:(h[x],-x))
        return a

        
        