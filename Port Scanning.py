from IPy import IP
import socket

# I AM NOT RESPONSABLE OF WHAT TYPE OF INFORMATION YOU CAN SEE OR WHAT THINGS YOU CAN DO WITH THIS TOOL
# THIS IS FOR PENTEST PORPOUSES ONLY, MALICIOUS USE OF THIS IS NOT ALLOWED
# AGAIN I AM NOT RESPONSABLE OF WHAT CAN BE DONE WITH THIS TOOL
# USE THIS WITH AUTHORIZED USE ONLY, NEVER USE THIS WITHOUT AUTHORIZATION
# BE ETHICAL..


print("PORT SCANNING BY TheCodingDude\n")   


# Converts the link to IP if requiered

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)


# Scan the port and prints the information to the user

def scan_port(ipaddressUser, port):
    try:
        s = socket.socket()
        s.settimeout(0.3)
        s.connect((ipaddressUser, port))
        print("[+] Port " + str(port) + " is open! [+]")
    except:
        print("[-] Port " + str(port) + " is Closed! ")

# Evaluates what command is inputed and print the information to the user

command_question = input("[+] Enter any command: ")
if(command_question == "help"):
    print("YOU CAN SCAN LINKS NOT ONLY IP\n")
    print("AUTHOR IS TheCodingDude\n")
    print("THIS WAS PROGRAMED WITH PYTHON 3.10.1\n")
    print("PLEASE BE ETHICAL AND DONT USE THIS FOR BAD PORPOUSES")
    print("FOR ANY SUPPORT PLEASE EMAIL basico1234prueba@gmail.com\n")
else:
    pass

# Gets Target IP by asking the user, also calls some requieres functions

ipaddressUser = input("[+] Enter The IP Address of the Target [+] ")
converted_ip = check_ip(ipaddressUser)
print("Scanning..")

# for every port between 0 to 10000000 will be shown and scanned

for port in range(0,10000000):
    scan_port(ipaddressUser, port)

# By TheCodingDude

# End of the code for now..