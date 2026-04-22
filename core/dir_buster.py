import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore
from utils.helpers import load_wordlist
from utils.logger import log_to_txt

def check_directory(target_url, directory):
    url = f"{target_url}/{directory}"
    try:
        response = requests.get(url, timeout=3, allow_redirects=False)
        if response.status_code == 200:
            return f"[+] Found: /{directory} (Status: 200)"
        elif response.status_code in [301, 302]:
            return f"[!] Redirect: /{directory} (Status: {response.status_code})"
    except:
        pass
    return None

def run_dir_buster(target, verbose=False):
    if not target.startswith(("http://", "https://")):
        target_url = f"http://{target}"
    else:
        target_url = target

    wordlist_path = "wordlists/common_dirs.txt"
    directories = load_wordlist(wordlist_path)
    
    if not directories: return

    print(f"{Fore.YELLOW}[*] Brute-forcing directories on {target_url}...")
    found_dirs = []

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(check_directory, target_url, d): d for d in directories}
        for future in as_completed(futures):
            res = future.result()
            if res:
                print(f"{Fore.GREEN}{res}")
                found_dirs.append(res)

    if found_dirs:
        log_to_txt(target, "Directory Brute-force", found_dirs)
    else:
        print(f"{Fore.RED}[-] No directories found.")