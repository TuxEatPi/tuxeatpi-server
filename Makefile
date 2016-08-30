
#######################################
### Dev targets
#######################################
env-dev:
	virtualenv --system-site-packages -p /usr/bin/python3 env
	env/bin/pip3 install -r requirements-dev.txt --upgrade --force-reinstall
	env/bin/pip3 install -r requirements.txt --upgrade --force-reinstall
	env/bin/python setup.py develop

#######################################
### Virtual env targets
#######################################
env:
	virtualenv -p /usr/bin/python3 env
	env/bin/pip3 install -r requirements.txt --upgrade --force-reinstall

tux_example:
	env/bin/python examples/simple_tux_with_gpiosim.py

doc-update-refs:
	rm -rf doc/source/refs/
	sphinx-apidoc -M -f -e -o doc/source/refs/ tuxeatpi_server/

doc-generate:
	cd doc && make html
	touch doc/build/html/.nojekyll

lang-gen:
	# TODO find something cleaner 
	rm -rf tuxeatpi/locale
	mkdir -p tuxeatpi
	cp -r `python -c "import os,tuxeatpi;print(os.path.dirname(tuxeatpi.__file__))"`/locale tuxeatpi
	cd tuxeatpi/locale/fr/LC_MESSAGES/ && msgfmt tuxeatpi.po -o tuxeatpi.mo
	cd tuxeatpi/locale/en/LC_MESSAGES/ && msgfmt tuxeatpi.po -o tuxeatpi.mo

#######################################
### Test targets
#######################################

test-run:
	rm -rf .coverage cover/
	pep8 --max-line-length=100 --exclude='*.pyc' --exclude=tuxeatpi_server/experimental tuxeatpi_server
	pylint --rcfile=.pylintrc -r no tuxeatpi_server
	env/bin/nosetests --with-coverage --cover-html --cover-package=tuxeatpi_server -svd --with-xunit --with-html tests
