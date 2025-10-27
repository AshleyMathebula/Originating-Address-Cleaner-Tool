"""
main.py

Main entry point for Originating Address Cleaner Tool.
Logs all activity to logs/activity.log and formats addresses as regex 1,1,<address>.
"""

from utils.file_handler import read_input_file, write_output_file
from utils.validator import clean_validate_and_format
from utils.logger import log_info, log_success, log_error

def main():
    """Main workflow: read, clean, validate, format, and write addresses."""
    input_path = "data/input_addresses.txt"
    output_path = "output/cleaned_addresses.txt"

    try:
        # Step 1: Read raw addresses
        raw_addresses = read_input_file(input_path)
        log_info(f"Loaded {len(raw_addresses)} addresses from {input_path}")

        # Step 2: Clean, validate, remove duplicates, and format
        formatted_addresses = clean_validate_and_format(raw_addresses)

        # Step 3: Write output file
        write_output_file(output_path, formatted_addresses)
        log_success(f"Cleaned addresses written to {output_path}")
        log_info(f"Final count: {len(formatted_addresses)} unique addresses")

    except FileNotFoundError as e:
        log_error(str(e))
    except Exception as e:
        log_error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
