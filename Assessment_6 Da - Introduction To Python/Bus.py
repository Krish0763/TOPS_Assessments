class BusReservation:
    def __init__(self):
        self.routes = {
            "Mumbai-Pune": 500,
            "Delhi-Jaipur": 600,
            "Chennai-Bangalore": 700,
        }
        self.bookings = {}
        self.ticket_counter = 200
        self.seats = {route: [] for route in self.routes}

    def show_routes(self):
        print("\nAvailable Routes:")
        for route, price in self.routes.items():
            print(f"{route} - ₹{price}")

    def book_ticket(self):
        name = input("Enter passenger name: ")
        age = int(input("Enter age: "))
        mobile = input("Enter mobile number: ")
        self.show_routes()
        route = input("Enter route: ")

        if route not in self.routes:
            print("Invalid route.")
            return
        if len(self.seats[route]) >= 40:
            print("No seats available on this route.")
            return

        self.ticket_counter += 1
        tid = self.ticket_counter
        seat_no = len(self.seats[route]) + 1
        booking = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "route": route,
            "seat": seat_no,
            "price": self.routes[route],
        }
        self.bookings[tid] = booking
        self.seats[route].append(tid)
        print(f"Ticket booked ✅ | Ticket ID: {tid}, Seat: {seat_no}")

    def view_ticket(self):
        tid = int(input("Enter Ticket ID: "))
        if tid in self.bookings:
            print("Ticket Details:", self.bookings[tid])
        else:
            print("Ticket not found.")

    def cancel_ticket(self):
        tid = int(input("Enter Ticket ID: "))
        if tid in self.bookings:
            route = self.bookings[tid]["route"]
            self.seats[route].remove(tid)
            del self.bookings[tid]
            print("Ticket cancelled ❌")
        else:
            print("Ticket not found.")

    def run(self):
        while True:
            print("\n1. Show Routes\n2. Book Ticket\n3. View Ticket\n4. Cancel Ticket\n5. Exit")
            ch = input("Enter choice: ")
            if ch == "1":
                self.show_routes()
            elif ch == "2":
                self.book_ticket()
            elif ch == "3":
                self.view_ticket()
            elif ch == "4":
                self.cancel_ticket()
            elif ch == "5":
                break
            else:
                print("Invalid choice!")
