import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(
    name="py2048",
    version="1.0.0",
    author="Gantulga G",
    author_email="limited.tulgaa@gmail.com>",
    description="Pygame base class for ease of use",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gantulga9480/Game",
    packages=['py2048'],
    license='MIT',
    install_requires=['pygame'],
)
