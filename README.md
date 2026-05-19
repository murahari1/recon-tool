# Recon Tool

A Python-based reconnaissance tool for penetration testers. 
Automates port scanning, service banner grabbing, and CVE 
lookup in one run.

## What it does
- Scans ports 1–1024 on a target
- Grabs service banners to identify software and versions
- Looks up known CVEs for detected services via NVD API
- Saves a full JSON report of findings

## Built and tested against
- Metasploitable2 (10.10.10.142)
- Detected vsFTPd 2.3.4 → automatically found CVE-2011-2523

## How to run

git clone https://github.com/yourusername/recon-tool.git
cd recon-tool
python3 main.py

## Sample output
[+] Port 21: 220 (vsFTPd 2.3.4)
[+] Port 22: SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1
[+] CVE-2011-2523: vsftpd 2.3.4 backdoor opens shell on port 6200/tcp

## Tech used
- Python 3
- socket, requests, json modules
- NVD CVE API

## Author
Doddoji Murahari — BTech CSE (AI/DS), Parul University
