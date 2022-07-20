# All The Names

[![Code Hygiene](https://github.com/diabolical-ninja/AllTheNames/actions/workflows/pipeline.yml/badge.svg)](https://github.com/diabolical-ninja/AllTheNames/actions/workflows/pipeline.yml)
<br/>

[![](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
![t](https://img.shields.io/badge/status-maintained-yellow.svg)
![black codestyle](https://img.shields.io/badge/Code%20Style-Black-black)
<br/>


Collection of various names datasets.


## The Data

There are currently 15 sources which produces:

| Item     | Count |
|----------------|------------|
| Total Rows     | 14,607,135 |
| Unique Names   | 289,755    |
| Unique Origins | 623        |


There is no guarantee of the accuracy of the data, ie the associated gender & origin, as it will vary (significantly) source to source. 

To use the data you can read it straight from github into `pandas`:
```python
import pandas as pd

names_df = pd.read_csv("https://raw.githubusercontent.com/diabolical-ninja/AllTheNames/main/names.csv", sep = "|")
```

### Structure
Found in `names.csv`

| Field 	| Type 	| Description 	|
|---	|---	|---	|
| First Name 	| String 	| First Name, noting some first names may be longer than 1 word	|
| Origin 	| String 	| Country, classification or race of origin. If multiple countries/classification/races are available they should be represented as new lines 	|
| Gender 	| String 	| *If available.*  Defined as `F`, `M`, `Other` or `NULL` |



## How To Run

This project uses [poetry](https://python-poetry.org/) for dependency management. This assumes `python 3.9+`. It may well work for lower versions but has not been tested.

First setup the environment by running:
```bash
poetry install
```

You can then generate a dataset of interest from the command line via:
```bash
poetry run python src/data_collection/<generation_script_run>.py
```

To build all sources, run:
```bash
poetry run python all_the_names.py
```

You should see a file `names.csv` appear in the root directory.

This process will depend on your network speed but on my 2021 MBP & 50Mbps internet connection it takes roughly 2min & 10sec

## Contributions

Contributions are absolutely welcomed and encouraged. To do so, raise a PR with the new datasource and its integration into the names dataset and schema.

Ideas:
- Some datasets have a "frequency" measure of sorts. It would be cool to include that & have a mechanism to standardise/normalise the value across all datasets
- Standardise `origin` so that difference sources better match. Eg USA, United States of America, US of A, etc are all consistently presented as the same location


## Issues

If you encounter any problems,
please [file an issue](https://github.com/diabolical-ninja/nbn/issues) along with a detailed description.