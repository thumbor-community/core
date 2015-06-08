# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='thumbor_community',
    version='0.1',
    url='http://github.com/thumbor_community/thumbor_community',
    license='MIT',
    author='Thumbor Community',
    description='Thumbor community extensions core',
    packages=['thumbor_community'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'thumbor',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
