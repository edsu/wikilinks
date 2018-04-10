from setuptools import setup

setup(
    version = '0.0.3',
    name = 'wikilinks',
    url = 'http://github.com/edsu/wikilinks',
    author = 'Ed Summers',
    author_email = 'ehs@pobox.com',
    license = 'http://www.opensource.org/licenses/mit-license.php',
    py_modules = ['wikilinks'],
    install_requires = ['six'],
    setup_requires = ['pytest-runner'],
    tests_require= ['pytest'],
    description = 'Get a list of Wikipedia articles that link to a website.',
    entry_points = {'console_scripts': ['wikilinks = wikilinks:main']},
)
