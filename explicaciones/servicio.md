# Configurar servicio

Con ayuda de las herramientas [gunicorn](https://gunicorn.org/) y [supervisor](http://supervisord.org/) podremos generar el servicio para después manejarlo con el fabfile (_start_, _stop_, _restart_ y _status_)
## Gunicorn
Para que funcione _gunicorn_ he creado el archivo [wsgi.py](https://github.com/OMGitsXupi/WikiRandom/tree/master/my_app/wsgi.py)
```
from apirest import *

if __name__ == "__main__":
    app.run()
```
Esto se ejecutará con la orden `gunicorn --chdir [UBICACIÓN] wsgi:app` y se creará el proceso.
## Supervisor
Para gestionar el proceso de _gunicorn_ usaremos Supervisor. Este el archivo de configuración que necesitará:
```
[program:wikirandom]

command=/bin/bash /tmp/wikirandom/script.sh
chmod=0777

autostart=true
autorestart=true
stdout_logfile = /tmp/wikirandom/wikirandoms_out.log
stderr_logfile = /tmp/wikirandom/wikirandoms_err.log
```
El script que ejecuta es el siguiente:
```
gunicorn --chdir /tmp/wikirandom/my_app wsgi:app
```
Podemos ver que la ubicación puesta para el proyecto es _fab start_, porque es necesaria una dirección absoluta ya que el archivo de configuración de supervisor se copia en _/etc/supervisor/conf.d/_. En el [Fabfile](https://github.com/OMGitsXupi/WikiRandom/blob/master/fabfile.py) está la configuración para que se copie el proyecto a _/tmp/wikirandom/_