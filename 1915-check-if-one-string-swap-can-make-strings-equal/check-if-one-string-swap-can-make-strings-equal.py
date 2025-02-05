class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count=0
        check=0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                if count==0:
                    m=s2[i]
                    n=s1[i]
                    count+=1
                elif count==1:
                    if s1[i]!=m or s2[i]!=n:
                        return False
                    else:
                        check=1
                        count+=1
                else:
                    return False
        if check==0 and count!=0:
            return False
        return True

        