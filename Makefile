# would use a docker compose file if this wasn't a small one off app
docker.run:
	sudo docker build --no-cache --target app -t python-number-prettifier . && sudo docker run -it python-number-prettifier

docker.test:
	sudo docker build --no-cache --target test -t python-number-prettifier . && sudo docker run -it python-number-prettifier

requirements:
	pip-compile requirements.in

clean:
	rm -rf ./*.venv

lint.check:
	pylint ./src || true
	black ./src --check --diff

lint.fix:
	black ./src

test:
	pytest src/

