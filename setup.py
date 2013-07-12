from setuptools import setup, find_packages
import os

version = '2.0a6.dev0'

setup(name='uvc.layout',
      version=version,
      description="Basic Layout for UVC-Projects",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Christian Klinger',
      author_email='cklinger@novareto.de',
      url='http://www.novareto.de',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['uvc'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'dolmen.forms.composed',
      ],
      entry_points={
          'fanstatic.libraries': [
              'uvc.layout = uvc.layout.libraries:library',
          ]
      }
      )
