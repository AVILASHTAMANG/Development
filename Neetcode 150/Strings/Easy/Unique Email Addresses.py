# A valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters,
# the email may contain one or more '.' or '+'.
#
# For example, in "alice@neetcode.io", "alice" is the local name, and "neetcode.io" is the domain name.
# If you add periods '.' between some characters in the local name part of an email address, mail sent there will be
# forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.
#
# For example, "alice.z@neetcode.io" and "alicez@neetcode.io" forward to the same email address.
# If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain
# emails to be filtered. Note that this rule does not apply to domain names.
#
# For example, "m.y+name@email.com" will be forwarded to "my@email.com".
# It is possible to use both of these rules at the same time.
# You are given an array of strings emails where we send one email to each emails[i], return the number of different
# addresses that actually receive mails.

from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local, domain = email.split('@')
            local_clean = []
            for ch in local:
                if ch == "+":
                    break
                elif ch == ".":
                    continue
                else:
                    local_clean.append(ch)
            normalized_email = ''.join(local_clean) + '@' + domain
            unique_emails.add(normalized_email)
        return len(unique_emails)

if __name__ == '__main__':
    emails = ["test.email+alex@neetcode.com", "test.e.mail+bob.cathy@neetcode.com", "testemail+david@nee.tcode.com"]
    print(Solution().numUniqueEmails(emails))