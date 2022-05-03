import re
from scrapli import Scrapli

runconfig = """
Building configuration...

Current configuration : 5878 bytes
!
! Last configuration change at 16:01:10 UTC Sat Oct 9 2021
!
version 16.12
service timestamps debug datetime msec
service timestamps log datetime msec
! Call-home is enabled by Smart-Licensing.
service call-home
platform qfp utilization monitor load 80
platform punt-keepalive disable-kernel-core
platform console serial
!
hostname rtr1
!
boot-start-marker
boot-end-marker
!
"""
pattern = r"version (\d{2}).(\d{2})"

def main():
    '''
    '''
    match = re.search(pattern, runconfig)
    print(match, type(match), dir(match))
    print(match.group())
    print(match.span())
    for group in match.groups():
        print(group)

    device = {
        "host": "172.20.20.21",
        "auth_username": "admin",
        "auth_password": "admin",
        "auth_strict_key": False,
        "platform": "arista_eos",
        "transport": "paramiko"
    }

    conn = Scrapli(**device)
    conn.open()
    print(conn.get_prompt())
    commands = ['show interface management 0']
    response = conn.send_commands(commands)
    print(response, type(response), dir(response))
    print(response.result)

    match = re.search(r"Internet address is \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}", response.result)
    print(match.group())
    match = re.search(r"Up .*", response.result)
    print(match.group())
    match = re.search(r"(Internet address is \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2})(?:[\s\S]+)(Up .*)", response.result, flags=re.M)
    print(match.groups()[0])
    print(match.groups()[1])
    match = re.search(r"(?P<addr>Internet address is \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2})(?:[\s\S]+)(?P<up>Up .*)", response.result, flags=re.M)
    print(match.groupdict()["addr"])
    print(match.groupdict()["up"])

# Internet address is 172.20.20.21/24
# Up 5 days, 5 hours, 33 minutes, 19 seconds

if __name__ == "__main__":
    main()
