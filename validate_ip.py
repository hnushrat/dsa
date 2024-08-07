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
            