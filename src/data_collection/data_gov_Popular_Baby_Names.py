"""Popular Baby Names.

Source:
    - https://data.gov.au/dataset/ds-sa-9849aa7f-e316-426e-8ab5-74658a62c7e6/details
"""
from io import BytesIO
from zipfile import ZipFile

import pandas as pd
import requests

# Open zip into memory
names_url = "https://data.sa.gov.au/data/dataset/9849aa7f-e316-426e-8ab5-74658a62c7e6/resource/534d13f2-237c-4448-a6a3-93c07b1bb614/download/baby-names-1944-2013.zip"
content = requests.get(names_url)
zf = ZipFile(BytesIO(content.content))

# For each file, derive the gender & read in CSV
name_dfs = []
for item in zf.namelist():
    gender = "f" if "female" in item else "m"
    df = pd.read_csv(zf.open(item))
    df["gender"] = gender
    name_dfs.append(df)

# Stick into a single DF
names_df = pd.concat(name_dfs)

# Update & Select Desired Fields
colnames_dict = {"Given Name": "first_name", "gender": "gender"}
names_df = names_df[list(colnames_dict.keys())]
names_df.rename(columns=colnames_dict, inplace=True)


# Restructure into the required format
names_df["origin"] = "australia"
names_df["definition"] = pd.NA

# Save
names_df.to_csv("data/popular_baby_names.csv", sep="|", index=False, encoding="utf-8")
