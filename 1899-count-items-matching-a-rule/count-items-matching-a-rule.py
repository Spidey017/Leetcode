class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        type=[]
        color=[]

        name=[]

        for i in items:
            type.append(i[0])
            color.append(i[1])
            name.append(i[2])



        count=0
        for i in range(0,len(type)):
            if ruleKey=="color" and color[i]==ruleValue:
                count=count+1

            elif ruleKey=="type" and type[i]==ruleValue:
                count=count+1

            elif ruleKey=="name" and name[i]==ruleValue:
                count=count+1

            

        return count

        




        