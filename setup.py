# importing necessary libraries:
from setuptools import setup, find_packages
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# setup:
# basic info:
PKG_NAME = 'dbsconnector'
__version__ = '0.1'
AUTHOR_USER_NAME = 'yuvaneshkm'
AUTHOR_EMAIL = 'yuvaneshkm05@gmail.com'
REPO_NAME = 'dbsconnector'

def read_file(filepath):
    filepath = Path(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

# setup:
setup(
    name = PKG_NAME,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = 'Python package for connecting and importing data from different DataBases',
    long_description = read_file('README.md'),
    long_description_content_type = 'text/markdown',
    url = f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls = {
        'Bug Trackers':f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues'
    },
    package_dir = {"":'src'},
    packages = find_packages(where='src') 
)
