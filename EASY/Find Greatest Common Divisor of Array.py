class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = min(nums)
        b = max(nums)
        if a == 0:
            return b
        elif b == 0:
            return a
        elif a == b:
            return a
        if a > b:
            p = math.gcd(a-b, b)
        p = math.gcd(a, b-a)

        return p
