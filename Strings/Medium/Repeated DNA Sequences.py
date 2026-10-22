# Find every distinct substring of length exactly 10 that occurs at least twice in the DNA string s.
# The alphabet is A, C, G, and T. Occurrences may overlap. Return each repeated substring once, in any order.
# If no length-10 substring repeats, return an empty array.

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        repeated = set()
        for i in range(len(s) - 9):
            sub = s[i:i+10]
            if sub in seen:
                repeated.add(sub)
            else:
                seen.add(sub)
        return list(repeated)

        ###Need to understand this : Can we avoid slicing and hashing 10-character strings at every step?########
        # class Solution:
        #     def findRepeatedDnaSequences(self, s: str) -> list[str]:
        #         if len(s) < 10:
        #             return []
        #
        #         mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        #         mask = (1 << 20) - 1  # 20 ones: 0b11111111111111111111 (0xFFFFF)
        #
        #         seen = set()
        #         repeated = set()
        #
        #         bitmask = 0
        #         # Initialize the first 9 characters
        #         for i in range(9):
        #             bitmask = (bitmask << 2) | mapping[s[i]]
        #
        #         # Slide the 10th character onwards
        #         for i in range(9, len(s)):
        #             # Shift left by 2, add new character, mask out bits older than 20
        #             bitmask = ((bitmask << 2) | mapping[s[i]]) & mask
        #
        #             if bitmask in seen:
        #                 repeated.add(s[i - 9: i + 1])
        #             else:
        #                 seen.add(bitmask)
        #
        #         return list(repeated)

if __name__ == '__main__':
    s = "ACGTACGTACGTAC" #Output: ["ACGTACGTAC"]
    print(Solution().findRepeatedDnaSequences(s))
