"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
Accepted
1,404,735
Submissions
3,621,690"""

l1 = ["flower", "flow", "flight"]
l2 = ["dog", "racecar", "car"]
l3 = ['123', '1234', '12345']
l4 = ['apple', 'aba', 'flowerer']


def pref(list_: list) -> str:
    if len(list_) != 0:
        pref_ = ''
        list_for_pref = sorted(list_, key=len)
        word = list_for_pref[0]
        for index, letter in enumerate(word):
            for i in range(1, len(list_for_pref) - 1):
                if list_for_pref[i][index] == letter:
                    pref_ += letter
                else:
                    break
        return pref_
    return ""


print(pref(l4))
