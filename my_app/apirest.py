from flask import Flask, jsonify, request
from my_app.__init__ import *
import os

app = Flask(__name__)
#Se crea una instancia de la clase original		
img = RandomImage()

@app.route('/')
def index():
	return jsonify('{ "status": "OK" }')

@app.route('/get', methods=['GET', 'POST'])
def getimage():
	if request.method == 'GET':
		id = int(request.args.get('link'))
		if id>=0 and id<img.getSize():
			return jsonify(img.getImage(id))
		else: return jsonify('Ruta no dispnible'), 404
	return jsonify('{ "status": "OK" }')

@app.route('/random')
def random():
	return jsonify(link = img.getRandomImage()), 200

@app.route('/status')
def status():
	return jsonify('{ "status": "OK" }')

@app.errorhandler(404)
def page_not_found(error):
    return jsonify('Ruta no dispnible'), 404

if __name__ == '__main__':
 app.run(debug=True)
