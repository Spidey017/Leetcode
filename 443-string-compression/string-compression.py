class Solution:
    def compress(self, chars: List[str]) -> int:
        ans=[]

        i=0

        while i <len(chars):
            ch=chars[i]
            count=0

            while i<len(chars) and chars[i]==ch:
                count=count+1
                i=i+1

            ans.append(ch)

            if count>1:
                for x in str(count):
                    ans.append(x)

        chars[:]=ans

        return len(ans)

        