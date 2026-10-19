class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            # if the new char is already in our window, shrink from the left
            # until the duplicate is removed
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # now it's safe to add the new char
            seen.add(s[right])

            # window size right now is right - left + 1
            longest = max(longest, right - left + 1)

        return longest