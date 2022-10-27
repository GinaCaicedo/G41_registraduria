from Repositorio.RepositorioMesa import RepositorioMesa
from Modelos.Mesa import Mesa

class ControladorMesa():
    def __init__(self):
        #print("Creando Controlador Mesa")
        self.repositorioMesa=RepositorioMesa()

    # def index(self):
    #     print("Listar todos los Mesas")
    #     unaMesa = {
    #         "_id": "m1",
    #         "numero": "1",
    #         "cantidad_inscritos": "100"}
    #     return [unaMesa]

    def create(self, infoMesa):
        print("Crear un Mesa")
        nuevaMesa = Mesa(infoMesa)
        print("mesa a crear en base de datos",nuevaMesa.__dict__)
        return True

    def showid(self, id):
        print("Mostrando un Mesa con id ", id)
        mesa=Mesa(self.repositorioMesa.findById(id))
        return mesa.__dict__

    def showall(self):
        print("Mostrando las mesas de la base de datos ")
        return self.repositorioMesa.findAll()

    def update(self, infoMesa):
        mesaactual=Mesa(self.repositorioMesa.findById((infoMesa["idObject"])))
        print("Actualizando Mesa con id ", mesaactual)
        mesaactual.numero=infoMesa["numero"]
        mesaactual.cantidad_inscritos = infoMesa["cantidad_inscritos"]
        self.repositorioMesa.save(mesaactual)
        return True

    def delete(self, id):
        print("Elimiando Mesa con id ", id)
        self.repositorioMesa.delete(id)
        return True
