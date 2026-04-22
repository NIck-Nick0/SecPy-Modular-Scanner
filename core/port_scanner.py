import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore
from utils.helpers import load_wordlist
from utils.logger import log_to_txt

def get_banner(s):
    """
    Attempts to grab the service banner from an open socket.
    """
    try:
        return s.recv(1024).decode().strip()
    except:
        return None

def scan_port(target, port, verbose=False):
    """
    Connects to a port and attempts to grab the service banner.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.5) 
        result = s.connect_ex((target, int(port)))
        
        if result == 0:
            banner = get_banner(s)
            service_info = f"[+] Port {port} is OPEN"
            if banner:
                service_info += f" | Banner: {banner}"
            
            print(f"{Fore.GREEN}{service_info}")
            s.close()
            return service_info
        
        elif verbose:
            print(f"{Fore.RED}[- ] Port {port} is CLOSED")
        
        s.close()
    except Exception:
        pass
    return None

def run_port_scan(target, verbose=False):
    """
    Executes the scan and logs the results including service banners.
    """
    wordlist_path = "wordlists/common_ports.txt"
    ports = load_wordlist(wordlist_path)
    
    if not ports:
        ports = [21, 22, 80, 443, 3389] 

    print(f"{Fore.YELLOW}[*] Initializing Banner Grabbing scan on {target}...")
    
    open_ports_found = []

    with ThreadPoolExecutor(max_workers=50) as executor:
        future_to_port = {executor.submit(scan_port, target, port, verbose): port for port in ports}
        
        for future in as_completed(future_to_port):
            result = future.result()
            if result:
                open_ports_found.append(result)

    if open_ports_found:
        log_to_txt(target, "Port Scan with Banner Grabbing", open_ports_found)
            
    print(f"\n{Fore.CYAN}[*] Port scan finished.")