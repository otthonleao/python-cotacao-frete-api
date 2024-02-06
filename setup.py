import io
import os
from setuptools import find_packages, setup

def read(*paths, **kwargs):
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content

def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]

setup(
    name="shippingPriceAPI",
    version="0.2.0",
    description="API to check delivery prices and compare shipping companies",
    url="shippingPriceAPI.io",
    python_requires=">=3.8",
    long_description="Shipping Price API developed with FastAPI Framework for Python to check delivery prices and compare shipping companies",
    long_description_content_type="text/markdown",
    author="Otthon Leao",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["shippingPriceAPI = shippingPriceAPI.cli:main"]
    }
)
