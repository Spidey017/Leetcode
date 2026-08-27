class Solution:
    def maximumValue(self, strs: List[str]) -> int:

        ans=0

        for i in strs:
            if i.isdigit():
                value=int(i)
            else:
                value=len(i)

            ans=max(ans,value)

        return ans
        