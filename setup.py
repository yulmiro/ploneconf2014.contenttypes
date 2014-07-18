from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='ploneconf2014.contenttypes',
      version=version,
      description="Custom Contenttype for Plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Dexterity ContentType Cantv.com.ve Training Custom',
      author='Freddy Banquez',
      author_email='fmbs79@gmail.com',
      url='https://github.com/fbanquez/ploneconf2014.dexterity',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ploneconf2014'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity [grok]',
          'plone.namedfile [blobs]',
          # -*- Extra requirements: -*-
      ],
      extras_require={
          'test': ['plone.app.testing'],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      # The next two lines may be deleted after you no longer need
      # addcontent support from paster and before you distribute
      # your package.
      setup_requires=["PasteScript"],
      paster_plugins = ["ZopeSkel"],

      )
