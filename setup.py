from setuptools import find_packages, setup

with open("README.rst", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    requirements = [rq.replace("==", ">=") for rq in f.read().splitlines()]

setup(
    name="dummypackage12624",
    version="0.0.16",
    author="ronilpatil",
    author_email="xyz@gmail.com",
    description=("Dummy python package"),
    keywords=["package", "python", "pytest"],
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/ronylpatil/test_package",
    classifiers=[
        "Development Status ::  2 - Pre-Alpha",
        "License :: MIT",
        "Operating System :: Windows 10 :: Linux :: MacOS",
        "Environment :: Console",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Intended Audience :: Researchers/Data Analysts",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    python_requires=">=3.9",
    project_urls={
        "Bug Tracker": f"https://github.com/ronylpatil/test_package/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=requirements    
)
