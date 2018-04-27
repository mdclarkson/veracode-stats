from setuptools import setup, find_packages

setup(
    name="veracodestats",
    version="2018.4.4",
    packages=find_packages(),
    license="MIT",
    author="ctcampbell",
    url="https://github.com/ctcampbell/veracode-stats",
    author_email="chris@ctcampbell.com",
    description="Generate interesting statistics for a Veracode account",
    install_requires=[
        "requests >= 2.18.4",
        "pytz >= 2018.4",
    ],
    entry_points={
        "console_scripts": ["veracodestats = veracodestats.main:start"]
    }
)
