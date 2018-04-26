from setuptools import setup

setup(
    name="veracodestats",
    version="2018.4",
    packages=["veracodestats", "veracodestats.model"],
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
