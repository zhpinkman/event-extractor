from setuptools import setup


setup(
    name="event_extractor",
    version='0.1',
    description='Get the historical events easily',
    author='Zhivar Sourati',
    author_email='zhivarsourati@gmail.com',
    packages=['event_extractor'],
    zip_safe=False,
    install_requires=[
        'bs4',
        'requests'
    ],
)
