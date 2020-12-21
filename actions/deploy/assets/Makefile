ACTION_ASSETS_DIR := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))

scaffolding:
	# install
	sudo apt install nginx
	
	# create main directory
	cd /; sudo mkdir $(project); sudo chown -R $(USER): $(project)

	# create other directories
	cd /$(project); mkdir -p app; mkdir -p etc/nginx/sites-available; mkdir -p var/log/$(project); mkdir -p etc/systemd/system
	
	# create sample nginx-gunicorn config
	cp $(ACTION_ASSETS_DIR)/scaffolding/gunicorn.socket /$(project)/etc/systemd/system/$(project).socket
	sudo ln -s /$(project)/etc/systemd/system/$(project).socket /etc/systemd/system/$(project).socket
	
	cp $(ACTION_ASSETS_DIR)/scaffolding/gunicorn.service /$(project)/etc/systemd/system/$(project).service
	sudo ln -s /$(project)/etc/systemd/system/$(project).service /etc/systemd/system/$(project).service

	cp $(ACTION_ASSETS_DIR)/scaffolding/nginx-gunicorn-config /$(project)/etc/nginx/sites-available/$(project)
	sudo ln -s /$(project)/etc/nginx/sites-available/$(project) /etc/nginx/sites-enabled/$(project)

	# create under construction page
	cp -r $(ACTION_ASSETS_DIR)/scaffolding/under-construction /$(project)/app
	
	# add some alias
	echo "alias cd.app='cd /$(project)/app'" >> /home/$(USER)/.bashrc
	echo "alias cd.nginx='cd /$(project)/etc/nginx/sites-available'" >> /home/$(USER)/.bashrc
	echo "alias cd.log='cd /$(project)/var/log'" >> /home/$(USER)/.bashrc
	echo "alias cd.system='cd /$(project)/etc/systemd/system'" >> /home/$(USER)/.bashrc
	echo "alias ll='ls -l'" >> /home/$(USER)/.bashrc
	echo "alias la='ls -la'" >> /home/$(USER)/.bashrc

	# create help file for newcomers
	cd ~; printf '# $(project) project\n\nproject and all of the project related content is in /$(project)\n\ncd /$(project)\n' >> README.md
