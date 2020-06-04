doc:
	rm -Rf html
	pdoc --html directory_observer

clean:
	rm -Rf html htmlcov
	rm -Rf directory_observer.egg-info
	find . -type d -name __pycache__ -exec rm -Rf {} \; 2>/dev/null || exit 0

test: clean
	pytest tests/

coverage:
	pytest --cov-report html --cov=directory_observer tests/
	pytest --cov=directory_observer tests/
