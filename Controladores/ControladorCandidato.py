from Modelos.Candidato import Candidato

class ControladorCandidato():
    def __init__(self):
        print("Creando ControladorCandidato")

    # def index(self):
    #     print("Listar todos los Candidatos")
    #     unCandidato = {
    #         "cedula": "1023867848",
    #         "numero_resolucion": "1",
    #         "nombre": "Gina",
    #         "apellido": "Caicedo"
    #     }
    #     return [unCandidato]

    def create(self, infoCandidato):
        print("Crear un Candidato")
        candidato = Candidato(infoCandidato)
        return candidato.__dict__

    def show(self, id):
        print("Mostrando un Candidato con id ", id)
        return True

    def update(self, id, infoCandidato):
        print("Actualizando Candidato con id ", id)
        candidato = Candidato(infoCandidato)
        return candidato.__dict__

    def delete(self, id):
        print("Eliminando Candidato con id ", id)
        return True
