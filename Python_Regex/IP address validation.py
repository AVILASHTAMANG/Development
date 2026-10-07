'''
ipv4 pattern :
To understand this regex, we have to remember that regular expressions read **characters**, not numerical values. It doesn't know what "less than 255" means; it only knows how to look for specific digit combinations.

Here is the exact pattern broken down piece by piece:
`r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'`

### 1. The Anchors
* **`^`** (Start of string): Ensures the match starts at the very beginning of the text.
* **`$`** (End of string): Ensures the match ends at the very end.
Together, they ensure the string is *only* an IP address, rejecting something like `"My IP is 192.168.1.1 and more text"`.

### 2. The Number Validator (0 to 255)
This is the core engine of the regex: `(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)`. Because an IPv4 block can only be a number from 0 to 255, we use the OR operator (`|`) to split it into three possible character scenarios:

* **`25[0-5]`**: Catches the highest numbers, **250 through 255**. It looks for a "2", then a "5", then a digit from 0 to 5.
* **`2[0-4][0-9]`**: Catches **200 through 249**. It looks for a "2", then a digit from 0 to 4, then any digit from 0 to 9.
* **`[01]?[0-9][0-9]?`**: Catches everything else, from **0 to 199**.
* `[01]?`: An optional `0` or `1` at the beginning.
* `[0-9]`: A mandatory middle digit (so single digits like `7` still pass).
* `[0-9]?`: An optional final digit.

### 3. The Separator and Multiplier
* **`\.`**: A literal period. Because a plain dot (`.`) in regex means "any character", we have to escape it with a backslash to say "exactly a period."
* **`{3}`**: This means "repeat the exact previous group 3 times."
Since the group is `((Number Validator)\.)`, this part perfectly matches the first three blocks of an IP address, like `192.` `168.` `1.`

### 4. The Final Block
* **`(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)`**: We paste the exact same Number Validator one more time at the very end. We do this outside the `{3}` loop because the final number in an IP address (like the `126` in `10.110.129.126`) does not have a period after it.
'''

'''
ipv6 pattern :
This pattern is much simpler than IPv4 because IPv6 uses base-16 (hexadecimal) math, allowing a straightforward character match rather than complex numerical range checks. It strictly expects 8 blocks of characters.

Here is the exact pattern broken down piece by piece:
`r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'`

### 1. The Anchors

* **`^`** (Start) and **`$`** (End): Just like in the IPv4 pattern, these ensure the regex evaluates the entire string from start to finish. This rejects strings where a valid IP is just buried inside a longer sentence.

### 2. The Hexadecimal Block

* **`[0-9a-fA-F]`**: This character class matches any valid hexadecimal digit. It allows numbers `0` through `9`, lowercase letters `a` through `f`, and uppercase letters `A` through `F`.
* **`{1,4}`**: This length quantifier dictates that the preceding character class must appear between 1 and 4 times. This handles both full blocks (like `abcd`) and valid blocks where leading zeros are omitted (like `a` instead of `000a`).

### 3. The Separator and Multiplier

* **`:`**: A literal colon, which is the standard separator in IPv6.
* **`([0-9a-fA-F]{1,4}:){7}`**: By wrapping the hex block and the colon in parentheses and adding `{7}`, the regex demands exactly **seven** sequential blocks formatted as "up to four hex digits followed by a colon" (e.g., `2001:0db8:85a3:0000:0000:8a2e:0370:`).

### 4. The Final Block

* **`[0-9a-fA-F]{1,4}`**: The eighth and final hexadecimal block is written explicitly at the end, outside the `{7}` multiplier group. This is required because the final block of an IP address must not end with a colon.

> **Key insight:** Because this specific regex strictly requires 8 distinct blocks, it will return "Neither" for valid, compressed IPv6 addresses that use the double-colon shorthand for consecutive zeros (e.g., `2001:db8::1`).
'''

'''
To support :: One or more consecutive all-zero groups may be replaced by ::  

To support the double-colon (`::`) shorthand, the regex must account for a fundamental limitation of regular expressions: **regex cannot do math.**

Because `::` can replace any number of consecutive zero blocks, a strict regex cannot simply check for "up to 8 blocks." It must use the `OR` (`|`) operator to explicitly map out every single valid position where the `::` could exist without exceeding the 8-block limit.

Here is what that pattern looks like in Python using `re.VERBOSE` (which allows you to write regex across multiple lines with comments for readability):

```python
import re

def is_valid_ipv6_regex(ip):
    # This pattern maps out the 9 possible structural variations of an IPv6 address
    ipv6_pattern = re.compile(r"""^(
        ([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|          # 1. Fully expanded (8 blocks)
        ([0-9a-fA-F]{1,4}:){1,7}:|                       # 2. Compressed at the very end (e.g., 2001:db8::)
        ([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|       # 3. Compressed before the last block
        ([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|# 4. Compressed before the last 2 blocks
        ([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|# 5. Compressed before the last 3 blocks
        ([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|# 6. Compressed before the last 4 blocks
        ([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|# 7. Compressed before the last 5 blocks
        [0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|     # 8. Compressed right after the first block
        :((:[0-9a-fA-F]{1,4}){1,7}|:)                    # 9. Compressed at the start (::1) or fully compressed (::)
    )$""", re.VERBOSE)

    return bool(ipv6_pattern.match(ip))

```

### Why Developers Avoid Regex for IP Validation

As you can see, using regex for IPv6 validation results in a massive, hard-to-maintain block of code (and the pattern above doesn't even account for hybrid IPv4-mapped IPv6 addresses like `::ffff:192.168.0.1`).

In production Python code, developers almost never use regex for this. Instead, Python has a built-in library specifically designed to handle all IP address edge cases instantly:

```python
import ipaddress

class Solution:
    def ipAddressValidation(self, ip_str):
        try:
            ip_obj = ipaddress.ip_address(ip_str)
            return f"IPv{ip_obj.version}"
        except ValueError:
            return "Neither"

if __name__ == '__main__':
    # Tests standard IPv4, compressed IPv6, and an invalid string
    for ip in ["10.110.129.126", "2001:db8::1", "256.0.0.1"]:
        print(f"{ip:16} -> {Solution().ipAddressValidation(ip)}")

```

The `ipaddress.ip_address()` function automatically checks the syntax, processes the `::` compression, handles character limits, and verifies mathematical boundaries, making it entirely foolproof and far cleaner than regular expressions.
'''

import re
import ipaddress

class Solution:
    def ipAddressValidation(self, ip_str):
        ipv4 = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        ipv6 = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
        if re.match(ipv4, ipaddress):
            return ('IPv4')
        elif re.match(ipv6, ipaddress):
            return ('IPv6')
        else:
            return ('Neither')

        # try:
        #     ip_obj = ipaddress.ip_address(ip_str)
        #     return f"IPv{ip_obj.version}"
        # except ValueError:
        #     return "Neither"

if __name__ == '__main__':
    ip_str = "10.110.129.126"
    print(Solution().ipAddressValidation(ip_str))