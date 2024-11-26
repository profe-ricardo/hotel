import models.database as db
class Room:
    def __init__(self, room, location, cantidad_personas):
        self.room = room
        self.location = location
        self.cantidad_personas = cantidad_personas

    def getDisponibilidad(pieza):
        conn = db.conn()
        cursor = conn.cursor()
        consulta = "select disponibilidad from habitaciones where id = ?"
        disp = cursor.execute(consulta, (pieza,))
        disp = cursor.fetchone()

        if disp:
            cursor.close()
            conn.close()
            
            return disp
        else:
            return { "error": "Error al buscar en base de datos"}