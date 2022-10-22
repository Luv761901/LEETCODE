class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        rem = {}
        k = 60
        for i in time:
            x = i % k
            if x in rem:
                rem[x] += 1
            else:
                rem[x] = 1
        print(rem)
        pairs = 0
        if 0 in rem:
            pairs += (rem[0]*(rem[0]-1))//2
            del rem[0]
        half = k//2
        if half in rem:
            pairs += (rem[half]*(rem[half]-1))//2
            del rem[half]
        for i in range(1, k//2):
            if i in rem and (k-i) in rem:
                pairs += rem[i]*rem[k-i]
        return pairs
