class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        h={}

        for path in paths:
            h[path[0]]=path[1]

        for path in paths:
            if path[1] not in h:
                return path[1]