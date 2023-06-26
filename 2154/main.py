from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:

        if original not in nums:
            return original
        else:
            return self.findFinalValue(nums=nums, original=(original * 2))


if __name__ == '__main__':
    pass
