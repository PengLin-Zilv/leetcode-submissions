class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # given temperatures: daily temperature list
        # return answer list, which answer[i] is the # of days this day have to wait to get warmer temp


        # temperatures = [73,74,75,71,69,72,76,73]
        # answers = [1,1,4,2,1,0,0]

        # we want to get stack storing the index, so we can use difference = j - i, which will be the answer[j]
        # so what we want is, for each interation
        # compare to the stack list, see if temp is warmer, if so, get the answers to whatever many as possible
        
        # push i into the stack
        answers = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            # ith day, with its temperature
            while stack and temp > temperatures[stack[-1]]:
                # we always compare to the last one since it might have more, but we will compare one by one

                # j will be the day we plug in for its answer, since it is colder than today and it is in stack
                j = stack.pop()
                difference = i - j
                answers[j] = difference
                # plug in the answer for jth day
            stack.append(i)
        return answers

        # dry run: [4,5,3,2,8,1]
        # answers = [1,3,2,1,0,0]

