"""AfricanNamesDatabase from Slave Voyages.

Source:
    - https://www.slavevoyages.org/documents/download/AfricanNamesDatabase.csv
"""

import pandas as pd


url = "https://www.slavevoyages.org/documents/download/AfricanNamesDatabase.csv"
names_df = pd.read_csv(url, sep=",", skipfooter=1, engine="python")


colnames_dict = {"name": "first_name", "sexage": "gender", "country": "origin"}

# Select the desired columns & translate
names_df = names_df[list(colnames_dict.keys())]
names_df.rename(columns=colnames_dict, inplace=True)


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


names_df["gender"] = names_df["gender"].apply(remap_gender)


# Save
names_df["definition"] = pd.NA
names_df.to_csv("data/AfricanNamesDatabase.csv", sep="|", index=False, encoding="utf-8")
