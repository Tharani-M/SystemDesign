from TicketBooking import bookTicket
from passenger import passengers as p

class TicketCancelling(bookTicket):
    def __init__(self):
        super().__init__()
        self.preferenceTracker = None
        self.cancelledSeatNumber = 0
        self.seatNumberWithBerth = {}
    
    def cancelling(self, id):
        # Search in confirmed list
        for passenger in self.confirmedList:
            if passenger.id == id:
                self.cancel(passenger)
                print(f"Ticket {id} cancelled successfully")
                return True
        
        # Search in RAC queue
        for passenger in self.racQueue:
            if passenger.id == id:
                self.cancel(passenger)
                print(f"RAC Ticket {id} cancelled successfully")
                return True
                
        # Search in waiting queue
        for passenger in self.waitingQueue:
            if passenger.id == id:
                self.cancel(passenger)
                print(f"Waiting Ticket {id} cancelled successfully")
                return True
                
        print("Invalid ticket id")
        return False
    
    def cancel(self, passenger):
        ticket_type = passenger.getTicketType()
        
        if ticket_type == "berth":
            self.preferenceTracker = passenger.getPreference()
            self.cancelledSeatNumber = passenger.getSeatNumber()
            self.seatNumberWithBerth[self.cancelledSeatNumber] = self.preferenceTracker
            self.deleteFromAllLists(passenger)
            
            # Move RAC to berth if available
            if self.racQueue:
                rac_passenger = self.racQueue.pop(0)
                self.addRacToBerth(rac_passenger)
            
            # Move waiting to RAC if available
            if self.waitingQueue:
                waiting_passenger = self.waitingQueue.pop(0)
                self.addWaitingToRac(waiting_passenger)
                
        elif ticket_type == "RAC":
            self.racQueue.remove(passenger)
            # Move waiting to RAC if available
            if self.waitingQueue:
                waiting_passenger = self.waitingQueue.pop(0)
                self.addWaitingToRac(waiting_passenger)
                
        else:  # Waiting list
            self.waitingQueue.remove(passenger)
    
    def addWaitingToRac(self, passenger):
        if passenger is not None:
            passenger.setTicketType("RAC")
            self.racQueue.append(passenger)
    
    def addRacToBerth(self, passenger):
        if passenger is not None and self.preferenceTracker is not None:
            passenger.setPreference(self.preferenceTracker)
            passenger.setSeatNumber(self.cancelledSeatNumber)
            passenger.setTicketType("berth")

            # Add to appropriate berth list
            if self.preferenceTracker == 'U':
                self.upperList.append(passenger)
            elif self.preferenceTracker == 'M':
                self.middleList.append(passenger)    
            else:  # 'L'
                self.lowerList.append(passenger)

            self.confirmedList.append(passenger)
            
            # Remove from seatNumberWithBerth and reset trackers
            if self.cancelledSeatNumber in self.seatNumberWithBerth:
                del self.seatNumberWithBerth[self.cancelledSeatNumber]
            self.preferenceTracker = None
            self.cancelledSeatNumber = 0
    
    def deleteFromAllLists(self, passenger):
        # Remove from all lists
        if passenger in self.confirmedList:
            self.confirmedList.remove(passenger)
        if passenger in self.upperList:
            self.upperList.remove(passenger)
        if passenger in self.middleList:
            self.middleList.remove(passenger)    
        if passenger in self.lowerList:
            self.lowerList.remove(passenger)
    
    def getSeatNumberWithBerth(self):
        return self.seatNumberWithBerth
    
    def displayAllTickets(self):
        """Utility method to display all tickets"""
        print("\n=== CONFIRMED TICKETS ===")
        for passenger in self.confirmedList:
            print(passenger)
        
        print("\n=== RAC TICKETS ===")
        for passenger in self.racQueue:
            print(passenger)
        
        print("\n=== WAITING LIST TICKETS ===")
        for passenger in self.waitingQueue:
            print(passenger)