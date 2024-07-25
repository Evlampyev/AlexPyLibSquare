from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='find_squares',
    version='0.0.1',
    author='Evlampyev Alexandr',
    author_email='Evlampyev.Alex@gmail.com',
    description='This is the simplest module for finding squares',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='your_url',
    packages=find_packages(),
    install_requires=['requests>=2.25.1'],
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='squares finding',
    project_urls={
        'GitHub': 'your_github'
    },
    python_requires='>=3.6'
)
