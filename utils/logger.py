import os
from datetime import datetime

def log_to_txt(target, scan_type, results):
    """
    Saves the scan results into a formatted .txt file.
    """
    # Ensure the exports directory exists
    export_dir = "exports"
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)

    # Create a filename based on the target and current date
    # Example: scan_google.com_2024-05-20.txt
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{export_dir}/scan_{target}_{date_str}.txt"

    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write("="*50 + "\n")
            f.write(f"SEC-PY SCAN REPORT\n")
            f.write(f"Target: {target}\n")
            f.write(f"Scan Type: {scan_type}\n")
            f.write(f"Date/Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*50 + "\n\n")

            if isinstance(results, list):
                for item in results:
                    f.write(f"{item}\n")
            else:
                f.write(f"{results}\n")

            f.write("\n" + "="*50 + "\n")
            f.write("End of Report\n")
        
        print(f"\n[+] Results successfully saved to: {filename}")
    except Exception as e:
        print(f"\n[!] Failed to save log: {e}")