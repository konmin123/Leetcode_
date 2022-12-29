"""Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo
attacks Ashe, Ashe gets poisoned for a exactly duration seconds. More formally,
an attack at second t will mean Ashe is poisoned during the inclusive time
interval [t, t + duration - 1]. If Teemo attacks again before the poison effect
ends, the timer for it is reset, and the poison effect will end duration
seconds after the new attack.

You are given a non-decreasing integer array timeSeries, where timeSeries[i]
denotes that Teemo attacks Ashe at second timeSeries[i], and an integer
duration.

Return the total number of seconds that Ashe is poisoned.

Example 1:
Input: timeSeries = [1,4], duration = 2
Output: 4
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.

Example 2:
Input: timeSeries = [1,2], duration = 2
Output: 3
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 2 however, Teemo attacks again and resets the poison timer.
Ashe is poisoned for seconds 2 and 3.
Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total."""
from typing import List


class Solution:
    @staticmethod
    def find_poisoned_duration(time_series: List[int], duration: int) -> int:
        duration_time = 0
        start_time = time_series[0]
        for current_time in time_series[1:]:
            if current_time - start_time < duration:
                duration_time += current_time - start_time
            else:
                duration_time += duration
            start_time = current_time
        duration_time += duration
        return duration_time


assert Solution.find_poisoned_duration([1], 2) == 2
assert Solution.find_poisoned_duration([1, 2], 2) == 3
assert Solution.find_poisoned_duration([1, 4], 2) == 4
assert Solution.find_poisoned_duration([1, 4, 5], 2) == 5
