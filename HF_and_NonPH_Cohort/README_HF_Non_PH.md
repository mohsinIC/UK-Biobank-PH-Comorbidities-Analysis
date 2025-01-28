
# README_HF_Non_PH

## Overview
This README provides guidance on creating matched control cohorts using logistic regression and propensity scores for both general and specific datasets, such as the Heart Failure (HF) cohort matched against the Pulmonary Hypertension (PH) cohort. The methodology includes detailed steps for:
- Data preprocessing
- Propensity score calculation
- Nearest-neighbor matching with a caliper
- Summary statistics (e.g., demographics, smoking status, and comorbidities)
- Validation of the matched cohorts

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Input Datasets](#input-datasets)
3. [Data Preparation](#data-preparation)
4. [Propensity Score Calculation](#propensity-score-calculation)
5. [Matching Cohorts](#matching-cohorts)
6. [Validation and Summary Statistics](#validation-and-summary-statistics)
7. [Saving the Results](#saving-the-results)
8. [Advanced Features](#advanced-features)

---

## Prerequisites
- Python 3.x
- Required libraries:
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `matplotlib`
- CSV files containing the datasets for PH and matched control cohorts.

---

## Input Datasets
1. **PH Dataset**: Contains participants with Pulmonary Hypertension (ICD-10 codes: `I27.0`, `I27.2`, `I27.9`).
2. **Control Dataset**: Used for matching based on demographic and clinical covariates.

#### Key Columns Required:
- `Participant ID`
- `Sex`
- `Age Range`
- `Ethnicity`
- `Smoking Status`
- `BMI Range`
- `IMD Quintile`
- `Alive/Dead`
- `Combined ICD10 Codes`

---

## Data Preparation
#### Steps:
1. **Remove Unnecessary Columns**:
   ```python
   columns_to_drop = ['Date of Death', 'Death Cause Diseases', 'Death Cause Disease ICD10 Codes']
   dataset.drop(columns=columns_to_drop, inplace=True)
   ```
2. **Handle Missing Data**:
   ```python
   dataset.dropna(subset=['Combined ICD10 Codes', 'Participant ID', 'IMD_quintile'], inplace=True)
   ```
3. **Encode Categorical Variables**:
   ```python
   df_encoded = pd.get_dummies(dataset[['Sex', 'Ethnicity', 'Age Range', 'Smoking Status', 'BMI Range', 'IMD_quintile', 'Alive / Dead']], drop_first=True)
   ```

---

## Propensity Score Calculation
1. Define treatment and control groups:
   - Treatment: Participants with specific ICD-10 codes (e.g., `I27.0`, `I27.2`, `I27.9` for PH; `I50.0`, `I50.1` for HF).
   ```python
   treatment_group = dataset[dataset['Combined ICD10 Codes'].str.contains('I27.0|I27.2|I27.9', na=False)]
   control_group = dataset[~dataset['Participant ID'].isin(treatment_group['Participant ID'])]
   ```
2. Train logistic regression for propensity scores:
   ```python
   model = LogisticRegression(max_iter=1000)
   model.fit(df_encoded, treatment_indicator)
   dataset['propensity_score'] = model.predict_proba(df_encoded)[:, 1]
   ```

---

## Matching Cohorts
1. Use Nearest Neighbors with a caliper for matching:
   ```python
   from sklearn.neighbors import NearestNeighbors

   caliper = 0.05
   nn = NearestNeighbors(n_neighbors=1)
   nn.fit(control_group[['propensity_score']])
   distances, indices = nn.kneighbors(treatment_group[['propensity_score']])
   ```
2. Filter matches within the caliper:
   ```python
   matched_controls_indices = [index for distance, index in zip(distances.flatten(), indices.flatten()) if distance <= caliper]
   ```
3. Expand caliper if necessary:
   ```python
   while len(matched_controls_indices) < len(treatment_group):
       caliper += 0.01
       matched_controls_indices = [index for distance, index in zip(distances.flatten(), indices.flatten()) if distance <= caliper]
   ```

---

## Validation and Summary Statistics
1. **Participant Counts**:
   ```python
   unique_ph_ids = treatment_group['Participant ID'].nunique()
   unique_control_ids = matched_controls['Participant ID'].nunique()
   ```
2. **Demographic Statistics**:
   - Count and percentages for `Sex`, `Ethnicity`, `Age Range`, `Smoking Status`, `BMI Range`, `IMD Quintile`.
   ```python
   sex_counts = unique_participants['Sex'].value_counts()
   sex_percentages = (sex_counts / total_participants) * 100
   sex_counts_with_percentages = sex_counts.astype(str) + " (" + sex_percentages.round(2).astype(str) + "%)"
   ```
3. **Check Overlap Between Groups**:
   ```python
   common_participants = pd.merge(treatment_group, matched_controls, on='Participant ID', how='inner')
   ```

---

## Saving the Results
- Save matched control datasets:
   ```python
   matched_controls.to_csv('Matched_Control_Cohort.csv', index=False)
   ```
- Save combined treatment and control cohorts:
   ```python
   combined_cohort = pd.concat([treatment_group, matched_controls])
   combined_cohort.to_csv('Combined_Cohort.csv', index=False)
   ```

---

## Advanced Features
#### 1. **Process Mining**:
   - Apply process mining techniques to analyze temporal trajectories.
   - Extract event logs from matched cohorts for visualization (e.g., Sunburst or Tracer plots).

#### 2. **Disease Categorization**:
   - Assign ICD-10 codes to chapters and subchapters:
   ```python
   dataset['Chapter'], dataset['Subchapter'] = zip(*dataset['Combined ICD10 Codes'].apply(categorize_icd10))
   ```

#### 3. **Cox Proportional Hazards Analysis**:
   - For survival analysis comparing cohorts.

---

## Notes
- Ensure the number of matched controls is equivalent to the treatment group size.
- Validate that matched controls are distinct from the treatment group.
- Adjust the caliper size iteratively to achieve the required number of matches.
