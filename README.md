@@ -1,28 +1,28 @@
# PDC_TIER-1
-PDC TIER 1 ASSIGNMENT
-Name = Shahrukh Hassan
-roll number = 21b-059-cs
PDC TIER 1 ASSIGNMENT
**Name** = Saad Rashid
**roll number** = 21b-059-cs
# Parallel vs Serial Processing Assignment

This repository demonstrates the comparison between **serial processing** and **parallel processing** using Python for a data processing task involving student and fee data.

## **Objective**
To implement and compare the performance of **serial computation** and **multiprocessing-based parallel computation** for processing large datasets. This assignment highlights the benefits of parallel processing in reducing execution time for computationally intensive tasks.

---

## **Dataset**
### Files Used:
1. **students.csv**: Contains a list of students with their IDs, names, and major.
2. **student_fees.csv**: Contains fee payment details, including student IDs, amounts, and payment dates.

### Sample Data:

#### **students.csv**
| Student Name    | Student ID | Major        |
|-----------------|------------|--------------|
| Scott Conner    | SID1000    | Art          |
| Daniel Harrison | SID1001    | Engineering  |
| Lisa Mclaughlin | SID1002    | Biology      |
| Richard Guerra  | SID1003    | Psychology   |
| Beth Hess       | SID1004    | Biology      |


#### **student_fees.csv**
| Fee Status | Payment Date | Student ID |
|------------|--------------|------------|
| Paid       | 6-Jan        | SID1000    |
| Paid       | 13-Feb       | SID1000    |
| Paid       | 20-Mar       | SID1000    |
| Paid       | 4-Apr        | SID1000    |
| Paid       | 2-May        | SID1000    |

---

## **Scripts**
### **1. Serial Computation (`serial_computation.py`)**
- This script processes the data sequentially using **pandas**.
- Iterates through each student record and matches it with relevant fee payment dates from the fees dataset.
- Calculates the frequency of fee payment dates using a dictionary.
- result
### **Serial Computation (serial_computation.py)**
| Student Name      | Student ID | Major        | Most Consistent Payment Day |
|-------------------|------------|--------------|-----------------------------|
| Scott Conner      | SID1000    | Art          | 20                          |
| Daniel Harrison   | SID1001    | Engineering  | 1                           |
| Lisa Mclaughlin   | SID1002    | Biology      | 26                          |
| Richard Guerra    | SID1003    | Psychology   | 13                          |
| Beth Hess         | SID1004    | Biology      | 24                          |

- **Execution Time**: 93.1830 seconds


### **2. Parallel Computation (`multiprocessing_computation.py`)**
- This script processes the data using Python's **multiprocessing** module.
- Distributes the processing of student records across multiple CPU cores to reduce computation time.
- Also calculates the frequency of fee payment dates using dictionaries, but in parallel.

### **Parallel Computation (multiprocessing_computation.py)**
| Student Name      | Student ID | Major        | Most Consistent Payment Day |
|-------------------|------------|--------------|-----------------------------|
| Scott Conner      | SID1000    | Art          | 20                          |
| Daniel Harrison   | SID1001    | Engineering  | 1                           |
| Lisa Mclaughlin   | SID1002    | Biology      | 26                          |
| Richard Guerra    | SID1003    | Psychology   | 13                          |
| Beth Hess         | SID1004    | Biology      | 24                          |

- **Execution Time**: 29.7680 seconds
