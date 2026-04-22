import os

def load_wordlist(file_path):
    """
    Reads a file and returns a list of lines, 
    stripping whitespace and removing empty lines.
    """
    if not os.path.exists(file_path):
        return []
        
    with open(file_path, "r") as f:
        # Read lines and convert to integer if they are port numbers
        lines = [line.strip() for line in f.readlines() if line.strip()]
        return lines