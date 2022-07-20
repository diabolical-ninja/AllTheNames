"""Arabic Names from zakahmad/ArabicNameGenderFinder/.

Source:
    - https://github.com/zakahmad/ArabicNameGenderFinder
"""
import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).parent.parent))

import utils as ut  # noqa

# Source names & combine into a single DF
female_names_url = "https://raw.githubusercontent.com/zakahmad/ArabicNameGenderFinder/master/females_en.csv"  # noqa
female_names_df = pd.read_csv(female_names_url)

male_names_url = "https://raw.githubusercontent.com/zakahmad/ArabicNameGenderFinder/master/males_en.csv"  # noqa
male_names_df = pd.read_csv(male_names_url)

names_df = pd.concat([female_names_df, male_names_df])


# Select & Clean Desired Fields
colnames_dict = {"Name": "first_name", "Gender": "gender"}
names_df = names_df[list(colnames_dict.keys())]
names_df.rename(columns=colnames_dict, inplace=True)


# Restructure into the required format
names_df["gender"] = names_df["gender"].apply(ut.remap_gender)
names_df["origin"] = pd.NA


# Save
names_df.to_csv("data/arabic_names.csv", sep="|", index=False, encoding="utf-8")
