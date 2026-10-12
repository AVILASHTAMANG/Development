# Charlie's second assignment was given by the Professor as soon as he submitted the first one.
# Professor asked Charlie to create a list of all the attributes of every tag found in HTML pages.
#
# <p>This is a paragraph</p>
# The above HTML string has p as its tag but no attributes.
#
# <a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a>
# This string has a as a tag and href as an attribute.

import re
from collections import defaultdict

class Solution:
    def detect_html_attributes(self, s):
        tags = defaultdict(set)

        for html in s:
            for tag, attributes in re.findall(r'<(\w+)([^>]*)>', html):
                attrs = re.findall(r'(\w+)\s*=', attributes)
                tags[tag].update(attrs)

        for tag, attributes in sorted(tags.items()):
            print(f"{tag}:{','.join(sorted(attributes))}")


if __name__ == '__main__':
    s = [
        '<p>This is a paragraph</p>',
        '<a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a>'
    ]

    Solution().detect_html_attributes(s)


