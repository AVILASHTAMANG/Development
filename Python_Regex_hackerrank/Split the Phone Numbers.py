# There is a list of phone numbers which needs the attention of a text processing expert. As an expert in regular
# expressions, you are being roped in for the task. A phone number directory can reveal a lot such as country codes and
# local area codes. The only constraint is that one should know how to process it correctly.
#
# A Phone number is of the following format
#
# [Country code]-[Local Area Code]-[Number]
# There might either be a '-' ( ascii value 45), or a ' ' ( space, ascii value 32) between the segments
# Where the country and local area codes can have 1-3 numerals each and the number section can have 4-10 numerals each.
#
# And so, if we tried to apply the a regular expression with groups on this phone number: 1-425-9854706
#
# We'd get:
# Group 1 = 1
# Group 2 = 425
# Group 3 = 9854706
#
# You will be provided a list of N phone numbers which conform to the pattern described above. Your task is to split
# it into the country code, local area code and the number.
import re


class Solution:
    def split_the_phone_number(self, s):
        pattern = r'(?P<country_code>\d{1,3})[ -](?P<area_code>\d{1,3})[ -](?P<number>\d{4,10})'
        match = re.match(pattern, s)
        #match = re.fullmatch(pattern, s)
        country_code = match.group('country_code')
        area_code = match.group('area_code')
        number = match.group('number')
        result = f"CountryCode={country_code},LocalAreaCode={area_code},Number={number}"
        return result

if __name__ == '__main__':
    s = ["1 877 2638277", "91-011-23413627"]
    for phone in s:
        print(Solution().split_the_phone_number(phone))