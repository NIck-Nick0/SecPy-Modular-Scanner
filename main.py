import argparse
import sys

from utils.banner import print_banner
from core.port_scanner import run_port_scan
from core.web_recon import run_web_recon
from core.dir_buster import run_dir_buster
from core.sub_finder import run_sub_finder 

def main():
    print_banner()

    parser = argparse.ArgumentParser(
        description="SecPy-Modular-Scanner: tool for Recon & Security Testing",
        epilog="Usage example: python main.py -t google.com -m all"
    )

    parser.add_argument("-t", "--target", help="Target Domain (e.g., google.com)")
    parser.add_argument("-m", "--mode", choices=["ports", "web", "dir", "sub", "all"], help="Scan mode")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    if not args.target:
        print("\n[!] Error: Please specify a target using -t")
        sys.exit(1)

    try:
        if args.mode == "ports":
            run_port_scan(args.target, args.verbose)
            
        elif args.mode == "web":
            run_web_recon(args.target, args.verbose)
            
        elif args.mode == "dir":
            run_dir_buster(args.target, args.verbose)

        elif args.mode == "sub":
            run_sub_finder(args.target, args.verbose)

        elif args.mode == "all":
            print(f"[*] Running full reconnaissance on: {args.target}")
            run_sub_finder(args.target, args.verbose) # نبدأ بالـ Subdomains أولاً
            run_port_scan(args.target, args.verbose)
            run_web_recon(args.target, args.verbose)
            run_dir_buster(args.target, args.verbose)

    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user...")
        sys.exit(0)

if __name__ == "__main__":
    main()