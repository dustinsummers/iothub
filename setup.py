"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from iothub import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()


class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['py.test', '--cov=iothub', '--cov-report-term-missing'])
        raise SystemExit(errno)


    setup(
            name = 'iothub',
            version = __version__,
            description = 'A command line program for Azure IoT_Hub Interactions.',
            long_description = long_description,
            url = 'https://www.google.com',
            author = 'Dustin Summers',
            author_email = 'dustin.summers@fortegollc.com',
            license = 'UNLICENSE',
            classifiers = [
                'Intended Audience :: Developers/Hackers',
                'Topic :: Utilities',
                'License :: Fortego, LLC',
                'Natural Language :: English',
                'Operating System :: OS Independent',
                'Programming Language :: Python :: 2',
                'Programming Language :: Python :: 2.6',
                'Programming Language :: Python :: 2.7',
                'Programming Language :: Python :: 3',
                'Programming Language :: Python :: 3.2',
                'Programming Language :: Python :: 3.3',
                'Programming Language :: Python :: 3.4',
                'Programming Language :: Python :: 3.6',
                'Programming Language :: Python :: 3.7'
                ],
            keywords = 'cli',
            packages = find_packages(exclude=['docs', 'tests*']),
            install_requires = ['docopt'],
            extras_require = {
                'test': ['coverage', 'pytest', 'pytest-cov'],
            },
            entry_points = {
                'console_scripts': [
                'iothub=iothub.CLI:main',
                ],
            },
        #cmdclass = {'test': RunTests},
    )




