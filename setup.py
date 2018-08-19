from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()


setup(
    name = 'redvelvet',
    version = '0.0.6',
    description = 'A package for some common data types',
    long_description=long_description,
    author = 'soumasish',
    author_email = 'soumasish@gmail.com',
    url = 'https://github.com/soumasish/redvelvet',
    license = 'Apache 2.0',
    packages = ['redvelvet.graph', 'redvelvet.heap', 'redvelvet.trie'],
    entry_points = {},
)