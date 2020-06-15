from setuptools import setup, find_packages


with open('requirements.txt') as fp:
    install_requires = fp.readlines()


setup(
    name='bori-models',
    packages=find_packages(),
    version='0.1',
    description='Models to use with BORI discord bot.',
    author='Fran Agustín',
    install_requires=install_requires
)
