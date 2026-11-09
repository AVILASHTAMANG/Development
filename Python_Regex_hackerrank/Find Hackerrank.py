# At HackerRank, we always want to find out how popular we are getting every day and have scraped conversations from
# popular sites. Each conversation fits in 1 line and there are N such conversations. Each conversation has at most 1
# word that says hackerrank (all in lowercase). We would like you to help us figure out whether a conversation:
#
# Starts with hackerrank
# Ends with hackerrank
# Start and ends with hackerrank

import re

class Solution:
    def find_hackerrank(self,sentence):
        if re.match(r'^hackerrank$', sentence):
            return 0
        elif re.match(r'^hackerrank', sentence):
            return 1
        elif re.search(r'hackerrank$', sentence):
            return 2
        else:
            return -1

if __name__ == '__main__':
    s = ["i love hackerrank", "hackerrank is an awesome place for programmers","hackerrank","i think hackerrank is a great place to hangout"]
    for sentence in s:
        print(Solution().find_hackerrank(sentence))
