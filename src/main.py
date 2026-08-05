print("Student Risk Checker")
print("--------------------")

student_name = input("Enter student name: ")
score = float(input("Enter score from 0 to 100: "))
attendance = float(input("Enter attendance percentage from 0 to 100: "))
assignment_completed_input = input("Assignment completed? (yes/no): ")

assignment_completed_input = assignment_completed_input.lower()

if assignment_completed_input == "yes":
    assignment_completed = True
elif assignment_completed_input == "no":
    assignment_completed = False
else:
    assignment_completed = None

print()
print("Risk Assessment")
print("---------------")

if score < 0 or score > 100:
    print("Invalid score. Score must be between 0 and 100.")
elif attendance < 0 or attendance > 100:
    print("Invalid attendance. Attendance must be between 0 and 100.")
elif assignment_completed is None:
    print("Invalid assignment input. Please enter yes or no.")
else:
    if score >= 70 and attendance >= 80 and assignment_completed:
        risk_level = "Low Risk"
    elif score >= 50 and attendance >= 60:
        risk_level = "Medium Risk"
    else:
        risk_level = "High Risk"

    print(f"Student name: {student_name}")
    print(f"Score: {score}")
    print(f"Attendance: {attendance}%")
    print(f"Assignment completed: {assignment_completed}")
    print(f"Risk level: {risk_level}")



