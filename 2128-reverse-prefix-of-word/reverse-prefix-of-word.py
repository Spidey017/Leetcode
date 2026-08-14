class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        a = list(word)

        i = 0
        while i < len(word):
            if word[i] == ch:
                break

            i = i + 1

        if i==len(word):
            return word

        k = 0
        j = i

        while k < j:
            a[k], a[j] = a[j], a[k]

            k = k + 1
            j = j - 1

        return "".join(a)