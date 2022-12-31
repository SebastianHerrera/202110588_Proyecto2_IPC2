from usuario import Usuario
from cancion import Cancion
from playlist import Playlist
import json

class Gestor:
    def __init__(self):
        self.usuarios=[]
        self.canciones=[]
        self.playlist=[]
        self.usuarios.append(Usuario('Kirby','Superstar','kirby123','kirby'))
        self.usuarios.append(Usuario('Santa','Claus','santita1','papanoel'))

    def obtener_usuarios(self):
        return json.dumps([ob.__dict__ for ob in self.usuarios])

    def obtener_usuario(self,user,password):
        for x in self.usuarios:
            if x.user==user and x.password==password:
                return x
        return None

    def agregar_playlist(self,nombre,imagen):
        nuevo=Playlist(nombre,imagen)
        self.playlist.append(nuevo)
        return True

    def agregar_cancion(self,nombre,artista,imagen,album):
        nuevo=Cancion(nombre,artista,imagen,album)
        self.canciones.append(nuevo)
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


    def obtener_playlist(self):
        json=[]
        for i in self.playlist:
            play={
                'name':i.name,
                'image':i.image
            }
            json.append(play)
        return json
