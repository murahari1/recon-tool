import socket

def grab_banner(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((target, port))
        s.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner = s.recv(1024).decode().strip()
        s.close()
        return banner
    except:
        return None

if __name__ == "__main__":
    target = input("Enter target IP: ")
    ports = [21, 22, 80, 443, 8080]

    for port in ports:
        banner = grab_banner(target, port)
        if banner:
            print(f"[+] Port {port}: {banner[:100]}")
        else:
            print(f"[-] Port {port}: No banner")