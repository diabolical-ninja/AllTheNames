"""Data World - Baby Names.

Source:
    - https://data.world/alexandra/baby-names
"""
import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).parent.parent))

import utils as ut  # noqa

url = "https://query.data.world/s/pyywmosekc5zst7l5imicuuyltsumv"
names_df = pd.read_csv(url, header=None, names=["first_name", "gender"])


# Restructure into the required format
names_df["gender"] = names_df["gender"].apply(ut.remap_gender)
names_df["origin"] = pd.NA


# Save
names_df.to_csv("data/data_world_babynames.csv", sep="|", index=False, encoding="utf-8")
