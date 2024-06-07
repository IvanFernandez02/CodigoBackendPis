from enum import Enum

from django.db import models


class Estado(Enum):
    APAGADO = 'Apagado'
    ENCENDIDO = 'Encendido'


ESTADO_CHOICES = [(tag.name, tag.value) for tag in Estado]


class Brazo(models.Model):
    antebrazo = models.CharField(max_length=50)
    base = models.CharField(max_length=50)
    brazo = models.CharField(max_length=50)
    muñeca = models.CharField(max_length=50)
    pinza = models.CharField(max_length=50)
    estado = models.CharField(max_length=10, choices=[(tag, tag.value) for tag in Estado])

    def realizar_movimiento(self):
        pass


class Movimiento(models.Model):
    duracion = models.IntegerField()
    ejex = models.IntegerField()
    ejey = models.IntegerField()
    ejez = models.IntegerField()
    brazo = models.ForeignKey(Brazo, on_delete=models.CASCADE, related_name='movimientos')

    def obtener_duracion(self):
        return self.duracion

    def obtener_ejex(self):
        return self.ejex

    def obtener_ejey(self):
        return self.ejey

    def obtener_ejez(self):
        return self.ejez


class Posicion(models.Model):
    coordenadax = models.IntegerField()
    coordenaday = models.IntegerField()
    coordenadaz = models.IntegerField()
    movimiento = models.ForeignKey(Movimiento, on_delete=models.CASCADE, related_name='posiciones')

    def obtener_coordenadax(self):
        return self.coordenadax

    def obtener_coordenaday(self):
        return self.coordenaday

    def obtener_coordenadaz(self):
        return self.coordenadaz

    def obtener_movimiento(self):
        return self.movimiento


class PlacaControladora(models.Model):
    numeroPines = models.IntegerField()
    brazo_robotico = models.OneToOneField(Brazo, on_delete=models.CASCADE, related_name='placa_controladora')

    def cargar_codigo(self):
        pass

    def compilar_codigo(self):
        pass

    def ejecutar_codigo(self):
        pass


class ModuloBluetooth(models.Model):
    estado = models.CharField(max_length=10, choices=[(tag, tag.value) for tag in Estado])
    placa_controladora = models.OneToOneField(PlacaControladora, on_delete=models.CASCADE, related_name='modulos')


