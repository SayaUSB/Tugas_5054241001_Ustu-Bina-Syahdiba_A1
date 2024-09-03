# Input
grade = input("Enter desired grade => ")
rerata_minimal = float(input("Enter minimum average required => "))
rerata_skrg = float(input("Enter current average in course => "))
persentase_exam = float(input("Enter how much the final counts as a percentage of the course grade => "))

# Kalkulasi
persentase_exam /= 100
required_score = rerata_minimal - rerata_skrg*abs(persentase_exam-1)
required_score /= persentase_exam

# Output
print(f"You need a score of {required_score:.2f} on the final to get a {grade}")