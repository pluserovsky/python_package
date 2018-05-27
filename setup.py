from setuptools import setup, find_packages

setup(
    name='python-package',
    version='2.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='C to F grades converter',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://git.e-science.pl/lbroll225972/lab10_python_package',
    author='Lukasz Broll',
    author_email='225972@student.pwr.edu.pl'
)
