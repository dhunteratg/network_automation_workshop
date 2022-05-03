"""
module docstring
"""
import os
import json
from scrapli import Scrapli

payload = os.environ["PAYLOAD"]

PLATFORM_MAP = {
    "leaf1": "arista_eos",
    "leaf2": "arista_eos",
    "leaf3": "cisco_nxos",
    "spine1": "arista_eos",
}

NAT_MAP = {
    "leaf1": "2221",
    "leaf2": "2222",
    "leaf3": "2223",
    "spine1": "2211",
}


def main():
    """
    method docstring
    """
    # print("hi")
    # with open("webhook_payload.json", "r") as f:
    #    netbox_payload = json.load(f)

    netbox_payload = json.loads(payload)

    device_changed = netbox_payload["data"]["device"]["name"]
    intf_changed = netbox_payload["data"]["name"]
    new_descr = netbox_payload["data"]["description"]

    print(
        f"device {device_changed} interface {intf_changed} updated description to: {new_descr}"
    )

    #    device = {
    #        "host": device_changed,
    #        "auth_username": "admin",
    #        "auth_password": "admin",
    #        "auth_strict_key": False,
    #        "platform": "arista_eos",
    #        "transport": "paramiko"
    #    }
    with Scrapli(
        host="student-davidh.us-west1-a",
        port=NAT_MAP[device_changed],
        auth_username="admin",
        auth_password="admin",
        auth_strict_key=False,
        platform=PLATFORM_MAP[device_changed],
        transport="paramiko",
    ) as conn:
        configs = ["interface " + intf_changed, "description " + new_descr]
        response = conn.send_configs(configs)
        print(response.result)


#    conn = Scrapli(**device)
#    conn.open()
#    print(conn.get_prompt())
#    print(response, type(response), dir(response))
#    print(response.result)
#    for response in response:
#        print(response, type(response), dir(response))
#        print(response.result)
#
#    conn.close()


if __name__ == "__main__":
    main()
