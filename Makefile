

install:
	pip install -e .['dev'] 

uninstall:
	pip uninstall delivery
	rm -r delivery.egg-info
# ['dev'] instala os requirements-dev.txt também. extras_require do setup.py
