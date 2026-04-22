import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore
from utils.helpers import load_wordlist
from utils.logger import log_to_txt

def check_subdomain(target_domain, sub):
    """
    Attempts to resolve a subdomain and returns the result if found.
    """
    full_domain = f"{sub}.{target_domain}"
    try:
        # Resolve domain to IP
        ip = socket.gethostbyname(full_domain)
        result = f"[+] Found: {full_domain} ({ip})"
        print(f"{Fore.GREEN}{result}")
        return result
    except (socket.gaierror, socket.timeout):
        return None

def run_sub_finder(target, verbose=False):
    """
    Main function to run subdomain discovery using threads.
    """
    wordlist_path = "wordlists/subdomains.txt"
    subs = load_wordlist(wordlist_path)

    if not subs:
        print(f"{Fore.RED}[!] Error: No subdomains found in {wordlist_path}")
        return

    print(f"{Fore.YELLOW}[*] Enumerating subdomains for {target}...")
    
    found_subs = []

    # Using 50 threads for fast DNS lookups
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(check_subdomain, target, sub): sub for sub in subs}
        
        for future in as_completed(futures):
            res = future.result()
            if res:
                found_subs.append(res)

    if found_subs:
        log_to_txt(target, "Subdomain Discovery", found_subs)
    else:
        print(f"{Fore.RED}[-] No subdomains found.")

    print(f"\n{Fore.CYAN}[*] Subdomain discovery finished.")