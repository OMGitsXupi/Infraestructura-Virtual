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

#### [Servicio desplegado en Heroku](https://wikirandom.appspot.com/)
#### [Servicio desplegado en Google App Engine](https://xupi.herokuapp.com/)

## :books: Documentación extra
buildtool: fabfile.py
- #### [Explicaciones](explicaciones/README.md)
- [Servicio (gunicorn + supervisor)](explicaciones/servicio.md)
- [API REST (con tests)](explicaciones/apirest.md)
- [Despliegue en Heroku](heroku.md)
- [Despliegue en Google App Engine](GoogleAppEngine.md)
