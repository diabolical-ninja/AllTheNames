"""General Utilities for Name Collection."""


def remap_gender(gender: str) -> str:
    """Map gender to standard notation.

    Args:
        gender (str): Original gender, eg male, girl, etc

    Returns:
        str: m, f or other
    """
    if not isinstance(gender, str):
        return "other"

    gender = gender.strip().lower()
    if gender in ["man", "male", "boy"]:
        return "m"
    elif gender in ["woman", "female", "girl"]:
        return "f"
    else:
        return "other"
