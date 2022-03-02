# All The Names
Dataset of all people names.


### Data Structure
Found in `all_names.csv`

| Field 	| Type 	| Description 	|
|---	|---	|---	|
| First Name 	| String 	| First Name 	|
| Origin 	| String 	| Country of origin. If multiple countries are available they should be represented as new lines 	|
| Gender 	| String 	| *If available.*  Defined as `F`, `M`, `Other` or `NULL` |
| Definition 	| String 	| Historical meaning of the name 	|


## Contributions

Contributions are absolutely welcomed and encouraged. To do so, raise a PR with the new datasource and its integration into the names dataset and schema.

Ideas:
- Some datasets have a "frequency" measure of sorts. It would be cool to include that & have a mechanism to standardise/normalise the value across all datasets