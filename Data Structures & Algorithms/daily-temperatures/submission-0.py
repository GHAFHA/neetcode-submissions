class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # create an output list with the same number of elements
        output = [0] * len(temperatures)

        # form a stack, the purpose of the stack is what in this case ?
        # it is to remember which days need to be looked into
        stack = []

        # using enumerate to get the index and the temp
        for i, temp in enumerate(temperatures):

            # while the stack is not empty and the temp at the current index is greater than the temp at the top of the stack
            # we pop the prev one since this is sitting on the stack
            # output at the index we saw becomes the current index - prev since that is the number of days
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                output[prev_index] = i - prev_index

            # if the condition in the while is false we append
            stack.append(i)

        # return the output
        return output