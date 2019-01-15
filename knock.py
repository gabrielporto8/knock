import socket
import sys

main = """
    Welcome to Knock, a simple portscan!

     _  __                 _    
    | |/ /                | |   
    | ' / _ __   ___   ___| | __
    |  < | '_ \ / _ \ / __| |/ /
    | . \| | | | (_) | (__|   < 
    |_|\_\_| |_|\___/ \___|_|\_\


    Powered by Gabriel Porto.
"""

print("#" * 40)
print(main)
print("#" * 40)

while True:
    try:
        host = str(input("\nHost: "))
        if host.isspace():
            raise ValueError
        elif host == '':
            raise ValueError
        else:
            break
    except ValueError:
        print("\nHostname invalid, please try again...")
        
while True:

    try:
        print("\nWould you like to test standart ports or choose a range?")
        print("1 - Standart ports (1, 1025)")
        print("2 - Choose a range")
        option = int(input("\nPlease choose an option: "))

        if option == 1:
            begin = 1
            end = 1025
            break
        elif option == 2:
            while True:
                try:
                    print('\nPlease choose your range ports...')
                    begin = int(input('Begin: '))
                    end = int(input('End: ')) + 1
                    print("\n")
                
                    if begin <= 0:
                        raise ValueError("\nThe number was not positive, please try again...")
                    elif begin >= end:
                        raise ValueError("\nEnd could not be minor than begin, please try again...")
                    break

                except ValueError as exp:
                    print(exp)
                    
            break
        
        else:
            raise ValueError("\n==> ERROR! Choose 1 or 2, please try again...")
        
        
    except ValueError as exp:
        print(exp)
        
    except KeyboardInterrupt:
        print("\nYou pressed Ctrl+C. Exiting...")
        sys.exit()
        
try:
    print("\n ===> I'm knocking on the ports... Please wait... <===\n")
    for port in range(begin, end):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.5)
        cod = client.connect_ex((host, port))
        ip = socket.gethostbyname(host)

        if cod == 0:
            print ('PORT', port, 'from', ip, 'is OPEN')
        client.close()
            

except KeyboardInterrupt:
    print("\nYou pressed Ctrl+C. Exiting...")
    sys.exit()

except socket.gaierror:
    print("\nHostname could not be resolved. Exiting...")
    sys.exit()

except socket.error:
    print("\nCouldn't connect to server. Exiting...")
    sys.exit()
    
print("\nExiting...")
    
            
