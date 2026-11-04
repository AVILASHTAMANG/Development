# You are given an array of strings words and a string pref.
#
# Return the number of strings in words that contain pref as a prefix.
#
# A prefix of a string s is any leading contiguous substring of s.

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for ch in words:
            # if ch[:len(pref)] == pref:
            if ch.startswith(pref):
                count+=1
        return count

if __name__=='__main__':
    words = ["pay", "attention", "practice", "attend"]
    pref = "at"
    print(Solution().prefixCount(words, pref)) #op: 2