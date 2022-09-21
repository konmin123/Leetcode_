"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only
one
valid
answer
exists.

Follow - up: Can
you
come
up
with an algorithm that is less than O(n2) time complexity?"""

nums = [-5, 2, 3, 4, 5, 6, 7, 8, 9]
target = 17


def two_sum_binary_find(seq: list) -> list:
    for index, value in enumerate(seq):
        left = index + 1
        right = len(seq) - 1
        while left <= right:
            middle_index = (left + right) // 2
            if value + seq[middle_index] < target:
                left = middle_index + 1
            elif value + seq[middle_index] > target:
                right = middle_index - 1
            else:
                return [index, middle_index]
    return []


def two_sum_line(seq: list) -> list:
    i = 0
    j = len(seq) - 1
    while i < j:
        if seq[i] + seq[j] == target:
            return [i, j]
        elif seq[i] + seq[j] < target:
            i += 1
        elif seq[i] + seq[j] > target:
            j -= 1
    return []


def two_sum_dict(seq: list) -> list:
    dict_ = {}
    for index, value in enumerate(seq):
        if target >= value:
            find_number = target - value
        else:
            find_number = value + target
        if str(find_number) in dict_.keys():
            return [dict_[str(find_number)], index]
        else:
            dict_[str(value)] = index
    return []


if __name__ == '__main__':
    print(two_sum_binary_find(nums))

