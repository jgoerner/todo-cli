import click
import os
import sys
from .db_utils import insert_record, retrieve_record, mark_done
from .printing_utils import print_records, task_selection


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
            click.echo("Please specify it directly or create an empty *.tdb file")
            sys.exit(1)
        else:
            taskdb = matches[0]
    ctx.obj = {}
    ctx.obj["DB"] = taskdb


@main.command()
@click.option("--due", "-d", default="alltime",
              type=click.Choice(["alltime", "today"]))
@click.option("--all", is_flag=True, default=False)
@click.pass_context
def show(ctx, due, all):
    """
    Show tasks based on <due>
    """
    records = retrieve_record(ctx.obj["DB"], due=due, all=all)
    print_records(records)


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
    due = "sometime" if due == "-1" else "today"
    insert_record(ctx.obj["DB"], task=task, due=due)
    click.echo("'{}' successfully added to your todo list".format(task))


@main.command()
@click.pass_context
def done(ctx):
    """
    Mark an "OPEN" task as "COMPLETED"
    """
    open_tasks = retrieve_record(ctx.obj["DB"], due="alltime", all=False)
    choices = list(map(lambda dct: dct["task"], open_tasks))
    done_idx = click.prompt(task_selection(choices), type=click.IntRange(1, len(choices)))
    done = choices[done_idx-1]
    mark_done(ctx.obj["DB"], task=done)
