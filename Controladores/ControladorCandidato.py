from Modelos.Candidato import Candidato
class ControladorCandidato():
    def __init__(self):
        print("Creando ControladorCandidato")

    def index(self):
        print("Listar todos los Candidatos")
        unCandidato = {
            "_id": "r1",
            "numero_resolucion": "1",
            "nombre": "Gina",
            "apellido": "Caiced0"
        }
        return [unCandidato]

    def create(self, infoCandidato):
        print("Crear un Candidato")
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    def show(self, id):
        print("Mostrando un Candidato con id ", id)
        elCandidato = {
            "_id": "r1",
            "numero_resolucion": "1",
            "nombre": "Gina",
            "apellido": "Caiced0"
        }
        return elCandidato

    def update(self, id, infoCandidato):
        print("Actualizando Candidato con id ", id)
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    def delete(self, id):
        print("Eliminando Candidato con id ", id)
        return {"deleted_count": 1}
