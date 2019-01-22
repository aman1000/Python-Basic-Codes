ca_total=100
ca_wtg=25
mtt_total=40
mtt_wtg=20
ete_total=70
ete_wtg=50
course_code=input("Enter Course Code:")
ca_obtained_marks=float(input("Enter total CA obtained marks:"))
mtt_obtained_marks=float(input("Enter total MTT obtained marks:"))
ete_obtained_marks=float(input("Enter total ETE obtained marks:"))
ATT=float(input("Enter total Attendance Marks:"))
CA=(ca_obtained_marks*ca_wtg)/ca_total
MTT=(mtt_obtained_marks*mtt_wtg)/mtt_total
ETE=(ete_obtained_marks*ete_wtg)/ete_total

Total=CA+MTT+ETE+ATT
print("----REPORT CARD----")
print("Percentage in course_code",course_code,Total,end="")
print("%")
print("CGPA in course_code:",course_code,Total/10,end="")
