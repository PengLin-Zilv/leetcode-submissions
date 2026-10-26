class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # two sum version 2
        # 1-indexed array of numbers, sorted in non decreasing order
        # given target
        # exact 1 solution
        # return integer array [index+1, index+1]

        # we want to use two pointers
        l, r = 0, len(numbers) - 1

        # a window, while they are not same, otherwise only 1 num left
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1