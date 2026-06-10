class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Complexity :
        # Let:
        # n = number of strings
        # k = maximum string length
        # Sorting each string costs O(k log k), so:
        # Time: O(n * k log k)
        # Space: O(n * k)

        # group_anagrams = defaultdict(list)
        # for s in strs:
        #     sorted_str = ''.join(sorted(s))
        #     group_anagrams[sorted_str].append(s)
        # return list(group_anagrams.values())

        # For optimal performance, a common alternative is to use a 26-character frequency count as the key, giving O(n * k) time.
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')]+=1
            groups[tuple(count)].append(s)
        return list(groups.values())
