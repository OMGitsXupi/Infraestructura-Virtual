from fabric.api import local

def test():
    local("pytest")

def run():
    local("cd my_app")
    local("python hola.py")
