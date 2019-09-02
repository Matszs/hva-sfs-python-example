# Software for Science - Python

This repository is used to get started with Python in the Software for Science minor.
Authors: Mats Otten & ...

## Installation

First set-up a Python environment for yourself. This project requires Python3.

When you are done, install the requirements with pip3:

```bash
pip3 install -r requirements.txt
```

## Usage

```python
python3 main.py
```

## Run tests
go to tests directory and run
```python
python3 test_api.py 
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Updating requirements:

When you use a library, you can install it by:
```bash
pip3 install [name-library]
```

To add this library to the requirements list, run the following:
```bash
pip freeze > requirements.txt
```