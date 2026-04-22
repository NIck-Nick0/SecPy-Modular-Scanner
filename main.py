import argparse
import sys

from utils.banner import print_banner
from core.port_scanner import run_port_scan
from core.web_recon import run_web_recon

def main():
    print_banner()

    parser = argparse.ArgumentParser(
        description="SecPy-Modular-Scanner: tool for Recon & Security Testing",
        epilog="Usage example: python main.py -t 192.168.1.1 -m ports"
    )

    parser.add_argument("-t", "--target", help="Target IP address or Domain (e.g., 192.168.1.1 or google.com)")
    parser.add_argument("-m", "--mode", choices=["ports", "web", "all"], help="Scanning mode: ports, web, or all")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output for more details")

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    if not args.target:
        print("\n[!] Error: Please specify a target using -t or --target")
        sys.exit(1)

    try:
        if args.mode == "ports":
            print(f"[*] Starting Port Scan on: {args.target}")
            run_port_scan(args.target, args.verbose)
            
        elif args.mode == "web":
            print(f"[*] Starting Web Recon on: {args.target}")
            run_web_recon(args.target, args.verbose)
            
        elif args.mode == "all":
            run_port_scan(args.target, args.verbose)
            run_web_recon(args.target, args.verbose)
            
        else:
            print("[!] Please specify a mode (-m ports or -m web)")

    except KeyboardInterrupt:
        print("\n Scan interrupted ...")
        sys.exit(0)

if __name__ == "__main__":
    main()