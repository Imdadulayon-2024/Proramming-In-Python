def calculate_average(marks):
    if not marks:
        return None

    for mark in marks:
        if not isinstance(mark, (int, float)) or isinstance(mark, bool):
            return None
        if mark < 0 or mark > 100:
            return None

    return sum(marks) / len(marks)


def classify_performance(average):
    if average is None:
        return "Invalid or Missing Marks"
    elif average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"


def display_report(students):
    print("\nSTUDENT PERFORMANCE REPORT")
    print("-" * 75)
    print(f"{'ID':<10}{'Name':<20}{'Average':<15}{'Performance'}")
    print("-" * 75)

    for student in students:
        student_id = student.get("id", "N/A")
        name = student.get("name", "Unknown")
        marks = student.get("marks", [])

        average = calculate_average(marks)

        if average is None:
            average_text = "N/A"
        else:
            average_text = f"{average:.2f}"

        performance = classify_performance(average)

        print(
            f"{student_id:<10}{name:<20}"
            f"{average_text:<15}{performance}"
        )

    print("-" * 75)


# Test data
students = [
    {"id": 101, "name": "Ayon", "marks": [85, 85, 85]},
    {"id": 102, "name": "Rahim", "marks": [75, 80, 85]},
    {"id": 103, "name": "Karim", "marks": [75, 80, 85]},
    {"id": 104, "name": "Nila", "marks": [90, 105, 80]},
    {"id": 105, "name": "Sadia", "marks": []},
    {"id": 106, "name": "Rafi", "marks": [50, 55, 60]}
]

display_report(students)