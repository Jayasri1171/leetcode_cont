class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        minn =34567890123456789
        l=[]
        for i in range(len(timePoints)):
            hr=int(timePoints[i][0])*10+int(timePoints[i][1])
            mi=int(timePoints[i][3])*10+int(timePoints[i][4])
            timee=hr*60+mi
            l.append(timee)
        # print(l)
        for i in range(1,len(l)):
            diff=l[i]-l[i-1]
            if diff<minn:
                minn=diff
        oo=(l[0]+1440)-l[len(l)-1]
        if oo<minn:
            minn=oo
        return minn

        