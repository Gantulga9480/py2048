import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Py2048",
    version="1.0.4",
    author="Gantulga G",
    author_email="limited.tulgaa@gmail.com",
    description="Python implementation of 2048 game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gantulga9480/Py2048",
    packages=['Py2048'],
    license='MIT',
    install_requires=['pygame', 'numpy'],
)
