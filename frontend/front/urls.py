from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name='front-login'),
    path('login/',views.signin, name='signin'),
    path('home/', views.home,name='front-home'),
    path('add/',views.add,name='add'),
    path('cargar/',views.cargaMasiva,name='carga'),
    path('newplaylist/',views.newplaylist,name='playlist'),
    path('playlists/',views.playlists,name='playlists'),
    path('empresas/',views.empresas,name='empresas')
]