from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from flask_cors import cross_origin
import json
from waitress import serve

##importar los controladores

from Controladores.ControladorCandidato import ControladorCandidato
controladorCandidato=ControladorCandidato()
from Controladores.ControladorMesa import ControladorMesa
controladorMesa=ControladorMesa()
from Controladores.ControladorPartido import ControladorPartido
controladorPartido=ControladorPartido()
from Controladores.ControladorResultado import ControladorResultado
controladorResultado=ControladorResultado()


app = Flask(__name__)
cors = CORS(app)

@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)

@app.route("/Candidatos", methods=['GET'])
def getCandidatos():
    json = controladorCandidato.index()
    return jsonify(json)

@app.route("/Candidatos", methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json = controladorCandidato.create(data)
    return jsonify(json)


@app.route("/Candidatos/<string:id>", methods=['GET'])
def getCandidato(id):
    json = controladorCandidato.show(id)
    return jsonify(json)


@app.route("/Candidatos/<string:id>", methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json = controladorCandidato.update(id, data)
    return jsonify(json)


@app.route("/Candidatos/<string:id>", methods=['DELETE'])
def eliminarCandidato(id):
    json = controladorCandidato.delete(id)
    return jsonify(json)

###Mesa
#
@app.route("/Mesa", methods=['GET'])
def getMesas():
    json = controladorMesa.index()
    return jsonify(json)

#
@app.route("/Mesa", methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = controladorMesa.create(data)
    return jsonify(json)

@app.route("/Mesa/<string:id>", methods=['GET'])
def getMesa(id):
    json = controladorMesa.show(id)
    return jsonify(json)

@app.route("/Mesa/<string:id>", methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json = controladorMesa.update(id, data)
    return jsonify(json)

@app.route("/Mesa/<string:id>", methods=['DELETE'])
def eliminarMesa(id):
    json = controladorMesa.delete(id)
    return jsonify(json)

#Partido

@app.route("/Partido",methods=['GET'])
def getPartidos():
    json=controladorPartido.index()
    return jsonify(json)

@app.route("/Partido",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json=controladorPartido.create(data)
    return jsonify(json)

@app.route("/Partido/<string:id>",methods=['GET'])
def getPartido(id):
    json=controladorPartido.show(id)
    return jsonify(json)
@app.route("/Partido/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=controladorPartido.update(id,data)
    return jsonify(json)

@app.route("/Partido/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=controladorPartido.delete(id)
    return jsonify(json)

# Resultado
@app.route("/Resultado",methods=['GET'])
def getResultado():
    json=controladorResultado.index()
    return jsonify(json)

@app.route("/Resultado",methods=['POST'])
def crearResultado():
    data = request.get_json()
    json=controladorResultado.create(data)
    return jsonify(json)

@app.route("/Resultado/<string:id>",methods=['GET'])
def getResultadoid(id):
    json=controladorResultado.show(id)
    return jsonify(json)
@app.route("/Resultado/<string:id>",methods=['PUT'])
def modificarResultado(id):
    data = request.get_json()
    json=controladorResultado.update(id,data)
    return jsonify(json)

@app.route("/Resultado/<string:id>",methods=['DELETE'])
def eliminarResultado(id):
    json=controladorResultado.delete(id)
    return jsonify(json)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
