#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#
# https://leetcode.com/problems/asteroid-collision/description/
#
# algorithms
# Medium (45.38%)
# Likes:    7163
# Dislikes: 791
# Total Accepted:    396.6K
# Total Submissions: 877.1K
# Testcase Example:  '[5,10,-5]'
#
# We are given an array asteroids of integers representing asteroids in a row.
#
# For each asteroid, the absolute value represents its size, and the sign
# represents its direction (positive meaning right, negative meaning left).
# Each asteroid moves at the same speed.
#
# Find out the state of the asteroids after all collisions. If two asteroids
# meet, the smaller one will explode. If both are the same size, both will
# explode. Two asteroids moving in the same direction will never meet.
#
#
# Example 1:
#
#
# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never
# collide.
#
#
# Example 2:
#
#
# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
#
#
# Example 3:
#
#
# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide
# resulting in 10.
#
#
#
# Constraints:
#
#
# 2 <= asteroids.length <= 10^4
# -1000 <= asteroids[i] <= 1000
# asteroids[i] != 0
#
#
#

# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for num in asteroids:
            while stack and num < 0 and stack[-1] > 0:
                if stack[-1] == -num:
                    stack.pop()
                    break
                elif stack[-1] > -num:
                    break
                elif stack[-1] < -num:
                    stack.pop()
            else:
                stack.append(num)
        return stack



        # for num in asteroids:
        #     if not stack:
        #         stack.append(num)
        #     if num > 0:
        #         stack.append(num)
        #     elif num < 0 and stack[-1] < 0:
        #         stack.append(num)
        #     elif num < 0 and stack[-1] > 0:
        #         while stack and stack[-1] > 0:
        #             if stack[-1] == abs(num):
        #                 stack.pop()
        #                 break
        #             if stack[-1] > abs(num):
        #                 break
        #             elif stack[-1] < abs(num):
        #                 stack.pop()
        #         else:
        #                 stack.append(num)
        # return stack
# @lc code=end
