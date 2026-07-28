class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]


        for i in nums:
            if i>0:
                pos.append(i)

            else:
                neg.append(i)


        ans=[]
        x=0
        for i in range(0,len(pos)-1+1,1):
            ans.append(pos[x])
            ans.append(neg[x])
            x=x+1

        return ans

        