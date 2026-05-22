from scanner import scan_ports
from banner import grab_banner
from report import generate_report
from cve_lookup import search_cve, extract_keyword, PORT_SERVICES

def main():
    target = input("Enter target IP: ")
    
    print("\n[*] Starting port scan...")
    open_ports = scan_ports(target, range(1, 65536))

    print("\n[*] Grabbing banners...")
    banners = {}
    for port in open_ports:
        banner = grab_banner(target, port)
        if banner:
            banners[port] = banner
            print(f"[+] Port {port}: {banner[:80]}")

    print("\n[*] Looking up CVEs...")
    cves = {}
    for port in open_ports:
        banner = banners.get(port)
        if banner:
            keyword = extract_keyword(banner)
        else:
            keyword = PORT_SERVICES.get(port)

        if keyword:
            print(f"[*] Searching CVEs for port {port}: {keyword}")
            found_cves = search_cve(keyword)
            if found_cves:
                cves[port] = found_cves

    generate_report(target, open_ports, banners, cves)
    print("\n[+] Done.")

if __name__ == "__main__":
    main()