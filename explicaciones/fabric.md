# Herramienta de construcción

Como Python no necesita una herramienta de construcción, usaré el módulo de python llamado Fabric, que consiste en un archivo [fabfile.py](https://github.com/OMGitsXupi/WikiRandom/blob/master/fabfile.py), el cual, con unas funciones simples, ejecuta los test y construye la aplicación.
- `fab install` instala lo necesario según el archivo [requeriments.txt](https://github.com/OMGitsXupi/WikiRandom/blob/master/requirements.txt)
- `fab start` inicia el servicio.
- `fab stop` detiene el servicio.
- `fab status` comprueba si el servicio está funcionando.
- `fab restart` reinicia el servicio.
- `fab test` ejecuta los tests.
- `fab gunicornPaaS` ejecuta gunicorn directamente, está pensado solo para que se use en Heroku y Google App Engine.

La versión que se usa en este proyecto es _Fabric3_
