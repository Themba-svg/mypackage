from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Themba-svg/package-name',
    author='Sinethemba',
    author_email='sinengwenya97@gmail.com'
)
