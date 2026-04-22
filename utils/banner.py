from colorama import Fore, Style, init

init(autoreset=True)

def print_banner():
    banner = f"""
    {Fore.GREEN}
    ███████╗███████╗ ██████╗██████╗ ██╗   ██╗
    ██╔════╝██╔════╝██╔════╝██╔══██╗╚██╗ ██╔╝
    ███████╗█████╗  ██║     ██████╔╝ ╚████╔╝ 
    ╚════██║██╔══╝  ██║     ██╔═══╝   ╚██╔╝  
    ███████║███████╗╚██████╗██║        ██║   
    ╚══════╝╚══════╝ ╚═════╝╚═╝        ╚═╝   
    {Fore.CYAN}--- SecPy Modular Scanner | SOC Analyst Edition ---
    """
    print(banner)