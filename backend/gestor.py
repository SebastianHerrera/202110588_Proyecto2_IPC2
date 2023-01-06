from usuario import Usuario
from cancion import Cancion
from playlist import Playlist
from empresas import Empresa
from clientes import Cliente
import datetime
import json
import fitz
import webbrowser

class Gestor:
    def __init__(self):
        self.empresas=[]
        self.usuarios=[]
        self.canciones=[]
        self.playlist=[]
        self.clientes=[]
        self.usuarios.append(Usuario('Sebastián','Herrera','hola123','Sebastiancho'))
        self.id=0


    def obtener_usuarios(self):
        return json.dumps([ob.__dict__ for ob in self.usuarios])

    def obtener_usuario(self,user,password):
        for x in self.usuarios:
            if x.user==user and x.password==password:
                return x
        return None

    def agregar_cliente(self,nit,nombre,usuario,clave,direccion,correo,empresa,playlists):
        nuevo=Cliente(nit,nombre,usuario,clave,direccion,correo,empresa,playlists)
        if (len(nuevo.playlists))<=3:
            self.clientes.append(nuevo)
            return True
    
    def agregar_cliente_web3(self,nit,nombre,usuario,clave,direccion,correo,empresa,playlist3,playlist2,playlist1):
        nuevo=Cliente(nit,nombre,usuario,clave,direccion,correo,empresa,[playlist3,playlist2,playlist1])
        if (len(nuevo.playlists))<=3:
            self.clientes.append(nuevo)
            return True  

    def agregar_cliente_web2(self,nit,nombre,usuario,clave,direccion,correo,empresa,playlist2,playlist1):
        nuevo=Cliente(nit,nombre,usuario,clave,direccion,correo,empresa,[playlist2,playlist1])
        if (len(nuevo.playlists))<=3:
            self.clientes.append(nuevo)
            return True      

    def agregar_cliente_web1(self,nit,nombre,usuario,clave,direccion,correo,empresa,playlist1):
        nuevo=Cliente(nit,nombre,usuario,clave,direccion,correo,empresa,[playlist1])
        if (len(nuevo.playlists))<=3:
            self.clientes.append(nuevo)
            return True      


    def eliminar_cliente(self,nit,nombre,usuario,clave,direccion,correo,empresa,playlists):
        nuevo=Cliente(nit,nombre,usuario,clave,direccion,correo,empresa,playlists)
        for x in self.clientes:
            if x.nit == nuevo.nit:
                print(str(x.nit) , x.nombre)
                self.clientes.remove(x)
        return True

    def agregar_playlist(self,id,nit,vinyl,compacto,categoria,canciones):
        nuevo=Playlist(id,nit,vinyl,compacto,categoria,canciones)
        self.playlist.append(nuevo)
        return True

    def agregar_playlist_web(self,id,nit,vinyl,compacto,categoria):
        nuevo=Playlist(id,nit,vinyl,compacto,categoria,[])
        self.playlist.append(nuevo)

    def agregar_cancion(self,playlistId,id,name,artist,año,genero):
        nuevo=Cancion(playlistId,id,name,artist,año,genero)
        for x in self.playlist:
            if nuevo.playlistId == x.id:
                new_song=[nuevo.id,nuevo.name,nuevo.artist,nuevo.año,nuevo.genero]
                x.canciones.append(new_song)
        return True

    def eliminar_cancion(self,id,name,artist,año,genero):
        nuevo=Cancion(id,name,artist,año,genero)
        for x in self.playlist:
            for i in x.canciones:
                if i[0] == nuevo.id:
                   x.canciones.remove(i)
        return True

    def generar_factura(self,name):
        factura=[]
        clientes=[]
        self.id = self.id+1
        self.precio=0
        nombre_empresa = name
        for empresa in self.empresas:
            if empresa.nombre == nombre_empresa:
                factura.append("Número de factura: "+str(self.id))
                factura.append("Nombre: "+nombre_empresa)
                for cliente in self.clientes:
                    if cliente.empresa == empresa.id:
                        factura.append("Playlist de: "+cliente.nombre)
                        clientes.append(cliente.nombre)
                        for play in cliente.playlists:
                            for x in self.playlist:
                                if play == x.id:
                                    if x.vinyl == "True":
                                        self.precio = self.precio+500
                                        if x.compacto == "True":
                                            self.precio = self.precio+100
                                    elif x.compacto == "True":
                                        self.precio = self.precio+100
                                    for i in x.canciones:
                                        if i[2] <=1960:
                                            self.precio= self.precio+25
                                        elif i[2]<=1990:
                                            self.precio = self.precio+15
                                        elif i[2]>1990:
                                            self.precio = self.precio+5
                                        else:
                                            print("Ingreso erróneo")
        fecha = str(datetime.datetime.now().date())
        factura.append("Fecha: "+fecha)
        precio = ("Precio: Q"+str(self.precio)+".00")
        factura.append(precio)

        
        # Nuevo documento
        doc = fitz.open()
        # Nueva página en el documento. Se insertará tras la última página
        pagina = doc.new_page(pno=-1,width=800,height=1200)
        pagina.insert_image(rect=(0, 0, 800, 195),filename="C:/Users/sebas/Documents/USAC/Vacaciones Diciembre 2022/Lab IPC2/Proyecto 2/backend/facturas/headerFacturas.png", keep_proportion=True, overlay=True)
        # Establecemos la posición sobre la que vamos a dibujar
        posicion = fitz.Point(100, 250)
        pagina.insert_font(fontname="Roboto", fontfile="C:/Users/sebas/Downloads/Roboto/Roboto-Medium.ttf")
        # Insertamos un texto en la página
        pagina.insert_text(posicion, "No. De Factura: " + str(self.id), fontsize=20,fontname="Roboto")
        posicion = fitz.Point(100, 280)
        pagina.insert_text(posicion, "Nombre de la Empresa: " + nombre_empresa, fontsize=20,fontname="Roboto")
        posicion = fitz.Point(100, 330)
        pagina.insert_text(posicion, "Descripción de Pedido:", fontsize=18,fontname="Roboto")
        num = 360
        for clientecito in range(len(clientes)):
            posicion = fitz.Point(100, num+(30*clientecito))
            pagina.insert_text(posicion, "Playlists de " + (clientes[clientecito]), fontsize=14,fontname="Roboto")
        posicion=fitz.Point(500,1000)
        pagina.insert_text(posicion, "Fecha: " + fecha, fontsize=18,fontname="Roboto")
        posicion=fitz.Point(500,1030)
        pagina.insert_text(posicion, "Total: Q " + str(self.precio)+".00", fontsize=18,fontname="Roboto")
        # Guardamos los cambios en el documento
        doc.write()
        # Guardamos el fichero PDF
        doc.save(nombre_empresa+".pdf", pretty=True) 
        webbrowser.open_new_tab(nombre_empresa+".pdf")

        return factura


    def agregar_empresa(self,id,nombre):
        nuevo=Empresa(id,nombre)
        self.empresas.append(nuevo)
        return True

    def obtener_canciones(self):
        json=[]
        for i in self.playlist:
            cancion={
                'name':i.canciones
            }
            json.append(cancion)
            for x in i.canciones:
                print(x[1])
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