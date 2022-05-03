from jinja2 import Template, FileSystemLoader, Environment

def main():
    env = Environment(loader=FileSystemLoader("/home/davidh/network_automation_workshop/templates/"))
    template = env.get_template("interface.j2")

if __name__ == "__main__":
    main()
