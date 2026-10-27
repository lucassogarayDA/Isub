# Isub

[![PyPI version](https://img.shields.io/pypi/v/isubing.svg)](https://pypi.org/project/isubing/)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-Apache--2.0-green)](./LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows%20%7C%20Termux-lightgrey)]()

**Fast, multithreaded TCP port scanner with service detection and logging.**

---

## 🚀 Install

```bash
pip install isubing
```

Or install from source:

```bash
git clone https://github.com/lucassogarayDA/isub.git
cd isub
pip install -e .
```

---

⚠️ Disclaimer

Use Isub only on systems you own or have explicit written authorization to test.
Unauthorized scanning is illegal in most jurisdictions. The author assumes no responsibility for misuse.

---

⚡ Quick Start

Scan the first 1024 ports on localhost:

```bash
isub -H 127.0.0.1 -p 1-1024
```

Scan specific ports on a remote host:

```bash
isub -H example.com -p 22,80,443 --lang en
```

Full scan with custom threads and timeout:

```bash
isub -H 192.168.1.1 -p 1-65535 -t 200 --timeout 1.0 -y
```

---

Features

· ⚡ Fast: multithreaded scanning (configurable thread count)
· 🔍 Service detection: identifies common services (SSH, HTTP, MySQL, etc.)
· 📡 Banner grabbing: captures the first bytes sent by services to reveal versions
· 📝 Rotating logs: automatic log rotation to avoid filling your disk
· 🌐 Bilingual: Spanish and English output (--lang es / --lang en)
· 📦 Zero dependencies: pure Python standard library
· 🖥️ Cross-platform: Linux, macOS, Windows, Termux

---

Options

Flag Description Default
-H, --host Target host (IP or domain) — required —
-p, --ports Port range or list (1-1024 or 22,80,443) 1-1024
-t, --threads Number of concurrent threads 100
--timeout Timeout per port in seconds 0.5
--no-banner Skip banner grabbing False
-l, --log Log file path isub.log
-y, --yes Skip authorization confirmation False
--lang Language: es or en es
-v, --version Show version and exit —

---

Example Output

```
  ___ ____  _   _ ____
 |_ _/ ___|| | | | __ )
  | |\___ \| | | |  _ \
  | | ___) | |_| | |_) |
 |___|____/ \___/|____/

    Isub v1.0 - TCP Port Scanner

Scanning 127.0.0.1 ...
[+] 22/SSH OPEN | OpenSSH 8.9
[+] 80/HTTP OPEN
[+] 443/HTTPS OPEN
--------------------------------------------------
[OK] 3 open ports in 1.24s
Log saved to isub.log
```

---

Logging

Isub writes all scan results to a rotating log file (isub.log by default). Logs rotate automatically at 5 MB, keeping up to 3 backups, so you never have to worry about disk space.

---

Development

Run locally without installing:

```bash
python -m isub -H 127.0.0.1 -p 1-1024
```

Build the package from source:

```bash
python -m build
```

---

License

Apache License 2.0 — see LICENSE and NOTICE.

---

Author

Lucas Sogaray — @lucassogarayDA
