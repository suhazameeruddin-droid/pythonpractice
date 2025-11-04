def calculate_average_marks(students):
    averages = {}
    for name, marks in students.items():
        averages[name] = round(sum(marks) / len(marks), 2)
    return averages

def find_top_performer(averages):
    top_student = max(averages, key=averages.get)
    return top_student

# Example input
students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}

# Calculations
average_marks = calculate_average_marks(students)
top_performer = find_top_performer(average_marks)

# Output
print("Average Marks:", average_marks)
print("Top Performer:", f'"{top_performer}"')
