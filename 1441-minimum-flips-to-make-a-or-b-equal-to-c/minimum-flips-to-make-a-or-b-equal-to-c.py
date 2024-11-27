class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        aa=list(bin(a))
        aa=aa[2::]
        bb=list(bin(b))
        bb=bb[2::]
        cc=list(bin(c))
        cc=cc[2::]
        count=0
        z=len(cc)
        bb=['0']*z+bb
        aa=['0']*z+aa
        # print(aa,bb,cc)
        i=len(cc)-1
        j=len(bb)-1
        k=len(aa)-1
        while(i>=0):
            if cc[i]=='1':
                if aa[k]=='0' and bb[j]=='0':
                    count+=1
            else:
                if aa[k]=='1':
                    count+=1
                if bb[j]=='1':
                    count+=1
            k-=1
            j-=1
            i-=1
        for jj in range(0,k+1):
            if aa[jj]=='1':
                count+=1
        for jj in range(0,j+1):
            if bb[jj]=='1':
                count+=1
        return count


        