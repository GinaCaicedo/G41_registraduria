from Modelos.Resultado import Resultado
class ControladorResultado():
    def __init__(self):
        print("Creando ControladorResultado")

    def index(self):
        print("Listar todos los Resultados")
        unResultado = {
            "_id": "abc123",
            "numero_mesa": "2",
            "cedula_candidato": "123232",
            "numero_votos": "50"

        }
        return [unResultado]

    def create(self, infoResultado):
        print("Crear un Resultado")
        elResultado = Resultado(infoResultado)
        return elResultado.__dict__

    def show(self, id):
        print("Mostrando un Resultado con id ", id)
        elResultado = {
            "_id": "abc123",
            "numero_mesa": "2",
            "cedula_candidato": "123232",
            "numero_votos": "50"
        }
        return elResultado

    def update(self, id, infoResultado):
        print("Actualizando Resultado con id ", id)
        elResultado = Resultado(infoResultado)
        return elResultado.__dict__

    def delete(self, id):
        print("Elimiando Resultado con id ", id)
        return {"deleted_count": 1}
