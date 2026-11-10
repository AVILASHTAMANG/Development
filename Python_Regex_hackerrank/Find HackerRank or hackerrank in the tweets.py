# Increasing popularity of hackerrank can be seen in tweets like
#
# I love #hackerrank
# I just scored 27 points in the Picking Cards challenge on #HackerRank
# I just signed up for summer cup @hackerrank
# Given a set of most popular tweets, your task is to find out how many of those tweets has the string hackerrank in it.

import re

class Solution:
    def find_hackerrank(self,tweet):
        #regex_pattern = r'(h|H)(a|A)(c|C)(k|K)(e|E)(r|R)(r|R)(a|A)(n|N)(k|K)'
        regex_pattern=r'hackerrank'
        count = 0
        if re.search(regex_pattern, tweet, re.IGNORECASE):
            return 1
        return 0

if __name__ == "__main__":
    tweets = ['I love #hackerrank', 'I just scored 27 points in the Picking Cards challenge on #HackerRank',
                 'I just signed up for summer cup @hackerrank','interesting talk by hari, co-founder of hackerrank']
    count = 0
    for tweet in tweets:
        count +=Solution().find_hackerrank(tweet)
    print(count)
