import socket
import threading

def scan_ports(target, ports):
    open_ports = []
    lock = threading.Lock()
    print(f"\n[*] Scanning {target}...\n")

    def scan(port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                with lock:
                    print(f"[+] Port {port} is OPEN")
                    open_ports.append(port)
            s.close()
        except:
            pass

    threads = []
    for port in ports:
        t = threading.Thread(target=scan, args=(port,))
        threads.append(t)
        t.start()

        if len(threads) >= 100:
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()

    return sorted(open_ports)

if __name__ == "__main__":
    target = input("Enter target IP: ")
    ports = range(1, 65536)
    open_ports = scan_ports(target, ports)
    print(f"\n[*] Open ports: {open_ports}")