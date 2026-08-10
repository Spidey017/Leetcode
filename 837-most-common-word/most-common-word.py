class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        h = {}

        paragraph = paragraph.lower()

        for i in paragraph:
            if not i.isalpha():
                paragraph = paragraph.replace(i, " ")

        words = paragraph.split()

        for i in words:
            if i in h:
                h[i] = h[i] + 1
            else:
                h[i] = 1

        ans = ""
        c = 0

        for i in h:
            if i not in banned and h[i] > c:
                ans = i
                c = h[i]

        return ans