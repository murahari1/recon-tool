import requests
import re
import time

PORT_SERVICES = {
    21: "vsFTPd",
    22: "OpenSSH",
    23: "Telnet",
    25: "Postfix SMTP",
    80: "Apache httpd",
    111: "rpcbind",
    139: "Samba SMB",
    445: "Microsoft SMB",
    512: "rexec",
    513: "rlogin",
    514: "rsh",
    1099: "Java RMI",
    1524: "Metasploitable root shell",
    2049: "NFS",
    2121: "ProFTPD",
    3306: "MySQL",
    3632: "distccd",
    5432: "PostgreSQL",
    5900: "VNC",
    6667: "UnrealIRCd",
    8009: "Apache Tomcat AJP",
    8180: "Apache Tomcat",
    8787: "Ruby DRb"
}

def extract_keyword(banner):
    match = re.search(r'([a-zA-Z]+[/ ][\d.]+[\w]*)', banner)
    if match:
        return match.group(1).replace("/", " ")
    return banner.split("\n")[0][:30]

def search_cve(keyword):
    print(f"\n[*] Searching CVEs for: {keyword}")
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    params = {
        "keywordSearch": keyword,
        "resultsPerPage": 5
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        vulnerabilities = data.get("vulnerabilities", [])
        if not vulnerabilities:
            print("[-] No CVEs found")
            return []
        results = []
        for item in vulnerabilities:
            cve = item["cve"]
            cve_id = cve["id"]
            description = cve["descriptions"][0]["value"][:150]
            print(f"[+] {cve_id}: {description}")
            results.append(cve_id)
        time.sleep(1)
        return results
    except Exception as e:
        print(f"[-] Error: {e}")
        return []