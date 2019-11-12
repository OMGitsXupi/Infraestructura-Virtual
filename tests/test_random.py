from .context import my_app
from my_app.hola import *
from my_app.__init__ import *

def test_get_image():
	imagen=RandomImage()
	cadena=imagen.getRandomImage()
	assert cadena, "Error al devolver cadena"

def test_set_image():
	imagen=RandomImage()
	t=imagen.pushImage('CadenaDePrueba')
	assert (t==0) and (len(imagen.getLinks())==4), "Error al introducir cadena"

def test_hola():
	h=Hola()
	assert isinstance(h,Hola), "Error al crear una instancia"
