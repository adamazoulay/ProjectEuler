def findMedianSortedArrays(nums1, nums2):

    def popSmallest(l1, l2):
        if (l1 and l2):
            if (l1[0] < l2[0]):
                small = l1.pop(0)
            else:
                small = l2.pop(0)
        elif (l1):
            small = l1.pop(0)
        else:
            small = l2.pop(0)
        return small


    len1 = len(nums1)
    len2 = len(nums2)
    total = len1 + len2

    is_even = (total % 2 == 0)

    if is_even:
        target = (total / 2) - 1
    else:
        target = int(total / 2)

    cur = 0
    while cur < target:
        popSmallest(nums1, nums2)
        cur += 1

    if is_even:
        num1 = popSmallest(nums1, nums2)
        num2 = popSmallest(nums1, nums2)
        median = (num1 + num2) / 2
    else:
        median = popSmallest(nums1, nums2)

    return float(median)


print(findMedianSortedArrays([1,2], [3,4]))
