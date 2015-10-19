# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='tc_core',
    version='0.3.0',
    url='http://github.com/thumbor_community/core',
    license='MIT',
    author='Thumbor Community',
    description='Thumbor community extensions core',
    packages=['tc_core'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'thumbor>=5.0.6',
    ],
    extras_require={
        'tests': [
            'pyvows',
            'coverage',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
