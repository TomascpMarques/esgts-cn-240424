install:
	python3 -m pip install --upgrade pip && \
	python3 -m pip install -r requirements.txt # grab whatever packages the project might need

format:
	python3 -m black src/*.py # this is totally optional, just for code looks, using the formatting tool "Python Black"

lint:
	python3 -m pylint --disable=R,C ./src/main.py || true # disable warnings which are extra-verbose. This is recommended: you will only get warnings and error messages. Run the lint on my_code.py

test:
	# python3 -m pytest -vv --cov=my_code test_my_code.py # use the pytest library with verbose output with "coverage" and run the test_code.py test
	# python3 -m pytest -vv --cov=my_code test_my_code.py --capture=no # to disable PyTest's output capture
	python3 -m pytest -vv --cov=main ./src/main_test.py -s # to disable PyTest's output capture
	# without -s or --capture=no, the outputs from the setup_function and teardown_function would NOT appear

all: install lint test
