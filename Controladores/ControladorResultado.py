from Modelos.Resultado import Resultado


class ControladorResultado():
    def __init__(self):
        print("Creando Controlador Resultado")

    # def index(self):
    #     print("Listar todos los Resultados")
    #     unResultado = {
    #         "_id": "abc123",
    #         "numero_mesa": "2",
    #         "cedula_candidato": "123232",
    #         "numero_votos": "50"}
    #     return [unResultado]

    def create(self, infoResultado):
        print("Crear un Resultado")
        resultado = Resultado(infoResultado)
        return resultado.__dict__

    def show(self, id):
        print("Mostrando un Resultado con id ", id)
        return True

    def update(self, infoResultado):
        print("Actualizando Resultado con id ", id)
        resultado = Resultado(infoResultado)
        return resultado.__dict__

    def delete(self, id):
        print("Elimiando Resultado con id ", id)
        return True
