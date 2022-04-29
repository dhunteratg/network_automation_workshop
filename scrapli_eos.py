from scrapli import Scrapli

def main():
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
    commands = ['show version', 'show inventory']
    response = conn.send_commands(commands)
    print(response, type(response), dir(response))
    print(response.result)
    for response in response:
        print(response, type(response), dir(response))
        print(response.result)

    conn.close()

if __name__ == "__main__":
    main()
