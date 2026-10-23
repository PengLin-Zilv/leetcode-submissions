class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # given nums
        # given target
        # return of 2 nums' which adds up to target as a list

        # what we trying to do:
        # initialize a dictionary storing the num and its index as the key
        # we also want to find complement
        # complement = target - num
        # we want to return [d[complement], num's index], or just i for num's index

        # so what we want is really just to calculate complement first
        # then we see if complement in d
        # if in: return [d[complement], i]
        # if not: add num to d, d[num] = i
        d = {}

        for i, n in enumerate(nums):
            # for each num, we find its complement
            complement = target - n
            # we want to return complement index and i
            if complement in d:
                return [d[complement], i]

            d[n] = i


                


        

