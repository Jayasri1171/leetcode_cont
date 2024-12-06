class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
       
        count=0
        suncount=0
        i=1
        j=0
        banned=list(set(banned))
        banned.sort()
        # print(banned)
        while(i<=n and j<len(banned)):
            if i==banned[j]:
                j+=1
            else:
                if suncount+i<=maxSum:
                    suncount+=i
                    count+=1
                else:
                    break
            i+=1
        # print(suncount,count,i)
        while(True):
            if suncount+i<=maxSum and i<=n:
                suncount+=i
                count+=1
                i+=1
            else:
                break
        return count

        