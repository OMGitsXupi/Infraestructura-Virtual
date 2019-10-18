from .context import my_app
from my_app.hola import *

def suma(x):
	return x+1

def test_suma():
	assert suma(4) ==5

def test_hola():
	h=Hola()
	assert isinstance(h,Hola), "Error al crear una instancia"
