class Solution:
    def maxArea(self, height: List[int]) -> int:
        # given integer array height, length n
        # example: height = [1,8,6,2,5,4,8,3,7]

        # return int, the area of the water it can store
        # area = (r-l) * min(height[r], height[l])

        # logic: keep a max, keep updating potential new max, by updating the l+=1

        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            # calculate area
            area = (r-l) * min(height[r], height[l])
            # update potential new max area
            max_area = max(area, max_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area

