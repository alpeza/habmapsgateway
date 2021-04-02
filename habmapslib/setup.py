
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="habmapslib",
    version="1.0.0",
    author="Alpeza",
    author_email="",
    description="Librería para el acceso a habmaps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alpeza/habmapsgateway",
    packages=setuptools.find_packages(),
    install_requires=[
        'paho_mqtt>=1.5.1'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
) 
