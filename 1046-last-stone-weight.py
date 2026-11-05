import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # given stones, stones[i] is the weight of ith stone
        # each turn, we choose the heaviest two stone, smash them together

        # x, y and x <= y
        # if x == y: both destroy
        # if x != y, x destroyed and y = y-x

        # return the weight of last remaining stone. If none, return 0

        # so we have a list
        # we want to make it biggest first

        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)
        # now we have heap, can do heap operations:
        # see heap[0], heappop, heappush

        while len(stones) > 1:
            y = - heapq.heappop(stones)
            x = - heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, -(y-x))
        return -stones[0] if stones else 0