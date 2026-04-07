from core.scanner_port import threading_port_scan
from core.scanner_ip import threading_ip_scan

def option_name():
    print("-"*40)
    print("[1]:Sacnner Port/Port Service")
    print("[2]:Scanner IP/local")
    print("[3]:Exit")
    print("-"*40)
    

def run_port_scanner():
    try:
        target = input("Enter Target IP: ")
        start_port = int(input("Enter Start Port: "))
        end_port = int(input("Enter End Port: "))
        
        print(f"\n[!] Scanning {target}...")
        threading_port_scan(target, start_port, end_port)
        
    except ValueError:
        print("\n[Error] Invalid input. Please enter numbers for ports.")
        
    input("\nPress Enter to return to menu...")


def run_ip_scanner():
    try:
        target = input("Enter Target IP: ")
        print(f"\n[!] Scanning {target}...")
        threading_ip_scan(target)
    except  ValueError:
         print("\n[Error] Invalid input. Please enter numbers for ports.")

    input("\nPress Enter to return to menu...")