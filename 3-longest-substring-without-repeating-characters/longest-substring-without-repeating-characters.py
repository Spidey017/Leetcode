class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=""
        temp=""


        for i in s:
            if i not in temp:
                temp=temp+i

            else:

                if len(temp)>len(ans):
                    ans=temp

                x=0

                for j in range(0,len(temp),1):
                    if temp[j]!=i:
                        x=x+1

                    else:
                        x=x+1
                        break

                temp=temp[x:len(temp)-1+1]
                temp=temp+i

        if len(temp)>len(ans):
            ans=temp

        return len(ans)