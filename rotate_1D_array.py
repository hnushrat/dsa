class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0 or len(nums) == 1:
            pass
        elif len(nums) == k:
            pass
        else:
            x = nums[-k%len(nums):]
            x.extend(nums[: len(nums) - k%len(nums)])
            # print(x)
            nums[:] = x[:]

        