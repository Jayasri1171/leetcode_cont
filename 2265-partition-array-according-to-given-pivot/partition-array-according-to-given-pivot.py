class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ls=[]
        gr=[]
        pv=[]
        for i in nums:
            if i==pivot:
                pv.append(i)
            elif i<pivot:
                ls.append(i)
            else:
                gr.append(i)
        ans=ls+pv+gr
        return ans