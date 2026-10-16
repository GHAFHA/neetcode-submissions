class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a new set and as we see add back to the set and iterate
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False
