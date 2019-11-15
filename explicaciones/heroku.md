# Despliegue en la PaaS Heroku

A continuación voy a detallar los pasos para que se haya podido desplegar el servicio en un PaaS (Platform as a Service) para que sea más accesible. En este caso hemos escogido Heroku por su eficacia al configurar la aplicación y su alta disponibilidad (además de que qeu ofrece un buen plan gratuito.
Primero nos hemos creado una cuenta en [Heroku](https://cloud.google.com/) y la hemos conectado con GitHub.
Lo esencial para que se pueda desplegar nuestra aplicación es crear un archivo llamado [Procfile](https://github.com/OMGitsXupi/WikiRandom/blob/master/Procfile) que va a usar gunicorn.
```
web: gunicorn --chdir my_app wsgi:app
```
Para poder usar Heroku tendremos que tener su herramienta de línea de órdenes, que podremos instalar con `sudo snap install heroku --classic`
Una vez hecho esto hemos iniciado sesión con `heroku login`
Tras esto nos hemos movido al directorio de nuestro proyecto, y hemos ejecutado `heroku create xupi` para crear una aplicación llamada _xupi_ aunque se puede poner cualquier otro nombre o incluso ninguno y se pondrá uno automático. A continuación para subir nuestra aplicación a Heroku he usado `git push heroku master` y, para asegurarnos de que se cree una instancia: `heroku ps:scale web=1`
Ahora con `heroku open` se nos abrirá la [aplicación](https://xupi.herokuapp.com/) en el navegador.
En el _dashboard_ de _Heroku_ podremos crear un _pipeline_, que tendremos que sincronizar con GitHub para que la aplicación se actualice con cada push a git en vez de tener que usar `git push heroku master` continuamente.