import setuptools

VERSION = '19.2.5.0'

setuptools.setup(
    name='daterangepy',
    version=VERSION,
    description="Генерация периодов",
    packages=['daterangepy'],
    install_requires=['pandas', 'python-dateutil', 'pendulum'],
    license='MIT',
    url='https://github.com/pavelmaksimov/daterangepy',
    author='Pavel Maksimov',
)
