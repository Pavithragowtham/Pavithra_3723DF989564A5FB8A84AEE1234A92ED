class Student:
    def __init__(self, name, roll_number, mark):
        self.name = name
        self.roll_number = roll_number
        self.mark = mark  # Corrected to use mark

    def __str__(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}, Marks: {self.mark}"

def sort_students(student_list):
    # Sort the list of students based on marks in descending order
    sorted_students = sorted(student_list, key=lambda student: student.mark, reverse=True)
    return sorted_students

# Create instances of the Student class
students = [
    Student("Miller", "A02121", 70),
    Student("Leo", "B02123", 75),
    Student("Rolex", "C02124", 85),
    Student("Vikram", "D02125", 95)
]

# Sort the students by Marks
sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print(student)

