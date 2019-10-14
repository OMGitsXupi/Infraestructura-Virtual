from fabric.api import local

def main():
    local("cd my_app")
    local("python hola.py")

def test():
    local("pytest")

def install():
    local("pip install -r requirements.txt")
