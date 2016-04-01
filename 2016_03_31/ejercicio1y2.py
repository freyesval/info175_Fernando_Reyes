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
	def mover(self, num):   #num es la distancia a reccorrer en km
		if num < self.rendimiento * self.bencina: #rendimiento (km/lt) * bencina (lt) = km 
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


class Acoplado(object):
        def __init__(self,peso,ruedas,carga):
                self.peso = peso #float toneladas
                self.ruedas = ruedas #int
                self.carga = carga #texto

class Camion(Auto):
        def __init__(self,kilometraje,bencina,rendimiento,encendido,peso,ruedas,acoplados):
                super(Camion,self).__init__(kilometraje,bencina,rendimiento,encendido)
                self.peso = peso
                self.ruedas = ruedas
                self.acoplados = acoplados
	

        def agregar_acoplado(self,acoplado):
                self.acoplados.append(acoplado)
                print "El acoplado a sido agregado"

        def quitar_acoplado(self,acoplado):
                self.acoplados.remove(acoplado)
                print "El acoplado ha sido removido"

        def obtener_acoplados(self):
                for i in range(len(self.acoplados)):
                        print "Acoplado "+str(i)
                        print "Peso: "+ str(self.acoplados[i].peso)
                        print "Ruedas: "+str(self.acoplados[i].ruedas)
                        print self.acoplados[i].carga
                        print

        def obtener_ruedas(self):
                return self.ruedas

        def obtener_peso(self):
                return self.peso



acoplado1 = Acoplado(7,4,"Bencina")
acoplado2 = Acoplado(4,6,"Lenha")
acoplado3 = Acoplado(2,3,"Muebles")
acoplado4 = Acoplado(1,6, "Bencina")

 

camion1 = Camion(3,50,10,False,50,6,[acoplado3,acoplado4]) #kilometraje,bencina,rendimiento,encendido,peso,ruedas,acoplados

print camion1.obtener_acoplados()

camion1.agregar_acoplado(acoplado1)
camion1.agregar_acoplado(acoplado2)

print camion1.obtener_acoplados()

print camion1.quitar_acoplado(acoplado3)

print camion1.quitar_acoplado(acoplado4)

print camion1.obtener_acoplados()

print "Peso del camion: "+str(camion1.obtener_peso())
print "Ruedas del camion: "+str(camion1.obtener_ruedas())




