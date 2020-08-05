del build
python setup.py sdist bdist_wheel
twine upload -u xpandalord -p #Nyancat19 --repository-url https://test.pypi.org/legacy/ dist/*