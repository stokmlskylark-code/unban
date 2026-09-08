from setuptools import setup, find_packages
import os

# Baca file requirements.txt
def read_requirements():
    with open('requirements.txt') as req:
        return [line.strip() for line in req if line.strip() and not line.startswith('#')]

setup(
    name='auto-email-bot',
    version='0.1.0',
    packages=find_packages(),
    install_requires=read_requirements(),
    python_requires='>=3.8',
)
