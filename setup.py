from setuptools import setup
from setuptools import find_packages


setup(
    name="event_extractor",
    version='0.1',
    description='Get the historical events easily',
    author='Zhivar Sourati',
    author_email='zhivarsourati@gmail.com',
    packages=find_packages(include=['event_extractor']),
    zip_safe=False,
    install_requires=[
        'bs4',
        'requests'
    ],
)
