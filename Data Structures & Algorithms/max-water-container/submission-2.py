class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area is width * height, we have the heights, but what about the width
        # is it the distance between the two indices ? yes
        # we dont want this list sorted
        max_area = 0

        left, right = 0, len(heights) - 1

        # gonna start on one and keep checking
        while left < right:
            width=right-left
            height=min(heights[left], heights[right])
            area=width*height

            max_area=max(area, max_area)

            # what is there to compare to either increment one pointer or the other ?
            # we have the heights themselves
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1

        return max_area