# Integración Continua con Travis

La Integración Continua la usaremos para poder realizar tests automáticos cada vez que se actualice el proyecto en Git (con un push)

Haciendo click [aquí](https://travis-ci.com/OMGitsXupi/WikiRandom) se puede comprobar si el proyecto pasa los tests de Travis con la configuración puesta en el archivo [.travis.yml](https://github.com/OMGitsXupi/WikiRandom/blob/master/.travis.yml).
En este caso he configurado que los tests se realicen a través del fabfile (también es una manera de testear esta herramienta de construcción) y en las versiones de Python 2.7 y 3.7 porque son las versiones más populares según lo que tengo entendido para Python 2 y Python 3.
