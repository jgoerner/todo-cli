import click
import os
import sys
from .db_utils import insert_record, retrieve_record


@click.group()
@click.pass_context
@click.option("--taskdb", default=".")
def main(ctx, taskdb):
    """
    Handle todos
    """
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
@click.option("--due", "-d", default="all", type=click.Choice(["all", "today"]))
@click.pass_context
def show(ctx, due):
    """
    Show tasks based on <due>
    """
    click.echo("SHOWING {} from {}".format(due, ctx.obj["DB"]))
    retrieve_record(ctx.obj["DB"], due=due)


@main.command()
@click.option("--task", "-t", help="Task to be added (in ' ')")
@click.option("--due", "-d", default="-1", help="Due in x days")
@click.pass_context
def new(ctx, task, due):
    """
    Add a new task
    """
    if task is None:
        click.echo("Please specify a task")
        sys.exit(1)
    due = "sometime" if due == "-1" else "in {} days".format(due)
    insert_record(ctx.obj["DB"], task=task, due=due)
    click.echo("'{}' successfully added to your todo list".format(task))
