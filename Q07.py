from typing import List


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1 in range(len(nums)):
            for index2 in range(len(nums)):
                if nums[index1] + nums[index2] == target:
                    return [index1,index2]

    twoSum(1, [2,7,11,15], 9)