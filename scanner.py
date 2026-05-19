import socket

def scan_ports(target, ports):
    open_ports = []
    print(f"\n[*] Scanning {target} ...\n")

    for port in ports:
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target,port))
            if result == 0:
                print(f"[+] port {port} is OPEN")
                open_ports.append(port)
            s.close()
        except socket.error as e:
            print(f"[-] Error: {e}")

    return open_ports
if __name__ == "__main__":
    target = input("Enter target IP: ")
    ports = range(1,1025)
    open_ports = scan_ports(target, ports)
    print(f"\n[+] open ports: {open_ports}")

