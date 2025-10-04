class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        l=[]
        while(i<j):
            s=height[i]
            m=height[j]
            c=min(s,m)
            x=j-i
            l.append(c*x)
            if s==c:
                i+=1
            else:
                j=j-1
        return max(l)
        