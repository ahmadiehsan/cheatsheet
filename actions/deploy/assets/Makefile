scaffolding:
	# install
	sudo apt install nginx
	
	# create main directory
	cd /; sudo mkdir $(project); sudo chown -R $(USER): $(project)
	
	# create other directories
	cd /$(project); mkdir -p app; mkdir -p etc/nginx/sites-available; mkdir -p var/log/$(project); mkdir -p systemd/system
	
	# clone chearsheet repo
	cd /$(project)/etc; git clone https://mgit.mparsict.com/ahmadiehsan/cheatsheet.git
	
	# create sample nginx-gunicorn config
	cp /$(project)/etc/cheatsheet/linux/gunicorn.socket /$(project)/etc/systemd/system/$(project).socket
	sudo ln -s /$(project)/etc/systemd/system/$(project).socket /etc/systemd/system/$(project).socket
	
	cp /$(project)/etc/cheatsheet/linux/gunicorn.service /$(project)/etc/systemd/system/$(project).service
	sudo ln -s /$(project)/etc/systemd/system/$(project).service /etc/systemd/system/$(project).service

	cp /$(project)/etc/cheatsheet/nginx/nginx-gunicorn-config /$(project)/etc/nginx/sites-available/$(project)
	sudo ln -s /$(project)/etc/nginx/sites-available/$(project) /etc/nginx/sites-enabled/$(project)	
	
	# add some alias
	echo "alias cd.app='cd /$(project)/app'" >> /home/$(USER)/.bashrc
	echo "alias cd.cheatsheet='cd /$(project)/etc/cheatsheet'" >> /home/$(USER)/.bashrc
	echo "alias cd.nginx='cd /$(project)/etc/nginx/sites-available'" >> /home/$(USER)/.bashrc
	echo "alias cd.log='cd /$(project)/var/log'" >> /home/$(USER)/.bashrc
	echo "alias cd.system='cd /$(project)/systemd/system'" >> /home/$(USER)/.bashrc
	echo "alias ll='ls -l'" >> /home/$(USER)/.bashrc
	echo "alias la='ls -la'" >> /home/$(USER)/.bashrc

	# create help file for newcomers
	cd ~; printf '# $(project) project\n\nproject and all of the project related content is in /$(project)\n\ncd /$(project)\n' >> README.md
