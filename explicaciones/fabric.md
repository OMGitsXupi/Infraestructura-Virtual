# Herramienta de construcción

Como Python no necesita una herramienta de construcción, usaré el módulo de python llamado Fabric, que consiste en un archivo [fabfile.py](https://github.com/OMGitsXupi/WikiRandom/blob/master/fabfile.py), el cual, con unas funciones simples, ejecuta los test y construye la aplicación.
- "fab install" instala lo necesario según el archivo [requeriments.txt](https://github.com/OMGitsXupi/WikiRandom/blob/master/requirements.txt)
- "fab main" ejecuta la aplicación
- "fab test" ejecuta los tests
