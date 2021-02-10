# Always prefer setuptools over distutils
from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="wa_leg_api",  # Required
    version="0.0.0",  # Required
    description="A python API for the Washington State Legislature web services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/j-carson/wa-leg-api",
    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 2 - Pre-Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        # Pick your license as you wish
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent"
    ],
    keywords=["washington-state",
              "legislature",
              "government-data"],  # Optional
    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    packages=["wa_leg_api"],
    python_requires=">=3.7, <4",
    install_requires=[
        "beautifulsoup4",
        "requests",
    ],  # Optional
    extras_require={  # Optional
        "dev": ["lxml", "pytest"],
        "docs": ["sphinx", "recommonmark"]
    },
    # List additional URLs that are relevant to your project as a dict.
    project_urls={"Source": "https://github.com/j-carson/wa-leg-api",
                 "Documentation": "https://wa-leg-api.readthedocs.io"},  
)
