class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        val=c=0
        for i in costs:
            if(val+i>coins):break
            val+=i
            c+=1
        return c
            