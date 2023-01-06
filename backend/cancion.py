class Cancion:
    def __init__(self,playlistId,id,name,artist,año,genero):
        self.playlistId = playlistId
        self.id = id
        self.name=name
        self.artist=artist
        self.año=año
        self.genero=genero

    def getCancion(self):
        return self