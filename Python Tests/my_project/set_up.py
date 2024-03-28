from setuptools import setup, find_packages

setup(
    name='my_project',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your project's dependencies here.
        # They will be installed by pip when your project is installed.
        'pandas==1.2.4',
        'numpy==1.20.3',
        # Add other dependencies as needed
    ],
    # Add other setup parameters as needed
)
