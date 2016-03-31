import time


class Auto(object):
	def __init__(self,kilometraje,bencina,rendimiento,encendido):
		self.kilometraje = kilometraje
		self.bencina = bencina
		self.rendimiento = rendimiento
		self.encendido = encendido
	def encender(self):
		if not self.encendido:
			self.encendido = True
	def apagar(self):
		if self.encendido:
			self.encendido = False
	def mover(self, num):
		if num < self.rendimiento * self.bencina:
			print "El vehiculo se esta moviendo"
			self.bencina = self.bencina - num/self.rendimiento
			self.kilometraje = self.kilometraje + num

		else:
			print "Error... no posee bencina suficiente para hacer este viaje"
	def obtener_kilometraje(self):
		return self.kilometraje

	def obtener_bencina(self):
		return self.bencina

	def cargar_bencina(self,num):
		if self.encendido:
			self.apagar()
		self.bencina = self.bencina + num

class Camion(Auto):
	def __init__(self,peso,ruedas):
		self.peso = peso
		self.ruedas = ruedas
		self.acoplados = {"ruedas":0,"peso":0.00,"carga"=""}
	def acoplado(self,ruedas,peso,carga):
		self.acoplados{"ruedas":ruedas,"peso":peso,"carga":carga}

	def agregar_acoplado():

	def quitar_acoplado():

	def obtener_acoplados():

	def obtener_ruedas():

	def obtener_peso():



class Persona(object):
	def __init__(self,rut,nombre,fecha_nac,genero):
		self.rut = rut
		self.nombre = nombre
		self.fecha_nac = fecha_nac
		self.genero = genero
	def obtener_edad(self):
		fecha = time.strftime("%d %m %y")