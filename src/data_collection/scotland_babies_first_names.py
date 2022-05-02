"""Scotland - Babies First Names.

Source:
 # noqa  - https://www.nrscotland.gov.uk/statistics-and-data/statistics/statistics-by-theme/vital-events/names/babies-first-names/babies-first-names-summary-records-comma-separated-value-csv-format
"""
import sys
from pathlib import Path
from urllib.request import Request, urlopen

import pandas as pd

sys.path.append(str(Path(__file__).parent.parent))

import utils as ut  # noqa

# Trick site into thinking it's a browser
url = "https://www.nrscotland.gov.uk/files//statistics/babies-names/20/babies-first-names-all-names-all-years.csv"  # noqa
req = Request(url)
req.add_header(
    "User-Agent",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0",
)
content = urlopen(req)

# Read data
names_df = pd.read_csv(content)


# Select the desired columns & update
colnames_dict = {"FirstForename": "first_name", "sex": "gender"}
names_df = names_df[list(colnames_dict.keys())]
names_df.rename(columns=colnames_dict, inplace=True)


# Restructure into the required format
names_df["gender"] = names_df["gender"].apply(ut.remap_gender)
names_df["origin"] = "scotland"
names_df["definition"] = pd.NA

# Save
names_df.to_csv(
    "data/scotland_babies_first_names.csv", sep="|", index=False, encoding="utf-8"
)
