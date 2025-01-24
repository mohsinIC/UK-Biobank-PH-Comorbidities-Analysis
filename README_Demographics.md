# UK Biobank and Pulmonary Hypertension (PH) Cohort: Demographic Table Generation

## Overview
This Jupyter Notebook processes the UK Biobank data to create a comprehensive demographic table for participants, focusing on the Pulmonary Hypertension (PH) cohort. It performs data preprocessing, cleaning, and formatting to ensure the data is ready for analysis and visualization.

## Features
- **Data Import**: Reads raw datasets from CSV or other structured files into pandas DataFrames.
- **Data Cleaning**:
  - Handles missing values (`NaN`), duplicates, and irrelevant columns.
  - Filters and extracts relevant rows for the PH cohort.
- **Demographic Table Creation**:
  - Summarizes key participant characteristics such as age, sex, ethnicity, and other variables.
  - Aggregates data into a structured table for reporting and analysis.
- **Visualization (if applicable)**: Includes basic plots or summaries for exploratory data analysis.

## Technical Details

### Libraries Used
The following Python libraries are used in the notebook:
- **pandas**: For data manipulation and cleaning.
- **numpy**: For numerical operations and handling missing data.
- **matplotlib** (if applicable): For creating visualizations.
- **seaborn** (if applicable): For enhanced data visualization.

### Input Datasets
This notebook requires input files from the UK Biobank, which include:
- Participant-level demographic data.
- Pulmonary Hypertension cohort data.
- Additional clinical or diagnostic datasets.

### Output
- A structured demographic table summarizing the PH cohort.
- Cleaned and preprocessed datasets for further analysis.

## Usage
1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
