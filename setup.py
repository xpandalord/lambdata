"""
lambdata - a collection of Data Science helper functions
"""

import setuptools

REQUIRED = [
    "numpy",
    "pandas",
    "matplotlib",
    "scikit-learn"
]

with open("README.md", "r") as file:
    LONG_DESCRIPTION = file.read()

setuptools.setup(
    name="lambdata-xpandalord",
    version="0.0.6",
    author="xpandalord",
    description="A collection of Data Science helper functions",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/xpandalord/lambdata",
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)