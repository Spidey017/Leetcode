class Solution:
    def isBalanced(self, num: str) -> bool:


        eans=0

        oans=0
        for i in range(0,len(num),2):

            eans=eans+int(num[i])


        for i in range(1,len(num),2):

            oans=oans+int(num[i])

        if eans==oans:
            return True

        return False

        
        