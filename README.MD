# Airplane Accidents Analytics Project

This project is designed to analyze airplane accident data using Python. The goal is to study patterns in airplane accidents and incidents and extract meaningful insights from the data. The analysis includes data loading, processing, and visualization using various analytical techniques.

## Project Structure

This project follows several key coding principles and conventions:

- **SOLID Principles**: The code is organized according to SOLID principles, ensuring that it is modular, maintainable, and scalable.
- **Camel Case Naming**: All variable and function names use camel case for consistency and readability (e.g., `loadData`, `dataLoader`).
- **Modular Architecture**: The code is divided into separate, well-defined modules to separate concerns and improve reusability.

### Folder Structure

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


