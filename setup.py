try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'pyduino',
    description = 'PyDuino project aims to make python interactive with hardware particularly arduino.',
    url = 'https://github.com/lite-david/PyDuino',
    keywords = 'python arduino',
    author = '###', #edit this line
    author_email = '###', #edit this line too
    version = '0.0.0',
    packages = ['pyduino'],
    scripts=["bin/pyduino"],
    install_requires = ['pyserial'],
    classifiers = [
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha', #Development status 3-Alpha,4-Beta,5-stable
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
