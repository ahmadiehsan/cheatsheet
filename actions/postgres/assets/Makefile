install:
	sudo apt install -y postgresql

create:
	sudo -u postgres psql -c "CREATE DATABASE $(db);"
	sudo -u postgres psql -c "CREATE USER $(user) WITH PASSWORD '$(pass)';"
	sudo -u postgres psql -c "ALTER ROLE $(user) SET client_encoding TO 'utf8';"
	sudo -u postgres psql -c "ALTER ROLE $(user) SET default_transaction_isolation TO 'read committed';"
	sudo -u postgres psql -c "ALTER ROLE $(user) SET timezone TO 'Asia/Tehran';"
	sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $(db) TO $(user);"

