# Imports
import dns.resolver

# Main Loop
running = True
while running:
    raw_input = input("What method would you like to use? ")
    usr_input = raw_input.strip().lower()
    # Help
    if usr_input == "help":
        print("""
        OPTIONS:
         help - shows this help screen
         wordlist - uses the 'domlist.txt' wordlist to check urls
         input - uses your input to check if a url exists
         s - stops this program
         """)
    # Stop Program
    elif usr_input == "s":
        running = False
    # Wordlist Option
    elif usr_input == "wordlist":
        dn = input("enter the domain name: ")
        with open("domlist.txt") as domlist:
            for name in domlist:
                url = ''.join([name.strip(), dn.strip()])
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
    # Input option
    elif usr_input == "input":
        print("Insert your website!")
        while True:
            url = input("- ")
            if url == "s":
                break
            try:
                result = dns.resolver.resolve(url.strip().lower())
                print(" -works")
            except dns.resolver.NXDOMAIN:
                print(" -does not work")
            except dns.resolver.NoAnswer:
                print(" -no answer")
            except dns.resolver.Timeout:
                print(" -timeout")
            except dns.resolver.NoNameservers:
                print(" -refused")
            except:
                print(" -does not work for some reason")
    # Blank Input
    elif usr_input == "":
        pass
    # So it doesnt cause any errors!
    else:
        print("Please specify your method better!")
