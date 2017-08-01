from palabras import *

__palabra=''
__EstasJugando=False
__contador=0

def NuevoJuego():
	#tiene una nueva palabra
	__palabra=palabras.ObtenerPalabra()
	EstasJugando=True



def validarletra(letraEntrada):
	#ddevuelve true si la palabra cumple con las caracteristicas necesarias.
	if condicion1&condicion2&condicion3:
		return True:
	else:
		return False

def LeerLetra():
	#este modulo lee una letra, en caso la letra sea mal jugada colocará un anuncio
	Teclado=mayus(str(input()))
