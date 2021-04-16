
    # this is flight function
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger = []

    def add_passenger(self, name):
        if not self.open_seats():
           return False 
        self.passenger.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passenger)


flight = Flight(3)

people = ["Ross", "Rachel", "Monica", "Chandler","Joey","Phoebe"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight sucessfully.")
    else:
        print(f"No available seats for that {person} ")
