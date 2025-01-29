# 📊 Analyzing Disease Progression in Pulmonary Hypertension: A Process Mining Approach  

## **Overview**  
This repository contains an **R script** designed for **process mining and event log analysis** to explore **disease progression pathways in Pulmonary Hypertension (PH) patients** using **clinical data**.  

By leveraging **event log analysis, process maps, and survival trajectories**, this project aims to uncover **frequent comorbidity transitions**, identify **high-risk patient pathways**, and **visualize disease progression** over time.  

## **Key Features**  
- **Preprocessing Clinical Data**  
  - Cleans and formats clinical records from a CSV file.  
  - Handles missing values using **last observation carried forward (LOCF)**.  
  - Ensures each patient has a valid event timeline.  

- **Event Log Creation**  
  - Defines **Participant ID** as **case_id**.  
  - Assigns **ICD-10 codes** as activities.  
  - Uses **diagnosis timestamps** to structure patient timelines.  

- **Process Mining & Visualization**  
  - Generates **process maps** showing the most frequent **comorbidity sequences**.  
  - Creates a **transition matrix** between ICD-10 diagnoses.  
  - Produces **animated patient journeys** to understand PH progression.  
  - Filters **frequent disease pathways** using `filter_trace_frequency(percentage = 0.95)`.  

## **Installation & Dependencies**  
Ensure you have R installed on your system. Then, install the required R packages:  

```bash
install.packages(c("dplyr", "igraph", "bupaR", "processcheckR", "bupaverse", 
                   "gganimate", "transformr", "processanimateR", "networkD3", "data.table", "zoo"))
```

## **How to Use**  

### **Clone this Repository:**  
First, navigate to your preferred working directory and clone this repository:

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/UK-Biobank-PH-Comorbidities-Analysis.git
cd UK-Biobank-PH-Comorbidities-Analysis/Process_Mining
```
### **Open the Script in RStudio or R Terminal**

Open RStudio or your R terminal.
Load the script **Process_Mining.R**.

### **Modify the File Path**
Locate the following line in the script:
```bash
file_path <- "file path"
```
Replace **"file path"** with the actual path of your CSV dataset.

### **Run the Script**

Execute the script in RStudio or your R terminal.
The script will preprocess clinical data, generate process maps, and perform event log analysis.

## **Generated Outputs & Analysis**

### **Process Map (Absolute Frequency)**

   - Visualizes frequent comorbidity transition sequences in PH patients.
   - Helps identify common disease progression pathways.

### **Performance Process Map (Mean Duration)**

   - Displays the average time spent in different disease states.
   - Aids in understanding delays and progression rates in PH.

### **Event Log Exploration**

   - Uses trace_explorer() to analyze common pathways in PH patients.
   - Filters high-frequency patient journeys to focus on significant transitions.

### **Animated Patient Pathways**
   - Creates dynamic visualizations of disease progression over time.
   - Useful for identifying high-risk pathways and predicting outcomes.

    

