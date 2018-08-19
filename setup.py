from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()


setup(
    name = 'redvelvet',
    version = '0.1.1',
    description = 'Some not so common data types, white hot, ready to use!',
    long_description=long_description,
    author = 'soumasish',
    author_email = 'soumasish@gmail.com',
    url = 'https://github.com/soumasish/redvelvet',
    license = 'Apache 2.0',
    packages = ['redvelvet.graph', 'redvelvet.heap', 'redvelvet.trie'],
)