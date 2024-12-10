import pandas as pd
import time

# File paths
students_file_path = "c:/Users/redpo/Desktop/pdc/students.csv"
fees_file_path = "c:/Users/redpo/Desktop/pdc/student_fees.csv"

# Load the datasets
students_df = pd.read_csv(students_file_path)
fees_df = pd.read_csv(fees_file_path)

# Measure the start time
start_time = time.time()

# Extract the day from the Payment Date in the fees dataset
fees_df['Day'] = fees_df['Payment Date'].str.extract(r'(\d+)$').astype(int)

# Dictionary to store the most frequent payment day for each student
payment_day_count = {}

# Iterate over the fees data and count the frequency of payment days per student
for _, row in fees_df.iterrows():
    student_id = row['Student ID']
    payment_day = row['Day']
    if student_id not in payment_day_count:
        payment_day_count[student_id] = {}
    if payment_day not in payment_day_count[student_id]:
        payment_day_count[student_id][payment_day] = 1
    else:
        payment_day_count[student_id][payment_day] += 1

# Now find the most frequent day for each student
most_frequent_payment_day = {}
for student_id, day_count in payment_day_count.items():
    most_frequent_payment_day[student_id] = max(day_count, key=day_count.get)

# Convert the dictionary to a DataFrame
consistent_payment_days = pd.DataFrame(list(most_frequent_payment_day.items()), columns=['Student ID', 'Most Consistent Payment Day'])

# Merge the consistent payment data with the student information
merged_df = pd.merge(students_df, consistent_payment_days, on='Student ID', how='inner')

# Measure the end time
end_time = time.time()
execution_time = end_time - start_time

# Display runtime and a preview of the merged dataset
print(f"Execution Time: {execution_time:.4f} seconds")
print(merged_df.head())
