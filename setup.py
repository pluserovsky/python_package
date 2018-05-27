from setuptools import setup, find_packages

setup(
    name='python-package',
    version='3.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='temp converter & fibonacci counter',
    long_description=open('README.txt').read(),
    install_requires=['numpy'],
    url='https://github.com/pluserovsky/python_package',
    author='Lukasz Broll',
    author_email='225972@student.pwr.edu.pl'
)
