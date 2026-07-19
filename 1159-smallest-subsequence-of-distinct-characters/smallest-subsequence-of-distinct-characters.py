class Solution:
    def smallestSubsequence(self, s: str) -> str:
        h = {}

        # Frequency
        for i in s:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1

        stack=[]
        visited =set()

        for ch in s:
            h[ch]=h[ch]-1

            if ch in visited:
                continue

            while stack and stack[-1]>ch and h[stack[-1]]>0:
                visited.remove(stack.pop())

            stack.append(ch)
            visited.add(ch)

        return "".join(stack)