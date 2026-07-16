# student grade classifier
print("\n~~ student grade classifier ~~\n")

student_name = input("Enter your name: ")
marks = (float(input("Mark for 1 subject: ")),
         float(input("Mark for 2 subject: ")),
         float(input("Mark for 3 subject: ")))

avg_grade = sum(marks)/len(marks)

status = "Pass"

if avg_grade >= 80:
    assign_letter = "A"
elif avg_grade >=70 and avg_grade <=79:
    assign_letter = "B"
elif avg_grade >=60 and avg_grade <=69:
    assign_letter = "C"
elif avg_grade >=50 and avg_grade <=59:
    assign_letter = "D"
elif avg_grade < 50:
    assign_letter = "F"
    status = "Fail"
intervention = None
if avg_grade < 40:
    intervention = "needs intervention"

print(f"""\nStudent report card: 
Name: {student_name}
Average: {avg_grade}
Grade: {assign_letter}
intervention Flag: {intervention}""")