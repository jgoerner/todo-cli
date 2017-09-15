import click
import os
import sys


@click.group()
@click.pass_context
@click.option("--taskdb", default=".")
def main(ctx, taskdb):
    if taskdb == ".":
        matches = [match for match in os.listdir(".") if
                   match.endswith(".tdb")]
        if len(matches) != 1:
            click.echo("Could not find a distinct task db in current dir.")
            click.echo("Please specify it directly.")
            sys.exit(1)
        else:
            taskdb = matches[0]
    ctx.obj = {}
    ctx.obj["DB"] = taskdb


@main.command()
@click.option("--filter", "-f", default="all", type=click.Choice(["all", "today"]))
@click.pass_context
def show(ctx, filter):
    """
    Show tasks based on <filter>
    """
    click.echo("SHOWING {} from {}".format(filter, ctx.obj["DB"]))


@main.command()
@click.option("--task", "-t", help="Task to be added (in ' ')")
@click.option("--due", "-d", default="-1", help="Due in x days")
def new(task, due):
    """
    Add a new task
    """
    if task is None:
        click.echo("Please specify a task")
        sys.exit(1)
    due = "sometime" if due == "-1" else "in {} days".format(due)
    print("added {}, due {}".format(task, due))

