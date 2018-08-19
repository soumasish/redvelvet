from distutils.core import setup

setup(
    name = 'redvelvet',
    version = '0.0.2',
    description = 'A package for some common data types',
    author = 'soumasish',
    author_email = 'soumasish@gmail.com',
    url = 'https://github.com/soumasish/redvelvet',
    license = 'Apache 2.0',
    packages = ['redvelvet.graph', 'redvelvet.heap', 'redvelvet.trie'],
    entry_points = {},
)