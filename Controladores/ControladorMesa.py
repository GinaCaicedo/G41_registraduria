from Modelos.Mesa import Mesa

class ControladorMesa():
    def __init__(self):
        print("Creando Controlador Mesa")

    def index(self):
        print("Listar todos los Mesas")
        unaMesa = {
            "_id": "m1",
            "numero": "1",
            "cantidad_inscritos": "100"}
        return [unaMesa]

    def create(self, infoMesa):
        print("Crear un Mesa")
        laMesa = Mesa(infoMesa)
        return laMesa.__dict__

    def show(self, id):
        print("Mostrando un Mesa con id ", id)
        laMesa = {
            "_id": "m1",
            "numero": "1",
            "cantidad_inscritos": "100"}
        return laMesa

    def update(self, id, infoMesa):
        print("Actualizando Mesa con id ", id)
        laMesa = Mesa(infoMesa)
        return laMesa.__dict__

    def delete(self, id):
        print("Elimiando Mesa con id ", id)
        return {"deleted_count": 1}
