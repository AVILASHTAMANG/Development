# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an
# empty record.
#
# Given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one
# of the following:
#
# An integer x: Record a new score of x.
#
# '+': Record a new score that is the sum of the previous two scores.
#
# 'D': Record a new score that is the double of the previous score.
#
# 'C': Invalidate the previous score, removing it from the record.
#
# Return the sum of all the scores on the record after applying all the operations.
#
# Note: The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and
# that all operations are valid.

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec = []
        for ch in operations:
            # if ch.lstrip('-').isdigit():
            #     rec.append(int(ch))
            # elif ch=='+':
            #     rec.append(rec[-2]+rec[-1])
            # elif ch=='D':
            #     rec.append(rec[-1]*2)
            # else:
            #     rec.pop()
            try:
                rec.append(int(ch))
            except ValueError:
                if ch == '+':
                    rec.append(rec[-1] + rec[-2])
                elif ch == 'D':
                    rec.append(rec[-1] * 2)
                else:
                    rec.pop()

        return sum(rec)

if __name__=='__main__':
    ops = ["1", "2", "+", "C", "5", "D"]
    print(Solution().calPoints(ops))