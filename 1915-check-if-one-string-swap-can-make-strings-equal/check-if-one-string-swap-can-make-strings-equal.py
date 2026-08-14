class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        a=[]

        for i in range(0,len(s1)):
            if s1[i]!=s2[i]:
                a.append(i)

        if len(a)==0:
            return True
        if len(a)!=2:
            return False

        i=a[0]
        j=a[1]

        return  s1[i]==s2[j] and s2[i]==s1[j]

        