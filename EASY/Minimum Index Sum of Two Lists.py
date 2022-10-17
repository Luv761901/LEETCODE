class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        inds = []
        for i in range(len(list1)):
            if list1[i] in list2:
                inds.append(i+list2.index(list1[i]))
        m = min(inds)
        for i in range(len(list1)):
            if list1[i] in list2:
                if m == (i+list2.index(list1[i])):
                    ans.append(list1[i])
        return ans
