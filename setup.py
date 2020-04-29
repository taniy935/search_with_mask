"""Setup file"""

from setuptools import setup, find_packages
import search_with_mask

setup(
    name='search_with_mask',
    version=search_with_mask.__version__,
    description='search with mask',
    long_description=open('README.md').read(),
    url='',
    author='taniy935',
    author_email='taniy935@yandex.ru',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={
        'console_scripts': [
            'search_with_mask = search_with_mask.search_with_mask:run'
        ]
    },
    include_package_data=True,
    packages=find_packages(exclude=['tests']),
    test_suite='tests'
)
