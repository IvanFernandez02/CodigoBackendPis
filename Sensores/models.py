from django.db import models

class Sensor(models.Model):
    brazo_robotico = models.ForeignKey('BrazoRobotico.Brazo', on_delete=models.CASCADE, related_name='sensores')

class Dinanometro(Sensor):

    def calcular_fuerza(self):
        pass

class SensorProximidad(Sensor):

    def detectar_objeto(self):
        pass

class Camara(Sensor):
    resolucion = models.CharField(max_length=50)

    def capturar_video(self):
        pass