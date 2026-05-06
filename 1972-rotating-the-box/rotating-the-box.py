class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        for i in range(len(boxGrid)):
            sz=0
            tmp=0
            for j in range(len(boxGrid[0])):
                if(boxGrid[i][j]=="#"):
                    sz+=1
                elif(boxGrid[i][j]=="*"):
                    sz=0
                    tmp=j+1
                else:
                    if(sz>0):
                        boxGrid[i][tmp]="."
                        boxGrid[i][j]="#"
                        tmp=tmp+1
                    else:
                        tmp=j+1
        # print(boxGrid)
        boxGrid=boxGrid[::-1]
        transpose = [list(row) for row in zip(*boxGrid)]
        # transpose = transpose[::-1]
        return transpose


