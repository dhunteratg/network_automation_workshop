import json
from scrapli import Scrapli
import os

payload = os.environ["PAYLOAD"]

def main():
    #print("hi")
    #with open("webhook_payload.json", "r") as f:
    #    netbox_payload = json.load(f)

    netbox_payload = json.loads(payload)

    device_changed = netbox_payload["data"]["device"]["name"]
    intf_changed = netbox_payload["data"]["name"]
    new_descr = netbox_payload["data"]["description"]

    print(f"device {device_changed} interface {intf_changed} updated description to: {new_descr}")

    device = {
        "host": device_changed,
        "auth_username": "admin",
        "auth_password": "admin",
        "auth_strict_key": False,
        "platform": "arista_eos",
        "transport": "paramiko"
    }

    conn = Scrapli(**device)
    conn.open()
    print(conn.get_prompt())
    configs = ['interface ' + intf_changed, 'description ' + new_descr]
    response = conn.send_configs(configs)
    print(response, type(response), dir(response))
    print(response.result)
    for response in response:
        print(response, type(response), dir(response))
        print(response.result)

    conn.close()


if __name__ == "__main__":
    main()
