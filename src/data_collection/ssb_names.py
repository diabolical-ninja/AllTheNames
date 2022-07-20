"""Top Names from 1880-2018 from SSB (Statistics Norway).

Source:
    - https://www.ssb.no/en/befolkning/navn/statistikk/navn
"""
import pandas as pd

# Source datasets
female_names_url = "https://www.ssb.no/eksport/tabell.csv?key=375474"
female_names_df = pd.read_csv(female_names_url, sep=";")

male_names_url = "https://www.ssb.no/eksport/tabell.csv?key=375475"
male_names_df = pd.read_csv(male_names_url, sep=";")

female_names_df["gender"] = "f"
male_names_df["gender"] = "m"

# Combine all
names_df = pd.concat([female_names_df, male_names_df])

# Pivot to a normalised form
names_df = names_df.melt(id_vars=["gender", "\xa0"])

# Remap columns to standard names
colnames_dict = {"gender": "gender", "value": "first_name"}

names_df = names_df[list(colnames_dict.keys())]
names_df.rename(columns=colnames_dict, inplace=True)

# Restructure into the required format
names_df["origin"] = "norway"

# Save
names_df.to_csv("data/ssb_names.csv", sep="|", index=False, encoding="utf-8")
