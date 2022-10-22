from Modelos.Mesa import Mesa


class ControladorMesa():
    def __init__(self):
        print("Creando ControladorMesa")

    def index(self):
        print("Listar todos los Mesas")
        unMesa = {
            "_id": "a12",
            "numero": "1",
            "cantidad_inscritos": "23"
        }
        return [unMesa]

    def create(self, infoMesa):
        print("Crear un Mesa")
        elMesa = Mesa(infoMesa)
        return elMesa.__dict__

    def show(self, id):
        print("Mostrando un Mesa con id ", id)
        elMesa = {

            "_id": "a12",
            "numero": "1",
            "cantidad_inscritos": "100"
        }
        return elMesa

    def update(self, id, infoMesa):
        print("Actualizando Mesa con id ", id)
        elMesa = Mesa(infoMesa)
        return elMesa.__dict__

    def delete(self, id):
        print("Elimiando Mesa con id ", id)
        return {"deleted_count": 1}
