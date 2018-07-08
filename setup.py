from setuptools import setup

setup(
    name="luoo",
    packages=["luoo"],
    include_package_data=True,
    install_requires=[
        "flask",
        "peewee",
        "requests",
        "beautifulsoup4",
        "celery",
        "user_agent",
        "click",
    ],
    entry_points={"console_scripts": ["luoo=wiki:luoo"]},
)
