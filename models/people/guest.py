import services.booking as rs
import models.things.room as rm
import models.database as db

class Guest:
    def __init__(self, name, id, phone, pais, room):
        self.name = name # str
        self.id = id # int
        self.phone = phone # str
        self.pais = pais # str
        self.room = room # int

    def setReserva(habitacion, cantidad_dias, cantidad_personas, huesped):
        if (type(cantidad_dias) == int) and (type(cantidad_personas) == int):
            nombre = huesped.name
            telefono = huesped.phone
            pais = huesped.pais
            pieza = habitacion.room
            
            if (rs.BookingService.getDisponibilidad(pieza)):
                conn = db.conn()
                cursor = conn.cursor()
                consulta = """
                    insert into reservas (nombre, telefono, pais, pieza, cantidad_personas, cantidad_dias)
                    values (?, ?, ?, ?, ?, ?)
                """

                cursor.execute(consulta, (nombre, telefono, pais, pieza, cantidad_personas, cantidad_dias))
                conn.commit()

                return { "msg": "Reserva realizada" }
            else:
                return { "msg": "Pieza ocupada" }
        else:
            print("Error al generar la reserva")