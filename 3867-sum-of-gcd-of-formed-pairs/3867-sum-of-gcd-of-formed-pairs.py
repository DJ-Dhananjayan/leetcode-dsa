class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        m,n=0,len(nums)
        for i in range (n):
            m=max(m,nums[i])
            nums[i]=gcd(m,nums[i])
        nums.sort()
        return sum(gcd(nums[i],nums[~i]) for i in range (n//2))