class Staff:
    # class attributes
    staffid = ""
    name = ""
    gradelvl = ""
    step = ""
    dept = ""
    faculty = ""
    pensioncode = ""
    pfa = ""
    bank = ""
    accountno = ""


# create new staff object
newstaff = Staff()

print("Staff ID:")
newstaff.staffid = input()

print("Staff Name:")
newstaff.name = input()

print("Grade Level:")
newstaff.gradelvl = input()

print("Step:")
newstaff.step = input()

print("Department:")
newstaff.dept = input()

print("Faculty:")
newstaff.faculty = input()

print("Pension Code:")
newstaff.pensioncode = input()

print("PFA:")
newstaff.pfa = input()

print("Bank:")
newstaff.bank = input()

print("Account No:")
newstaff.accountno = input()

print("\n")

# Output staff information on a single line
output = "Staff ID: " + newstaff.staffid + " | Staff Name: " + newstaff.name + " | Grade level: " + newstaff.gradelvl + " | Step: " + newstaff.step + " | Department: " + newstaff.dept + \
    " | Faculty: " + newstaff.faculty + " | Pension Code: " + newstaff.pensioncode + " | PFA: " + \
    newstaff.pfa + " | Bank: " + newstaff.bank + \
    " | Account no: " + newstaff.accountno

print(output)

# Write staff information to a file
with open('staffdata.txt', 'a') as f:
    f.write(output + "\n")
