from setuptools import find_packages, setup

setup(
    name='test_package',
    packages=find_packages(where='src'),
    version='0.0.1',
    description='creating dummy pyton package',
    author='ronilpatil',
    license='MIT',
    package_dir={'': 'src'},
    url=f"https://github.com/ronylpatil/test_package",
    project_urls={
        "Bug Tracker": f"https://github.com/ronylpatil/test_package/issues",
    },
)
