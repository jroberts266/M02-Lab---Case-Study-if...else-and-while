# M02 Lab - Case Study: if...else and while
# author: jdr
# created: 2023-1-22  updated: 2022-01-14 (drm)
# evalutes GPAs to see if student qualifies for Dean's List or Honor Roll

lname = "Trump" # assigns a default value to lname variable
fname = "Donald" # assigns a default value to fname variable
GPA = 0 # assigns default value to GPA variable
while True:
    lname = input("Enter students last name:") # Asks for students last name
    if lname == "ZZZ": # Breaks loop if "ZZZ" is entered
        break
    fname = input("Enter students first name: ") # Asks for students first name
    GPA = float(input("Enter students GPA as a decimal: ")) # Asks for GPA assigns the value as a float to GPA variable
    # If statements to evaluate the entered GPA to determine if studnent made Honor Roll or Dean's List
    if GPA >= 3.5:
        print(fname, lname, " has made the Dean's List")
    elif GPA >= 3.25:
        print(fname, lname, "has made the Honor Roll")
    

