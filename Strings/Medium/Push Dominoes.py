# There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push
# some of the dominoes either to the left or to the right.
#
# After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the
# dominoes falling to the right push their adjacent dominoes standing on the right.
#
# When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.
#
# For the purposes of this question, we will consider that a falling domino expends no additional force to a falling
# or already fallen domino.
#
# You are given a string dominoes representing the initial state where:
#
# dominoes[i] = 'L', if the ith domino has been pushed to the left,
# dominoes[i] = 'R', if the ith domino has been pushed to the right, and
# dominoes[i] = '.', if the ith domino has not been pushed.
# Return a string representing the final state.

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        padded = "L" + dominoes + "R"
        i = 0 # needed to track segment to be patched
        result = []
        for j in range(1, len(padded)):
            if padded[j] == '.':
                continue
            k = j - i - 1 # number of dots in between j and i
            if padded[i] == padded[j]: # Both sides push in their own/same direction L..L or R...R
                middle = padded[i] * k
            elif padded[i] == 'L' and padded[j] == 'R': # in between dots remain uneffected
                middle = '.' * k
            else: # the outer halves are falling inward as R...L
                middle = ('R' * (k//2)) + ('.' if k%2 else '') + ('L' * (k//2))
            result.append(padded[i] + middle)
            i = j
        return ''.join(result)[1:]



if __name__=='__main__':
    dominoes = ".L.R...LR..L.." # "LL.RR.LLRRLL.."
    print(Solution().pushDominoes(dominoes))