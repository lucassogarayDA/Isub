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

Scan selected ports on a system you are authorized to test:

```bash
isub -H example.com -p 22,80,443 --lang en
```

Run a small, controlled scan against your own local machine:

```bash
isub -H 127.0.0.1 -p 1-1024 -t 50 --timeout 1.0
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

## Options

| Flag | Description | Default |
|---|---|---|
| `-H, --host` | Target IPv4 address or hostname (required) | — |
| `-p, --ports` | Comma-separated ports or inclusive ranges | `1-1024` |
| `-t, --threads` | Concurrent worker threads (1–256) | `100` |
| `--timeout` | Connection timeout in seconds (greater than 0, up to 30) | `0.5` |
| `--no-banner` | Skip banner grabbing | Disabled |
| `-l, --log` | Log file path | `isub.log` |
| `-y, --yes` | Skip the interactive authorization prompt | Disabled |
| `--lang` | Output language: `es` or `en` | `es` |
| `-v, --version` | Show version and exit | — |

Port values must be between 1 and 65535. Ranges must be ascending. Isub validates the input before starting.

The `--yes` flag only skips the prompt; it does not grant authorization. Use Isub only on systems you own or have explicit permission to test.

---

Example Output

```
  ___ ____  _   _ ____
 |_ _/ ___|| | | | __ )
  | |\___ \| | | |  _ \
  | | ___) | |_| | |_) |
 |___|____/ \___/|____/

    Isub v1.0.1 - TCP Port Scanner

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

## Development

Run the unit tests:

```bash
python -m unittest discover -s tests -v
```

GitHub Actions runs this test suite on Python 3.8, 3.10, 3.12, and 3.14.

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
