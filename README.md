# All The Names
Dataset of all people names.


### Data Structure
Found in `all_names.csv`

| Field 	| Type 	| Description 	|
|---	|---	|---	|
| First Name 	| String 	| First Name 	|
| Origin 	| String 	| Country or race of origin. If multiple countries/races are available they should be represented as new lines 	|
| Gender 	| String 	| *If available.*  Defined as `F`, `M`, `Other` or `NULL` |
| Definition 	| String 	| Historical meaning of the name 	|


## How To Run

You can generate a dataset of interest from the command line via:
```bash
python src/data_collection/<generation_script_run>.py
```

Once you have the desired data sources you can combine them via:
```bash
python all_the_names.py
```

You should see a file `names.csv` appear in the root directory.

## Contributions

Contributions are absolutely welcomed and encouraged. To do so, raise a PR with the new datasource and its integration into the names dataset and schema.

Ideas:
- Some datasets have a "frequency" measure of sorts. It would be cool to include that & have a mechanism to standardise/normalise the value across all datasets