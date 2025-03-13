Student Management System

Overview

This Python project is a Student Management System that allows users to create, read, update, delete, search, and sort student records stored in a CSV file. The system is designed to be efficient and user-friendly with a command-line interface (CLI).

Features

CRUD Operations

Create: Add a new student with a unique ID.

Read: Retrieve student details by ID.

Update: Modify an existing student’s information.

Delete: Remove a student (with confirmation prompt).

Handles edge cases such as duplicate IDs and invalid fields.

Binary Search

Searches students by ID or Last Name.

If multiple students share the same name, prompts for ID selection.

Data is sorted once before searching for efficiency.

Sorting (MergeSort Implementation)

Allows sorting by Last Name, Class, or ID.

MergeSort was chosen for its stability and consistent performance.

User-Friendly CLI

Case-insensitive commands (C for Create, R for Read, etc.).

Displays available fields when updating.

Confirms before deleting a student.

Justification for Sorting Algorithm

MergeSort vs. QuickSort

MergeSort:

Time Complexity: O(n log n)

Space Complexity: O(n)

Stability: Yes

Pros: Always O(n log n), stable, predictable performance

Cons: Uses extra memory

QuickSort:

Time Complexity: O(n log n) (average), O(n²) (worst case)

Space Complexity: O(log n)

Stability: No

Pros: Faster in most cases, in-place sorting (less memory usage)

Cons: Unstable, worst-case time complexity of O(n²)

Why MergeSort was chosen:

Stability: Maintains the order of equal elements (important for students with the same last name).

Predictable Performance: Unlike QuickSort, MergeSort consistently runs in O(n log n) time.

Best for Structured Data: Since student records may contain duplicate last names, we needed a stable sort.

Pros and Cons of Binary Search

Binary Search:

Time Complexity: O(log n)

Pros: Faster than linear search, efficient for large datasets

Cons: Requires sorted data beforehand

Linear Search:

Time Complexity: O(n)

Pros: Works on unsorted data

Cons: Slow for large datasets

Why Binary Search was chosen:

It is significantly faster than linear search for large datasets.

Since we sort data once on load, searching remains efficient throughout.

Helps scale the system if the number of students grows.

Running the Project

Run the main program:
python student_management_system.py

Run unit tests:
python -m unittest test_students.py

File Structure

student_management_system.py → Main application.

test_students.py → Unit tests for CRUD, search, and sorting.

students.csv → Database file (automatically created if missing).

Credits

Implementation: [Eric] & [Emmett] (Specify who worked on which parts if necessary)

Sorting Justification & Binary Search Explanation: [Eric] & [Emmett]

Testing & UI Enhancements: [Eric]