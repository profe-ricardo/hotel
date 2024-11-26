from models.things.room import Room
from models.people.guest import Guest

class BookingService:
    def __init__(self):
        self.rooms = [] # [103, 104, 105, 106]
        self.guests = [] # 
    
    def getDisponibilidad(room):
        disponibilidad = Room.getDisponibilidad(room)

        if disponibilidad and not disponibilidad["error"]:
            return True
        else:
            return False
    
    def setReserva(self, guest, room):
        pass