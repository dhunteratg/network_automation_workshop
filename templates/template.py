from jinja2 import Environment, FileSystemLoader, select_autoescape, Template

def main():
    env = Environment(
        loader=FileSystemLoader("/home/davidh/network_automation_workshop/templates"),
    )
    template = env.get_template("interface.j2")
    intf={"num": "1234", "descr": "tacocat was here!", "ip_addr": "1.2.3.4/30"}
    print(template.render(intf=intf))

    #template = Template('Hello {{ name }}!')
    #print(template.render(name='John Doe'))

    output = ""
    interfaces = [{"num": "1", "descr": "apple", "ip_addr": "1.2.3.4/30"},
                    {"num": "2", "descr": "banana", "ip_addr": "2.3.4.5/30"},
                    {"num": "3", "descr": "cherry", "ip_addr": "3.4.5.6/30"},
                    {"num": "4", "descr": "durian", "ip_addr": "4.5.6.7/30"}]
    for interface in interfaces:
        output += template.render(intf=interface)

    print(output)

if __name__ == "__main__":
    main()
