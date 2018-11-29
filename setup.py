import setuptools

VERSION = '29.11.18'

setuptools.setup(
    name='daterange',
    version=VERSION,
    packages=['daterange'],
    install_requires=['pandas'],
    license='MIT',
    url='https://github.com/pavelmaksimov/daterange',
    author='Pavel Maksimov',
)
