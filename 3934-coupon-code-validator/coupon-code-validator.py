class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        chk='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789_'
        d={"electronics":[],"grocery":[],"pharmacy":[],"restaurant":[]}
        for i in range(len(code)):
            if(isActive[i]==True):
                if businessLine[i] in d:
                    tmp=0
                    if code[i]!="":
                        for ii in code[i]:
                            if ii not in chk:
                                tmp=-1
                                break
                        if tmp==0:
                            d[businessLine[i]].append(code[i])
        ans=[]
        for i in d:
            z=d[i]
            z.sort()
            if z!=[""]:
                ans+=z
        return ans