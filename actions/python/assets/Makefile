install:
ifeq ($(version), 3.5)
	sudo apt install -y libssl-dev libncurses5-dev libsqlite3-dev libreadline-dev libtk8.5 libgdm-dev libdb4o-cil-dev libpcap-dev
	cd /usr/src; sudo wget https://www.python.org/ftp/python/3.5.6/Python-3.5.6.tgz; sudo tar xzf Python-3.5.6.tgz
	cd /usr/src/Python-3.5.6; sudo ./configure --enable-optimizations; sudo make altinstall
	python3.5 -V
else ifeq ($(version), 3.9)
	sudo apt install -y wget build-essential libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
	cd /usr/src; sudo wget https://www.python.org/ftp/python/3.9.4/Python-3.9.4.tgz
	cd /usr/src; sudo tar xzf Python-3.9.4.tgz
	cd /usr/src/Python-3.9.4; sudo ./configure --enable-optimizations; sudo make altinstall
	python3.9 -V
endif

virtualenv:
	sudo apt install python3-pip
	sudo pip3 install virtualenv
	cd $(path); mkdir -p .virtualenvs; cd .virtualenvs; virtualenv -p $(version) $(name)_env
	cd $(path); echo "source $(path)/.virtualenvs/$(name)_env/bin/activate \nexport DJANGO_SETTINGS_MODULE=$(settings)" >> env_$(name)

locale:
	sudo apt-get clean && sudo apt-get update && sudo apt-get install -y locales
	sudo sed -i 's/^# *\(fa_IR.UTF-8\)/\1/' /etc/locale.gen
	sudo locale-gen
