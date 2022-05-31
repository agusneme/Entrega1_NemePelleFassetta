from django.urls import path
from familia import views


urlpatterns = [
    path('', views.home, name="home"),
    ## path('', views.front, name="front"),
    path('agregar/', views.agregar, name="agregar"),
    path('borrar/<identificador>', views.borrar, name="borrar"),
    path('borrarCurso/<identificador>', views.borrarCurso, name="borrarCurso"),
    path('borrarProfe/<identificador>', views.borrarProfe, name="borrarProfe"),
    path('actualizar/', views.actualizar, name="actualizar_action"),
    path('actualizar/<identificador>', views.actualizar, name="actualizar"),
    path('actualizarCurso/<identificador>', views.actualizarCurso, name="actualizarCurso"),
    path('actualizarCurso/', views.actualizarCurso, name="actualizarCurso_action"),


    path('actualizarProfe/', views.actualizarProfe, name="actualizarProfe_action"),
    path('actualizarProfe/<identificador>', views.actualizarProfe, name="actualizarProfe"),


    path('buscar/', views.buscar, name="buscar"),

    path('index/', views.index, name="index"),

    path('index2/', views.index2, name="index2"),

    path('index3/', views.index3, name="index3"),
    
    path('agregarCurso/', views.agregarCurso, name="agregarCurso"),
    path('agregarProfe/', views.agregarProfe, name="agregarProfe"),
]
