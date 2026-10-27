"""ASCII banner and bilingual strings for Isub."""

LOGO = r"""
  ___ ____  _   _ ____
 |_ _/ ___|| | | | __ )
  | |\___ \| | | |  _ \
  | | ___) | |_| | |_) |
 |___|____/ \___/|____/

    Isub v1.0 - TCP Port Scanner
"""

STRINGS = {
    "es": {
        "confirm": "¿Confirmas que tienes autorización para escanear el objetivo? [s/N]: ",
        "aborted": "Abortado. Solo debes escanear sistemas autorizados.",
        "scanning": "Escaneando {host} ...",
        "open_port": "[+] {port}/{service} ABIERTO{extra}",
        "done": "[OK] {count} puertos abiertos en {time:.2f}s",
        "log_saved": "Log guardado en {path}",
        "invalid_range": "Rango de puertos inválido.",
        "invalid_host": "Host inválido o no resuelve.",
    },
    "en": {
        "confirm": "Do you confirm you have authorization to scan the target? [y/N]: ",
        "aborted": "Aborted. Only scan systems you are authorized to test.",
        "scanning": "Scanning {host} ...",
        "open_port": "[+] {port}/{service} OPEN{extra}",
        "done": "[OK] {count} open ports in {time:.2f}s",
        "log_saved": "Log saved to {path}",
        "invalid_range": "Invalid port range.",
        "invalid_host": "Invalid host or cannot resolve.",
    },
}
