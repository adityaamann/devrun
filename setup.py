from setuptools import setup

setup(
    name="devrun",
    version="0.1",
    py_modules=["main"],
    install_requires=[
        "groq",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "devrun=main:main",
        ],
    },
)

