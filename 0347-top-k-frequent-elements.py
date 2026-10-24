from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # given nums, integer k
        # return a list of k top frequent elements

        # we want to use hashmap to count the frequence
        # then find a way to: return top k elements
        # while len(result) < k: result.add...

        # use Counter for all element in the list
        # d is a dictionary storing each n and its frequencies
        d = Counter(nums)

        # we now have a dictionary, want to get highest frequencies

        keys = sorted(d, key=lambda x: d[x], reverse=True)
        return keys[:k]


