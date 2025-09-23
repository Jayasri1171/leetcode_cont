class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1=list(version1.split('.'))
        l2=list(version2.split('.'))
        print(l1,l2)
        i=0
        j=0
        while(i<len(l1) and j<len(l2)):
            if(int(l1[i])<int(l2[j])):
                return -1
            elif(int(l1[i])>int(l2[j])):
                return 1
            i+=1
            j+=1
        if(i<len(l1)):
            while(i<len(l1)):
                if(int(l1[i])>0):
                    return 1
                i+=1
        if(j<len(l2)):
            while(j<len(l2)):
                if(int(l2[j])>0):
                    return -1
                j+=1
        return 0
        