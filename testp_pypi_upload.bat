del /s /q build, dist, lambdata_xpandalord.egg-info
python setup.py sdist bdist_wheel
twine upload -u xpandalord -p #Nyancat19 --repository-url https://test.pypi.org/legacy/ dist/*