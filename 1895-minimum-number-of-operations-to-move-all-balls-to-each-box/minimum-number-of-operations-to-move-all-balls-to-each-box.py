class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l=[]
        for i in range(len(boxes)):
            if boxes[i]=="1":
                l.append(i)
        ans=[]
        for i in range(len(boxes)):
            count=0
            for j in range(len(l)):
                count+=abs(i-l[j])
            ans.append(count)
        return ans
        