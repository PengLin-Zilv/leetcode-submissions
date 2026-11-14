class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # given an list of ints, temperatures
        # return an list, answer such that answer[i] is the number of days you have to wait
        # after ith day to get a warmer temperature
        # if no future day is warmer for answer[i], then = 0

        # use stack example: [30,40,50,60]
        # we want to check, if current day is warmer than the prevs?

        # init an answers list
        answers = [0] * len(temperatures)
        stack = [] # storing the index, for calcultaing the distance

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                j = stack.pop()
                distance = i - j
                answers[j] = distance
            stack.append(i)
        return answers

        