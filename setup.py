from setuptools import setup

setup(name='zas-rep-tools',
      version='0.1',
      description='This Tool-set helps to make a repetitions analysis in social media corpora much comfortable',
      url='https://github.com/savin-berlin/zas-rep-tools',
      git_url='git@github.com:savin-berlin/zas-rep-tools.git',
      author='Egor Savin',
      author_email='science@savin.berlin',
      license='MIT',
      packages=['zas_rep_tools'],
      install_requires=[ 'sure','nose', 'rednose', 'blessings', 'testfixtures',
      'click', 'regex',  'cached_property', 'raven', "email",  "tweepy", "nltk",
      "langid",  "lxml", "logutils", "pyhashxx", "colored_traceback", "colorama",
      "unicodecsv","psutil","execnet","validate_email","console-menu","python-twitter", "twitter",
      "enlighten", "emoji", "textblob","textblob_de", "textblob_fr", "kitchen", "uniseg",
      "pysqlcipher", "pystemmer"],
      zip_safe=False,
      test_suite='nose.collector', # test by installationls
      tests_require=['nose'], #test by installation
      entry_points={
          'console_scripts': [
              'zas-rep-tools=zas_rep_tools.cli.main:main',
          ],
      },
      classifiers=[ 
      'Development Status :: 1 - Beta', 
      'Intended Audience :: NLP', 
      'License :: OSI Approved :: MIT',
      'Programming Language :: Python :: 2'
]
)
