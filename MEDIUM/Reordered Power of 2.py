class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = Counter(str(n))
        print(digits)
        for i in range(30):
            power = str(1 << i)
            if digits == Counter(power):
                print(Counter(power))
                return True
        return False
