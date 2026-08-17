class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        ans=[]

        for i in range(0,len(arr2)):
            for j in range(0,len(arr1)):
                if arr2[i]==arr1[j]:
                    ans.append(arr1[j])

        remaining=[]
        for i in arr1:
            if i not in arr2:
                remaining.append(i)

        remaining.sort()

        ans.extend(remaining)


        return ans


        