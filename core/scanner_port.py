import socket
import threading
import datetime

file_lock = threading.Lock()
max_threading = threading.BoundedSemaphore(100)
results = [] 

def scanner_port(target, port):
    with max_threading:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((target, port))

                if result == 0:
                    try:
                        service = socket.getservbyport(port, "tcp")
                    except:
                        service = "unknown"

                    output_line = f"[+] Port {port} is OPEN ({service})"
                    
                    with file_lock:
                        print(output_line)
                        results.append(f"Target: {target} | {output_line}") 
                        
        except Exception as e:
            pass

def threading_port_scan(target, strat_port, end_port):
    results.clear() 
    filename = datetime.datetime.now().strftime("scan_port_%Y%m%d_%H%M%S.txt")
    
    threads = []
    for port in range(strat_port, end_port + 1):
        t = threading.Thread(target=scanner_port, args=(target, port))
        if port not in threads:
            threads.append(t)
        t.start()

    for t in threads:
        t.join()

    if results:
        with open(filename, "a", encoding="utf-8") as f:
            for line in results:
                f.write(line + "\n")
        print(f"[!] Results saved to {filename}")
    else:
        print("[!] No open ports found.")

    print("Port scanning completed.")