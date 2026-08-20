class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, arr2 = [], []
        for i, val in enumerate(nums, 1):
            if i == 1:
                arr1.append(val)
            elif i == 2:
                arr2.append(val)
            else:
                if arr1[-1] > arr2[-1]:
                    arr1.append(val)
                else:
                    arr2.append(val)
        return arr1 + arr2