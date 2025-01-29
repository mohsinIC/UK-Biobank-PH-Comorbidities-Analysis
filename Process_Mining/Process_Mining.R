
######################################################################################################################
######################################################################################################################
######################################################################################################################

#               Analyzing Disease Progression in Pulmonary Hypertension: A Process Mining Approach


######################################################################################################################
######################################################################################################################
######################################################################################################################

if (!requireNamespace("dplyr", quietly = TRUE)) {
  install.packages("dplyr")
}
#install.packages("processanimateR")
#install.packages("gganimate")
#install.packages("transformr")
#install.packages("networkD3")

library(dplyr)
library(igraph)
library(bupaR)
library(processcheckR)
library(bupaverse)
library(gganimate)
library(transformr)
library(processanimateR)
library(networkD3)

# Replace the file path with your actual file path
file_path <- "file path"


# Import the CSV file
dff <- read.csv(file_path)

View(dff)

colnames(dff)
process_mining_Dead_Alive <- dff[, c(1, 8,10, 15, 16, 17, 18, 19, 20, 21, 22, 23)]
View(process_mining_Dead_Alive)

colnames(process_mining_Dead_Alive)


# Create a new row for each Participant.ID by duplicating the last row
new_rows_2 <- process_mining_Dead_Alive %>%
  group_by(Participant.ID) %>%
  slice(n()) %>%
  ungroup()

View(new_rows_2)

# Print the resulting dataset
new_rows_2 <- new_rows_2 %>%
  mutate(
    ICD10.Codes.Range = `Alive...Dead`,
    Diagnosis.Date = `Date.of.Death`,
    activity_instance_id = activity_instance_id + 1,
    order = order + 1
  )
View(new_rows_2)

# Combine the new_rows with the original dataset using bind_rows
final_dff <- process_mining_Dead_Alive %>%
  bind_rows(new_rows_2)

# Assuming final_df is your dataset
final_dff <- final_dff %>%
  arrange(Participant.ID)

# Print the resulting modified final_df
View(final_dff)



# Convert empty strings to NA in Diagnosis.Date
final_dff$Diagnosis.Date[final_dff$Diagnosis.Date == ""] <- NA

# Fill missing values with the previous non-missing value
final_dff$Diagnosis.Date <- zoo::na.locf(final_dff$Diagnosis.Date)

# View the modified dataset
View(final_dff)


# Mutate the DataFrame
final_dff <- final_dff %>%
  mutate(
    lifecycle_id = "complete",
    activity_instance_id = row_number(),
    resource_id = NA,
    timestamp = as.POSIXct(Diagnosis.Date)  # Assuming 'timestamp' is the column with real timestamps
  )

# Creating the event log
my_eventlog_final_dff <- final_dff %>%
  eventlog(
    case_id = "Participant.ID",
    activity_id = "ICD10.Codes.Range", 
    lifecycle_id = "lifecycle_id",
    activity_instance_id = "activity_instance_id",
    resource_id = "resource_id",
    timestamp = "timestamp"
  )

View(my_eventlog_final_dff)

# Filter traces based on frequency
filtered_eventlog_final_dff <- my_eventlog_final_dff %>%
  filter_trace_frequency(percentage = 0.95)


# Create and plot a process map
filtered_eventlog_final_dff %>%
  process_map(frequency("absolute"))


filtered_eventlog_final_dff %>%
  process_map(performance(mean, "months"))


filtered_eventlog_final_dff %>%
  process_matrix(frequency("absolute")) 

filtered_eventlog_final_dff %>%
  process_matrix(frequency("absolute")) %>%
  plot()

filtered_eventlog_final_dff %>%
  dotted_chart(x = "absolute")

animate_process(filtered_eventlog_final_dff)




# Assuming you have my_eventlog
library(bupaR)

# Use trace_explorer() to explore traces in the eventlog
trace_explorer(my_eventlog_final_dff, coverage = 0.70, abbreviate = FALSE)


######################################################################################################################
######################################################################################################################
######################################################################################################################

#            Unveiling Pulmonary Hypertension Patient Journeys Using Event Logs and Process Mining

######################################################################################################################
######################################################################################################################
######################################################################################################################

if (!requireNamespace("dplyr", quietly = TRUE)) {
  install.packages("dplyr")
}
#install.packages("processanimateR")
#install.packages("gganimate")
#install.packages("transformr")
#install.packages("networkD3")

