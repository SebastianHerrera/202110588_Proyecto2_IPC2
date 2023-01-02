from usuario import Usuario
from cancion import Cancion
from playlist import Playlist
from empresas import Empresa
from clientes import Cliente
import json

class Gestor:
    def __init__(self):
        self.empresas=[]
        self.usuarios=[]
        self.canciones=[]
        self.playlist=[]
        self.clientes=[]
        self.usuarios.append(Usuario('Sebastián','Herrera','hola123','Sebastiancho'))


    def obtener_usuarios(self):
        return json.dumps([ob.__dict__ for ob in self.usuarios])

    def obtener_usuario(self,user,password):
        for x in self.usuarios:
            if x.user==user and x.password==password:
                return x
        return None

    def agregar_cliente(self,nit,nombre,usuario,clave,direccion,correo,empresa,playlists):
        nuevo=Cliente(nit,nombre,usuario,clave,direccion,correo,empresa,playlists)
        self.clientes.append(nuevo)
        return True
    
    def eliminar_cliente(self,nit,nombre,usuario,clave,direccion,correo,empresa,playlists):
        nuevo=Cliente(nit,nombre,usuario,clave,direccion,correo,empresa,playlists)
        for x in self.clientes:
            if x.nit == nuevo.nit:
                print(x.nit + x.nombre)
                self.clientes.remove(x)
        return True

    def agregar_playlist(self,id,nit,vinyl,compacto,categoria,canciones):
        nuevo=Playlist(id,nit,vinyl,compacto,categoria,canciones)
        self.playlist.append(nuevo)
        return True

    def agregar_cancion(self,nombre,artista,imagen,album):
        nuevo=Cancion(nombre,artista,imagen,album)
        self.canciones.append(nuevo)
        return True

    def agregar_empresa(self,id,nombre):
        nuevo=Empresa(id,nombre)
        self.empresas.append(nuevo)
        return True

    def obtener_canciones(self):
        json=[]
        for i in self.canciones:
            cancion={
                'name':i.name,
                'artist':i.artist,
                'image':i.image,
                'album':i.album
            }
            json.append(cancion)
        return json

    def obtener_clientes(self):
        json=[]
        for i in self.clientes:
            cliente={
                'nit':i.nit,
                'nombre':i.nombre,
                'usuario':i.usuario,
                'clave':i.clave,
                'direccion':i.direccion,
                'correo':i.correo,
                'empresa':i.empresa,
                'playlists':i.playlists
            }
            json.append(cliente)
        return json


    def obtener_playlist(self):
        json=[]
        for i in self.playlist:
            playlis={
                'id':i.id,
                'nit':i.nit,
                'vinyl':i.vinyl,
                'compacto':i.compacto,
                'categoria':i.categoria,
                'canciones':i.canciones
            }
            json.append(playlis)
        return json

    def obtener_empresas(self):
        json=[]
        for i in self.empresas:
            empresa={
                'id':i.id,
                'nombre':i.nombre
            }
            json.append(empresa)
        return json