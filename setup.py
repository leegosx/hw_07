from setuptools import setup, find_namespace_packages

setup(
    name="clean_folder",
    version=0.1,
    description="This is a sorter for files, it sorts files by folders and rename the folders according to the names of files",
    url="https://github.com/leegosx/hw_06/blob/main/sorter.py",
    author="Dmytro Klymenko",
    author_email="klimenko.dmitris@gmail.com",
    packages=find_namespace_packages(),
    include_package_data=True, 
    entry_points={
        'console_scripts':  [
        'clean-folder = clean_folder.clean:main',
        ],

    },
)