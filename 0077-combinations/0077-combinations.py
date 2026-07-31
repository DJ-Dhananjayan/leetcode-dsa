class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def result(p,a):
            if len(a)==k:
                ans.append(a.copy())
                return

            for i in range (p,n+1):
                if i not in a:
                    a.append(i)
                    result(i+1,a)
                    a.pop()
        ans=[]
        result(1,[])
        return ans
        
