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

```r
install.packages(c("dplyr", "igraph", "bupaR", "processcheckR", "bupaverse", 
                   "gganimate", "transformr", "processanimateR", "networkD3", "data.table", "zoo"))

How to Use

    Clone this repository:

    git clone https://github.com/your-github-username/process-mining-ph.git
    cd process-mining-ph

    Open RStudio or R terminal.
    Run the script process_mining_PH.R.
    Replace "file path" in the script with the actual path of your CSV file.
    Execute the script to generate:
        Process maps for PH progression.
        Survival trajectory analysis.
        Animated visualizations of disease pathways.

Example Outputs

✅ Process Map (Absolute Frequency)
Shows common transition sequences between PH-related conditions.

✅ Performance Process Map (Mean Duration)
Displays average time spent in different disease states.

✅ Survival Analysis
Predicts risk groups based on clinical progression.

✅ Animated Patient Pathways
Visualizes how patients transition through different ICD-10 conditions over time.
Expected Findings & Applications

    Identification of key comorbidities influencing PH progression.
    Risk stratification for early detection and personalized interventions.
    Insights into frequent disease transition patterns in PH cohorts.

License

This project is licensed under the MIT License – feel free to use and modify it!
Author

