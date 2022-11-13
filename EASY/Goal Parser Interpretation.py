class Solution:
    def interpret(self, command: str) -> str:
        ans = command.replace('()', 'o')
        ans = ans.replace('(al)', 'al')
        return ans
