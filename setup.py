# Always prefer setuptools over distutils
from setuptools import setup, find_packages

from os import path

here = path.abspath(path.dirname(__file__))

description = 'A platform for managing peer-to-peer feedback within an organisation.'

def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except FileNotFoundError:
        return ""

setup(
    name='adaero',

    version='1.0.0',

    description=description,
    long_description=readme(),
    long_description_content_type='text/markdown',
    # The project's main homepage.
    url='https://github.com/man-group/adaero',
    download_url='https://github.com/man-group/adaero/archive/v1.0.0.tar.gz',

    # Author details
    author='MAN Alpha Tech',
    author_email='ManAlphaTech@man.com',

    # Choose your license
    license='AGPL 3.0',

    python_requires='>=3.9',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],

    # What does your project relate to?
    keywords='feedback',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'alembic>=1.12,<2',
        'apscheduler>=3.10,<4',
        'beautifulsoup4>=4.10,<5',
        'click>=8.1,<9',
        'gunicorn>=21,<22',
        'jinja2>=3,<4',
        'lxml>=4.9,<5',
        'pandas>=1.5,<3',
        'Paste>=3.10,<4',
        'psycopg2-binary>=2.9,<3',
        'pyramid>=2.0,<3',
        'pyramid-beaker>=0.9,<1',
        'pyramid_tm>=2.6,<3',
        'python-dateutil>=2.8,<3',
        'python-ldap>=3.4,<4',
        'pytz>=2023.3',
        'rest_toolkit>=0.17,<0.18',
        'SQLAlchemy>=1.4,<2',
        'transaction>=3,<4',
        'unicodecsv>=0.14,<0.15',
        'waitress>=2.1,<3',
        'zope.sqlalchemy>=1.6,<2',
        'pycryptodome>=3.18,<4'
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'test': [
            'pytest',
            'pytest-cov',
            'mock',
            'python-dateutil',
            'WebTest',
            'faker',
            'click',
            'freezegun',
            'pytest-xdist',
            'tox'
        ],
        'oracle': [
            'cx_Oracle'
        ],
        'postgres': [
            'psycopg2'
        ]
    },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'adaero=adaero.scripts.feedback_app:main',
            'configure_db=adaero.scripts.configure_db:cli',
        ],
        'paste.app_factory': [
            'main = adaero:main'
        ]
    },
)
