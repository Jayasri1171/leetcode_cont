class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1[0]!=s2[0]:
            if s1[2]==s2[2]:
                return False
            else:
                if s1[2]!=s2[0]:
                    return False
                if s2[2]!=s1[0]:
                    return False
        if s1[1]!=s2[1]:
            if s1[3]==s2[3]:
                return False
            else:
                if s1[3]!=s2[1]:
                    return False
                if s2[3]!=s1[1]:
                    return False
        if s1[3]!=s2[3]:
            if s1[1]==s2[1]:
                return False
            else:
                if s1[3]!=s2[1]:
                    return False
                if s2[3]!=s1[1]:
                    return False
        if s1[2]!=s2[2]:
            if s1[0]==s2[0]:
                return False
            else:
                if s1[2]!=s2[0]:
                    return False
                if s2[2]!=s1[0]:
                    return False
        return True

        