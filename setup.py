import setuptools

VERSION = '29.11.18'

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='daterange',
    version=VERSION,
    description="Генерация периодов",
    long_description=long_description,
    packages=['daterange'],
    install_requires=['pandas', 'dateutil'],
    license='MIT',
    url='https://github.com/pavelmaksimov/daterange',
    author='Pavel Maksimov',
)
