# Imports
import dns.resolver

dn = ".mk"
with open("domlist.txt") as domlist:
    for name in domlist:
        url = ''.join([name.strip(), dn])
        try:
            result = dns.resolver.resolve(url)
            print(url, " -works")
        except dns.resolver.NXDOMAIN:
            print("-")
        except dns.resolver.NoAnswer:
            print(url, " -no answer")
        except dns.resolver.Timeout:
            print(url, " -timeout")
        except dns.resolver.NoNameservers:
            print(url, " -refused")
        except:
            print("-")
