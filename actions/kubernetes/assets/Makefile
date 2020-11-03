install:
ifeq ($(os), debianbase)
	sudo apt-get update && sudo apt-get install -y apt-transport-https curl
	curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
	echo 'deb https://apt.kubernetes.io/ kubernetes-xenial main' | sudo tee -a /etc/apt/sources.list.d/kubernetes.list > /dev/null
	sudo apt-get update
	sudo apt-get install -y kubelet kubeadm kubectl
	sudo apt-mark hold kubelet kubeadm kubectl
	echo 'source <(kubectl completion bash)' >>~/.bashrc
endif

init:
ifeq ($(os), ubuntu)
	sudo kubeadm init --pod-network-cidr=10.244.0.0/16
	mkdir -p $(HOME)/.kube
	sudo cp -i /etc/kubernetes/admin.conf $(HOME)/.kube/config
	sudo chown $(USER): $(HOME)/.kube/config
	kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/2140ac876ef134e0ed5af15c65e414cf26827915/Documentation/kube-flannel.yml
endif

