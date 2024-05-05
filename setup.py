from setuptools import setup, find_packages

setup(
    name='MCFG_PARSER',
    version='0.1',
    packages= find_packages(),
    description='A Python package for parsing with MCFGs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Lateef Adeleke',
    author_email='ladeleke@ur.rochester.edu',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: NLP researchers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='parsing grammar MCFG', 'Agenda_based parsing'
)

