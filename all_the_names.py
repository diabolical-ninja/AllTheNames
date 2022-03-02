"""Create All The Names.

Merges all the various name sources together into one big CSV.
"""

import os

import pandas as pd

names_data_files = os.listdir("data/")


def read_csv(base_path: str, name: str, sep: str = "|") -> pd.DataFrame:
    """Basic wrapper on pandas read_csv method.

    Args:
        base_path (str): Path to the file
        name (str): file name & extension to read
        sep (str, optional): CSV delimiter. Defaults to "|".

    Returns:
        pd.DataFrame: The read in data
    """
    read_path = f"{base_path}/{name}"
    return pd.read_csv(read_path, sep=sep)


# Read & Merge
names_data = [read_csv("data", name) for name in names_data_files]
names_df = pd.concat(names_data)

# Save
names_df.to_csv("names.csv", sep="|", index=False, encoding="utf-8")
