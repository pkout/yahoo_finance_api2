import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yahoo_finance_api2",
    version="0.0.6",
    author="Petr Kout",
    description="Yahooo Finance API package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pkout/yahoo_finance_api2",
    packages=setuptools.find_packages(),
    install_requires=[
      "pprint",
      "pyyaml",
      "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
