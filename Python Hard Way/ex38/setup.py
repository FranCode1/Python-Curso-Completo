from setuptools import setup, find_packages

setup(
    name='projectname',
    version='0.1',
    description='My Project',
    author='My Name',
    author_email='My email',
    url='URL to get it at.',
    download_url='Where to download it.',
    packages=find_packages(),
    install_requires=['nose'],
    scripts=[],
)