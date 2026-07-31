class Solution:
    def combinationSum(self, c: List[int], t: int) -> List[List[int]]:
        ans=[]
        def result(s,rem,a):
            if rem==0:
                ans.append(a[:])
                return 
            if rem<0:return 
            for i in range (s,len(c)):
                a.append(c[i])
                result(i,rem-c[i],a)
                a.pop()
        result(0,t,[])
        return ans