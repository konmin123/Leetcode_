"""Given two integer arrays startTime and endTime and given an integer
queryTime. The ith student started doing their homework at the time
startTime[i] and finished it at time endTime[i]. Return the number of students
doing their homework at time queryTime. More formally, return the number of
students where queryTime lays in the interval [startTime[i], endTime[i]]
inclusive.

Example 1:
Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
Output: 1
Explanation: We have 3 students where:
The first student started doing homework at time 1 and finished at time 3 and
wasn't doing anything at time 4. The second student started doing homework at
time 2 and finished at time 2 and also wasn't doing anything at time 4.
The third student started doing homework at time 3 and finished at time 7 and
was the only student doing homework at time 4.

Example 2:
Input: startTime = [4], endTime = [4], queryTime = 4
Output: 1
Explanation: The only student was doing their homework at the queryTime.

Constraints:
startTime.length == endTime.length
1 <= startTime.length <= 100
1 <= startTime[i] <= endTime[i] <= 1000
1 <= queryTime <= 1000"""
from typing import List


class Solution:
    @staticmethod
    def busy_student(start: List[int], end: List[int], query: int) -> int:
        output = 0
        cur_index = 0
        while cur_index < len(start):
            if start[cur_index] <= query <= end[cur_index]:
                output += 1
            cur_index += 1
        return output

    @staticmethod
    def busy_student_line(start: List[int], end: List[int], query: int) -> int:
        return len([x for x in zip(start, end) if x[0] <= query <= x[1]])


assert Solution.busy_student([1, 2, 3], [3, 2, 7], 4) == 1
assert Solution.busy_student([4], [4], 4) == 1
assert Solution.busy_student_line([1, 2, 3], [3, 2, 7], 4) == 1
assert Solution.busy_student_line([4], [4], 4) == 1
