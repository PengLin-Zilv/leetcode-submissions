import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # given stones
        # take 2 biggest stone and smash
        # x and y, x <= y, so y is biggest and x is 2nd(or = y)
        # if x == y, both destory
        # if not, y weight become y - x

        # max heap, so we can do heap operations
        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)
        # now is max heap, but start with - sign, we have to put - when we try to use it

        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            if y != x:
                heapq.heappush(stones, -(y-x))
        return -stones[0] if stones else 0