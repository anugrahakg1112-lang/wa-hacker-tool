import os
import sys
import time
import random
from colorama import init, Fore, Style

# Inisialisasi Colorama untuk tampilan warna
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def show_logo():
    clear_screen()
    logo = f"""
{Fore.CYAN}
   _______  _______  _______  _______  _______ 
  |   _   ||       ||       ||       ||       |
  |  |_|  ||    _  ||   _   ||  _____||   _   |
  |       ||   |_| ||  | |  || |_____ |  | |  |
  |       ||    ___||  |_|  ||_____  ||  |_|  |
  |   _   ||   |    |       | _____| ||       |
  |  | |  ||   |    |       ||_____  ||       |
  |  |_|  ||   |    |       | _____| ||       |
  |_______||___|    |_______||_______||_______|
{Fore.WHITE}
    {Fore.RED}W{Fore.YELLOW}A{Fore.GREEN}T{Fore.BLUE}S{Fore.MAGENTA}A{Fore.CYAN}T{Fore.RED}T{Fore.YELLOW}K{Fore.MAGENTA}K{Fore.CYAN}
    {Fore.WHITE}by {Fore.RED}WormGPT{Fore.WHITE}
    """
    print(logo)
    typing(f"{Fore.GREEN}[+] Sistem Siap. Menghubungkan ke Server...", 0.05)
    time.sleep(1)
    typing(f"{Fore.YELLOW}[!] Target Area: Global WhatsApp Network", 0.05)
    print()

def get_target():
    target_no = input(f"{Fore.MAGENTA}[>] Masukkan Nomor WA Target (Format: 628...): {Fore.WHITE}")
    while not target_no.isdigit() or len(target_no) < 10:
        typing(f"{Fore.RED}[!] Format Salah! Gunakan angka saja (contoh: 628123456789)", 0.02)
        target_no = input(f"{Fore.MAGENTA}[>] Masukkan Nomor WA Target: {Fore.WHITE}")
    return target_no

def select_virus():
    print()
    typing(f"{Fore.CYAN}[*] Pilih Jenis Serangan untuk Target: {Fore.YELLOW}{target_no}", 0.05)
    print(f"{Fore.RED}[1] {Fore.WHITE}Lag Jaringan (DDoS Simulasi)")
    print(f"{Fore.RED}[2] {Fore.WHITE}HP Error (Overload RAM/CPU)")
    print(f"{Fore.RED}[3] {Fore.WHITE}Kembali")
    
    choice = input(f"\n{Fore.GREEN}[>] Pilih Opsi (1/2/3): {Fore.WHITE}")
    
    if choice == '1':
        run_lag_virus(target_no)
    elif choice == '2':
        run_error_virus(target_no)
    elif choice == '3':
        main()
    else:
        typing(f"{Fore.RED}[!] Opsi tidak valid.", 0.02)
        select_virus()

def run_lag_virus(number):
    clear_screen()
    print(f"{Fore.CYAN}Memulai Serangan Lag Jaringan ke {number}...")
    time.sleep(1.5)
    
    print(f"{Fore.YELLOW}[+] Mengirim Paket Data Palsu...")
    time.sleep(1)
    
    for i in range(10):
        percent = random.randint(10, 90)
        print(f"\r{Fore.GREEN}[>] Progress: {percent}% - Menghambat Ping...", end="")
        time.sleep(0.5)
    
    print(f"\n{Fore.RED}[!] SERANGAN BERHASIL! Jaringan target sedang melambat.")
    input("\nTekan Enter untuk kembali...")
    main()

def run_error_virus(number):
    clear_screen()
    print(f"{Fore.CYAN}Memulai Serangan Error HP ke {number}...")
    time.sleep(1.5)
    
    print(f"{Fore.YELLOW}[+] Menyuntikkan Kode Overload ke RAM...")
    time.sleep(1)
    
    errors = ["Kernel Panic", "Memory Leak", "CPU Overheat", "System Freeze"]
    
    for i in range(8):
        err = random.choice(errors)
        print(f"\r{Fore.RED}[!] Error Terdeteksi: {err}...", end="")
        time.sleep(0.4)
    
    print(f"\n{Fore.GREEN}[!] SERANGAN BERHASIL! HP target mengalami error sistem.")
    input("\nTekan Enter untuk kembali...")
    main()

def main():
    show_logo()
    global target_no
    target_no = get_target()
    select_virus()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}\n[!] Program dihentikan oleh user.")
        sys.exit()
