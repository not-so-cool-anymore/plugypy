clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	name '*~' -exec rm --force  {} 

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

build-and-upload:
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload --repository pypi dist/*
