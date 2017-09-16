from setuptools import setup, find_packages


setup(
    name="todo-cli",
    version="0.1",
    author="Joshua Goerner",
    author_email="joshua.goerner@gmail.com",
    packages=find_packages(),
    install_requires=[
        "Click",
    ],
    entry_points="""
        [console_scripts]
        todo=todo_cli.todo_cli:main
    """,
)
