# API REST y tests

Se ha creado una estructura de API REST para manejar la aplicación, por lo que se han creado las rutas que permiten usarla.
Para el enrutamiento de mi clase, he barajado hacerlo con 'hug', pero como en otra asignatura hemos estado trabajando con Flask, al final me he decantado por esta opción.

#### Cabecera
```
from flask import Flask, jsonify, request
from __init__ import RandomImage
import os

app = Flask(__name__)
#Se crea una instancia de la clase original
img = RandomImage()
```
#### Rutas por defecto
Ruta por defecto sin funcionalidad
```
@app.route('/')
def index():
	return jsonify('{ "status": "OK" }')
```
Ruta para comprobar disponibilidad
```
@app.route('/status')
def index():
	return jsonify('{ "status": "OK" }')
```
#### Obtener una imagen (link) aleatoria del array de strings
```
@app.route('/random')
def random():
	return jsonify(link = img.getRandomImage()), 200
```
#### Obtener una imagen (link) mandando el ídice en la URL
```
@app.route('/get', methods=['GET', 'POST'])
def getimage():
	if request.method == 'GET':
		id = int(request.args.get('link'))
		if id>=0 and id<img.getSize():
			return jsonify(img.getImage(id))
		else: return jsonify('Ruta no dispnible'), 404
	return jsonify('{ "status": "OK" }')
```
#### Manejador de error para cualquier ruta desconocida
```
@app.errorhandler(404)
def page_not_found(error):
    return jsonify('Ruta no dispnible'), 404
```
#### Configuración para crear servicio
```
if __name__ == '__main__':
 app.run(debug=True)
```

### Tests
Para testear la api estos son las funciones. Todas se basan en recibir un código de estado (error o éxito).
```
from .context import my_app
from my_app.apirest import *
from my_app.__init__ import *
import unittest
from flask import Flask, json, jsonify

class RandomTest(unittest.TestCase):
	def test_status(self):
		client = app.test_client(self)
		response = client.get('/status')
		self.assertEqual(response.status_code, 200)

	def test_random(self):
		client = app.test_client(self)
		response = client.get('/random')
		self.assertEqual(response.status_code, 200)

	def test_get(self):
		client = app.test_client(self)
		response = client.get('/get?link=0')
		self.assertEqual(response.status_code, 200)

	def test_get2(self):
		client = app.test_client(self)
		response = client.get('/get?link=100')
		self.assertEqual(response.status_code, 404)

	def test_notFound(self):
		client = app.test_client(self)
		response = client.get('/notfound')
		self.assertEqual(response.status_code, 404)
```