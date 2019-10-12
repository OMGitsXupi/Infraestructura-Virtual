import pytest
from hola import Hola

def suma(x):
	return x+1

def test_suma():
	assert suma(4) ==5

#def test_hola():
#	h=hola()
#	assert isinstance(h,Hola), "Error al crear una instancia"
