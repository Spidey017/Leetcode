class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        s=set()
        ans=[]

        for i in nums:
            if i in s:
                ans.append(i)

            else:
                s.add(i)


        num1=0
        n=len(s)+1

        for i in range(0,n+1,1):
            num1=num1+i
        num2=0

        for i in s:
            num2=num2+i

        ans1=num1-num2

        ans.append(ans1)

        return ans



    



        