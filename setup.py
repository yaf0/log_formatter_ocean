# setup.py

from setuptools import setup, find_packages

setup(
    name='log_formatter_ocean',
    version='0.4.1',
    description='log formatting utility',
    license="MIT",
    author="ocean",
    long_description = "A simple log formatting utility for Python projects",
    long_description_content_type='text/markdown',
    url="https://github.com/yaf0/log_formatter_ocean",
    project_urls={
        'Documentation': 'https://github.com/yaf0/log_formatter_ocean',
        'Source': 'https://github.com/yaf0/log_formatter_ocean',
        'Bug Tracker': 'https://github.com/yaf0/log_formatter_ocean/issues',
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='logging log formatting',
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[
        'requests',
        'numpy',
        'log-formatter-oc',
        'huluwa-art',
    ]
)
