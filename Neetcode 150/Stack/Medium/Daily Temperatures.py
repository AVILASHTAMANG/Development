# You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.
# Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day.
# If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # stores indices

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)

        return result

if __name__ == '__main__':
    temperatures = [30,38,30,36,35,40,28]
    print(Solution().dailyTemperatures(temperatures))
