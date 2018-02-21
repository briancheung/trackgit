from setuptools import find_packages
from setuptools import setup

version = '0.01dev'

install_requires = []

setup(
    name='trackgit',
    version=version,
    description='Tool for using git to track experiments and maintain reproducibility',
    author='Brian Cheung',
    author_email='bcheung@berkeley.edu',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    )
