from setuptools import setup

version = '0.0.2'

REQUIREMENTS = [
    'lxml',
    'python-amazon-mws',
    'python-dateutil',
    'requests'
]

PACKAGES = [
    'mwstools',
    'mwstools.parsers',
    'mwstools.requesters'
]

setup(
    name='python-amazon-mws-tools',
    version=version,
    packages=PACKAGES,
    url='https://github.com/ziplokk1/python-amazon-mws-tools',
    license='LICENSE.txt',
    author='Mark Sanders',
    author_email='sdscdeveloper@gmail.com',
    install_requires=REQUIREMENTS,
    description='Wrapper modules to request and parse responses for python-amazon-mws.',
    include_package_data=True
)
