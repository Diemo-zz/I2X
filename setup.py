from setuptools import setup

setup(name='first_package_structure',
      version='0.1',
      description='The funniest joke in the world',
      url='https://github.com/Diemo-zz/I2X',
      author='Diarmaid de Búrca',
      author_email='diarmaiddeburca@gmail.com',
      license='MIT',
      packages=['first_package_structure'],
      install_requires=[
          'nltk',
      ],
      zip_safe=False)