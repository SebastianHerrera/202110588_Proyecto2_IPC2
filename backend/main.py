from tkinter.tix import Tree
from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS

from gestor import Gestor
from xml.etree import ElementTree as ET

app = Flask(__name__)
app.config["DEBUG"]=True

CORS(app)

gestor=Gestor()

@app.route('/')
def home():
    return "Esta corriendo bien mi API"

@app.route('/login/<user>/<password>')
def login(user=None,password=None):
    res = gestor.obtener_usuario(user,password)
    if res==None:
        return {'data':False,'message':'Usuario no encontrado o erroneo'}
    return {'data':True}

@app.route('/agregarEmpresa',methods=['POST'])
def agregarEmpresa():
    json=request.get_json()
    gestor.agregar_empresa(json['id'],json['nombre'])
    return jsonify({'ok':True,'message':'Empresa añadida con exito'}),200

@app.route('/agregarPlaylist',methods=['POST'])
def agregarPlaylist():
    json=request.get_json()
    try:
        gestor.agregar_playlist(json['id'],json['nit'],json['vinyl'],json['compacto'],json['categoria'],json['canciones'])
        return jsonify({'ok':True,'message':'Playlist añadida con exito'}),200
    except:
        gestor.agregar_playlist_web(json['id'],json['nit'],json['vinyl'],json['compacto'],json['categoria'])
        return jsonify({'ok':True,'message':'Playlist añadida con exito'}),200

@app.route('/agregarCliente',methods=['POST'])
def agregarCliente():
    json=request.get_json()
    try:
        gestor.agregar_cliente(json['nit'],json['nombre'],json['usuario'],json['clave'],json['direccion'],json['correo'],json['empresa'],json['playlists'])
        return jsonify({'ok':True,'message':'Cliente agregado con exito'}),200
    except:
        try:
            gestor.agregar_cliente_web3(json['nit'],json['nombre'],json['usuario'],json['clave'],json['direccion'],json['correo'],json['empresa'],json['playlist3'],json['playlist2'],json['playlist1'])
            return jsonify({'ok':True,'message':'Cliente web3 agregado con exito'}),200
        except:
            try:
                gestor.agregar_cliente_web2(json['nit'],json['nombre'],json['usuario'],json['clave'],json['direccion'],json['correo'],json['empresa'],json['playlist2'],json['playlist1'])
                return jsonify({'ok':True,'message':'Cliente web2 agregado con exito'}),200
            except:
                gestor.agregar_cliente_web1(json['nit'],json['nombre'],json['usuario'],json['clave'],json['direccion'],json['correo'],json['empresa'],json['playlist1'])
                return jsonify({'ok':True,'message':'Cliente web1 agregado con exito'}),200

    

@app.route('/eliminarCliente',methods=['DELETE'])
def eliminarCliente():
    json=request.get_json()
    gestor.eliminar_cliente(json['nit'],json['nombre'],json['usuario'],json['clave'],json['direccion'],json['correo'],json['empresa'],json['playlists'])
    return jsonify({'ok':True,'message':'Cliente eliminado con exito'}),200

@app.route('/agregarCancion',methods=['POST'])
def agregarCancion():
    json=request.get_json()
    gestor.agregar_cancion(json['playlistId'],json['id'],json['name'],json['año'],json['artist'],json['genero'])
    return jsonify({'ok':True,'message':'Cancion añadida con exito'}),200

@app.route('/eliminarCancion',methods=['DELETE'])
def eliminarCancion():
    json=request.get_json()
    gestor.eliminar_cancion(json['id'],json['name'],json['artist'],json['año'],json['genero'])
    return jsonify({'ok':True,'message':'Cliente eliminado con exito'}),200

@app.route('/agregarCanciones',methods=['POST'])
def agregarCanciones():
    xml=request.data.decode('utf-8')
    raiz=ET.XML(xml)
    for elemento in raiz:
        gestor.agregar_cancion(elemento.attrib['name'],elemento.attrib['artist'],elemento.attrib['image'],elemento.text)
    return jsonify({'ok':True,'message':'Canciones cargadas con exito'}),200

@app.route('/factura',methods=['POST'])
def gen_factura():
    json=request.get_json()
    gestor.generar_factura(json["name"])
    return jsonify(gestor.generar_factura(json["name"])),200

@app.route('/canciones',methods=['GET'])
def get_canciones():
    c=gestor.obtener_canciones()
    return jsonify(c),200

@app.route('/playlists',methods=['GET'])
def get_playlists():
    c=gestor.obtener_playlist()
    return jsonify(c),200

@app.route('/clientes',methods=['GET'])
def get_clientes():
    c=gestor.obtener_clientes()
    return jsonify(c),200

@app.route('/empresas',methods=['GET'])
def get_empresas():
    c=gestor.obtener_empresas()
    return jsonify(c),200

if __name__ =="__main__":
    app.run(debug=True)

