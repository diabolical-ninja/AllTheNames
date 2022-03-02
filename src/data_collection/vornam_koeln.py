"""Get Names from Vornam Koeln.

Sources:
    - Official Source: https://offenedaten-koeln.de/
    - Download Samples: https://github.com/fxnn/vornamen
"""

import pandas as pd

urls = [
    "https://offenedaten-koeln.de/sites/default/files/Vornamen_Koeln_2017.csv",
    "https://offenedaten-koeln.de/sites/default/files/Vornamen_Koeln_2016.csv",
    "https://offenedaten-koeln.de/sites/default/files/Vornamen_Koeln_2015.csv",
    "https://offenedaten-koeln.de/sites/default/files/Vornamensstatistik_2014_0.csv",
    "https://offenedaten-koeln.de/sites/default/files/Vornamen_Koeln_2013.csv",
    "https://offenedaten-koeln.de/sites/default/files/Vornamen_Koeln_2012.csv",
    "https://offenedaten-koeln.de/sites/default/files/Vornamen_Koeln_2011.csv",
    "https://offenedaten-koeln.de/sites/default/files/Vornamen_Koeln_2010.csv",
]


names_dfs = []
for url in urls:

    # The files aren't consistent with their delimiter selection
    # Some use comma & others a semi-colon
    df = pd.read_csv(url, sep=";")
    if df.shape[1] == 1:
        df = pd.read_csv(url, sep=",")

    # Translation mapping from German to English
    colnames_dict = {
        "vorname": "first_name",
        "geschlecht": "gender",
    }

    # Select the desired columns & translate
    df = df[list(colnames_dict.keys())]
    df.rename(columns=colnames_dict, inplace=True)

    names_dfs.append(df)

# Combine all
names_df = pd.concat(names_dfs)

# Restructure into the required format
names_df["origin"] = "germany"
names_df["definition"] = pd.NA


# Save
names_df.to_csv(
    "data/vornam_koeln_names.csv", sep="|", index=False, encoding="utf-8"
)
