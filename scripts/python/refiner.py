import os
import shutil
import re
import sys
import logging

def setup_logging():
    logging.basicConfig(
        filename="refiner.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def move_pdfs_to_subdirs(parent_dir: str):
    """Move PDF files into matching subdirectories based on a specific identifier in their filenames."""
    
    # Ensure the directory exists
    if not os.path.isdir(parent_dir):
        logging.error(f"Error: Directory '{parent_dir}' not found.")
        print(f"Error: Directory '{parent_dir}' not found.")
        return
    
    # Create an "_unmatched" directory if it does not exist
    unmatched_dir = os.path.join(parent_dir, "_unmatched")
    os.makedirs(unmatched_dir, exist_ok=True)
    
    # List all subdirectories
    subdirs = {d for d in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, d))}
    
    # List all PDF files in the parent directory
    pdf_files = [f for f in os.listdir(parent_dir) if f.endswith(".pdf")]
    
    # Regular expression to extract identifier from filename (supports '- FirstName LastName.pdf')
    pattern = re.compile(r"- ([A-Za-z]+ [A-Za-z]+)\.pdf")
    
    for pdf in pdf_files:
        try:
            match = pattern.search(pdf)
            if match:
                identifier = match.group(1)  # Extract matched identifier
                if identifier in subdirs:  # Check if there's a matching subdirectory
                    src = os.path.join(parent_dir, pdf)
                    dest = os.path.join(parent_dir, identifier, pdf)
                    shutil.move(src, dest)
                    logging.info(f"Moved: {pdf} -> {identifier}/")
                    print(f"Moved: {pdf} -> {identifier}/")
                else:
                    logging.warning(f"No matching directory for: {pdf}. Moving to _unmatched/")
                    print(f"No matching directory for: {pdf}. Moving to _unmatched/")
                    shutil.move(os.path.join(parent_dir, pdf), os.path.join(unmatched_dir, pdf))
            else:
                logging.warning(f"Skipping file (no match found): {pdf}. Moving to _unmatched/")
                print(f"Skipping file (no match found): {pdf}. Moving to _unmatched/")
                shutil.move(os.path.join(parent_dir, pdf), os.path.join(unmatched_dir, pdf))
        except Exception as e:
            logging.error(f"Error processing {pdf}: {str(e)}")
            print(f"Error processing {pdf}: {str(e)}")

if __name__ == "__main__":
    setup_logging()
    if len(sys.argv) != 2:
        print("Usage: python refiner.py /path/to/parent/directory")
        logging.error("Invalid usage: Missing parent directory argument.")
    else:
        move_pdfs_to_subdirs(sys.argv[1])
