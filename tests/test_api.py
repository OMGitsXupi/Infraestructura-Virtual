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
