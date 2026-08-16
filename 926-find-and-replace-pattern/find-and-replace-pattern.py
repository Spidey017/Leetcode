class Solution:
    def findAndReplacePattern(self, s: List[str], t: str) -> List[str]:

        ans = []

        for word in s:

            h = {}
            flag = True

            for i in range(len(t)):

                if word[i] in h and h[word[i]] != t[i]:
                    flag = False
                    break

                if word[i] not in h and t[i] in h.values():
                    flag = False
                    break

                h[word[i]] = t[i]

            if flag:
                ans.append(word)

        return ans