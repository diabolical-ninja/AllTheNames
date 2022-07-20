"""Firstnames Database from Github User MatthiasWinkelmann.

Source:
    - https://github.com/MatthiasWinkelmann/firstname-database
"""
import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).parent.parent))

import utils as ut  # noqa

names_url = "https://raw.githubusercontent.com/MatthiasWinkelmann/firstname-database/master/firstnames.csv"  # noqa
names_df = pd.read_csv(names_url, sep=";")

# Original format is wide, with a column for each country. Normalise
names_df = pd.melt(names_df, id_vars=["name", "gender"])

# Remap column names
colnames_dict = {
    "name": "first_name",
    "gender": "gender",
    "variable": "origin",
}

names_df = names_df[list(colnames_dict.keys())]
names_df.rename(columns=colnames_dict, inplace=True)

names_df["gender"] = names_df["gender"].apply(ut.remap_gender)

# Save
names_df.to_csv(
    "data/MatthiasWinkelmann_firstname_database.csv",
    sep="|",
    index=False,
    encoding="utf-8",
)
