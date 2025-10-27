"""
formatter.py

Formats cleaned originating addresses into the target system format:
- Standard: regex 1,1,<address>
- Pattern: if the address contains '?*', it becomes regex 1,1,<address>[0-9]*
"""

from typing import List


def format_address(address: str) -> str:
    """
    Format a single cleaned address for upload.
    Automatically detects '?*' and converts it into a regex pattern.

    Args:
        address (str): Cleaned originating address.

    Returns:
        str: Formatted string ready for upload.
    """
    if not address:
        raise ValueError("[ERROR] Address cannot be empty.")

    if "?*" in address:
        # Remove '?*' from the address and append regex pattern
        address_cleaned = address.replace("?*", "")
        return f"regex 1,1,{address_cleaned}[0-9]*"
    else:
        return f"regex 1,1,{address}"


def format_addresses(addresses: List[str]) -> List[str]:
    """
    Format a list of addresses using format_address().

    Args:
        addresses (List[str]): List of cleaned originating addresses.

    Returns:
        List[str]: List of formatted addresses.
    """
    return [format_address(addr) for addr in addresses]



