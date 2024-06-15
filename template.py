# importing necessary libraries:
import os
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# package name:
package_name = 'dbsconnector'

# creating a list of files and folders required for the project:
list_of_files = [

    # creating yaml files for git workflow (CI/CD):
    '.github/workflows/ci.yaml',
    '.github/workflows/python-publish.yaml',

    # creating src folder where the actual package present:
    'src/__init__.py',
    # src ------> dbsconnector:
    f'src/{package_name}/__init__.py',
    f'src/{package_name}/databases.py',

    # creating test folder:
    'tests/__init__.py',
    #tests -----> unit:
    'tests/unit/__init__.py',
    'tests/unit/test_unit.py',
    # tests ----> integration:
    'tests/integration/__init__.py',
    'tests/integration/test_integration.py',

    # setup files:
    'setup.py',
    'setup.cfg',
    # requirements:
    'requirements_dev.txt',
    'requirements.txt',
    # toml file:
    'pyproject.toml',
    # ini file:
    'tox.ini',
    # README file:
    'README.md',

    # jupyter notebook for experiments:
    'experiments/experiments.ipynb'

]

# creating files and folders:
for filepath in list_of_files:
    filepath = Path(filepath)
    # getting directory and filename:
    filedir, filename = os.path.split(filepath)
    # creating directory:
    if filedir!='':
        os.makedirs(filedir, exist_ok=True)
    # creating files:
    if ( (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0) ):
        with open(filepath, 'w') as f:
            pass
        f.close()
