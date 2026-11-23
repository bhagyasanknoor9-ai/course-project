
import sys
def calculate_grade(avg):
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 65:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"
if __name__ == "__main__":
    name = sys.argv[1]
    department = sys.argv[2]
    semester = sys.argv[3]

    course1 = sys.argv[4]
    marks1 = int(sys.argv[5])
    course2 = sys.argv[6]
    marks2 = int(sys.argv[7])
    course3 = sys.argv[8]
    marks3 = int(sys.argv[9])
    total = marks1 + marks2 + marks3
    average = total / 3
    grade = calculate_grade(average)
    print("\n--- Student Details ---")
    print("Name       :", name)
    print("Department :", department)
    print("Semester   :", semester)
    print(course1, ":", marks1)
    print(course2, ":", marks2)
    print(course3, ":", marks3)
    print("Total      :", total)
    print("Average    :", round(average, 2))
    print("Grade      :", grade)
