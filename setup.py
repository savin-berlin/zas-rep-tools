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
      install_requires=[ 'sure','nose', 'rednose', 'blessings', 'testfixtures', 'click', 'regex', 'scipy', 'cached_property', 'raven', "email",  "tweepy", "nltk", "langid", "unicodecsv"],
      zip_safe=False,
      test_suite='nose.collector', # test by installation
      tests_require=['nose'], #test by installation
      entry_points={
          'console_scripts': [
              'zas-rep-tools=zas_rep_tools.cli.main:main',
          ],
      },
)
