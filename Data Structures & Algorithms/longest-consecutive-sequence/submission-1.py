class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # still make the set and the lenght
        set_nums = set(nums)
        max_length = 0

        for num in nums:
            # do the check first so then we can loop in it
            # this lets us make a a checklist of sorts before continuing to the next num
            if (num - 1) not in set_nums:
                # we need to increment the number here
                current_num = num # so we can increment the number
                streak = 1 # streak counter

                # while the current num is in the set we increment the current num and streak
                # this while loop continues since we are doing the incementation and check within itseld
                while (current_num + 1) in set_nums:
                    current_num+=1
                    streak+=1
            
                # check and update the max length
                max_length = max(max_length, streak)
        
        return max_length