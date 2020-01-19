
from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Data_validation',
    url='https://github.com/aoyerinde/Data_validation_v1',
    author='Afiz Oyerinde',
    author_email='ayodejioyerinde93@gmail.com',
    # Needed to actually package something
    packages=['Data_validation_v1'],
    # Needed for dependencies
    install_requires=['numpy', 'pandas'],
    # *strongly* suggested for sharing
    version='1.0',
    # The license can be anything you like
    license='None',
    description='Data validation package',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)