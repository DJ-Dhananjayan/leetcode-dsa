class Solution:
    def pivotArray(self, nums: List[int], piv: int) -> List[int]:
        s=[]
        b=[]
        p=[]
        for i in nums:
            if i<piv :
                s.append(i)
            elif i>piv:
                b.append(i)
            else :
                p.append(i)
        ans=s+p+b
        return ans