from fabric.api import local

def test():
    local("cd my_app")
    local("pytest")

def run():
    local("cd my_app")
    local("hola.py")
