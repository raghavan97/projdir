from setuptools import setup,find_packages

setup(
    name='my-pyapp',
    version='0.0.1',
    packages=find_packages(),
    scripts=['myapp',],
    license='Junk',
    install_requires = [
        'colorlog >= 2.6.0'
    ],
    long_description='Project to demonstrate a directory structure',
    url='https://github.com/raghavan97/python_programs/tree/master/logger',
    author='Raghavan V',
    author_email='raghavan.compilers2009@gmail.com'
)

