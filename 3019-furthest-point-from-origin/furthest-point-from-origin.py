class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        lf=0
        rf=0
        ef=0
        for i in moves:
            if i=="L":
                lf+=1
            elif i=='R':
                rf+=1
            else:
                ef+=1
        if lf>rf:
            return lf-rf+ef
        return rf-lf+ef
