
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
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',

          'License :: OSI Approved :: MIT License',

          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
        ],

      )
