class bookTicket:
    berthLimit = 6 // 3  # Integer division
    racLimit = 1
    waitingListLimit = 1
    upperSeatNumber = 1
    middleSeatNumber = 2
    lowerSeatNumber = 3
    confirmedList = []
    upperList = []
    middleList = []
    lowerList = []
    racQueue = []
    waitingQueue = []
    
    def bookTickets(self, p):
        if len(self.upperList) == self.berthLimit and len(self.lowerList) == self.berthLimit and len(self.middleList) == self.berthLimit:
            if self.updateRacQueue(p):  # Use self, not class name
                print(f"Added to RAC your ticket id is {p.id}")
            elif self.updateWaitingQueue(p):
                print(f"Added to Waiting your ticket id is {p.id}")
            else:
                print("Tickets not available")
        elif self.checkAvailability(p):  # Correct method name
            print(f"Booking confirmed.\n {p}")
            p.setTicketType("berth")
            self.confirmedList.append(p)  # Use append, not add
        else:
            print(f"{p.preference} not available")
            self.availableList()

    def updateWaitingQueue(self, p):
        if len(self.waitingQueue) < self.waitingListLimit:
            p.setTicketType("Waiting List")
            self.waitingQueue.append(p)  # Use append
            return True
        return False

    def updateRacQueue(self, p):
        if len(self.racQueue) < self.racLimit:
            p.setTicketType("Rac")
            self.racQueue.append(p)  # Use append
            return True
        return False

    def checkAvailability(self, p):  # Correct spelling
        if p.getPreference() == 'U':  # Call method with ()
            if len(self.upperList) < self.berthLimit:
                p.setSeatNumber(self.upperSeatNumber)
                self.upperSeatNumber += 3
                self.upperList.append(p)
                return True
        elif p.getPreference() == 'M':
            if len(self.middleList) < self.berthLimit:
                p.setSeatNumber(self.middleSeatNumber)
                self.middleSeatNumber += 3
                self.middleList.append(p)
                return True
        elif p.getPreference() == 'L':
            if len(self.lowerList) < self.berthLimit:
                p.setSeatNumber(self.lowerSeatNumber)
                self.lowerSeatNumber += 3
                self.lowerList.append(p)
                return True
        return False
    def displayConfirmed(self):
        if len(self.confirmedList) == 0:
            print("No confirmed tickets")
        else:
            for p in self.confirmedList:
                print(p)