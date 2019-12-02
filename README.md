[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Build Status](https://travis-ci.com/OMGitsXupi/WikiRandom.svg?branch=master)](https://travis-ci.com/OMGitsXupi/WikiRandom) ![Build Status](https://github.com/omgitsxupi/WikiRandom/workflows/WikiRandom/badge.svg)
# :computer: WikiRandom:
Microservicio que te permitirá obtener una imagen aleatoria (en forma de link) o introducir otros.

## :page_with_curl: Instrucciones
#### Instalación
- Si tenemos instalado 'Fabric3': `fab install`
- Si no (usaremos 'pip'): `pip install -r requirements.txt`
#### Iniciar el servicio
`fab start`
#### Parar el servicio
`fab stop`
#### Reiniciar el servicio
`fab restart`
#### Testear (desarrollo)
`fab test`
#### Descargar imagen
`docker pull omgitsxupi/wikirandom`

## :books: Documentación extra
buildtool: fabfile.py

Despliegue: https://xupi.herokuapp.com

Despliegue 2 (ahora usando docker): https://wikirandom.appspot.com

Contenedor: https://xupi-docker.herokuapp.com

DockerHub: https://hub.docker.com/r/omgitsxupi/wikirandom

- #### [Explicaciones](explicaciones/README.md)
- [Servicio (gunicorn + supervisor)](explicaciones/servicio.md)
- [API REST (con tests)](explicaciones/apirest.md)
- [Despliegue en Heroku](explicaciones/heroku.md)
- [Despliegue en Google App Engine](explicaciones/GoogleAppEngine.md)
- [Despliegue usando contenedores](explicaciones/docker.md)
