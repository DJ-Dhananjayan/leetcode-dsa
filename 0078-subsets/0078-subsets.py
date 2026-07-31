class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(index,p):
            ans.append(p[:])

            for i in range(index, len(nums)):
                p.append(nums[i])
                backtrack(i + 1, p)
                p.pop()

        backtrack(0, [])
        return ans