from file_io import load_file
from ip_utils import get_ips
from scanner import check_ports
from ui import menu
from rich.console import Console
from ui import create_output
from rich.panel import Panel
import asyncio
console = Console()

async def main():
    while True:
        choice = menu()

        if choice == "1":
            path = input("Path: ")
            text = load_file(path)
            if text is None:
                continue
            else:
                output = create_output()
                ips = get_ips(text)
                for ip in ips:
                    ports = await check_ports(ip)
                    if ports is None:
                        continue
                    else:
                        for port, service in ports:
                            output.add_row(ip, str(port),service ,style="bold green")
                console.print(Panel(output, style="green"))
        elif choice == "2":
            ip = input("IP: ")
            ports = await check_ports(ip)
            output = create_output()
            if ports is None:
                continue
            else:
                for port, service in ports:
                    output.add_row(ip, str(port), service, style="bold green")
            console.print(Panel(output, style="green"))
        elif choice == "3":
            break
asyncio.run(main())