class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        curr_fuel = startFuel
        max_heap = []
        stops = 0
        for station in stations:
            pos, fuel = station[0], station[1]
            while curr_fuel < pos:
                if len(max_heap) == 0:
                    return -1
                curr_fuel += (-1)*heappop(max_heap)
                stops += 1
            heappush(max_heap, -fuel)
        while curr_fuel < target:
            if len(max_heap) == 0:
                return -1
            curr_fuel += (-1)*heappop(max_heap)
            stops += 1
        return stops
