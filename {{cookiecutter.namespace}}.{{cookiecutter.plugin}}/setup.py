from setuptools import find_namespace_packages, setup


def main():
    """Setup"""
    setup(
        name='{{cookiecutter.namespace}}-{{cookiecutter.plugin}}',
        version='1.0.0',
        author='{{cookiecutter.author}}',
        author_email='{{cookiecutter.author_email}}',
        packages=find_namespace_packages(exclude=("tests",)),
        install_requires=[
            'click',
        ],
        extras_require={
            'test': ['pytest', 'flake8', 'pytest-cov', 'pytest-flake8', 'flake8-import-order',
                     'flake8-docstrings'],
        },
        entry_points={
            '{{cookiecutter.namespace}}.commands': '{{cookiecutter.plugin}} = {{cookiecutter.namespace}}.{{cookiecutter.plugin}}.main:cli'}
    )


if __name__ == '__main__':
    main()
