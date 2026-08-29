class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi=0
        left=0
        right=0
        d={}

        while right<len(s):

            if s[right] in d:
                left=max(left,d[s[right]]+1)


            maxi=max(maxi,right-left+1)

            d[s[right]]=right
            right=right+1

        return maxi



        