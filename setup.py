from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    version = '0.0.4',
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
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points = {'console_scripts': ['wikilinks = wikilinks:main']},
)
