class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        self.iterate(nums, 0, target, [], result)
        return result

    def iterate(
        self,
        nums: List[int],
        start: int,
        remaining: int,
        combination: List[int],
        result: List[List[int]],
    ) -> None:
        if remaining == 0:
            result.append(combination.copy())
            return

        if remaining < 0:
            return

        for i in range(start, len(nums)):
            combination.append(nums[i])
            self.iterate(nums, i, remaining - nums[i], combination, result)
            combination.pop()
