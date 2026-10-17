# Given  lines of HTML, find the tag names (ignore any attributes) and print them as a single line
# of lexicographically ordered semicolon-separated values (e.g.: tag1, tag2, tag3).

import re

class Solution:
    def detect_html_tags(self, s):
        html = "\n".join(s)
        pattern = r'<\s*(\w+)'
        tags = set(re.findall(pattern, html))
        print(';'.join(sorted(tags)))

if __name__ == '__main__':
    s = [
        '<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>',
        '<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>'
    ]

    Solution().detect_html_tags(s)
