How to upload new version to pypi: 
- Detailed instructions here: https://packaging.python.org/en/latest/tutorials/packaging-projects/
- Basic version:
  - `pipenv run python3 -m build`
  - `python3 -m twine upload dist/*`
  - You will be prompted for your pypi token