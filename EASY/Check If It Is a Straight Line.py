class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort()
        x1 = coordinates[0][0]
        y1 = coordinates[0][1]
        x2 = coordinates[1][0]
        y2 = coordinates[1][1]
        for i in coordinates:
            x = i[0]
            y = i[1]
            if (x-x1)*(y2-y1) != (y-y1)*(x2-x1):
                return False
        return True
