from setuptools import setup, find_packages
from setuptools.command.install import install
import shutil
import os

# Custom install command to perform cleanup after installation
class CustomInstall():
    def __init__(self):
        self.run()
    def run(self):
        # Delete the build directory
        build_dir = 'build'
        if os.path.exists(build_dir):
            shutil.rmtree(build_dir)

        # Delete the .egg-info directory
        egg_info_dir = 'terrance.egg-info'  # Replace with your actual library name
        if os.path.exists(egg_info_dir):
            shutil.rmtree(egg_info_dir)

        print('Successful cleanup of extraeneous files')

# Call setup with the custom install command
setup(
    name='terrance',
    version='1beta',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': ['terrance = terrance.roboctl:main',]
    },
)

CustomInstall()