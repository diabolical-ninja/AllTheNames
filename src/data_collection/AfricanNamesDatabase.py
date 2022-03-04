"""AfricanNamesDatabase from Slave Voyages.

Source:
    - https://www.slavevoyages.org/documents/download/AfricanNamesDatabase.csv
"""
import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).parent.parent))

import utils as ut  # noqa

url = "https://www.slavevoyages.org/documents/download/AfricanNamesDatabase.csv"
names_df = pd.read_csv(url, sep=",", skipfooter=1, engine="python")


colnames_dict = {"name": "first_name", "sexage": "gender", "country": "origin"}

# Select the desired columns & translate
names_df = names_df[list(colnames_dict.keys())]
names_df.rename(columns=colnames_dict, inplace=True)


names_df["gender"] = names_df["gender"].apply(ut.remap_gender)


# Save
names_df["definition"] = pd.NA
names_df.to_csv("data/AfricanNamesDatabase.csv", sep="|", index=False, encoding="utf-8")
