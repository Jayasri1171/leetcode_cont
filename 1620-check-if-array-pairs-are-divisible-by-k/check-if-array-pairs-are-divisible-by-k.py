class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        l=[]
        for i in arr:
            l.append(i%k)
        l.sort()
        print(l)
        d={}
        for i in l:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        m=0
        for i in l:
            z=k-i
            if i==0:
                if m!=1:
                    if d[0]>=2:
                        d[0]-=2
                        m=1
                    else:
                        print("cvb")
                        return False
                else:
                    m=0
            else:

                if z not in d:
                    # print("cvb")
                    return False
                if d[z]>0:
                    d[z]-=1
                else:
                    # print("cvb")
                    return False
        return True
        