class ClinicAppointment:
    def __init__(self):
        self.appointments = {}
        self.slots = ["10am", "11am", "12pm", "2pm", "3pm"]

    def book_appointment(self):
        name = input("Enter patient name: ")
        age = int(input("Enter age: "))
        mobile = input("Enter mobile number: ")
        doctor = input("Enter preferred doctor name: ")
        
        if doctor not in self.appointments:
            self.appointments[doctor] = {slot: [] for slot in self.slots}

        print("\nAvailable slots:")
        for slot in self.slots:
            booked = len(self.appointments[doctor][slot])
            print(f"{slot} - {booked}/3 booked")

        slot = input("Choose a slot: ")

        if slot not in self.slots:
            print("Invalid slot!")
            return

        if len(self.appointments[doctor][slot]) < 3:
            self.appointments[doctor][slot].append({
                "name": name, "age": age, "mobile": mobile
            })
            print(f"Appointment booked with Dr.{doctor} at {slot}. ✅")
        else:
            print("Slot full! Please choose another slot.")

    def view_cancel(self):
        mobile = input("Enter your mobile number to search: ")
        found = False
        for doctor, slots in self.appointments.items():
            for slot, patients in slots.items():
                for p in patients:
                    if p["mobile"] == mobile:
                        found = True
                        print(f"Found: {p['name']} with Dr.{doctor} at {slot}")
                        choice = input("Do you want to cancel? (y/n): ")
                        if choice.lower() == 'y':
                            patients.remove(p)
                            print("Appointment cancelled. ❌")
                        return
        if not found:
            print("No appointment found with this mobile.")

    def run(self):
        while True:
            print("\n1. Book Appointment\n2. View/Cancel\n3. Exit")
            ch = input("Enter choice: ")
            if ch == "1":
                self.book_appointment()
            elif ch == "2":
                self.view_cancel()
            elif ch == "3":
                break
            else:
                print("Invalid choice!")
