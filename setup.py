#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='factur-x',
    version='0.1',
    author='Alexis de Lattre',
    author_email='alexis.delattre@akretion.com',
    url='https://github.com/akretion/factur-x',
    description='Factur-X: electronic invoicing standard for Germany & France',
    long_description=open('README.rst').read(),
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: BSD License',
        "Operating System :: OS Independent",
    ],
    keywords='e-invoice ZUGFeRD Factur-X Chorus',
    packages=find_packages(),
    install_requires=[r.strip() for r in
                      open('requirement.txt').read().splitlines()],
    include_package_data=True,
    scripts=[
        'bin/facturx-pdfgen',
        'bin/facturx-pdfextractxml',
        'bin/facturx-xmlcheck'],
    zip_safe=False,
)