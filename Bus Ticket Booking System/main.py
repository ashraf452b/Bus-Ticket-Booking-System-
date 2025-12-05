# from bus import Bus,BusSystem
# cholo=BusSystem('cholo')
# print(cholo)
# BusSystem.add_bus(cholo,123,'DhakaToctg',40)
# from passenger import Passenger
# pas=Passenger('sherlock',123,123)
# cholo.book_ticket(123,pas)
# print(cholo.Show_buses())


from bus import Bus,BusSystem
from passenger import Passenger
from admin import Admin

cholo_bhai=BusSystem('Cholo Bhai')

admin=Admin()

is_login=False
while True:
    print('--------Bus Ticket Booking System-----------')
    print('1. Admin Login')
    print('2. Book Ticket')
    print('3. View Buses')
    print('4. Exit')
    n=int(input('Enter Your Choice  '))
    if n== 1:
        username=input('Enter Your Username ')
        password=input('Enter Your Password ')
        if admin.login(username,password):
            is_login=True
            print('Admin Login Succesfully')

        if is_login is False:
            print('Invalid admin credentials')

        while is_login:
            print("\n--- ADMIN MENU ---")
            print("1. Add Bus")
            print("2. View All Buses")
            print("3. Logout")
            m=int(input('Admin! Enter Your Choice '))
            if m==1:
                number=input('Enter a bus number')
                route=input('Enter Bus Route ')
                seats=input('Enter Bus seats ')
                if(seats.isdigit()):
                    admin.add_bus(cholo_bhai,number,route,int(seats))
                else:
                    print('Seats Must be a integer')
            elif m==2:
                cholo_bhai.Show_buses()
            elif m==3:
                print('Logged Out')
                is_login=False
            else:
                print('Invalid input. Please Try again')
         
    elif n==2:
        name=input('Enter Your Name ')
        phone=input('Enter Your Phone ')
        bus=input('Enter Bus Number')
        pas=Passenger(name,phone,bus)
        cholo_bhai.book_ticket(bus,pas)
    elif n== 3:
        print('\n')

        cholo_bhai.Show_buses()
        print('\n')
    elif n==4:
        print('Exiting Programme')
        break
    else:
        print('Invalid Choice . Try Again!')

