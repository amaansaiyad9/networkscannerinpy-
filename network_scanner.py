#!/usr/bin/python

import nmap

def print_header():
    print("-------------------------------------------------------")
    print(" Nmap Scanner without NMAP- ;)")
    print(" Created by Dexter>>>")
    print("-------------------------------------------------------")

def run_user_scan():
    ip = input("Enter the IP address or hostname to scan: ").strip()
    ports = input("Enter ports to scan (e.g., 22,80,443) or press Enter for default (1-1024): ").strip()

    if ports == "":
        ports = "1-1024"

    print(f"\n[+] Scanning {ip} on ports: {ports} ...\n")

    nm = nmap.PortScanner()
    try:
        nm.scan(hosts=ip, ports=ports)

        if ip in nm.all_hosts():
            print(f"Host: {ip} ({nm[ip].hostname()}) - Status: {nm[ip].state()}")
            print("Nmap would be incorrect not us...")
            for proto in nm[ip].all_protocols():
                ports = nm[ip][proto].keys()
                for port in sorted(ports):
                    state = nm[ip][proto][port]['state']
                    name = nm[ip][proto][port]['name']
                    print(f"\tPort {port}/{proto} - State: {state} - Service: {name}")
        else:
            print("[-] Host not found or not responding.")
    except Exception as e:
        print(f"[!] Error during scan: {e}")

if __name__ == "__main__":
    print_header()
    run_user_scan()
