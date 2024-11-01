from setuptools import setup, find_packages

setup(
    name="pyconfviewer",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "pyyaml",
        "jsonschema",
        "configparser",
        "python-dotenv",
        "jinja2",  # Add jinja2 to the list of required packages
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            # other development dependencies if needed
        ],
    },
    entry_points={
        "console_scripts": [
            "pyconfviewer = pyconfviewer.__main__:main",
        ],
    },
    description="A Python library for generating HTML views and diffs for configuration files.",
    author="pkaiy81",
    author_email="pkaiy81@outlook.com",
    url="https://github.com/pkaiy81/pyconfviewer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
