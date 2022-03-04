"""SSA National Names.

Source:
    - https://www.ssa.gov/oact/babynames/limits.html
"""
import sys
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile

import pandas as pd
import requests

sys.path.append(str(Path(__file__).parent.parent))

import utils as ut  # noqa

# Open zip into memory
names_url = "https://www.ssa.gov/oact/babynames/names.zip"
content = requests.get(names_url)
zf = ZipFile(BytesIO(content.content))


# For each file, derive the gender & read in CSV
name_dfs = []
for item in zf.namelist():
    if ".txt" in item:
        df = pd.read_csv(zf.open(item), header=None)
        name_dfs.append(df)


# Stick into a single DF
names_df = pd.concat(name_dfs)
names_df.columns = ["first_name", "gender", "count"]
names_df.drop(columns="count", inplace=True)


# Restructure into the required format
names_df["gender"] = names_df["gender"].apply(ut.remap_gender)
names_df["origin"] = "united states of america"
names_df["definition"] = pd.NA

# Save
names_df.to_csv("data/ssa_national_names.csv", sep="|", index=False, encoding="utf-8")
