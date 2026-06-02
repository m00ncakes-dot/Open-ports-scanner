import pyfiglet
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
console = Console()

def menu():
    title = pyfiglet.figlet_format("Open Ports Scanner")
    console.print(Panel(title, style="bold red"))

    console.print(Panel("Choose one option: \n1. Scan IP's from path \n2. Enter IP manually \n3. Exit", style="bold green"))

    return input("Choice: ")

def create_output():
    output = Table(title="Open ports found")
    output.add_column("IP", justify="left", style="bold green")
    output.add_column("Port", justify="right", style="bold green")
    output.add_column("Service", justify="right", style="bold green")

    return output