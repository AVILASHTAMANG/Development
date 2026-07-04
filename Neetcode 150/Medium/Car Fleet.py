# There are n cars traveling to the same destination on a one-lane highway.
# You are given two arrays of integers position and speed, both of length n.
# position[i] is the position of the ith car (in miles)
# speed[i] is the speed of the ith car (in miles per hour)
# The destination is at position target miles.
# A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.
# A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.
# If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.
# Return the number of different car fleets that will arrive at the destination.

from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed),reverse=True)
        fleet, max_time = 0, 0
        for pos, spd in cars:
            time = (target - pos)/spd
            if time > max_time:
                fleet += 1
                max_time = time
        return fleet

if __name__ == '__main__':
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    print(Solution().carFleet(target,position,speed))
