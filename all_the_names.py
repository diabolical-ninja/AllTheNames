"""Create All The Names.

Merges all the various name sources together into one big CSV.
"""
import os

import pandas as pd


def build_data_sources() -> None:
    """Execute all the data sourcing scripts.

    Output expected to be in data/ folder
    """
    location = "src/data_collection"
    data_source_generators = os.listdir(location)
    data_source_generators = [x for x in data_source_generators if x.endswith(".py")]

    for source_generator in data_source_generators:
        print(f"Executing: {source_generator}")
        try:
            os.system(f"python {location}/{source_generator}")

        except:  # noqa
            print(f"FAILED: {source_generator}")


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
    return pd.read_csv(read_path, sep=sep, encoding="utf-8")


def merge_data_sources(data_location: str = "data/") -> None:
    """Takes all name data files & merges+cleans into a single file.

    Args:
        data_location (str, optional): Directory containing all files to merge
            - Defaults to "data/".
    """
    # Identify all generated files
    names_data_files = os.listdir(data_location)
    names_data_files = [x for x in names_data_files if x.endswith(".csv")]
    print(f"Found {len(names_data_files)} name source files to merge")

    # Read & Merge
    names_data = [read_csv("data", name) for name in names_data_files]
    names_df = pd.concat(names_data)

    # Clean up values & remove duplicates
    names_df["first_name"] = names_df["first_name"].str.strip().str.lower()
    names_df["origin"] = names_df["origin"].str.strip().str.lower()
    names_df.drop_duplicates(inplace=True)

    print("Stats:")
    print("===================")
    print(f"{names_df.size} entries present")
    print(f"{names_df['first_name'].unique().size} unique names")
    print(f"{names_df['origin'].unique().size} unique origins")

    # Save
    names_df.to_csv("names.csv", sep="|", index=False, encoding="utf-8")


if __name__ == "__main__":
    build_data_sources()
    merge_data_sources()
