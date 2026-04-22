import requests
from colorama import Fore
from utils.logger import log_to_txt

def check_security_headers(headers):
    """
    Analyzes HTTP headers and returns a list of security findings.
    """
    security_headers = [
        "X-Frame-Options", 
        "Content-Security-Policy", 
        "X-Content-Type-Options", 
        "Strict-Transport-Security"
    ]
    
    findings = []
    findings.append("[*] Security Headers Analysis:")
    
    for header in security_headers:
        if header in headers:
            findings.append(f"[+] {header}: Found")
        else:
            findings.append(f"[-] {header}: Missing")
    
    return findings

def run_web_recon(target, verbose=False):
    """
    Performs web reconnaissance and logs the findings to a TXT file.
    """
    # Ensure the target has a protocol
    if not target.startswith(("http://", "https://")):
        url = f"http://{target}"
    else:
        url = target

    print(f"{Fore.YELLOW}[*] Starting Web Reconnaissance on {url}...")
    
    web_findings = []
    web_findings.append(f"Target URL: {url}")

    try:
        user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) SecPyScanner/1.0'}
        response = requests.get(url, timeout=5, headers=user_agent)
        
        status_info = f"[+] Status Code: {response.status_code}"
        print(f"{Fore.GREEN}{status_info}")
        web_findings.append(status_info)
        
        server = response.headers.get("Server", "Unknown")
        server_info = f"[+] Server: {server}"
        print(f"{Fore.GREEN}{server_info}")
        web_findings.append(server_info)

        if verbose:
            print(f"\n{Fore.WHITE}--- Raw Headers ---")
            for key, value in response.headers.items():
                print(f"{key}: {value}")
            print(f"--- End of Raw Headers ---\n")

        header_results = check_security_headers(response.headers)
        for line in header_results:
            if "Found" in line:
                print(f"{Fore.GREEN}{line}")
            elif "Missing" in line:
                print(f"{Fore.RED}{line}")
            else:
                print(line)
            web_findings.append(line)

        if web_findings:
            log_to_txt(target, "Web Reconnaissance", web_findings)

    except requests.exceptions.RequestException as e:
        error_msg = f"[!] Web Recon Failed: {e}"
        print(f"{Fore.RED}{error_msg}")
        log_to_txt(target, "Web Recon Error", [error_msg])

    print(f"\n{Fore.CYAN}[*] Web reconnaissance completed.")