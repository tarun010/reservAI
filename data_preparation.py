import pandas as pd
import numpy as np

# Load the XLSX file
file_path = 'data/historical_data.xlsx'
xls = pd.ExcelFile(file_path)

# Load data from the specific sheet
sheet_name = '2 ED visits, month, age and sex'
sheet_data = pd.read_excel(xls, sheet_name=sheet_name)

# Display the first few rows of the sheet to inspect the data
print(sheet_data.head())

# Assuming the sheet_data contains columns like 'Month', 'Age', 'Sex', 'ED Visits'
# We will create a dummy dataset with daily visits based on this structure

# Create a dummy dataset
np.random.seed(42)  # For reproducibility

num_days = 180  # Example for 6 months
num_patients = np.random.randint(10, 50, size=num_days)  # Random number of patients per day
time_of_day = np.random.randint(0, 24, size=num_days)  # Random hour of the day (0-23)
day_of_week = np.random.randint(1, 8, size=num_days)  # Random day of the week (1-7)
wait_time = np.random.uniform(5, 120, size=num_days)  # Random wait time in minutes

# Create a DataFrame
dummy_data = pd.DataFrame({
    'num_patients': num_patients,
    'time_of_day': time_of_day,
    'day_of_week': day_of_week,
    'wait_time': wait_time
})

# Display the first few rows of the dummy dataset
print(dummy_data.head())

# Save the dummy dataset to a CSV file
dummy_data.to_csv('data/dummy_data.csv', index=False)
