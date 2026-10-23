# Given a line of text which possibly contains the latitude and longitude of a point, can you use regular expressions
# to identify the latitude and longitude referred to (if any)?
#
# Input Format
# The first line contains an integer N, which is the number of tests to follow.
# This is followed by N lines of text. Each line contains a pair of co-ordinates which possibly indicate the latitude
# and longitude of a place.
#
# Output Format
# "Valid" where X and Y are the latitude and longitude which you found to be a valid (latitude,longitude) pair.
# If the given pair of numbers are not a valid (latitude,longitude) pair, output "Invalid".

import re

class Solution:
    def detect_latitude_longitude(self, s):
        pattern = (
            r'^\(([+-]?(?:90|[1-8]?[0-9])(?:\.\d+)?),\s*'
            r'([+-]?(?:180|1[0-7][0-9]|[1-9]?[0-9])(?:\.\d+)?)\)$'
        )

        match = re.fullmatch(pattern, s)

        if match:
            lat = float(match.group(1))
            lon = float(match.group(2))

            if -90 <= lat <= 90 and -180 <= lon <= 180:
                return "Valid"

        return "Invalid"


if __name__ == '__main__':
    s = '''
(75, 180)
(+90.0, -147.45)
(77.11112223331, 149.99999999)
(+90, +180)
(90, 180)
(-90.00000, -180.0000)
(75, 280)
(+190.0, -147.45)
(77.11112223331, 249.99999999)
(+90, +180.2)
(90., 180.)
(-090.00000, -180.0000)
'''

    solution = Solution()

    for line in s.strip().splitlines():
        print(solution.detect_latitude_longitude(line.strip()))