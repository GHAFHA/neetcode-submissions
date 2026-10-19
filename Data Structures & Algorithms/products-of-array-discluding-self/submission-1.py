class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # Pass 1: fill output[i] with prefix product (left side)
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # Pass 2: multiply in suffix product (right side)
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output