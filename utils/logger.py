import os
from datetime import datetime

def log_to_txt(target, scan_type, results):
    """
    Saves results to a report. Using only the date in filename 
    to ensure all modules append to the same file.
    """
    export_dir = "exports"
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)

    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{export_dir}/report_{target}_{date_str}.txt"

    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write("\n" + "="*50 + "\n")
            f.write(f"MODULE: {scan_type}\n")
            f.write(f"TIME  : {datetime.now().strftime('%H:%M:%S')}\n")
            f.write("-" * 30 + "\n")

            if isinstance(results, list):
                for item in results:
                    f.write(f"{item}\n")
            else:
                f.write(f"{results}\n")
            
            f.write("="*50 + "\n")
        
        print(f"[+] Data appended to: {filename}")
    except Exception as e:
        print(f"[!] Logging error: {e}")