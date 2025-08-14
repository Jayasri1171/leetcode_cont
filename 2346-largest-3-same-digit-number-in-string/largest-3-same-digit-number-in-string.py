class Solution:
    def largestGoodInteger(self, num: str) -> str:
        chk=num[0]
        cnt=1
        ans=0
        rtu=""
        for i in range(1,len(num)):
            if num[i]==chk:
                cnt+=1
                if cnt==3:
                    if int(num[i])>=ans:
                        ans=int(num[i])
                        rtu=num[i]+num[i]+num[i]
            else:
                chk=num[i]
                cnt=1
        return rtu



        