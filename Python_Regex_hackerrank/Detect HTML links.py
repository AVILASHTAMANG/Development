# import re
# if __name__ == '__main__':
#     n = int(input())
#     Regex = r'<a href="(.*?)".*?>([\w ,./]*)(?=</)'
#     for _ in range(n):
#         s = input()
#         links = re.findall(Regex, s)
#         for link, att in links:
#             print('%s,%s' % (link, att.strip()))


# Charlie has been given an assignment by his Professor to strip the links and the text name from the html pages.
# A html link is of the form,
#
# <a href="http://www.hackerrank.com">HackerRank</a>
# Where a is the tag and href is an attribute which holds the link charlie is interested in. The text name is HackerRank.
#
# Charlie notices that the text name can sometimes be hidden within multiple tags
#
# <a href="http://www.hackerrank.com"><h1><b>HackerRank</b></h1></a>
# Here, the text name is hidden inside the tags h1 and b.
#
# Help Charlie in listing all the links and the text name of the links.


import re

class Solution:
    def detect_html_links(self, s):
        html = "\n".join(s)

        pattern = r'<a\s+[^>]*?href=["\'](.*?)["\'][^>]*>(.*?)</a>'

        for link, inner_html in re.findall(pattern, html, re.DOTALL | re.IGNORECASE):
            # Strip out any nested tags (e.g., <h1>, <b>, <span>)
            text_name = re.sub(r'<[^>]*>', '', inner_html)

            # Strip leading and trailing whitespace before printing
            print(f"{link.strip()},{text_name.strip()}")



if __name__ == '__main__':
    s = [
        '<div class="portal" role="navigation" id=\'p-navigation\'>',
        '<h3>Navigation</h3>',
        '<div class="body">',
        '<ul>',
        ' <li id="n-mainpage-description"><a href="/wiki/Main_Page" title="Visit the main page [z]" accesskey="z">Main page</a></li>',
        ' <li id="n-contents"><a href="/wiki/Portal:Contents" title="Guides to browsing Wikipedia">Contents</a></li>',
        ' <li id="n-featuredcontent"><a href="/wiki/Portal:Featured_content" title="Featured content  the best of Wikipedia">Featured content</a></li>',
        '<li id="n-currentevents"><a href="/wiki/Portal:Current_events" title="Find background information on current events">Current events</a></li>',
        '<li id="n-randompage"><a href="/wiki/Special:Random" title="Load a random article [x]" accesskey="x">Random article</a></li>',
        '<li id="n-sitesupport"><a href="//donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&utm_medium=sidebar&utm_campaign=C13_en.wikipedia.org&uselang=en" title="Support us">Donate to Wikipedia</a></li>',
        '</ul>',
        '</div>',
        '</div>'
    ]
    Solution().detect_html_links(s)
