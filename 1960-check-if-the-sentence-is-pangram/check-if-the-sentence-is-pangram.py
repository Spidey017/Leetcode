class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

        temp=[]

        for i in sentence:
            if i not in temp:
                temp.append(i)
        count=0

        for i in temp:
            if i in alphabets:
                count=count+1
            
        if count==26:
            return True

        return False