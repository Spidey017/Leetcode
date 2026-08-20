class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count=0

        i=0
        min=float("inf")


        for j in range(len(blocks)):
            if blocks[j]=="W":
                count=count+1

            if j-i+1==k:

                if count<min:
                    min=count

                if blocks[i]=="W":
                    count=count-1

                i=i+1

        return min


        

        

        