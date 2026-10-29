#Add Students Details
def add_students():
    id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    place = input("Enter Student place: ")

    with open("students.txt", "r") as f:
        data = f.readlines()
        for line in data:
            details = line.split(',')
            stu_id = int(details[0])
            if stu_id == id:
                print("This ID already Exist")
                return

    with open('students.txt', 'a') as f:
        f.write(f"{id}, {name}, {age}, {place}\n")
        print("Student details added successfully")

#delete studdents
def delete_student():
    with open("students.txt", 'r') as f:
        data = f.readlines()
        if len(data) == 0:
            print("No data available in the database")
            return
    id = int(input("Enter Student ID: "))
    with open("students.txt", "r") as f:
        data = f.readlines()
    is_found = False
    with open("students.txt", "w") as f: 
        for line in data:
            details = line.split(',')
            stu_id = int(details[0])
            if stu_id != id:
                f.write(line)
            else:
                is_found = True
    if is_found:
        print("Student Deleted Succesfully")
    else:
        print("Student Not Found")
   


#update Student details
def update_stu_details():
    with open("students.txt", 'r') as f:
        data = f.readlines()
        if len(data) == 0:
            print("No data available in the database")
            return
    id = int(input("Enter Student ID: "))
    with open("students.txt", "r") as f:
        data = f.readlines()
    is_found = False
    with open("students.txt", "w") as f: 
        for line in data:
            details = line.split(',')
            stu_id = int(details[0])
            if stu_id == id:
                is_found = True
                while True:
                    print("\n1) To Udate Name")
                    print("2) To Udate Age")
                    print("3) To Udate Place")
                    print("4) To Udate All")
                    print("5) To Exit")
                    choice = int(input("Enter your choice: "))
                    match choice:
                        case 1:
                            name = input("Enter New Name: ")
                            f.write(f"{details[0]}, {name}, {details[2]}, {details[3]}")
                            print("New Name updated successfully!")
                        case 2:
                            age = int(input("Enter New Age: "))
                            f.write(f"{details[0]}, {details[1]}, {age}, {details[3]}")
                            print("New age updated successfully!")
                        case 3:
                            place = input("Enter New Place: ")
                            f.write(f"{details[0]}, {details[1]}, {details[2]}, {place}")
                            print("New place updated succesfully!")
                        case 4:
                            name = input("Enter New Name: ")
                            age = int(input("Enter New Age: "))
                            place = input("Enter New Place: ")
                            f.write(f"{details[0]}, {name}, {age}, {place}")
                            print("All details updated successfully!")
                        case 5:
                            print("Thank You! visite again..")
                            break
                        case _:
                            
                            print("You Entered Invalid Choice!")
            else:
                f.write(line)
    if not is_found:
        print("Student Not Found!")

#Search student
def search_student():
    with open("students.txt","r") as f:
        data = f.readlines()
        if len(data) == 0:
            print("No data available in the dataset")
            return
    id = int(input("Enter Student ID: "))
    with open("students.txt","r") as f:
        data = f.readlines()
        for line in data:
            details = line.strip().split(',')
            stu_id = int(details[0])
            if stu_id == id:
                print("---------------------------------")
                print("|ID |Name      |Age  |Place     |")
                print("---------------------------------")
                print(f'|{details[0] + " " * (3 - len(details[0]))}|{details[1] + " " * (10 - len(details[1]))}|{details[2] + " " * (5 - len(details[2]))}|{details[3] + " " * (10 - len(details[3]))}|')
                print("--------------------------------- ")
                return
    print("Student Not Found")    
    
#View all students
def view_all_students():
    with open("students.txt","r") as f:
        data = f.readlines()
        if len(data) == 0:
            print("No data available in the dataset") 
            return
    with open("students.txt", "r") as f:
        data = f.readlines() 
        print("---------------------------------")
        print("|ID |Name      |Age  |Place     |")
        print("---------------------------------")
        for line in data:
            details = line.strip().split(",")
            print(f'|{details[0] + " " * (3 - len(details[0]))}|{details[1] + " " * (10 - len(details[1]))}|{details[2] + " " * (5 - len(details[2]))}|{details[3] + " " * (10 - len(details[3]))}|')
            print("--------------------------------- ")
        return    
    print("Student Not Found")
while True:
    print("1) To Add Students")
    print("2) To Delete Students")
    print("3) To Update Students")
    print("4) To Search Students")
    print("5) To View All Students")
    print("6) To Exit")
    choice = int(input("Enter Your Choice: "))
    match choice:
        case 1:
            add_students()
        case 2:
            delete_student()
        case 3:
            update_stu_details()
        case 4:
            search_student()
        case 5:
            view_all_students()
        case 6:
            print("Thank You! Visit Again..")
            break
        case _:
            print("You Entered Invalid Choice")

