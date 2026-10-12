# A valid IP address consists of exactly four integers separated by single dots. Each integer is
# between 0 and 255 (inclusive) and cannot have leading zeros.
#
# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245",
# "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# You are given a string s containing only digits, return all possible valid IP addresses
# that can be formed by inserting dots into s. You are not allowed to reorder or remove any
# digits in s. You may return the valid IP addresses in any order.

# Input: s = "010010"
# Output: ["0.10.0.10","0.100.1.0"]

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        def backtrack(start_index, path):
            if len(path) == 4:
                if start_index == len(s):
                    result.append('.'.join(path))
                return
            # Optimization/Pruning: If remaining characters are too many or too few to form valid remaining parts
            remaining_parts = 4 - len(path)
            remaining_chars = len(s) - start_index
            if remaining_chars > remaining_parts * 3 or remaining_chars < remaining_parts:
                return

            for end_index in range(start_index+1, min(start_index+4, len(s)+1)):
                segment = s[start_index:end_index]
                if (len(segment)>1 and segment[0] == "0") or int(segment) > 255:
                    continue
                backtrack(end_index, path+[segment])
        backtrack(0,[])
        return result


if __name__ == '__main__':
    s = "010010"
    print(Solution().restoreIpAddresses(s))