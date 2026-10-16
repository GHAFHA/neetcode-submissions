class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_occurences_count_s = {}
        char_occurences_countt = {}
        # check the length is the same else no point
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
