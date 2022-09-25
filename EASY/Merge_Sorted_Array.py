p = nums1.count(0)
if p == 0:
    return nums1
else:
    for i in range(len(nums2)):
        nums1.remove(0)
        nums1.append(nums2[i])
    nums1.sort()
    return nums1
