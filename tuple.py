print("===== STUDENT EXAM ELIGIBILITY CHECKER =====")

name = input("Enter student name: ")
marks = int(input("Enter marks (0-100): "))

print("Student Name:", name)
print("Marks:", marks)

if marks >= 50:
    print("Result: PASS ✅")
    print("Status: Eligible for exam 🎉")
else:
    print("Result: FAIL ❌")
    print("Status: Not eligible for exam")