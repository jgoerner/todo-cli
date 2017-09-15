from setuptools import setup


setup(
    name="todo-cli",
    version="0.1",
    py_modules=["todo_cli"],
    install_requires=[
        "Click",
    ],
    entry_points="""
        [console_scripts]
        todo=todo_cli:main
    """,
)
