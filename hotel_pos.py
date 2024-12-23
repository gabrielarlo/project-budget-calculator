class HotelPOS:
    def __init__(self):
        self.rooms = {}
        self.services = {}
        self.bookings = {}

    def add_room(self, room_number, room_type, price):
        self.rooms[room_number] = {'type': room_type, 'price': price, 'booked': False}
        print(f"Room {room_number} added.")

    def book_room(self, room_number, guest_name):
        if room_number in self.rooms and not self.rooms[room_number]['booked']:
            self.rooms[room_number]['booked'] = True
            self.bookings[guest_name] = room_number
            print(f"Room {room_number} booked for {guest_name}.")
        else:
            print(f"Room {room_number} is not available.")

    def add_service(self, service_name, price):
        self.services[service_name] = price
        print(f"Service {service_name} added.")

    def bill_guest(self, guest_name):
        if guest_name in self.bookings:
            room_number = self.bookings[guest_name]
            room_cost = self.rooms[room_number]['price']
            print(f"Billing for {guest_name}:")
            print(f"Room {room_number} ({self.rooms[room_number]['type']}): ${room_cost:.2f}")
            # Add more billing details as needed
        else:
            print(f"No booking found for {guest_name}.")


if __name__ == "__main__":
    pos = HotelPOS()
    pos.add_room(101, "Single", 100)
    pos.add_room(102, "Double", 150)
    pos.book_room(101, "John Doe")
    pos.add_service("Breakfast", 20)
    pos.bill_guest("John Doe")
