import pytest
from main import *


def testSingle_getAverage():
    nums = [8]
    k = 100000

    expected = [-1]

    solution = Solution()
    result = solution.getAverages(nums, k)

    assert result == expected

def testStd_getAverage():
    nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
    k = 3

    expected = [-1,-1,-1,5,4,4,-1,-1,-1]

    solution = Solution()
    result = solution.getAverages(nums, k)

    assert result == expected

def testStd_getAverage():
    nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
    k = 3

    expected = [-1,-1,-1,5,4,4,-1,-1,-1]

    solution = Solution()
    result = solution.getAverages(nums, k)

    assert result == expected


