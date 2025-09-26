class SchoolManagement:
    def __init__(self):
        self.students = {}
        self.student_id_counter = 1000

    def new_admission(self):
        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        if not (5 <= age <= 18):
            print("Invalid age, admission denied.")
            return
        student_class = int(input("Enter class (1–12): "))
        mobile = input("Enter guardian's mobile (10 digits): ")

        if len(mobile) != 10 or not mobile.isdigit():
            print("Invalid mobile number.")
            return

        self.student_id_counter += 1
        sid = self.student_id_counter
        self.students[sid] = {
            "name": name,
            "age": age,
            "class": student_class,
            "mobile": mobile,
        }
        print(f"Admission successful! Student ID = {sid}")

    def view_student(self):
        sid = int(input("Enter student ID: "))
        if sid in self.students:
            print("Student Details:", self.students[sid])
        else:
            print("Student not found.")

    def update_student(self):
        sid = int(input("Enter student ID: "))
        if sid not in self.students:
            print("Student not found.")
            return
        print("1. Update Mobile\n2. Update Class")
        ch = input("Enter choice: ")
        if ch == "1":
            mobile = input("Enter new mobile (10 digits): ")
            if len(mobile) == 10 and mobile.isdigit():
                self.students[sid]["mobile"] = mobile
                print("Mobile updated ✅")
            else:
                print("Invalid mobile.")
        elif ch == "2":
            new_class = int(input("Enter new class: "))
            self.students[sid]["class"] = new_class
            print("Class updated ✅")

    def remove_student(self):
        sid = int(input("Enter student ID: "))
        if sid in self.students:
            del self.students[sid]
            print("Student record removed ❌")
        else:
            print("Student not found.")

    def run(self):
        while True:
            print("\n1. New Admission\n2. View Student\n3. Update Info\n4. Remove Student\n5. Exit")
            ch = input("Enter choice: ")
            if ch == "1":
                self.new_admission()
            elif ch == "2":
                self.view_student()
            elif ch == "3":
                self.update_student()
            elif ch == "4":
                self.remove_student()
            elif ch == "5":
                break
            else:
                print("Invalid choice!")
