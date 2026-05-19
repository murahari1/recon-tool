import requests

def extract_keyword(banner):
    import re
    # match patterns like "vsFTPd 2.3.4" or "OpenSSH 4.7p1" or "Apache/2.2.8"
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

        return results

    except Exception as e:
        print(f"[-] Error: {e}")
        return []

if __name__ == "__main__":
    search_cve("vsFTPd 2.3.4")
    search_cve("OpenSSH 4.7")
    search_cve("Apache 2.2.8")