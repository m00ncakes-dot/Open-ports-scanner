from rich.console import Console
from rich.panel import Panel
console = Console()

def load_file(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError as err:
        console.print(Panel(f"[bold red]Error[/bold red] , {err}", style="red"))
        return None