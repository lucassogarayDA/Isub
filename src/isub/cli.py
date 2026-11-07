"""Command-line interface for Isub."""

import argparse
import sys
import time
import socket
import math
from isub.banner import LOGO, STRINGS
from isub.scanner import scan
from isub.logger import setup_logger

__version__ = "1.0.1"


def parse_ports(port_str: str):
    """Parse comma-separated ports and inclusive ranges.

    Raises ValueError for malformed entries or ports outside 1..65535.
    """
    if not isinstance(port_str, str) or not port_str.strip():
        raise ValueError("empty port specification")

    ports = set()
    for raw_part in port_str.split(","):
        part = raw_part.strip()
        if not part:
            raise ValueError("empty port entry")

        if "-" in part:
            bounds = part.split("-")
            if len(bounds) != 2 or not all(value.strip() for value in bounds):
                raise ValueError(f"invalid port range: {part}")
            start, end = (int(value.strip()) for value in bounds)
            if start > end:
                raise ValueError(f"descending port range: {part}")
            values = range(start, end + 1)
        else:
            values = (int(part),)

        for port in values:
            if not 1 <= port <= 65535:
                raise ValueError(f"port out of range: {port}")
            ports.add(port)

    return sorted(ports)


def main():
    parser = argparse.ArgumentParser(
        prog="isub",
        description="Isub - Fast TCP Port Scanner",
        epilog="Use only on systems you own or have written authorization to test.",
    )
    parser.add_argument("-H", "--host", required=True, help="Target host (IP or domain)")
    parser.add_argument("-p", "--ports", default="1-1024", help="Ports: '1-1024' or '22,80,443'")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Concurrent threads (default: 100)")
    parser.add_argument("--timeout", type=float, default=0.5, help="Timeout per port in seconds (default: 0.5)")
    parser.add_argument("--no-banner", action="store_true", help="Skip banner grabbing")
    parser.add_argument("-l", "--log", default="isub.log", help="Log file path (default: isub.log)")
    parser.add_argument("-y", "--yes", action="store_true", help="Skip authorization confirmation")
    parser.add_argument("--lang", choices=["es", "en"], default="es", help="Language (default: es)")
    parser.add_argument("-v", "--version", action="version", version=f"Isub {__version__}")

    args = parser.parse_args()
    t = STRINGS[args.lang]

    try:
        ports = parse_ports(args.ports)
    except (ValueError, OverflowError) as exc:
        parser.error(f"{t['invalid_range']} {exc}")

    if not 1 <= args.threads <= 256:
        parser.error(t["invalid_threads"])
    if not math.isfinite(args.timeout) or not 0 < args.timeout <= 30:
        parser.error(t["invalid_timeout"])

    print(LOGO)

    if not args.yes:
        answer = input(t["confirm"]).strip().lower()
        if answer not in ("s", "y"):
            print(t["aborted"])
            sys.exit(0)

    try:
        socket.gethostbyname(args.host)
    except socket.gaierror:
        print(t["invalid_host"])
        sys.exit(1)

    logger = setup_logger(args.log)
    logger.info(f"Scan start: host={args.host}, ports={args.ports}, threads={args.threads}")

    print(t["scanning"].format(host=args.host))
    start_time = time.time()

    results = scan(
        host=args.host,
        ports=ports,
        threads=args.threads,
        timeout=args.timeout,
        grab_banner=not args.no_banner,
    )

    elapsed = time.time() - start_time

    for port, service, banner in results:
        extra = f" | {banner}" if banner else ""
        msg = t["open_port"].format(port=port, service=service, extra=extra)
        print(msg)
        logger.info(msg)

    print("-" * 50)
    print(t["done"].format(count=len(results), time=elapsed))
    print(t["log_saved"].format(path=args.log))
    logger.info(f"Scan complete: {len(results)} open ports in {elapsed:.2f}s")


if __name__ == "__main__":
    main()
