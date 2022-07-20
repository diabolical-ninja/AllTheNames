"""List of Names Dataset.

Source:
    - https://www.back4app.com/database/back4app/list-of-names-dataset
"""
import json
import sys
from pathlib import Path

import pandas as pd
import requests

sys.path.append(str(Path(__file__).parent.parent))

import utils as ut  # noqa

url = "https://parseapi.back4app.com/classes/Complete_List_Names?limit=1000000"
headers = {
    "X-Parse-Application-Id": "zsSkPsDYTc2hmphLjjs9hz2Q3EXmnSxUyXnouj1I",  # noqa  # This is the fake app's application id
    "X-Parse-Master-Key": "4LuCXgPPXXO2sU5cXm6WwpwzaKyZpo3Wpj4G4xXK",  # noqa  # This is the fake app's readonly master key
}
names = json.loads(
    requests.get(url, headers=headers).content.decode("utf-8")
)  # Here you have the data that you need

# Convert to DF & clean into the desired format
names_df = pd.DataFrame(names["results"])

colnames_dict = {"Gender": "gender", "Name": "first_name"}
names_df = names_df[list(colnames_dict.keys())]
names_df.rename(columns=colnames_dict, inplace=True)

names_df["gender"] = names_df["gender"].apply(ut.remap_gender)
names_df["origin"] = pd.NA


# Save
names_df.to_csv("data/names_dataset.csv", sep="|", index=False, encoding="utf-8")
