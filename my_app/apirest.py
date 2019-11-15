from flask import Flask, jsonify, request
from my_app import *
import os

app = Flask(__name__)
#Se crea una instancia de la clase original		
img = RandomImage()

@app.route('/')
def index():
	return jsonify('Bienvenido a WikiRandom')

@app.route('/get', methods=['GET'])
def getimage():
	if request.method == 'GET':
		id = int(request.args.get('link'))
		if id>=0 and id<img.getSize():
			return jsonify(img.getImage(id))
		else: return jsonify('Ruta no dispnible'), 404
	return jsonify('{ "status": "OK" }')

@app.route('/push', methods=['POST'])
def push():
	if request.method == 'POST':
		link=request.form.get('link')
		tamanio=img.getSize()
		img.pushImage(link)
		if img.getSize()>tamanio:
			return jsonify(link), 200 #Devuelve el propio link
		else: return jsonify('No se ha podido introducir el nuevo dato'), 400
	else: return jsonify('Ruta no dispnible'), 404

@app.route('/random')
def random():
	return jsonify(link = img.getRandomImage()), 200

@app.route('/status')
def status():
	return jsonify(status='OK')

@app.errorhandler(404)
def page_not_found(error):
    return jsonify('Ruta no dispnible'), 404

if __name__ == '__main__':
 app.run(debug=True)
