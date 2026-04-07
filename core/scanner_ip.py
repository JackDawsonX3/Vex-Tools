import socket
import threading
import datetime

max_threading = threading.BoundedSemaphore(100)
file_lock = threading.Lock()
online_ips = []

def scan_ip(ip):
    with max_threading:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)

                for port in [80,445,22]:
                    result = s.connect_ex((ip,port))

                    if result == 0:
                        with file_lock:
                            print(f"[+] Found: {ip}")
                            online_ips.append(ip)
        except Exception as e:
            pass


def threading_ip_scan(base_ip):
    filename = datetime.datetime.now().strftime("scan_ip_%Y%m%d_%H%M%S.txt")
    online_ips.clear()
    threads = []

    for i in range(1,255):
        ip = base_ip + str(i)

        t = threading.Thread(target=scan_ip, args=(ip,))
        if ip not in online_ips:
            threads.append(t)
        t.start()

    for t in threads:
        t.join()

    for ip in online_ips:
        print(f"[+]IP: {ip} ONLINE")

    if online_ips:
        with open(filename,"a", encoding="utf-8") as f:
            for ips in online_ips:
                f.write(ips + " ONLINE" + "\n")
            print(f"[!] Results saved to {filename}")
    else:
        print("[!] No open ip found.")
    
    print("IP scanning completed.")