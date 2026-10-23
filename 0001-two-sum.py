class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, n in enumerate(nums):
            # for each num, we find its complement
            complement = target - n
            # we want to return complement index and i
            if complement in d:
                return [d[complement], i]

            d[n] = i


                


        

