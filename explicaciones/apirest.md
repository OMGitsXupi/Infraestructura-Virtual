# API REST y tests

Se ha creado una estructura de API REST para manejar la aplicación, por lo que se han creado las rutas que permiten usarla, con ayuda de _Flask_ que permite realizarlo fácilmente. Para testearlo también se ha usado la librería _unittest_

## API
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
	return jsonify(status='OK')
```
Ruta para comprobar disponibilidad
```
@app.route('/status')
def index():
	return jsonify(status='OK')
```
#### Rutas funcionales para historias de usuario
Obtener una imagen (link) aleatoria -> `/random`
```
@app.route('/random')
def random():
	return jsonify(link = img.getRandomImage()), 200
```
Obtener una imagen (link) concreta  -> `/get?link=[ÍNDICE]`
```
@app.route('/get', methods=['GET'])
def getimage():
	if request.method == 'GET':
		id = int(request.args.get('link'))
		if id>=0 and id<img.getSize():
			return jsonify(img.getImage(id))
		else: return jsonify(message='Ruta no dispnible'), 404
	else: return jsonify(message='Método no disponible'), 400
```
Introducir una imagen (link) mediante método POST -> `/push`
```
@app.route('/push', methods=['POST'])
def push():
	if request.method == 'POST':
		link=request.form.get('link')
		tamanio=img.getSize()
		img.pushImage(link)
		if img.getSize()>tamanio:
			return jsonify(link), 200 #Devuelve el propio link
		else: return jsonify(message='No se ha podido introducir'), 400
	else: return jsonify(message='Ruta no dispnible'), 404
```
#### Manejador de error para cualquier ruta desconocida
```
@app.errorhandler(404)
def page_not_found(error):
	return jsonify(message='Ruta no dispnible'), 404
```
#### Configuración para crear servicio
```
if __name__ == '__main__':
 	app.run(debug=True)
```

## Tests
Para testear la api estos son las funciones. Todas se basan en recibir un código de estado (error o éxito), la propia api ya está configurada para que solo se mande el código de exito si los datos se introducen correctamente (en el '_getImage_' o en '_push_').
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

	def test_push(self):
		client = app.test_client(self)
		mydata={'link': 'cadena de prueba'}
		response = client.post('/push?link=\'cadenadeprueba\'', data=mydata)
		self.assertEqual(response.status_code, 200)

	def test_notFound(self):
		client = app.test_client(self)
		response = client.get('/notfound')
		self.assertEqual(response.status_code, 404)
```