git add .
git commit -m "update"
git push
cd habmaps
python3 setup.py build
python3 setup.py install
python3 -m twine upload dist/*