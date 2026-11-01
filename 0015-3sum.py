class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # given nums
        # return a list of lists 3 numbers add up to 0
        # [[nums[i], nums[j], nums[k]], ...], i!=j!=k 

        # we want to loop for every number
        # we want to sort the nums to make it be non-decreasing order
        # then loop every number, to use pointers in the right side, l and r to check if add up to 0
        # Condition:
        # 1) if == 0, result.append([nums[i], nums[l], nums[r]])
        # 2) if < 0, l += 1
        # 3) else r -= 1

        # for loop, we need to skip same numbers because the result will be same

        nums.sort()
        result = []


        for i in range(len(nums)):
            # [-2,-2,-1,-1,-1,0,1,2,3,4]
            # avoid duplicate, we already found all possibles for this num
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l = i + 1     
            r = len(nums) - 1
       
            # calc sum
            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        # we want to keep moving l, if it is same
                            l += 1

                elif s < 0:
                    l += 1

                else:
                    r -= 1

        return result