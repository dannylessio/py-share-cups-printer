from setuptools import setup, find_packages

setup(name='py-share-cups-printer',
      version='0.1',
      description='Cups sharing becomes easy',
      url='https://github.com/dannylessio/py-share-cups-printer',
      author='Danny Lessio',
      author_email='danny.lessio@gmail.com',
      license='GPLv3',
      packages=find_packages(),
      install_requires=[
          'pycups',
      ],
      entry_points = {
        'console_scripts': ['print=py_share_cups_printer.command_line:main'],
      },
      zip_safe=False)
