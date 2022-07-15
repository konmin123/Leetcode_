from typing import List
nums = [15, 11, 7, 2]
target = 36


class Solution:
    @staticmethod
    def two_sum(numbers: List[int], target_: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target_:
                    return [i, j]


print(Solution.two_sum(nums, target))