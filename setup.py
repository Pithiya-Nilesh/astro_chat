from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in astro_chat/__init__.py
from astro_chat import __version__ as version

setup(
	name="astro_chat",
	version=version,
	description="this app for create a chat ui in frappe and astro",
	author="Nilesh Pithiya",
	author_email="nilesh@sanskartechnolab.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
