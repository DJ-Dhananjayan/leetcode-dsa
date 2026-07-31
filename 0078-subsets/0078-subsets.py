class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        ans = []

        def backtrack(index,p):
            ans.append(p[:])

            for i in range(index, len(nums)):
                p.append(nums[i])
                backtrack(i + 1, p)
                p.pop()

        backtrack(0, [])
        return ans
        """

        res=[[]]
        for i in nums:
            res+=[n+[i] for n in res]
            print(res)
        return res