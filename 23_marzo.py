
#Practica clases 1#
class Personaje():
	def __init__(self ):
		pass  
Harry_poter = Personaje()

#Practica clases 2#}
class Dinosaurio():
    def __init__(self):
        pass
velociraptor = Dinosaurio()
tiranosaurio_rex = Dinosaurio()
braquiosaurio = Dinosaurio()

#Practica clases 3#
class PlataformaStreaming ():
	def __init__(self) -> None:
		pass
netflix = PlataformaStreaming()
hbo_max = PlataformaStreaming()
amazon_prime_video = PlataformaStreaming()

#Practica atributos 1 #
class Casa():
	def __init__(self, color,  cantidad_pisos):
		self.color = color
		self.cantidad_pisos = cantidad_pisos

casa_blanca = Casa("blanco",4)
print("la casa es: " + casa_blanca.color, "y tiene " + str(casa_blanca.cantidad_pisos) + " pisos")

#Practica atributos 2 #

class Cubo():
	def __init__(self, color ):
		self.caras=  6
		self.color = color

cubo_rojo = Cubo ("rojo")
print(cubo_rojo.caras)

#Practica atributos 3 #
class Personaje():
    def __init__(self,especie,magico,edad,real):
        self.especie = especie
        self.magico = magico
        self.edad = edad
        self.real = False

Harry_poter = Personaje("humano",True,17,True)
print(f"la especie {Harry_poter.especie} es magico: {Harry_poter.magico} y tiene {str(Harry_poter.edad)} años y es real: {Harry_poter.real}")
    
#Practica Métodos 1 #

class Perro():
	def __init__(self,raza) :
		self.raza = raza

	def ladrar(self):
		ladrido = "Guau!"
		return ladrido

perro1 = Perro ("pincher")
print(perro1.ladrar())


    
#Practica Métodos 2 #

class mago():
	def __init__(self) :
		pass

	def lanzar_hechizo(self):
		palabra = "¡Abracadabraf!"
		return palabra

merlin = mago ()
print(merlin.lanzar_hechizo())

    
#Practica Métodos 3 #

class Alarma():
	def __init__(self) :
		pass

	def postergar(cantidad_minutos):
		return (f"la alarma ha sido pospuesta {cantidad_minutos} minutos")

alarma1 = Alarma
print(alarma1.postergar(5))
