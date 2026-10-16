class Solution:
    def isPalindrome(self, s: str) -> bool:
        # isalum explicity checks for alpha numeric chars, and is a python function that does so
        all_chars_forward = [char.lower() for char in s if char.isalnum()]

        # need to review slicing more often
        reversed_chars = all_chars_forward[::-1]

        if all_chars_forward == reversed_chars:
            return True
        
        return False