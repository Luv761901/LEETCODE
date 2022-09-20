i, j, k = 0, 0, 0
l = len(nums1)+len(nums2)
prev = 0
temp = 0
while(i < len(nums1) and j < len(nums2)):
    if nums1[i] <= nums2[j]:
        prev = temp
        temp = nums1[i]
        i += 1
    elif nums2[j] < nums1[i]:
        prev = temp
        temp = nums2[j]
        j += 1

    if k == l//2:
        if l % 2 != 0:
            return temp
        else:
            return (temp+prev)/2

    else:
        prev = temp
    k += 1
while(i < len(nums1)):
    prev = temp
    temp = nums1[i]
    i += 1

    if k == l//2:
        if l % 2 != 0:
            return temp
        else:
            return (temp+prev)/2
    k += 1
while(j < len(nums2)):
    prev = temp
    temp = nums2[j]
    j += 1
    if k == l//2:
        if l % 2 != 0:
            return temp
        else:
            return (temp+prev)/2
    k += 1
