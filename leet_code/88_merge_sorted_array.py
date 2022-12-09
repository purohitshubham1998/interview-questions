from typing import List
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i = j = 0
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            i += 1
        elif nums2[j] < nums1[i]:
            nums1[i], nums2[j] = nums2[j], nums1[i]
    while j < n and i < m+n:
        nums1[i] = nums2[j]
        i += 1
        j += 1
    print(nums1)

merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)