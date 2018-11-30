import setuptools

VERSION = '30.11.18.2'

setuptools.setup(
    name='daterangepy',
    version=VERSION,
    description="Генерация периодов",
    packages=['daterangepy'],
    install_requires=['pandas', 'python-dateutil'],
    license='MIT',
    url='https://github.com/pavelmaksimov/daterangepy',
    author='Pavel Maksimov',
)
