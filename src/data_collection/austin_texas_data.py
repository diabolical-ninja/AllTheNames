"""Names Datasets from data.austintext.gov .

Sources:
 # noqa  - https://data.austintexas.gov/Health-and-Community-Services/From-Aadhav-to-Zyva-6-087-Names-of-Babies-Born-in-/rmd7-g4yz  #noqa
 # noqa  - https://data.austintexas.gov/Health-and-Community-Services/Most-Popular-Baby-Names-2008-2017-City-Of-Austin/53bh-5yzd  #noqa
"""
import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).parent.parent))

import utils as ut  # noqa

# Source 1:
baby_names_2017_df = pd.read_csv("https://data.austintexas.gov/resource/rmd7-g4yz.csv")

colnames_dict = {"name": "first_name", "sex": "gender"}

baby_names_2017_df = baby_names_2017_df[list(colnames_dict.keys())]
baby_names_2017_df.rename(columns=colnames_dict, inplace=True)

# Source 2:
baby_names_2008_2017_df = pd.read_csv(
    "https://data.austintexas.gov/resource/53bh-5yzd.csv"
)

baby_names_2008_2017_df = baby_names_2008_2017_df.melt(id_vars=["year", "rank"])

colnames_dict = {"variable": "gender", "value": "first_name"}

baby_names_2008_2017_df = baby_names_2008_2017_df[list(colnames_dict.keys())]
baby_names_2008_2017_df.rename(columns=colnames_dict, inplace=True)


# Merge into single DF & clean up columns
names_df = pd.concat([baby_names_2017_df, baby_names_2008_2017_df])

names_df["gender"] = names_df["gender"].apply(ut.remap_gender)
names_df["origin"] = "USA"


# Save
names_df.to_csv(
    "data/austin_texas_names.csv",
    sep="|",
    index=False,
    encoding="utf-8",
)
