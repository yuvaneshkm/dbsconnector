# Database Connector Package

# Overview
**dbsconnector** is a Python package designed to simplify the process of connecting to different data sources like csv files, excel sheets, google sheets, MongoDB database etc. This package provides a streamlined API for loading the data from different sources and return as Pandas DataFrame for any kind of DataScience, DataAnalysis and MachineLearning purpose.

# Features
* Easy connection to multiple data sources
* Return Pandas DataFrame as the Output

# Project Structure
```plaintext
dbsconnector/
├── .github/
│   └── workflows/
│       └── ci.yaml
│       └── python-publish.yaml
├── src/
│   └── dbsconnector/
│       └── databases.py
├── tests/
│   ├── unit/
│   │   └── test_unit.py
│   └── integration/
│       └── test_integration.py
├── .gitignore
├── LICENSE
├── pyproject.toml
├── README.md
├── requirements_dev.txt
├── requirements.txt
├── setup.cfg
├── setup.py
├── template.py
└── tox.ini
```

## requirements_dev.txt we use for the testing
It makes it easier to install and manage dependencies for development and testing, separate from the dependencies required for production.

## difference between requirements_dev.txt and requirements.txt
requirements.txt is used to specify the dependencies required to run the production code of a Python project, while requirements_dev.txt is used to specify the dependencies required for development and testing purposes.

## tox.ini
We use if for the testing in the python package testing against different version of the python 

### how tox works tox enviornment creation
1. Install depedencies and packages 
2. Run commands
3. Its a combination of the (virtualenvwrapper and makefile)
4. It creates a .tox

## pyproject.toml
it is being used for configuration the python project it is a alternative of the setup.cfg file. its containts configuration related to the build system
such as the build tool used package name version author license and dependencies.

## setup.cfg
In summary, setup.cfg is used by setuptools to configure the packaging and installation of a Python projec

## Testing python application
*types of testing*
1. Automated testing 
2. Manual testing

*Mode of testing*
1. Unit testing
2. Integration tests

*Testing frameworks*
1. pytest
2. unittest
3. robotframework
4. selenium
5. behave
6. doctest

## check with the code style formatting and syntax(coding standard)
1. pylint
2. flake8(it is best because it containt 3 library pylint pycodestyle mccabe)
3. pycodestyle

## CI/CD
 Implemented a robust CI/CD pipeline using GitHub Actions to automate testing, building, and deployment of this package to the PyPI repository. This ensures that every change is thoroughly tested and seamlessly deployed, maintaining the highest quality standards.

# How to use this package?

## Installation
To install the package, use pip:
```bash
pip install dbsconnector==0.1
```

## Usage

### Connecting to csv
```py
# import the module:
from dbsconnector import databases
# load the data:
df = databases.load_csv('sample.csv', ',')
# display the data:
df
```

### Connecting to Excel
```py
# import the module:
from dbsconnector import databases
# load the data:
df = databases.load_excelsheet('sample.xlsx', 'sample_sheet')
# display the data:
df
```

### Connecting to gsheet
```py
# import the module:
from dbsconnector import databases
# load the data:
df = databases.load_gsheet('17r9f4BL7sjmdLBnt92OdQP3CHK5bdT3hozg6DUJXGqU', 'sample_sheet')
# display the data:
df
```

### Connecting to MongoDB
```py
# import the module:
from dbsconnector import databases
# load the data:
df = databases.load_mongodbdata('localhost', 'sample_database', 'sample_collection')
# display the data:
df
```

# Contributing
* Several other data sources are to be included in upcomming versions.
* Contributions are welcome! Please open an issue or submit a pull request on GitHub.

# License
This project is licensed under the MIT License.

# Contact
For any questions or suggestions, please contact [yuvaneshkm05@gmail.com](yuvaneshkm05@gmail.com)

# Connect
Connect with me on [LinkedIn](https://www.linkedin.com/in/yuvaneshkm)
