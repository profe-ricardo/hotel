from models.things.room import Room
from models.people.guest import Guest

class BookingService:
    def __init__(self):
        self.rooms = []
        self.guests = []
    
    def check_room_availability(self, room):
        pass
    
    def book_room(self, guest, room):
        pass