from Modelos.Partido import Partido

class ControladorPartido():
    def __init__(self):
        print("Creando ControladorPartido")

    def index(self):
        print("Listar todos los Partidos")
        unPartido = {
            "_id": "p1",
            "nombre": "verde",
            "lema": "verde verde"
        }
        return [unPartido]

    def create(self, infoPartido):
        print("Crear un Partido")
        elPartido = Partido(infoPartido)
        return elPartido.__dict__

    def show(self, id):
        print("Mostrando un Partido con id ", id)
        elPartido = {
            "_id": "p1",
            "nombre": "verde",
            "lema": "verde verde"
        }
        return elPartido

    def update(self, id, infoPartido):
        print("Actualizando Partido con id ", id)
        elPartido = Partido(infoPartido)
        return elPartido.__dict__

    def delete(self, id):
        print("Elimiando Partido con id ", id)
        return {"deleted_count": 1}
