# Air Occurrences Reported to the TSB - Data Analysis Project

This project is designed to analyze airplane accident data using Python. The goal is to study patterns in airplane accidents and incidents and extract meaningful insights from the data. The analysis includes data loading, processing, and visualization using various analytical techniques.

## Project Structure

This project follows several key coding principles and conventions:

- **SOLID Principles**: The code is organized according to SOLID principles, ensuring that it is modular, maintainable, and scalable.
- **Snake Case Naming**: All variable and function names use snake case for consistency and readability (e.g., `load_data`, `data_loader`).
- **Modular Architecture**: The code is divided into separate, well-defined modules to separate concerns and improve reusability.

### Folder Structure
- **Snake Case Naming**: All variable and function names use snake case for consistency and readability (e.g., `load_data`, `data_loader`).
- **data/**: Folder containing the project's data.
  - **final tables/**: Contains the final dataset (`fullData_V1.csv`) used for analysis.
  - **filtered tables/**: Folder for filtered data.
  - **original tables/**: Folder for unprocessed original data.
  
- **notebooks/**: Folder containing Jupyter notebooks used for analysis.
  - **preprocessing.ipynb**: Notebook for data preprocessing.
  - **analysis.ipynb**: Notebook for exploratory data analysis.
  - **predictions.ipynb**: Notebook for making predictions based on the data.

- **results/**: Folder to store output files, such as charts or CSV files generated during analysis.

- **scripts/**: Folder with Python scripts used in the project.
  - **data_loader.py**: Script for loading data from CSV files.
  - **visualizations.py**: Script for creating data visualizations.
  - **preprocessing/**, **analysis/**, **predictions/**, **common/**: Directories with additional functions organized by specific tasks.

- **venv/**: Virtual environment containing the project dependencies.

- **README.md**: This instructions file.



## Setup Instructions

Follow these steps to set up the project locally.

### Step 1: Clone the Repository
Clone the GitHub repository to your local machine:

```bash
git clone https://github.com/camiilavillamizar/DataAnalysisProject.git
```

### Step 2: Set Up Virtual Environment

#### Windows
```bash
python -m venv venv
venv\Scripts\activate

```
#### MacOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate

```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure jupyter kernel
```bash
& ".\venv\Scripts\python.exe" -m ipykernel install --user --name=venv --display-name "DA Project env"
```

### Step 5: Run Jupyter Notebook
```bash
cd notebooks
jupyter notebook

```

## Adding new libraries 

### Step 1: Activate the environment 
#### Windows
```bash
venv\Scripts\activate
```
#### MacOS/Linux
```bash
source venv/bin/activate
```
### Step 2: download current libraries 
```bash
pip install -r requirements.txt
```
### Step 3: install the specific library 
```bash
pip install <library>
```
### Step 4: Update requirements
```bash
pip freeze > requirements.txt
```