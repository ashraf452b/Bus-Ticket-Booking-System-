from passenger import Passenger
class Bus:
    def __init__(self,number,route,total_seats):
        self.number=number
        self.route=route
        self.total_seats=total_seats
        self.booked_seats=0

    def available_seats(self):
        return self.total_seats-self.booked_seats
    
    def book_seat(self):
        if self.available_seats()>0:
            print('Congrates! You seat Booked')
            print("Fare: 500 TK")
            self.booked_seats+=1
        else:
            print('No Seats available on this Bus')


class BusSystem:
    def __init__(self,name):
        self.buses=[]
        self.passengers=[]
        self.name=name

    def add_bus(self,number,route,seats):
        new_bus=Bus(number,route,seats)
        self.buses.append(new_bus)
        print('Bus Added Succesfulluy')
    
    def find_bus(self,number):
        for bus in self.buses:
            if bus.number==number:
                return bus
        return None


    def book_ticket(self,bus_number,passenger): #number,route,total_seats
        is_busFound=self.find_bus(bus_number)
        if is_busFound:
            passenger.bus=is_busFound
            is_busFound.book_seat()
            self.passengers.append(passenger)
        else:
            print('Bus Not Found!')

    def Show_buses(self):
        if len(self.buses)>0:
            for bus in self.buses:
                print(f'Bus Number = {bus.number}\nRoute = {bus.route}\nTotal Seat = {bus.total_seats}\nAvailable Seats = {bus.available_seats()}\n')


    def __repr__(self):
        print(f'Bus Company Name = {self.name}')
        return ''
