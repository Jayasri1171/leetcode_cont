class Solution:
    def dividePlayers(self, skills: List[int]) -> int:
        s=sum(skills)
        skills.sort()
        half=len(skills)//2
        if(s%half!=0):
            return -1
        l=[]
        count=0
        value=s//half
        i=0
        j=len(skills)-1
        while(i<j):
            if skills[i]+skills[j]==value:
               
               
                count+=skills[i]*skills[j]
                # print(count,skills[i],skills[j])
                i+=1
                j-=1
            else:
                return -1
        return count

