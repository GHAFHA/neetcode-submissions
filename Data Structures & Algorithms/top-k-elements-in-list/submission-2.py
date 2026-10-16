class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # in the dict each key will be the in from the list
        tracked = {}
        repeating_items = list()

        for num in nums:
            if num in tracked:
                tracked[num] += 1
            else:
                tracked[num] = 1

        # sort keys by their frequency (value), descending
        sorted_items = sorted(tracked.items(), key=lambda item: item[1], reverse=True)

        return [key for key, value in sorted_items[:k]]