from scrapli import Scrapli

def main():
    device = {
        "host": "172.20.20.23",
        "auth_username": "admin",
        "auth_password": "admin",
        "auth_strict_key": False,
        "platform": "cisco_nxos",
        "transport": "telnet"
    }

    conn = Scrapli(**device)
    conn.open()
    print(conn.get_prompt())
    response = conn.send_command("show haircut")
    print(response, type(response), dir(response))
    print(response.channel_input)
    print(response.failed_when_contains)
    print(response.result)
    print(response.elapsed_time)
    print(response.failed)
    commands = ['show inventory', 'show interface status', 'show run', 'foo']
    response = conn.send_commands(commands)
    print(response, type(response), dir(response))
    for response in response:
        print(response, type(response), dir(response))
        print(response.result)
    conn.close()

if __name__ == "__main__":
    main()
