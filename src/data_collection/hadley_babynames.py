"""Given Names from Github Repo Hadley/data-baby-names.

Source:
    - https://github.com/hadley/data-baby-names
"""
import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).parent.parent))

import utils as ut  # noqa

names_url = (
    "https://raw.githubusercontent.com/hadley/data-baby-names/master/baby-names.csv"
)
names_df = pd.read_csv(names_url, sep=",")

colnames_dict = {"name": "first_name", "sex": "gender"}

names_df = names_df[list(colnames_dict.keys())]
names_df.rename(columns=colnames_dict, inplace=True)


# Restructure into the required format
names_df["gender"] = names_df["gender"].apply(ut.remap_gender)
names_df["origin"] = pd.NA


# Save
names_df.to_csv(
    "data/hadley_data_baby_names.csv", sep="|", index=False, encoding="utf-8"
)
