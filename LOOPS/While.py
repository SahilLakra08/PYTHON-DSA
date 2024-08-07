#PTM-INPUT ROLL NUMBER AND PARENTS NAME UNTIL PARENTS ARE COMING
parent_status='Y'
while(parent_status=="Y"):
    RollNo=int(input("Student Roll Number: "))
    Parents_Name=input("Parents_name: ")
    print(RollNo,Parents_Name)
    parent_status=input("Next Parent=")