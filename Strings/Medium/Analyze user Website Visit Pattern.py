# You are given two string arrays username and website and an integer array timestamp. All the given arrays are of the
# same length and the tuple (username[i], website[i], timestamp[i]) indicates that the user username[i] visited the
# website website[i] at time timestamp[i].
#
# A list of three websites is called a pattern (not neccessarily distinct).
#
# For example, ["neetcode", "courses", "problems"], ["neetcode", "love", "neetcode"], and ["dsa", "dsa", "dsa] "
# are all patterns.
# The score of a pattern is the number of users visited all the websites in the pattern in the same order they appeared
# in the pattern. In other words, for a given user's sequence of website visits, the pattern must appear as a
# subsequence within that sequence.
#
# Your task is to return the pattern with the largest score. If there is more than one pattern with the same largest
# score, return the lexicographically smallest such pattern.

from collections import defaultdict
from typing import List
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_visits = defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            user_visits[u].append(w)
        #return user_visits

        pattern_count = defaultdict(int)

        # Generate all unique 3-websites patterns for each user
        for u, websites in user_visits.items():
            visited_patterns = set()
            n = len(websites)

            if n>=3: # Generate Combinations i<j<k
                for i in range(n):
                    for j in range(i+1, n):
                        for k in range(j+1, n):
                            patterns = (websites[i], websites[j], websites[k])
                            visited_patterns.add(patterns)

            for pattern in visited_patterns:
                pattern_count[pattern] += 1

        max_score = max(pattern_count.values())

        best_patterns = [p for p, score in pattern_count.items() if score == max_score]
        return list(min(best_patterns))



if __name__ == '__main__':
    username = ["bob","bob","bob","alice","alice","alice","alice","charlie","charlie","charlie"]
    timestamp = [1,2,3,4,5,6,7,8,9,10]
    website = ["home","about","career","home","cart","maps","home","home","about","career"]
    print(Solution().mostVisitedPattern(username, timestamp, website))