class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s)<k:
            return 0

        h={}


        for ch in s:
            h[ch]=h.get(ch,0)+1


        for ch in h:
            if h[ch]<k:

                left=s.split(ch)


                return max(self.longestSubstring(i,k) for i in left)

        return len(s)

        