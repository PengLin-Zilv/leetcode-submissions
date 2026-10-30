class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # given 1-indexed array, number, sorted in non-decreasing order, so can be same num in a roll
        # given target
        # find 2 numbers add up to target
        # return list [index1, index2]
        # exactly 1 solution

        # for two sum 2, since input array is sorted, if a+b < target, we move the left +=1
        # else right -= 1
        # return index+1, index+1 since it is 1-indexed array

        l, r = 0, len(numbers)-1

        while l < r:
            # quick example: [-5,-2,0,2,3,3,4,8], target = 0
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -=1
