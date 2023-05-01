"""Given a string date representing a Gregorian calendar date formatted as
YYYY-MM-DD, return the day number of the year.

Example 1:
Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.

Example 2:
Input: date = "2019-02-10"
Output: 41

Constraints:
date.length == 10
date[4] == date[7] == '-', and all other date[i]'s are digits
date represents a calendar date between Jan 1st, 1900 and Dec 31th, 2019."""


class Solution:
    @staticmethod
    def day_of_year(date: str) -> int:
        dict_days_in_month = [
            0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334
        ]
        year = int(date[:4])
        leap_year = year % 4 == 0
        month_number = int(date[-5:-3])
        days_for_previous_months = dict_days_in_month[month_number]
        days_per_month = int(date[-2:])
        days_per_year = days_for_previous_months + days_per_month
        return days_per_year + 1 if leap_year else days_per_year


assert Solution.day_of_year("2019-02-10") == 41
assert Solution.day_of_year("2019-01-09") == 9
assert Solution.day_of_year("2019-03-01") == 60
assert Solution.day_of_year("2020-03-01") == 61
