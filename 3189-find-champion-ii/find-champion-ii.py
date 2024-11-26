class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        l=[]
        m=[]
        if n==1:
            return 0
        for i in range(len(edges)):
            l.append(edges[i][0])
            l.append(edges[i][1])
            m.append(edges[i][1])
        l=list(set(l))
        m=list(set(m))
        if len(l)<n:
            return -1
        
        # print(l,m)
        if len(l)-len(m)!=1:
            return -1
        else:
            l.sort()
            m.sort()
            for j in range(len(m)):
                if l[j]!=m[j]:
                    return l[j]
            return l[len(l)-1]

        