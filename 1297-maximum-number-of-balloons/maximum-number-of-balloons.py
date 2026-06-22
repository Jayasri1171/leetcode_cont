class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d={}
        for i in text:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        ans=[]
        if 'b' in d:
            ans.append(d['b'])
        else:
            ans.append(0)
        if 'a' in d:
            ans.append(d['a'])
        else:
            ans.append(0)
        if 'l' in d:
            ans.append(d['l']//2)
        else:
            ans.append(0)
        if 'o' in d:
            ans.append(d['o']//2)
        else:
            ans.append(0)
        if 'n' in d:
            ans.append(d['n'])
        else:
            ans.append(0)
        return min(ans)
