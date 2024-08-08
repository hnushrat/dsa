'''
Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
Leading zeros are allowed in xi.
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.

 

'''

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        if len(queryIP) == 0:
            return 'Neither'
        sep = {}
        f = 0
        for i in queryIP:
            if i == ':':
                f = 1
                if sep.get(i):
                    sep[i]+=1
                else:
                    sep[i] = 1
            elif i == '.':
                if sep.get(i):
                    sep[i]+=1
                else:
                    sep[i] = 1
    
        # ipv6 check
        if f == 1:
            if sep[':']!=7:
                return 'Neither'
            t = queryIP.split(':')
            once = 0
            for i in t:
                if len(i) > 4:
                    return 'Neither'
                else:
                    if len(i) == 0:
                        return 'Neither'
                    x = i.upper()
                    c = 0
                    for j in x:
                        if not j.isdigit():
                            if j>'F' or j<'A':
                                return 'Neither'

                        if j=='0':
                            c+=1
                    if c == 4:
                        if once == 1:
                            return 'Neither'
                        else:
                            once+=1
            return 'IPv6'
        
        # ipv4
        else:
            t = queryIP.split('.')
            if sep['.']!=3:
                return 'Neither'

            for i in t:
                if len(i) > 3:
                    return 'Neither'
                if len(i) == 0:
                    return 'Neither'
                else:
                    if i[0] == '0' and len(i) > 1:
                        return 'Neither'
                    s = 0
                    for j in i:
                        if not j.isdigit():
                            return 'Neither'
                        else:
                            s+=int(j) 
                    if s > 12:
                        return 'Neither'
            return 'IPv4'
            