import socket
from rich.console import Console
from rich.panel import Panel
from rich.progress import track

console = Console()
services = {
    20: "FTP",
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    80: "HTTP"
}
def check_ports(ip):
    open_ports = []

    try:
        for port in track(range(20, 101), description=f"Scanning {ip}..."):
            services_match = services.get(port, "Unknown")
            with socket.socket() as sock:
                sock.settimeout(0.5)

                result = sock.connect_ex((ip, port))

                if result == 0:
                    open_ports.append((port, services_match))

        return open_ports

    except socket.gaierror as err:
        console.print(Panel(f"[red]Error[/red] , {err}"))
        return None

