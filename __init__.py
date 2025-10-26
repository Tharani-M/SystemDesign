from TicketBooking import bookTicket as b
from TicketCancelling import TicketCancelling as tc
from passenger import passengers as p

class ticketbooking:
    def __init__(self):
        self.booking_obj = b()
        self.cancel_obj = tc()
        self.run_menu()
    
    def run_menu(self):
        loop = True
        while loop:
            print('\n1.Book Ticket')
            print('2.Cancel Ticket')
            print('3.Display confirmed Ticket')
            print('4.Display RAC Ticket')
            print('5.Display Waiting Ticket')
            print('6.Exit')
            
            option = int(input('Enter your option : '))
            if option == 1:
                name = input("Enter your name: ")
                age = int(input("Enter your age: "))
                preference = input("Enter your preference (U/M/L): ").upper()
                self.booking_obj.bookTickets(p(name, age, preference))
            elif option == 2:
                id = int(input("Enter your ticket id: "))
                self.cancel_obj.cancelling(id)
            elif option == 3:
                self.booking_obj.displayConfirmed()
            elif option == 4:
                self.booking_obj.displayRAC()
            elif option == 5:
                self.booking_obj.displayWaiting()
            elif option == 6:
                loop = False
                print("Thank you")
            else:
                print("Invalid option")

ticket = ticketbooking()