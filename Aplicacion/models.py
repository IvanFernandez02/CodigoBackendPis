from django.db import models

class Usuario(models.Model):
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def iniciar_sesion(self):
        pass

    def conectar_brazo(self):
        pass

    def realizar_movimiento(self):
        pass

    def cerrar_sesion(self):
        pass

class Error(models.Model):

    def detectar_error(self):
        pass

    def notificar_error(self):
        return "Error detectado"