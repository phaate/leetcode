from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        result = [-1] * length
        if not 2 * k + 1 > length:
            for i, v in enumerate(nums):
                if i - k >= 0 and i + k <= length - 1:
                    slice_nums = nums[i - k:i + k+1]
                    result[i] = sum(slice_nums) // len(slice_nums)

        return result


if __name__ == '__main__':
    print(1)
