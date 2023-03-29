"""Given a valid (IPv4) IP address, return a defanged version of that IP
address. A defanged IP address replaces every period "." with "[.]".

Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

Constraints:
The given address is a valid IPv4 address."""


class Solution:
    @staticmethod
    def defang_ip_addr(address: str) -> str:
        def_ip: str = ''
        for element in address:
            if element == '.':
                def_ip = def_ip + '[.]'
            else:
                def_ip = def_ip + element
        return def_ip


assert Solution.defang_ip_addr("1.1.1.1") == "1[.]1[.]1[.]1"
assert Solution.defang_ip_addr("255.100.50.0") == "255[.]100[.]50[.]0"
