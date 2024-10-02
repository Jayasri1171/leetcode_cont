class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        changed=arr[::]
        
        changed=list(set(changed))
        changed.sort()
        d={}
        for i in range(len(changed)):
            d[changed[i]]=i+1


        l=[]
        # print(changed)
        for i in range(len(arr)):
            l.append(d[arr[i]])
        return l

        
        
        