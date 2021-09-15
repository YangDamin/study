from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()     #배열 정렬
        sum = 0

        for i in range(len(nums)):
            if i%2 == 0:            # 배열의 짝수번째는 항상 작은 값
                sum += nums[i]
        return sum
    arrayPairSum(1, [1,4,3,2])