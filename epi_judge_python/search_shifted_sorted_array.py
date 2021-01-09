from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    left = 0
    right = len(A)-1
    while left < right:
        mid = (left + right) // 2
        if A[mid] < A[right]:
            right = mid
        else:
            left = mid +1
    return left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
