class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        h={}

        for i in range(len(s)):
            h[s[i]]=i

        ans=[]
        start=0
        end=0

        for i in range(0,len(s)):
            end=max(end,h[s[i]])

            if i==end:
                ans.append(end-start+1)
                start=i+1

        return ans



        