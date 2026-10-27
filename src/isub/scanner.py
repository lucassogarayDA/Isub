"""TCP scanning logic for Isub."""

import socket
from concurrent.futures import ThreadPoolExecutor
from isub.services import SERVICES


def scan_port(host: str, port: int, timeout: float = 0.5, grab_banner: bool = True):
    """Return (port, service, banner) if open, else None."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            if sock.connect_ex((host, port)) != 0:
                return None

            service = SERVICES.get(port, "Unknown")
            banner = ""
            if grab_banner:
                try:
                    sock.settimeout(1.0)
                    raw = sock.recv(1024)
                    banner = raw.decode(errors="ignore").strip()[:80]
                except Exception:
                    pass
            return (port, service, banner)
    except Exception:
        return None


def scan(host: str, ports, threads: int = 100, timeout: float = 0.5,
         grab_banner: bool = True):
    """Scan a list of ports and return a sorted list of open results."""
    results = []
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [
            executor.submit(scan_port, host, p, timeout, grab_banner)
            for p in ports
        ]
        for f in futures:
            r = f.result()
            if r:
                results.append(r)
    return sorted(results)
