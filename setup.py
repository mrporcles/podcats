import codecs

from setuptools import setup


def _get_long_description():
    with codecs.open('README.rst', encoding='utf8') as f:
        return f.read()


setup(
    name='podcats',
    version='0.7.0',
    description=('An application that generates RSS feeds for podcast '
                 'episodes from local audio files and, optionally, '
                 'exposes both via a built-in web server'),
    long_description=_get_long_description(),
    url='https://github.com/jkbrzt/podcats',
    download_url='https://github.com/jkbrzt/podcats',
    author='Jakub Roztocil',
    author_email='jakub@subtleapps.com',
    license='BSD',
    packages=[
        'podcats'
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'podcats = podcats:main',
        ],
    },
    install_requires=[
        'Flask>=0.9',
        'mutagen>=1.20',
        'humanize>=0.5.1',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Topic :: Multimedia :: Sound/Audio',
    ],
)
