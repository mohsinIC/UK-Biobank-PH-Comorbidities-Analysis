
# Preprocessing of UK Biobank for PH Cohort (Pre-PH and Post-PH)

## Overview
This project analyzes Pulmonary Hypertension (PH) comorbidities in UK Biobank participants. Using data on death records, diagnoses, and demographic information, the code identifies trends, performs data cleaning, and visualizes key results. The analysis involves extracting and structuring data, handling missing values, and creating comprehensive datasets for further exploration and insights.

## Features
- Data import from multiple CSV files, including:
  - Death Date Records: Contains death dates of participants.
  - Death Cause Records: Includes causes of death for participants.
  - GP Prescription Records: Lists prescribed drugs and quantities.
  - ICD10 codes Records: Includes ICD10 codes along with diseases names and diagnosis dates for particpants
- Preprocessing steps:
  - Extraction of ICD-10 and Main ICD-10 codes with related diseases and diagnosis dates.
  - Handling missing values (e.g., NaNs) and empty strings.
  - Structuring datasets with participant IDs, demographic details, diagnoses, and dates.
- Visualization of data trends using `matplotlib`.
- Creation of a complete structured dataset that includes:
  - Participant demographics (e.g., year/month of birth, ethnicity, sex).
  - ICD-10 and Main ICD-10 codes with diagnosis dates.

## Technical Details

### Libraries Used
The code utilizes the following Python libraries for efficient data processing and visualization:

```bash
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.pyplot as plt
```
- **numpy**: For numerical computations and array handling.
- **pandas**: For powerful data manipulation and analysis.
- **matplotlib**: For creating visualizations to identify data trends and patterns.
 
## Requirements
Install the following Python libraries:

```bash
pip install numpy pandas matplotlib
```


### Datasets Used
The project requires the following datasets in CSV format:
- **All ICD10 Codes with Diseases Names and Dates Data.csv**: Dataset containing ICD10 codes records for participants along with diagnosis dates.
- **Dataset with ICD10 and Diseases Names and Death Records.csv**: Dataset containing ICD10 codes records for participants along with diagnosis dates and death records.
- **Death Date Records.csv**: Dataset containing death date records for participants.
- **Death Cause Records.csv**: Dataset detailing causes of death.
- **GP Prescription Records.csv**: Dataset listing prescribed drugs and quantities.
- **PH Patients with Commorbidities Dataset.csv**: PH Cohort dataset with PH comorbidities

Additional structured datasets generated during preprocessing.
Each dataset contributes to building a comprehensive view of participant health data, enabling detailed analysis of Pulmonary Hypertension comorbidities.


## Usage

1. Clone this repository to your local system:
   ```bash
   git clone <repository_url>
   ```
   
2. Navigate to the project directory:
   ```bash
   cd <repository_name>
   ```

3. Install the required libraries using the command provided above.

4. Open the Jupyter Notebook in your environment:

   ```bash
   jupyter notebook UK_Biobank_PH_Comorbidities.ipynb
   ```

5. Execute the notebook cells step-by-step to:
   - Import datasets.
   - Preprocess and clean the data.
   - Analyze trends and visualize results.

## Files
- **UK_Biobank_PH_Comorbidities.ipynb**: Main analysis notebook containing code for data processing and visualization.
- **README.md**: Comprehensive documentation for the project.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
Feel free to explore and contribute to the project for further advancements in Pulmonary Hypertension research.

