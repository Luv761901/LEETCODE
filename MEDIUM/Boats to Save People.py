class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        c = 0
        l = 0
        r = len(people)-1
        people.sort()
        while(l <= r):
            if people[l]+people[r] <= limit:
                l += 1
            c += 1
            r -= 1
        return c
