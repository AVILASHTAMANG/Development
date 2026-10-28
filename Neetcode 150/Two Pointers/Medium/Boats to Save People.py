# You are given an integer array people where people[i] is the weight of the ith person, and an infinite number of boats
# where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided
# the sum of the weight of those people is at most limit.
#
# Return the minimum number of boats to carry every given person.

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start = 0
        end = len(people)-1
        boats = 0
        # while start<end:
        #     total = people[start] + people[end]
        #     if total<=limit:
        #         boats+=1
        #         start+=1
        #         end-=1
        #     elif total>limit:
        #         end-=1
        #         boats+=1
        # if start==end:
        #     boats+=1
        # return boats
        while start<=end:
            if people[start]+people[end]<=limit:
                start+=1
            end-=1
            boats+=1
        return boats


if __name__ == '__main__':
    people = [1,3,2,3,2]
    limit = 3
    print(Solution().numRescueBoats(people, limit))