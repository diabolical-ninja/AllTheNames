"""CMU Artificial Intelligence Repository Names

Source:
    - https://www.cs.cmu.edu/Groups/AI/util/areas/nlp/corpora/names/0.html
"""
import pandas as pd

males_url = "https://www.cs.cmu.edu/Groups/AI/util/areas/nlp/corpora/names/male.txt"
females_url = "https://www.cs.cmu.edu/Groups/AI/util/areas/nlp/corpora/names/female.txt"

# Source data & combine
males_df = pd.read_csv(males_url)
females_df = pd.read_csv(females_url)

males_df.columns = ["first_name"]
females_df.columns = ["first_name"]

males_df["gender"] = "m"
females_df["gender"] = "f"

names_df = pd.concat([males_df, females_df])

# The files start with a header explaining the T&C's of usage
# They're identified with the # symbol
names_df = names_df[~names_df["first_name"].str.startswith("#")]

# Fill out the schema
names_df["origin"] = pd.NA
names_df["definition"] = pd.NA


# Save
names_df.to_csv(
    "data/CMU_Artificial_Intelligence_Repository_names.csv",
    sep="|",
    index=False,
    encoding="utf-8",
)
