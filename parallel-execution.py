import pandas as pd
import multiprocessing as mp
import time

# File paths
students_file_path = "c:/Users/redpo/Desktop/pdc/students.csv"
fees_file_path = "c:/Users/redpo/Desktop/pdc/student_fees.csv"

# Load the datasets
students_df = pd.read_csv(students_file_path)
fees_df = pd.read_csv(fees_file_path)

# Extract the day from the Payment Date in the fees dataset
fees_df['Day'] = fees_df['Payment Date'].str.extract(r'(\d+)$').astype(int)

# Function to calculate the most frequent payment day for a chunk of data
def calculate_consistent_payment_days(chunk):
    # Dictionary to store frequency of payment days
    payment_day_count = {}

    for _, row in chunk.iterrows():
        student_id = row['Student ID']
        payment_day = row['Day']
        if student_id not in payment_day_count:
            payment_day_count[student_id] = {}
        if payment_day not in payment_day_count[student_id]:
            payment_day_count[student_id][payment_day] = 1
        else:
            payment_day_count[student_id][payment_day] += 1

    # Find the most frequent payment day for each student in the chunk
    most_frequent_payment_day = {}
    for student_id, day_count in payment_day_count.items():
        most_frequent_payment_day[student_id] = max(day_count, key=day_count.get)

    return most_frequent_payment_day

if __name__ == '__main__':
    # Measure the start time
    start_time = time.time()

    # Split the fees dataset into chunks for parallel processing
    num_partitions = mp.cpu_count()
    chunk_size = len(fees_df) // num_partitions
    chunks = [fees_df.iloc[i:i + chunk_size] for i in range(0, len(fees_df), chunk_size)]

    # Use multiprocessing to process each chunk in parallel
    with mp.Pool(num_partitions) as pool:
        results = pool.map(calculate_consistent_payment_days, chunks)

    # Combine results from all processes
    consistent_payment_days_dict = {}
    for result in results:
        consistent_payment_days_dict.update(result)

    # Convert the dictionary to a DataFrame
    consistent_payment_days = pd.DataFrame(list(consistent_payment_days_dict.items()), columns=['Student ID', 'Most Consistent Payment Day'])

    # Merge the consistent payment data with the student information
    merged_df = pd.merge(students_df, consistent_payment_days, on='Student ID', how='inner')

    # Measure the end time
    end_time = time.time()
    execution_time = end_time - start_time

    # Display runtime and a preview of the merged dataset
    print(f"Execution Time: {execution_time:.4f} seconds")
    print(merged_df.head())
