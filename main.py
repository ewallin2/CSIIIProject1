import csv
import os

def load_data(filename):
    """Load student data from a CSV file and keep it sorted."""
    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "First Name", "Last Name", "Grade", "Class", "Email"])
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
        return sorted(data, key=lambda x: x["ID"])  # Sort by ID once on load

def save_data(filename, data):
    """Save student data to a CSV file."""
    with open(filename, 'w', newline='') as file:
        fieldnames = ["ID", "First Name", "Last Name", "Grade", "Class", "Email"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def create_student(filename):
    """Add a new student."""
    data = load_data(filename)
    student_id = input("Enter student ID: ")
    if any(student['ID'] == student_id for student in data):
        print("Error: Student ID already exists.")
        return
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    grade = input("Enter grade: ")
    student_class = input("Enter class: ")
    email = input("Enter email: ")
    
    data.append({"ID": student_id, "First Name": first_name, "Last Name": last_name, "Grade": grade, "Class": student_class, "Email": email})
    save_data(filename, data)
    print("Student added successfully.")

def read_student(filename):
    """Retrieve a student record by ID."""
    data = load_data(filename)
    student_id = input("Enter student ID to read: ")
    student = next((s for s in data if s['ID'] == student_id), None)
    if student:
        print(student)
    else:
        print("Student not found.")

def update_student(filename):
    """Update an existing student record."""
    data = load_data(filename)
    student_id = input("Enter student ID to update: ")
    student = next((s for s in data if s['ID'] == student_id), None)
    if not student:
        print("Student not found.")
        return
    
    print("Available fields to update: ID, First Name, Last Name, Grade, Class, Email")
    field = input("Enter the name of the feature to update: ")
    if field not in student:
        print("Invalid feature.")
        return
    new_value = input(f"The {field} feature is currently {student[field]}, what do you want to update it to? ")
    student[field] = new_value
    save_data(filename, data)
    print("Student updated successfully.")

def delete_student(filename):
    """Delete a student record with confirmation."""
    data = load_data(filename)
    student_id = input("Enter student ID to delete: ")
    student = next((s for s in data if s['ID'] == student_id), None)
    if not student:
        print("Student not found.")
        return
    
    confirm = input(f"Are you sure you want to delete {student['First Name']} {student['Last Name']} (ID: {student_id})? (Y/N): ").strip().lower()
    if confirm != 'y':
        print("Deletion cancelled.")
        return
    
    data = [s for s in data if s['ID'] != student_id]
    save_data(filename, data)
    print("Student deleted successfully.")

def binary_search(data, target, key):
    """Binary search to find a student by ID or name."""
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid][key] == target:
            return mid
        elif data[mid][key] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def mergesort(data, key):
    """MergeSort algorithm to sort student data."""
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = mergesort(data[:mid], key)
    right = mergesort(data[mid:], key)
    return merge(left, right, key)

def merge(left, right, key):
    """Helper function for MergeSort."""
    sorted_list = []
    while left and right:
        if left[0][key] < right[0][key]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    return sorted_list + left + right

def sort_students(filename):
    """Sort students by a specified attribute."""
    data = load_data(filename)
    attribute = input("Specify which attribute to sort on (Last Name, Class, ID): ")
    if attribute not in ["Last Name", "Class", "ID"]:
        print("Invalid attribute.")
        return
    sorted_data = mergesort(data, attribute)
    save_data(filename, sorted_data)
    print("Students sorted successfully.")

def main():
    filename = "students.csv"
    while True:
        print("""
----------------------------------------
        STUDENT MANAGEMENT SYSTEM       
----------------------------------------
[C] Create a new student
[R] Read student details
[S] Search student by ID
[T] Sort students by attribute
[U] Update student information
[D] Delete a student record
[E] Exit the program
""")
        command = input("Enter your choice: ").lower()
        if command in ["c"]:
            create_student(filename)
        elif command in ["r"]:
            read_student(filename)
        elif command in ["u"]:
            update_student(filename)
        elif command in ["d"]:
            delete_student(filename)
        elif command in ["s"]:
            key = "ID" if input("Search by ID or Name?: ").lower() == "id" else "Last Name"
            term = input("Enter search term: ")
            students = load_data(filename)
            students.sort(key=lambda x: x[key])
            index = binary_search(students, term, key)
            print(students[index] if index != -1 else "Student not found.")
        elif command in ["t"]:
            sort_students(filename)
        elif command in ["e"]:
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
