
#!/usr/bin/env python

from setuptools import setup
from os import path

setup(name='merkletree',
      version='1.0',
      description='A implemenation of Merkle Tree',
      author='Zhanchen Guo',
      author_email='markguo40@gmail.com',
      url='https://github.com/markguo40/merkletree',
      download_url='https://github.com/markguo40/merkletree.git',
      py_modules=['merkle'],
      keywords=['merkle', 'tree', 'blockchain'],
      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 3 - Alpha',

          # Indicate who your project is intended for
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
        ],

      )
