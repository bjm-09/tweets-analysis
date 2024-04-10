# Twitter data analysis


## Overview

This project contains six Python scripts designed to solve tweets analysis problems. The scripts are divided into two categories: memory-optimized and time-optimized. Additionally, there's a `utils.py` file containing utility functions, and a `data` folder containing a JSON file with the date to be analized.

- **data/**: Directory containing data files.
- **src/**: Directory containing Python source code.
- **utils/**: Directory containing main any utility functions that we may need.

### NOTE: The data file will not be uploaded as I am not certain on whether this data is private.

## Scripts

### Memory-Optimized Scripts

1. **q{n}_memory.py**: These files solve their respective problems with a focus on memory optimization.

### Time-Optimized Scripts

1. **q{n}time.py**: These files solve their respective problems with a focus on time optimization.

## Utils

- **utils.py**: Contains utility functions used across the scripts.

## Data

- **farmers-protest-tweets-2021-2-4.json**: JSON file containing data to be analized with the scripts.

## Usage

1. Clone the github repository:
```bash
git clone https://github.com/bjm-09/tweets-analysis.git
```

2. Move to the repository folder:
```bash
cd tweets-analysis
```

3. Initialize the project by running bash init the script. Note that the script needs you to input an argument with the name for your python virtual environment. For example
```bash
bash init-project.sh my-venv
```

### Note: Depending on your OS (or if you have conda) you may need to update line 11 with: python3 -> python

4. Make sure to download and unzip the JSON data file and save it under:
`data/farmers-protest-tweets-2021-2-4.json`

Each script can be executed independently to solve its respective problem. Ensure that the `data` folder and `utils.py` file are accessible for the scripts to run successfully.

### Example:

```bash
python3 src/{script_name}.py
```