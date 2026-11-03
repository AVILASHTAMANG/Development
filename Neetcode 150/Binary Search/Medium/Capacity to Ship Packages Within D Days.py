# A conveyor belt has packages that must be shipped from one port to another within days days.
#
# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the
# conveyor belt (in the order given by weights). It is not allowed to load weight more than the maximum weight capacity
# of the ship.
#
# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped
# within days days.

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

if __name__=='__main__':
    weights = [2, 4, 6, 1, 3, 10]
    days = 4
    print(Solution().shipWithinDays(weights,days))
