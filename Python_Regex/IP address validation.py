import re

class Solution:
    def ipAddressValidation(self, ipaddress):
        ipv4 = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        ipv6 = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
        if re.match(ipv4, ipaddress):
            return ('IPv4')
        elif re.match(ipv6, ipaddress):
            return ('IPv6')
        else:
            return ('Neither')

if __name__ == '__main__':
    ipaddress = "10.110.129.126"
    print(Solution().ipAddressValidation(ipaddress))