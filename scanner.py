import asyncio
from rich.console import Console
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
async def check_one_port(ip, port):
    services_match = services.get(port, "Unknown")
    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(ip, port),
            timeout=0.5
        )
        writer.close()
        return ((port, services_match))
    except:
        pass





async def check_ports(ip):
    tasks = []
    for port in range(20, 101):
        tasks.append(check_one_port(ip, port))

    results = await asyncio.gather(*tasks)
    open_ports = [r for r in results if r is not None]
    return open_ports
