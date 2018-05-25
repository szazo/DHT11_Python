import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rpi-dht11",
    version="1.0.0",
    author="szazo",
    description="A package for reading data from DHT11",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/szazo/DHT11_Python.git",
    packages=setuptools.find_packages()
)