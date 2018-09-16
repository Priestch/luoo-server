from setuptools import setup

setup(
    name="luoo",
    packages=["luoo"],
    include_package_data=True,
    install_requires=[
        "flask",
        "requests",
        "beautifulsoup4",
        "celery",
        "user_agent",
        "click",
        "sqlalchemy",
        "marshmallow",
    ],
    entry_points={"console_scripts": ["luoo=wiki:luoo"]},
)
