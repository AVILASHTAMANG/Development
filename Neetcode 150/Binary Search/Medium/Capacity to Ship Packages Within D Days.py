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
        def can_ship(cap):
            load = 0
            day = 1
            for w in weights:
                if load+w > cap:
                    load=w
                    day+=1
                else:
                    load+=w
            return day<=days
        lo, hi = max(weights), sum(weights)
        while lo<hi:
            mid = (lo+hi) // 2
            if can_ship(mid):
                hi = mid
            else:
                lo=mid+1
        return lo


if __name__=='__main__':
    # weights = [1,2,3,4,5]
    # days = 5
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days = 5
    print(Solution().shipWithinDays(weights,days))
