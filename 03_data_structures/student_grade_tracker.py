# You have a dictionary of student exam scores 
# across different subjects and need to calculate each student's average and assign a pass/fail status.
# using Nested data aggregator

students = {
    "Alice": {"Math": 85, "Science": 90, "History": 78},
    "Bob": {"Math": 92, "Science": 88, "History": 95},
    "Charlie": {"Math": 78, "Science": 85, "History": 82},
    "David": {"Math": 70, "Science": 65, "History": 75}
}

report = {}

for student, subjects in students.items():
    scores = subjects.values()
    avg_score = sum(scores) / len(scores)
    if avg_score >= 75:
        status = "Pass"
    else:
        status = "Fail"

    report[student] = {"Average": f"{avg_score:.2f}", "status": status}
    
    print(f"Student: {student}")
    print(f"Average Score: {avg_score:.2f}")
    print(f"Status: {status}")

    print("\nComprehensive Report: ", report)    
    
