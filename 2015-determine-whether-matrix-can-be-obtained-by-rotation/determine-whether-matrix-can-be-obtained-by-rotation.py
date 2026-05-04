class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for k in range(4):
            for i in range(len(mat)):
                for j in range(0,i):
                    mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
            for i in range(len(mat)):
                mat[i]=mat[i][::-1]
            if mat==target:
                return True
        return False