import pytest
from hola import Hola

def test_hola():
	h=hola()
	assert isinstance(h,Hola), "Error al crear una instancia"
