import os
import sys
import click
from functools import wraps


def needs_taskdb(func):
    """
    Decorator to ensure that a taskdb is given
    """
    @wraps(func)
    def wrapper(taskdb, *args, **kwargs):
        if taskdb == ".":
            matches = [match for match in os.listdir(".") if match.endswith(".tdb")]
            if len(matches) != 1:
                click.echo("Could not find a distinct task db in current dir.")
                click.echo("Please specify it directly or create an empty *.tdb file")
                sys.exit(1)
            else:
                taskdb = matches[0]
        # check if db exists
        if not os.path.exists(taskdb):
            click.echo("The task db {} does not exist".format(taskdb))
            # otionally create an empty db
            if click.confirm("Do you want it to be created?", abort=True):
                open(taskdb, "x")
        func(taskdb, *args, **kwargs)
    return wrapper
