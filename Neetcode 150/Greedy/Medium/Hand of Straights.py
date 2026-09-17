# You are given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize.
#
# You want to rearrange the cards into groups so that each group is of size groupSize, and card values are consecutively increasing by 1.
#
# Return true if it's possible to rearrange the cards in this way, otherwise, return false.

from typing import List
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        frequency ={}
        for item in hand:
            frequency[item]= frequency.get(item,0) + 1
        if len(hand)%groupSize!=0:
            return False
        for k in sorted(frequency.keys()):
            if frequency[k]>0:
                freq = frequency[k]
                for i in range(groupSize):
                    if frequency.get(k+i, 0) < freq:
                        return False
                    frequency[k+i] -= freq
        return True


if __name__ == '__main__':
    hand = [1,2,4,2,3,5,3,4]
    groupSize = 4
    print(Solution().isNStraightHand(hand, groupSize))