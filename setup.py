

from setuptools import setup, find_packages


with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()


REPO_NAME = 'Books_recommendation_system'
AUTHOR_USER_NAME = 'Augustin'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy']



setup(
    name = SRC_REPO,
    version= '0.0.0.0',
    author=AUTHOR_USER_NAME,
    long_description=long_description,
    install_requires = LIST_OF_REQUIREMENTS,
    python_requires = ">=3.7",
    license='MIT',
    packages = [SRC_REPO],
    author_email='augustin7766@gmail.com'
)