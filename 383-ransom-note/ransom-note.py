class Solution:
    def canConstruct(self, a: str,b: str) -> bool:

        x=list(b)

        for i in a:
            if i in x:
                x.remove(i)
            else:
                return False
        return True


        