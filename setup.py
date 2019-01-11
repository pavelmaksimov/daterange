import setuptools

VERSION = '11.01.19.0'

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
