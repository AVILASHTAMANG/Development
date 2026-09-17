# There are n gas stations along a circular route. You are given two integer arrays gas and cost where:
#
# gas[i] is the amount of gas at the ith station.
# cost[i] is the amount of gas needed to travel from the ith station to the (i + 1)th station. (The last station is connected to the first station)
# You have a car that can store an unlimited amount of gas, but you begin the journey with an empty tank at one of the gas stations.
#
# Return the starting gas station's index such that you can travel around the circuit once in the clockwise direction. If it's impossible, then return -1.
#
# It's guaranteed that at most one solution exists.

from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr_tank = 0
        start_station = 0
        if sum(gas)<sum(cost):
            return -1
        for i in range(len(gas)):
            curr_tank += gas[i] - cost[i]
            if curr_tank < 0:
                start_station = i+1
                curr_tank = 0
        return start_station

if __name__=='__main__':
    gas = [1,2,3,4]
    cost = [2,2,4,1]
    print(Solution().canCompleteCircuit(gas,cost))
