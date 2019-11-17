from fabric.api import local, env, settings

def test():
    local("pytest")

def install():
    local("pip install -r requirements.txt")
    local("sudo apt-get install supervisor")

def start():
	local("sudo cp -r . /tmp/wikirandom")
	local("sudo cp wikirandom-service.conf /etc/supervisor/conf.d/")
	local("sudo supervisorctl reread")
	local("sudo supervisorctl reload")
#	with settings(warn_only=True):
#		noexiste = local("ps aux | grep 'gunicorn: worker \[wsgi:app\]'",capture=True)
#		if noexiste.return_code == 0: 	
#			local("kill -CONT $(ps aux | grep 'gunicorn: worker \[wsgi:app\]' | awk '{print $2}')")
#		else:
#			local("gunicorn --chdir my_app wsgi:app")

def stop():
	local("sudo supervisorctl stop wikirandom")
#	local("kill -STOP $(ps aux | grep 'gunicorn: worker \[wsgi:app\]' | awk '{print $2}')")

def restart():
	stop()
	start()

def status(): #Estado del servicio
	local("sudo supervisorctl status wikirandom")

def gunicornPaaS():
	local("gunicorn --chdir my_app wsgi:app")

#def kill():
	#local("kill -9 $(ps aux | grep 'gunicorn: master \[wsgi:app\]' | awk '{print $2}')")
