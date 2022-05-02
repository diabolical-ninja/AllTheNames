# All The Names

 [![](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/) ![t](https://img.shields.io/badge/status-maintained-yellow.svg) [![Code Hygiene](https://github.com/diabolical-ninja/AllTheNames/actions/workflows/pipeline.yml/badge.svg)](https://github.com/diabolical-ninja/AllTheNames/actions/workflows/pipeline.yml)


Dataset of people names.


### Data Structure
Found in `all_names.csv`

| Field 	| Type 	| Description 	|
|---	|---	|---	|
| First Name 	| String 	| First Name, noting some first names may be longer than 1 word	|
| Origin 	| String 	| Country or race of origin. If multiple countries/races are available they should be represented as new lines 	|
| Gender 	| String 	| *If available.*  Defined as `F`, `M`, `Other` or `NULL` |
| Definition 	| String 	| *If available.* Historical meaning of the name 	|


## How To Run

You can generate a dataset of interest from the command line via:
```bash
python src/data_collection/<generation_script_run>.py
```

To build it all (source all files & merge), run:
```bash
python all_the_names.py
```

You should see a file `names.csv` appear in the root directory.

This process will depend on your network speed but on my 2014 MBP & 50Mbps internet connection it takes roughly 2min & 50sec

## Contributions

Contributions are absolutely welcomed and encouraged. To do so, raise a PR with the new datasource and its integration into the names dataset and schema.

Ideas:
- Some datasets have a "frequency" measure of sorts. It would be cool to include that & have a mechanism to standardise/normalise the value across all datasets
- Standardise `origin` so that difference sources better match. Eg USA, United States of America, US of A, etc are all consistently presented as the same location