library(dplyr)
library(igraph)
library(bupaR)
library(processcheckR)
library(bupaverse)
library(gganimate)
library(transformr)
library(processanimateR)
library(networkD3)



## Install the data.table package if not already installed
if (!requireNamespace("data.table", quietly = TRUE)) {
  install.packages("data.table")
}

# Load the data.table library
library(data.table)

# Replace the file path with your actual file path
file_path <- "file path"

# Import the CSV file with data.table
dff <- fread(file_path)

# Display the number of rows and columns in the imported dataset
print(paste("Number of rows:", nrow(dff)))
print(paste("Number of columns:", ncol(dff)))


#View(dff)

# Initial number of participants in the original dataframe
initial_participants <- dff %>%
  distinct(`Participant ID`) %>%
  nrow()
print(paste("Initial number of participants:", initial_participants))

colnames(dff)



# Replace spaces with dots in column names
colnames(dff) <- gsub(" ", ".", colnames(dff))

# Print new column names
print(colnames(dff))



process_mining_Dead_Alive <- dff[, c(1, 8, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25)]
#View(process_mining_Dead_Alive)


# Number of participants after selecting relevant columns
participants_after_selection <- process_mining_Dead_Alive %>%
  distinct(`Participant.ID`) %>%
  nrow()
print(paste("Participants after selecting relevant columns:", participants_after_selection))


colnames(process_mining_Dead_Alive)


# Create a new row for each Participant.ID by duplicating the last row
new_rows_2 <- process_mining_Dead_Alive %>%
  group_by(Participant.ID) %>%
  slice(n()) %>%
  ungroup()

#View(new_rows_2)

# Print the resulting dataset
new_rows_2 <- new_rows_2 %>%
  mutate(
    ICD10.Codes = `Alive./.Dead`,
    Diagnosis.Date = `Date.of.Death`,
    activity_instance_id = activity_instance_id + 1,
    order = order + 1
  )
#View(new_rows_2)

# Combine the new_rows with the original dataset using bind_rows
final_dff <- process_mining_Dead_Alive %>%
  bind_rows(new_rows_2)

# Assuming final_df is your dataset
final_dff <- final_dff %>%
  arrange(Participant.ID)

# Print the resulting modified final_df
#View(final_dff)



# Convert empty strings to NA in Diagnosis.Date
final_dff$Diagnosis.Date[final_dff$Diagnosis.Date == ""] <- NA

# Fill missing values with the previous non-missing value
final_dff$Diagnosis.Date <- zoo::na.locf(final_dff$Diagnosis.Date)

# View the modified dataset
#View(final_dff)


# Mutate the DataFrame
final_dff <- final_dff %>%
  mutate(
    lifecycle_id = "complete",
    activity_instance_id = row_number(),
    resource_id = NA,
    timestamp = as.POSIXct(Diagnosis.Date)  # Assuming 'timestamp' is the column with real timestamps
  )


# Number of participants after adding new rows
participants_after_adding_rows <- final_dff %>%
  distinct(`Participant.ID`) %>%
  nrow()
print(paste("Participants after adding new rows:", participants_after_adding_rows))


# Creating the event log
my_eventlog_final_dff <- final_dff %>%
  eventlog(
    case_id = "Participant.ID",
    activity_id = "ICD10.Codes", 
    lifecycle_id = "lifecycle_id",
    activity_instance_id = "activity_instance_id",
    resource_id = "resource_id",
    timestamp = "timestamp"
  )

#View(my_eventlog_final_dff)

# Filter traces based on frequency
filtered_eventlog_final_dff <- my_eventlog_final_dff %>%
  filter_trace_frequency(percentage = 0.95)


# Number of participants after final filtering
total_participants <- filtered_eventlog_final_dff %>%
  distinct(`Participant.ID`) %>%
  nrow()
print(paste("Total number of participants:", total_participants))


# Create and plot a process map
filtered_eventlog_final_dff %>%
  process_map(frequency("absolute"))


filtered_eventlog_final_dff %>%
  process_map(performance(mean, "years"))


filtered_eventlog_final_dff %>%
  process_matrix(frequency("absolute")) 

filtered_eventlog_final_dff %>%
  process_matrix(frequency("absolute")) %>%
  plot()

filtered_eventlog_final_dff %>%
  dotted_chart(x = "absolute")

animate_process(filtered_eventlog_final_dff)




# Assuming you have my_eventlog
library(bupaR)

# Use trace_explorer() to explore traces in the eventlog
trace_explorer(my_eventlog_final_dff, coverage = 0.30, abbreviate = FALSE)
