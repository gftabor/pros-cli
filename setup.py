import subprocess

from setuptools import setup

# setup.py for non-frozen builds
from pip.req import parse_requirements
install_reqs = [str(r.req) for r in parse_requirements('requirements.txt', session=False)]

try:
    v = subprocess.check_output(['git', 'describe', '--dirty'], stderr=subprocess.DEVNULL).decode().strip().replace('-','b', 1).replace('-','.')
except subprocess.CalledProcessError as e:
    v = open('version').read().strip()

setup(
    name='pros-cli',
    version=v,
    packages=['prosflasher', 'proscli', 'prosconfig', 'prosconductor', 'prosconductor.providers'],
    url='https://github.com/purduesigbots/pros-cli',
    license='MPL-2.0',
    author='Purdue ACM SIGBots',
    author_email='pros_development@cs.purdue.edu',
    description='Command Line Interface for managing PROS projects',
    install_requires=install_reqs,
    entry_points="""
        [console_scripts]
        pros=proscli.main:main
        """
)
