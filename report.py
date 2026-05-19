import json
from datetime import datetime

def generate_report(target, open_ports, banners, cves):
    report = {
        "target": target,
        "scan_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "open_ports": open_ports,
        "banners": banners,
        "cves": cves
    }

    filename = f"report_{target.replace('.', '_')}.json"
    with open(filename, "w") as f:
        json.dump(report, f, indent=4)

    print(f"\n[*] Report saved to {filename}")
    return filename