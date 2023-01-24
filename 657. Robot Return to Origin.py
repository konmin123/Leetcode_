"""There is a robot starting at the position (0, 0), the origin, on a 2D plane.
Given a sequence of its moves, judge if this robot ends up at (0, 0) after it
completes its moves. You are given a string moves that represents the move
sequence of the robot where moves[i] represents its ith move. Valid moves are
'R' (right), 'L' (left), 'U' (up), and 'D' (down). Return true if the robot
returns to the origin after it finishes all of its moves, or false otherwise.
Note: The way that the robot is "facing" is irrelevant. 'R' will always make
the robot move to the right once, 'L' will always make it move left, etc. Also,
assume that the magnitude of the robot's movement is the same for each move.

Example 1:
Input: moves = "UD"
Output: true
Explanation: The robot moves up once, and then down once. All moves have the
same magnitude, so it ended up at the origin where it started. Therefore, we
return true.

Example 2:
Input: moves = "LL"
Output: false
Explanation: The robot moves left twice. It ends up two "moves" to the left
of the origin. We return false because it is not at the origin at the end of
its moves.
1 <= moves.length <= 2 * 104
moves only contains the characters 'U', 'D', 'L' and 'R'."""


class Solution:
    @staticmethod
    def judge_circle(moves: str) -> bool:
        dict_coord = {'L': [0, -1], 'R': [0, 1], 'U': [1, 0], 'D': [-1, 0]}
        start_position = [0, 0]
        finish_position = [0, 0]
        for letter in moves:
            finish_position = [
                finish_position[0] + dict_coord[letter][0],
                finish_position[1] + dict_coord[letter][1]
            ]
        return True if start_position == finish_position else False

    @staticmethod
    def judge_circle_one_line(moves: str) -> bool:
        return (moves.count('L') == moves.count('R')
                and moves.count('U') == moves.count('D'))


assert Solution.judge_circle("UD")
assert not Solution.judge_circle("LL")
assert Solution.judge_circle("")
assert Solution.judge_circle_one_line("UD")
assert not Solution.judge_circle_one_line("LL")
assert Solution.judge_circle_one_line("")
