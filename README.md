# Recon Tool

A Python-based reconnaissance tool for penetration testers.
Automates port scanning, service banner grabbing, and CVE
lookup in a single run. Tested live against Metasploitable2.

## What it does
- Scans all 65535 ports on a target
- Grabs service banners to identify software and versions
- Falls back to known port-service mapping if no banner found
- Looks up known CVEs for every detected service via NVD API
- Saves a full JSON report of findings

## Requirements
- Linux (Kali, Parrot, Ubuntu, NixOS)
- Python 3.x
- requests library

Install requests (Ubuntu/Kali/Parrot):
pip install requests

On NixOS:
nix-shell -p python3Packages.requests --run "python3 main.py"

## How to run (Ubuntu/Kali/Parrot)
git clone https://github.com/murahari1/recon-tool.git
cd recon-tool
pip install requests
python3 main.py

## How to run (NixOS)
git clone https://github.com/murahari1/recon-tool.git
cd recon-tool
nix-shell -p python3Packages.requests --run "python3 main.py"

Enter target IP when prompted.

## Sample output
[+] Port 21 is OPEN
[+] Port 22 is OPEN
[+] Port 1524 is OPEN

[+] Port 21: 220 (vsFTPd 2.3.4)
[+] Port 22: SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1
[+] Port 1524: root@metasploitable:/#

[+] CVE-2011-2523: vsftpd 2.3.4 backdoor opens shell on port 6200/tcp
[+] CVE-1999-0113: Some implementations of rlogin allow root access

[*] Report saved to report_10_10_10_142.json

## Built and tested against
- Metasploitable2
- Detected 30 open ports
- Automatically found CVE-2011-2523 (vsFTPd 2.3.4 backdoor)
- Detected open root shell on port 1524

## File structure
recon-tool/
├── main.py          # Entry point, ties everything together
├── scanner.py       # Port scanner
├── banner.py        # Banner grabbing
├── cve_lookup.py    # CVE lookup via NVD API
└── report.py        # JSON report generation

## Tech used
- Python 3
- socket, threading, requests, json modules
- NVD CVE API (https://nvd.nist.gov/developers/vulnerabilities)

## Author
Doddoji Murahari — BTech CSE (AI/DS), Parul University
github.com/murahari1