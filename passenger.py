class passengers:
    id = 1
    
    def __init__(self, name, age=None, preference=None):
        self.name = name
        self.age = age
        self.preference = preference
        self.id = passengers.id  # Assign current id
        passengers.id += 1       # Then increment for next
        self.number = None
        self.ticketType = None
    
    # Add getter/setter methods
    def setTicketType(self, ticket_type):
        self.ticketType = ticket_type
    
    def getTicketType(self):
        return self.ticketType
    
    def setSeatNumber(self, number):
        self.number = number
    
    def getSeatNumber(self):
        return self.number
    
    def getPreference(self):
        return self.preference
    
    def setPreference(self, preference):
        self.preference = preference
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.id}, Preference: {self.preference}, Seat: {self.number}, Type: {self.ticketType}"