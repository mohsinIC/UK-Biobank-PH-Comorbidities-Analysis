# README: Cox Proportional Hazards Analysis (PH vs HF & PH vs COPD)

## Introduction
This study performs **Cox Proportional Hazards (CPH) analysis** on two separate comparisons:
1. **Pulmonary Hypertension (PH) vs Heart Failure (HF)**
2. **Pulmonary Hypertension (PH) vs Chronic Obstructive Pulmonary Disease (COPD)**

The analysis aims to identify the impact of various comorbidities and disease progression pathways on the hazard ratios for mortality in these conditions.

---

## Required Libraries
Ensure the following Python libraries are installed:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from lifelines import CoxPHFitter
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
```

---

## Data Loading & Preprocessing
The analysis uses separate datasets for PH, HF, and COPD. Data is processed as follows:

### **PH Cohort**
- Load pre-PH, post-PH, and common-PH datasets.
- Merge and remove duplicate records.
- Replace PH-specific ICD10 codes with "PH".
- Convert diagnosis dates into datetime format.
- Filter disease sequences before PH diagnosis.

### **HF Cohort**
- Load pre-HF, post-HF, and common-HF datasets.
- Replace HF-specific ICD10 codes with "HF".
- Filter HF pathways occurring before HF diagnosis.

### **COPD Cohort**
- Load pre-COPD, post-COPD, and common-COPD datasets.
- Replace COPD-specific ICD10 codes with "COPD".
- Filter COPD pathways occurring before COPD diagnosis.

### **Common Pathway Extraction**
- Identify shared pathways among PH, HF, and COPD cohorts.
- Filter pathways with **sufficient participants (≥5)**.
- Only include pathways with **at least one recorded death**.

---

## **Cox Proportional Hazards Model**

### **1. PH vs HF Hazard Ratio Analysis**
- Compute follow-up time and censoring.
- Encode categorical variables (sex, alive/dead status, disease pathways).
- Fit Cox Proportional Hazards model and visualize results.
- Identify key pathways with significantly high hazard ratios.

### **2. PH vs COPD Hazard Ratio Analysis**
- Similar approach as PH vs HF.
- Compute death follow-up times, apply Cox regression.
- Compare pathway risks between PH and COPD.
- Generate hazard ratio plots.

### **3. Combined Analysis (PH vs HF vs COPD)**
- Compare hazard ratios across PH, HF, and COPD cohorts.
- Identify overlapping pathways contributing to mortality risk.

---
## **Visualizations**
1. **Cox Hazard Ratio Plots** for each condition comparison.
2. **Disease Progression Pathway Diagrams** for PH, HF, and COPD.
3. **Common Pathway Overlap Visualization** between PH, HF, and COPD.

---

## **Future Work**
- Incorporate **machine learning models** for survival prediction.
- Extend analysis with additional risk factors.
- Validate findings using **external clinical datasets**.

---

## **Conclusion**
This study provides **insights into mortality risks associated with PH, HF, and COPD pathways**, helping clinicians identify high-risk patient groups for early intervention.

