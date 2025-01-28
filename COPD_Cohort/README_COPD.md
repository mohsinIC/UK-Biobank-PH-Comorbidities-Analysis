
# README_COPD

## Overview

This project focuses on creating, analyzing, and visualizing Chronic Obstructive Pulmonary Disease (COPD) cohorts and their associated comorbidities using various datasets. The study explores comorbidities, their temporal patterns, and their relationships with COPD, utilizing advanced analysis techniques such as propensity score matching, process mining, Sunburst plots, Forest plots, and Cox Proportional Hazards analysis.

---

## Key Objectives

1. **Generate a COPD-Matched Control Cohort**:
   - Use logistic regression and nearest-neighbor matching based on propensity scores.
   - Analyze matched cohorts for demographic and clinical variables.

2. **Analyze COPD Comorbidities**:
   - Explore pre- and post-COPD pathways.
   - Highlight comorbidities using visualization techniques like Sunburst and Forest plots.

3. **Identify Disease Pathways**:
   - Leverage process mining to reveal significant progression pathways leading to COPD.

4. **Survival Analysis**:
   - Use Cox Proportional Hazards to compare survival outcomes between COPD and Pulmonary Hypertension (PH) cohorts.

---

## Requirements

The following dependencies are required to run the analysis:

- Python 3.x
- pandas
- numpy
- scikit-learn
- plotly
- lifelines
- matplotlib

Install these dependencies using:

```bash
pip install pandas numpy scikit-learn plotly lifelines matplotlib
```

---

## Data Preparation

### Datasets

1. **COPD Matched Cohort with Comorbidities**:
   - Used for identifying pre- and post-COPD pathways.

2. **Pre-COPD, Post-COPD, and Combined COPD Cohorts**:
   - Analyze specific disease pathways and commonalities.

3. **COPD Control Cohort with Comorbidities Model**:
   - Utilized for generating Sunburst plots.

### Preprocessing Steps

1. **Data Cleaning**:
   - Remove unnecessary columns such as `Date of Death`, `Death Cause Diseases`, and `Death Cause Disease ICD10 Codes`.
   - Drop rows with missing values in key columns.

2. **Encoding Categorical Variables**:
   - Use one-hot encoding for variables like `Sex`, `Ethnicity`, `Age Range`, `Smoking Status`, and `BMI Range`.

3. **Filtering ICD10 Codes**:
   - Focus on key comorbidities like `E78.0`, `I25.1`, `I10`.

4. **Disease Pathway Identification**:
   - Group participants by `Participant ID` to generate disease sequences.

---

## Analysis Steps

### 1. Propensity Score Matching

- Use logistic regression to calculate propensity scores.
- Match PH and COPD cohorts using nearest-neighbor matching with a caliper of 0.05.
- Expand caliper dynamically if necessary to ensure adequate matches.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import NearestNeighbors
```

---

### 2. Visualization

#### **Sunburst Plot**
- Purpose: Visualize hierarchical comorbidity relationships in COPD cohorts.
- Steps:
  - Filter dataset for relevant ICD10 codes.
  - Use Plotly to generate Sunburst plots with hierarchical layers: `Diseases Chapter`, `Diseases Sub-Chapter`, and `ICD10 Codes`.

```python
import plotly.express as px

fig = px.sunburst(data, path=['Diseases Chapter', 'Diseases Sub-Chapter', 'ICD10 Codes'])
fig.write_html('sunburst_plot.html')
```

---

#### **Forest Plot**
1. Pre-COPD and Post-COPD Comorbidities:
   - Calculate prevalence, incidence rates, and survival outcomes.

2. Combined Forest Plot:
   - Overlay results for comparative analysis of COPD and PH cohorts.

---

### 3. Process Mining

- Purpose: Identify COPD progression pathways.
- Steps:
  - Combine pre-, post-, and common COPD datasets.
  - Generate unique traces and calculate mean time differences between conditions.
  - Highlight pathways like:
    - `E11.9 -> I10 -> COPD`
    - `E78.0 -> I10 -> COPD`

---

### 4. Cox Proportional Hazards Analysis

- Purpose: Compare survival times and hazard ratios for COPD and PH pathways.
- Steps:
  - Standardize columns and encode categorical variables.
  - Fit a Cox Proportional Hazards model.

```python
from lifelines import CoxPHFitter

cox_model = CoxPHFitter()
cox_model.fit(data, duration_col='time', event_col='event')
cox_model.plot()
```

---

## Key Findings

1. **Sunburst Plot**:
   - Revealed hierarchical relationships and prevalence of COPD comorbidities.

2. **Forest Plot**:
   - Highlighted significant differences in pre- and post-COPD comorbidities.

3. **Process Mining**:
   - Identified dominant pathways, emphasizing the temporal sequence of COPD progression.

4. **Cox Analysis**:
   - Quantified the impact of common pathways on survival outcomes.

---

## Outputs

- `COPD Matched cohort with Comorbidities.csv`: Final dataset.
- Sunburst and Forest plots for visualizing findings.
- Process mining pathway diagrams.
- Hazard ratio plots from Cox analysis.

---

## Future Work

1. Extend analysis to rare comorbidities.
2. Integrate additional datasets to validate findings.
3. Explore machine learning models for pathway prediction.

---

## How to Run

1. Place datasets in the working directory.
2. Execute scripts in the following order:
   - `data_preprocessing.py`
   - `visualization.py`
   - `process_mining.py`
   - `cox_analysis.py`

---

