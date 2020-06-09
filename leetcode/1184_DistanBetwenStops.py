from typing import List

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        clockwise=0
        counter=0
        if start > destination:
            start, destination = destination, start
            
        for s in range(len(distance)):
            if s < start or s >= destination:
                counter += distance[s]
            else:
                clockwise += distance[s]

        return min(clockwise, counter)


if __name__ == "__main__":
    temp = Solution()

    print(temp.distanceBetweenBusStops([1,2,3,4], 0, 1))
    print(temp.distanceBetweenBusStops([1,2,3,4], 0, 2))
    print(temp.distanceBetweenBusStops([1,2,3,4], 0, 3))
    print(temp.distanceBetweenBusStops([7,10,1,12,11,14,5,0], 7, 2))