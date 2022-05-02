"""Given Names from Github Repo SwedishData/personal-names.

Source:
    - https://github.com/swedishdata/personal-names
"""

import pandas as pd

column_names = ["first_name"]

female_names_url = "https://raw.githubusercontent.com/swedishdata/personal-names/master/female-first-names.csv"  # noqa
female_names_df = pd.read_csv(female_names_url, header=None, names=column_names)

male_names_url = "https://raw.githubusercontent.com/swedishdata/personal-names/master/male-first-names.csv"  # noqa
male_names_df = pd.read_csv(male_names_url, header=None, names=column_names)

female_names_df["gender"] = "f"
male_names_df["gender"] = "m"


# Combine all
names_df = pd.concat([female_names_df, male_names_df])

# Restructure into the required format
names_df["origin"] = "sweden"
names_df["definition"] = pd.NA

# Save
names_df.to_csv(
    "data/swedishdata_personalnames.csv", sep="|", index=False, encoding="utf-8"
)
