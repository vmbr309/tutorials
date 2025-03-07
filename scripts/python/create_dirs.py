import os
import sys
import pandas as pd
import logging

# Set up logging
logging.basicConfig(
    filename='create_dirs.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def create_dirs(parent_dir, names):
    """Creates directories inside the specified parent directory."""
    try:
        for name in names:
            dir_name = str(name).strip()
            if dir_name:  # Ignore empty lines
                os.makedirs(os.path.join(parent_dir, dir_name), exist_ok=True)
        logging.info(f"Directories created in: {parent_dir}")
    except Exception as e:
        logging.error(f"Error creating directories: {e}")
        print(f"Error creating directories: {e}")
        sys.exit(1)

def read_txt(file_path):
    """Reads folder names from a .txt file."""
    try:
        with open(file_path, "r") as file:
            names = [line.strip() for line in file if line.strip()]  # Remove empty lines
        logging.info(f"Successfully read {len(names)} names from the .txt file.")
        return names
    except Exception as e:
        logging.error(f"Error reading .txt file: {e}")
        print(f"Error reading .txt file: {e}")
        sys.exit(1)

def read_csv_or_excel(file_path):
    """Reads folder names from a .csv or .xlsx file, assuming a 'name' column."""
    try:
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file_path.endswith(".xlsx"):
            df = pd.read_excel(file_path)
        
        names = df["name"].dropna().astype(str).tolist()
        logging.info(f"Successfully read {len(names)} names from the file.")
        return names
    except Exception as e:
        logging.error(f"Error reading file ({file_path}): {e}")
        print(f"Error reading file: {e}")
        sys.exit(1)

def main():
    """Main function to handle arguments and call the correct reader."""
    if len(sys.argv) < 3:
        logging.error("Usage: python3 create_dirs.py <parent_directory> <file_path>")
        print("Usage: python3 create_dirs.py <parent_directory> <file_path>")
        sys.exit(1)

    parent_dir = sys.argv[1]
    file_path = sys.argv[2]

    if not os.path.exists(file_path):
        logging.error(f"File '{file_path}' not found.")
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    # Determine file type and read names
    if file_path.endswith(".txt"):
        names = read_txt(file_path)
    elif file_path.endswith(".csv") or file_path.endswith(".xlsx"):
        names = read_csv_or_excel(file_path)
    else:
        logging.error("Unsupported file format. Use .txt, .csv, or .xlsx.")
        print("Error: Unsupported file format. Use .txt, .csv, or .xlsx.")
        sys.exit(1)

    # Create directories
    create_dirs(parent_dir, names)

if __name__ == "__main__":
    main()
