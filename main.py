from models.people.manager import Manager
from models.people.chef import Chef
from models.things.food import FoodItem
from models.things.inventory import Inventory
from models.people.receptionist import Receptionist
from models.things.room import Room
from models.people.guest import Guest
from models.people.housekeeping import Housekeeping
from models.things.bill import Bill

from services.booking import BookingService
from services.billing import BillingService
from services.inventory import InventoryService

def main():
    # Crear instancias de algunos objetos del sistema
    manager = Manager(name="Alice", id=1, phone="1234567890", location="Office")
    chef = Chef(name="Bob", id=2, location="Kitchen")
    receptionist = Receptionist(name="Eve", id=3, phone="0987654321", location="Front Desk")
    housekeeping = Housekeeping(name="Carlos", id=4, location="Housekeeping Office")
    
    # Crear instancias de servicios
    booking_service = BookingService()
    billing_service = BillingService()
    inventory_service = InventoryService()

    # Crear habitaciones y añadirlas al servicio de reservas
    room1 = Room(room=101, location="First Floor")
    room2 = Room(room=102, location="First Floor")
    booking_service.add_room(room1)
    booking_service.add_room(room2)
    
    # Crear un huésped y hacer el check-in
    guest = Guest(name="John Doe", id=1001, phone="555-1234", address="123 Main St", room=101)
    booking_service.book_room(guest, room=101)
    
    # Generar factura para el huésped
    bill = billing_service.generate_bill(guest)
    print(f"Factura generada para el huésped {guest.name}: {bill.bill}")

    # Agregar un elemento de inventario
    inventory_item = Inventory(type="Food Supplies", status="Available")
    inventory_service.add_inventory_item(inventory_item)
    
    # Mostrar estado de algunas operaciones
    print(f"El huésped {guest.name} ha sido registrado en la habitación {guest.room}.")
    print(f"El inventario actual contiene: {inventory_service.list_inventory_items()}")

if __name__ == "__main__":
    main()