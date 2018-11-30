import setuptools

VERSION = '30.11.18'

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='daterangepy',
    version=VERSION,
    description="Генерация периодов",
    long_description=long_description,
    packages=['daterangepy'],
    install_requires=['pandas', 'python-dateutil'],
    license='MIT',
    url='https://github.com/pavelmaksimov/daterangepy',
    author='Pavel Maksimov',
)
