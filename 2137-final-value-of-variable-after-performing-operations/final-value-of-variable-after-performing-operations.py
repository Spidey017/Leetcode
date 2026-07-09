class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for word in operations:
            if "+" in word:
                x=x+1
            else:
                x=x-1

        return x
        