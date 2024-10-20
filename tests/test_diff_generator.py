from setuptools import setup, find_packages

setup(
    name='pyconfviewer',
    version='0.1.0',
    description='A Python library to visualize and compare configuration files as HTML reports.',
    author='Kohei Kishimoto',
    author_email='demo@demo.local',
    url='https://github.com/pkaiy81/pyconfviewer',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'PyYAML',
        'jinja2',
        'deepdiff',
        'python-dotenv',
        # 他の依存パッケージ
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
