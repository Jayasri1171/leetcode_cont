class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if(n*m!=len(original)):
            return []
        l=[]
        ij=0
        for i in range(m):
            p=[]
            for j in range(n):
                p.append(original[ij])
                ij+=1
            l.append(p)
        return l

        