class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        t=[]
        def back(l,r):
            if l==r==n:
                res.append("".join(t))
                return
            if l<n:
                t.append("(")
                back(l+1,r)
                t.pop()
            if r<l:
                t.append(")")
                back(l,r+1)
                t.pop()
        back(0,0)
        return res