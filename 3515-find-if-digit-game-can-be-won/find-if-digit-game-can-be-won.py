class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:

        alice=0
        bob=0

        for i in nums:
            if i<10:
                alice=alice+i

            else:
                bob=bob+i

        return alice!=bob
        