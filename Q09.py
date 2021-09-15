from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        results.append([nums[i], nums[j], nums[k]])
        return results

    threeSum(1,[-1, 0, 1, 2, -1, -4])