"""Given Names from Github User Mbejda.

Source:
    - https://gist.github.com/mbejda
"""

import pandas as pd

urls = [
    "https://gist.githubusercontent.com/mbejda/7f86ca901fe41bc14a63/raw/38adb475c14a3f44df9999c1541f3a72f472b30d/Indian-Male-Names.csv",  # noqa
    "https://gist.githubusercontent.com/mbejda/9b93c7545c9dd93060bd/raw/b582593330765df3ccaae6f641f8cddc16f1e879/Indian-Female-Names.csv",  # noqa
    "https://gist.githubusercontent.com/mbejda/1e77ee4ad268916142a6/raw/22d1b475217be7240aba54c1a1b545557d624ba8/Hispanic-Female-Names.csv",  # noqa
    "https://gist.githubusercontent.com/mbejda/21fbbfe24efd2a114800/raw/52db651f79a716c87b21ef06c224ff443cb41f06/Hispanic-Male-Names.csv",  # noqa
    "https://gist.githubusercontent.com/mbejda/61eb488cec271086632d/raw/6340b8045b28c2abc0b1d44cfbc80f40284ef890/Black-Male-Names.csv",  # noqa
    "https://gist.githubusercontent.com/mbejda/9dc89056005a689a6456/raw/bb6ef2375f1289d0ef10dbd8e9469670ac23ceab/Black-Female-Names.csv",  # noqa
    "https://gist.githubusercontent.com/mbejda/6c2293ba3333b7e76269/raw/60aa0c95e8ee9b11b915a26f47480fef5c3203ed/White-Male-Names.csv",  # noqa
    "https://gist.githubusercontent.com/mbejda/26ad0574eda7fca78573/raw/6936d1a8f5fa5220f2f60a51a06a35b172c50f93/White-Female-Names.csv",  # noqa
]


names_dfs = []
for url in urls:

    df = pd.read_csv(url, sep=",")

    # Map to standardised column names
    colnames_dict = {
        "first name": "first_name",
        "name": "first_name",
        "gender": "gender",
        "race": "origin",
    }

    # White spaces at the start & end are present some column names.
    # Remove them.
    df.columns = [x.strip() for x in df.columns]

    # Select the desired columns & standardise the names
    desired_names = [x for x in colnames_dict.keys() if x in df.columns]
    df = df[desired_names]
    df.rename(columns=colnames_dict, inplace=True)

    names_dfs.append(df)

# Combine all
names_df = pd.concat(names_dfs)

# Restructure into the required format
names_df["definition"] = pd.NA

# Save
names_df.to_csv("data/mbejda_names.csv", sep="|", index=False, encoding="utf-8")
