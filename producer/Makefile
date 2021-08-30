# Setting Variables
PYTHONPATH := $(shell pwd)
PKG_NAME := src

docker_run:
	@echo "---- Running Docker Compose ----"
	@docker-compose up --detach --build


docker_down:
	@echo "---- Stopping Docker Compose ----"
	@docker-compose down


docker_restart:
	@echo "---- Restarting Docker Compose ----"
	@docker-compose restart

