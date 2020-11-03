ACTION_ASSETS_DIR := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))

install:
ifeq ($(os), debian)
	bash $(ACTION_ASSETS_DIR)/install/debian10-installer.sh
	echo "done!!"
else ifeq ($(os), ubuntu)
	bash $(ACTION_ASSETS_DIR)/install/ubuntu18.04-installer.sh
	echo "done!!"
endif
