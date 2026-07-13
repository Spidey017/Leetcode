class Solution:
    def sequentialDigits(self, low: int, high: int):
        ans = []

        for i in range(1, 9):
            num = i
            next_digit = i + 1

            while next_digit <= 9:
                num = num * 10 + next_digit

                if low <= num <= high:
                    ans.append(num)

                next_digit += 1

        ans.sort()
        return ans