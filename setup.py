# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='tc_core',
    version='0.5',
    url='http://github.com/thumbor_community/core',
    license='MIT',
    author='Thumbor Community',
    description='Thumbor community extensions core',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'libthumbor>=2.0.2',
        'thumbor>=7.0.10',
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
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
