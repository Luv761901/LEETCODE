class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        d = {"++X": 1, "X++": 1, "--X": -1, "X--": -1}
        x = 0
        for i in operations:
            x += d[i]
        return x
