### Install Java
sudo apt-get update
sudo apt-get install openjdk-8-jdk openjdk-8-jre
java -version

### Download and install the Public Signing Key
wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

echo "deb https://packages.elastic.co/elasticsearch/2.x/debian stable main" | sudo tee -a /etc/apt/sources.list.d/elasticsearch-2.x.list

### Install Elasticsearch
sudo apt-get update && sudo apt-get install elasticsearch -y

# Start elasticsearch
sudo service elasticsearch start

# Wait 10 seconds
sleep 10

### Make sure service is running
curl http://localhost:9200
