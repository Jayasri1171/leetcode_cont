class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a=bin(start)
        b=bin(goal) 
        a=a[2::]
        b=b[2::]
        a=a[::-1]
        b=b[::-1]
        count=0
        if(len(a)>len(b)):
            i=0
            j=0
            while(j<len(b)):
                if a[i]!=b[j]:
                    count+=1
                i+=1
                j+=1
            while(i<len(a)):
                if a[i]=='1':

                    count+=1
                i+=1
        else:
            i=0
            j=0
            while(i<len(a)):
                if a[i]!=b[j]:
                    count+=1
                i+=1
                j+=1
            while(j<len(b)):
                if b[j]=='1':
                    count+=1
                j+=1

        return count
        