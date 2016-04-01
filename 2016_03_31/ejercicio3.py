from datetime import datetime
class Persona(object):
	def __init__(self,rut,nombre,fechanacimiento,genero):
		self.rut = rut
		self.nombre = nombre
		self.fechanacimiento = fechanacimiento
		self.genero = genero
              
	def obtener_edad(self):
                ahora = datetime.now()
                edad = ahora.year - int(self.fechanacimiento[6:])#anio actual
                if self.fechanacimiento[3]!="0": #si estamos en mes 10+
                    print self.fechanacimiento[3:5]
                    if int(self.fechanacimiento[3:5])<=ahora.month: #si el mes de nacimiento es menor o igual que el actual, no hago cambios en la edad
                        print edad
                    else: #si el mes de nacimiento es mayor que el actual le resto uno a la edad calculada
                        edad = edad - 1
                        print edad
                else: #si estamos en mes 01 a 09
                    if int(self.fechanacimiento[4])<=ahora.month: 
                        print edad
                    else:
                        edad = edad - 1
                        print edad

class Nota(object):
	def __init__(self,valor,ponderacion,ramo,carrera):
		self.valor = valor
		self.ponderacion = ponderacion
		self.ramo = ramo
		self.carrera = carrera

	def obtener_valor(self):
		return self.valor
	def obtener_ponderacion(self):
		return self.ponderacion
	def modificar1(self,valor):   
		if valor>=1.0:
			self.valor = valor
		else:
			print "No se pueden agregar notas negativas"
	

class Alumno(Persona,Nota):
	def __init__(self,rut,nombre,fecha_nac,genero,correo,carrera,promocion,notas):
		#Notas es una lista
		super(Alumno,self).__init__(rut,nombre,fecha_nac,genero)
		self.correo = correo
		self.carrera = carrera
		self.promocion = promocion
		self.notas = Notas
	def agregar_nota(self, nota):
		if nota>=1.0:
			self.notas.append(nota)
		else:
			print "Nota fuera de rango "
	def PGA(self, notas): #promedio global acumulado
		pass

	def promedio_por_ramo(self,notas):
		prom = 0.0
		for i in range(len(self.notas)):
			prom = prom + notas[i]

		prom = prom/len(self.notas)
		return prom



nota1 = Nota(3,0.2,"Taller", "Ing. Civil en Informatica")
nota2 = Nota(6.5,0.5,"Taller", "Ing. Civil en Informatica")

miPersona = Persona("18.459.815-9", "Fernando Reyes Diaz", "07/04/1993", "Masculino")
miPersona.obtenerEdad()

miAlumno = Alumno("18.459.815-9","Fernando Reyes Diaz","07/04/1993","Masculino", "monox_nino@hotmail.com", "Ing. Civil en Informatica", "...",[nota1,nota2])
