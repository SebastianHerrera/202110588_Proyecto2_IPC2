from django import forms

class LoginForm(forms.Form):
    username= forms.CharField(label="username")
    password= forms.CharField(widget=forms.PasswordInput(), label="password")
    remember= forms.BooleanField(label="exampleCheck1",required=False)

class FileForm(forms.Form):
    file=forms.FileField(label="file")

class AddForm(forms.Form):
    playlistId=forms.IntegerField(label="playlistId")
    id=forms.IntegerField(label="id")
    name=forms.CharField(label="name")
    año=forms.IntegerField(label="año")
    artist=forms.CharField(label="artist")
    genero=forms.CharField(label="genero")

class AddCliente(forms.Form):
    nit = forms.IntegerField(label="nit")
    nombre = forms.CharField(label="nombre")
    usuario = forms.CharField(label="usuario")
    clave = forms.CharField(label="clave")
    direccion = forms.CharField(label="direccion")
    correo = forms.CharField(label="correo")
    empresa = forms.IntegerField(label="empresa")
    playlist1 = forms.IntegerField(label="playlist1")
    playlist2 = forms.IntegerField(label="playlist2")
    playlist3 = forms.IntegerField(label="playlist3")

class AddEmpresa(forms.Form):
    id = forms.IntegerField(label="id")
    nombre = forms.CharField(label="nombre")
    
class GenFactura(forms.Form):
    name = forms.CharField(label="name")
    

class AddPlaylist(forms.Form):
    id=forms.IntegerField(label="id")
    nit=forms.IntegerField(label="nit")
    vinyl=forms.CharField(label="vinyl")
    compacto=forms.CharField(label="compacto")
    categoria=forms.CharField(label="categoria")