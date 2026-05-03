class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if(len(s)!=len(goal)):
            return False
        for i in range(len(goal)):
            z=s[i:]+s[0:i]
            if(z==goal):
                return True
        return False