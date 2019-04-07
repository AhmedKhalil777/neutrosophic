import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="neutrosophic_pkg",
    version="0.0.1",
    author="Haitham A. El-Ghareeb",
    author_email="helghareeb@mans.edu.eg",
    description="Python Open-Source Implementation of Neutrosophic Theory",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/helghareeb/neutrosophic",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
