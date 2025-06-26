
# Descriptive analysis of Longitudinal Patterns of Comorbidities

This repository contains Python and R files to analyse Longitudinal Patterns of Comorbidities in Pulmonary Hypertension using UK Biobank data

**July 2025**

**Publication**: Masood, M. et al. Longitudinal Patterns of Comorbidities in Pulmonary Hypertension: Insights from UK Biobank. XX. Submitted July 25. Under review.<br> 
**Authors**: Masood, M. (Imperial College London)<be>
[![DOI] <a href="https://doi.org/10.5281/zenodo.15747765"><img src="https://zenodo.org/badge/920683947.svg" alt="DOI"></a>





## Project Overview

This project explores longitudinal comorbidities of three matched cohorts: Chronic Obstructive Pulmonary Disease (COPD), HEart Failure (HF), and Pulmonary Hypertension (PH).  Each subdirectory focuses on a specific analysis or task:

* **COPD_Cohort:**  Analysis of a cohort of patients with COPD.  Includes data cleaning, feature engineering, and potentially some statistical modeling.  See the directory's README for more details.

* **HF_and_NonPH_Cohort:**  Analysis comparing patients with Heart Failure (HF) to those without Pulmonary Hypertension (Non-PH).  This might involve comparing demographics, clinical characteristics, and outcomes.  See the directory's README for more details.

* **Hazard_Ratio:**  Calculation and interpretation of hazard ratios, likely for specific outcomes related to the studied cohorts (e.g., time to event, mortality).  See the directory's README for more details.

* **Process_Mining:**  Application of process mining techniques to understand the pathways and processes of care for patients with these conditions.  See the directory's README for more details.

* **UK_and_PH_Cohort_Demographic_Table:**  Generation of demographic tables for the UK and PH cohort.  This will likely involve summarizing key patient characteristics. See the directory's README for more details.

* **UK_and_PH_Cohort_Preprocessing_Coding:**  Scripts and documentation related to the preprocessing and coding of the UK and PH cohort data.  This is a crucial step for data preparation. See the directory's README for more details.

## Getting Started

To reproduce the analyses and results, please follow the instructions in each subdirectory's README file.  These READMEs will provide specific details about the data used, the scripts to run, and the expected outputs. The codes are written in R (version) and python.
Installation guides:
### Installation Guide

**1. Clone the repository:**
```bash
git clone https://github.com/mohsinIC/UK-Biobank-PH-Comorbidities-Analysis.git
cd UK-Biobank-PH-Comorbidities-Analysis

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

install.packages(c("dplyr", "ggplot2", "survival", "bupaR", "eventdataR", "processmapR"))


## Dependencies

Please refer to the individual README files within each subdirectory for specific software and library dependencies.  Generally, you can expect the project to use common data science and statistical computing tools such as Python with libraries like Pandas, NumPy, Scikit-learn, and potentially R.

## Contributing

(Optional) If you wish to contribute to this project, please open an issue or submit a pull request.
