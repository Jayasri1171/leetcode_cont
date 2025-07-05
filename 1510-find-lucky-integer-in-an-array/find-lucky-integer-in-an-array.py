class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        arr=list(set(arr))
        arr.sort()
        arr=arr[::-1]
        # print(d)
        for i in range(len(arr)):
            if arr[i]==d[arr[i]]:
                # print(arr[i])
                return arr[i]
        return -1
            
        