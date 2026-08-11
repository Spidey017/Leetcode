class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win=[]
        los=[]

        for i in matches:
            win.append(i[0])
            los.append(i[1])

        a=[]
        loss=set(los)

        for i in win:
            if i not in loss and i not in a:
                a.append(i)

        h={}
        b=[]

        for i in los:
            if i in h:
                h[i]=h[i]+1

            else:
                h[i]=1
        for i in h:
            if h[i]==1:
                b.append(i)


        a.sort()
        b.sort()

        return [a,b]




        