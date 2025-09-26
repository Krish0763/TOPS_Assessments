class ClinicAppointment:
    def __init__(self):
        self.appointments = {}  # {doctor: {slot: [patients]}}
        self.slots = ["10am", "11am", "12pm", "2pm", "3pm"]

    def book_appointment(self):
        name = input("Enter patient name: ")
        age = int(input("Enter age: "))
        mobile = input("Enter mobile number: ")
        doctor = input("Enter preferred doctor: ")

        if doctor not in self.appointments:
            self.appointments[doctor] = {slot: [] for slot in self.slots}

        print("\nAvailable Slots:")
        for slot in self.slots:
            print(f"{slot}: {len(self.appointments[doctor][slot])}/3 booked")

        slot = input("Choose a slot: ")

        if slot not in self.slots:
            print("Invalid slot!")
            return

        if len(self.appointments[doctor][slot]) < 3:
            self.appointments[doctor][slot].append(
                {"name": name, "age": age, "mobile": mobile}
            )
            print(f"Appointment booked with Dr.{doctor} at {slot} ✅")
        else:
            print("Slot full, please choose another.")

    def view_cancel(self):
        mobile = input("Enter your mobile number: ")
        for doctor, slots in self.appointments.items():
            for slot, patients in slots.items():
                for p in patients:
                    if p["mobile"] == mobile:
                        print(f"Found {p['name']} with Dr.{doctor} at {slot}")
                        choice = input("Cancel? (y/n): ")
                        if choice.lower() == "y":
                            patients.remove(p)
                            print("Appointment cancelled ❌")
                        return
        print("No appointment found.")

    def run(self):
        while True:
            print("\n1. Book Appointment\n2. View/Cancel Appointment\n3. Exit")
            ch = input("Enter choice: ")
            if ch == "1":
                self.book_appointment()
            elif ch == "2":
                self.view_cancel()
            elif ch == "3":
                break
            else:
                print("Invalid choice!")
