class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # if we are being asked to use contant space, we can use a two pointer approach
        # the first pointer will be at the start of the list
        # the second pointer will be at the end of the list
        start, end = 0, len(numbers) - 1

        # while we have a list to iterate over
        while start < end:
            total = numbers[start] + numbers[end]
            if total == target:
                # it is plus 1 on both cause the output indexes are incremented by 1
                return [start + 1, end + 1]
            # if we are low we increment the start
            elif total < target:
                start += 1
            # if we are high we decrement the start
            else:
                end -= 1

        return []