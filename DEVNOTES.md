How to upload new version to pypi: 
- Detailed instructions here: https://packaging.python.org/en/latest/tutorials/packaging-projects/
- Basic version:
  - `pipenv run python3 -m build`
  - `python3 -m twine upload dist/*`
  - You will be prompted for your pypi token
- How to generate readme from docstrings:
  - run `pipenv run pydoc-markdown -p . --render-toc > texas_hold_em_utils.md` from `/texas_hold_em_utils` directory