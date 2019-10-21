# Integración Continua

La Integración Continua la usaremos para poder realizar tests automáticos cada vez que se actualice el proyecto en Git (con un push)

## Travis
Como primer servicio de CI he usado Travis, que tiene una configuración muy sencilla y fácil de entender.
Esta es mi configuración en el archivo [.travis.yml](https://github.com/OMGitsXupi/WikiRandom/blob/master/.travis.yml):
```
language: python

python:
  - "2.7"
  - "3.7"

install:
  - pip install -r requirements.txt

script:
  - fab test
```
En este caso he configurado que los tests se realicen a través del fabfile (también es una manera de testear esta herramienta de construcción) y en las versiones de Python 2.7 y 3.7 porque son las versiones más populares según lo que tengo entendido para Python 2 y Python 3.
Haciendo click [aquí](https://travis-ci.com/OMGitsXupi/WikiRandom) se puede comprobar si el proyecto pasa los tests de Travis

## Github Actions
Como un segundo servicio de Integración continua he usado GitHub Actions, que está integrado en GitHub, y también permite monitorizar Travis. Su configuración es parecida a la de Travis, pero al ejecutar los tests he encontrado que le ha llevado bastante más tiempo.
Esta es mi configuración en el archivo [action.yml](https://github.com/OMGitsXupi/WikiRandom/blob/master/.github/workflows/action.yml):
```
name: WikiRandom
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python: [ '2.7', '3.7']
    steps:
      - uses: actions/checkout@master
      - name: Setup python
        uses: actions/setup-python@v1
        with:
          python-version: ${{ matrix.python }}
          architecture: x64
      - run: |
          pip install -r requirements.txt
          fab test
```
He puestos las mismas versiones de Python que en Travis, y es tan sencillo como que en la parte de "run" ponemos la instalación de lo necesario y después el test con la herramienta de construcción (fab en este caso).
He observado que los tiempos de ejecución de los tests son más o menos similares, aunque la mayoría de veces Travis es un par de segundos más rápido.
Haciendo click [aquí](https://github.com/OMGitsXupi/WikiRandom/actions) se puede comprobar si el proyecto pasa los tests de GitHub Actions
