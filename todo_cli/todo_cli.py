import click
import os
import sys
from .db_utils import insert_record, retrieve_record, mark_done
from .printing_utils import print_records, task_selection
from .general_utils import needs_taskdb


@click.group()
def main():
    """
    Handle todos
    """
    pass


@main.command()
@click.option("--taskdb", "-tdb", default=".", help="DB where tasks are stored")
@click.option("--due", "-d", default="alltime", type=click.Choice(["alltime", "today"]))
@click.option("--all", is_flag=True, default=False, help="show all tasks (including closed ones)")
@needs_taskdb
def show(taskdb, due, all):
    """
    Show tasks
    """
    records = retrieve_record(taskdb, due=due, all=all)
    print_records(records)


@main.command()
@click.argument("task")
@click.option("--taskdb", "-tdb", default=".", help="DB where tasks are stored")
@click.option("--due", "-d", default="-1", help="Due in x days")
@needs_taskdb
def new(taskdb, task, due):
    """
    Add a new task
    """
    due = "sometime" if due == "-1" else "today"
    insert_record(taskdb, task=task, due=due)
    click.echo("'{}' successfully added to your todo list {}".format(task, taskdb))


@main.command()
@click.option("--taskdb", "-tdb", default=".", help="DB where tasks are stored")
@needs_taskdb
def done(taskdb):
    """
    Mark a task as done
    """
    open_tasks = retrieve_record(taskdb, due="alltime", all=False)
    choices = list(map(lambda dct: dct["task"], open_tasks))
    done_idx = click.prompt(task_selection(choices), type=click.IntRange(1, len(choices)))
    done = choices[done_idx -1]
    mark_done(taskdb, task=done)
