class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        c=[]
        for i in range(len(A)):
            a=A[0:i+1]
            b=B[0:i+1]
            C=a+b
            CC=list(set(C))
            # print(a,b,C,CC)
            c.append(len(C)-len(CC))
        return c

        