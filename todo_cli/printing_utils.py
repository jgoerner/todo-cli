import click
import sys
from terminaltables import AsciiTable

def print_records(records):
    """
    Print records as an ASCII table
    """
    # check for empty result set
    if len(records) == 0:
        click.echo("No Tasks :-)")
        sys.exit(0)
    # construct records from dicts
    header = [list(records[0].keys())]
    values = list(map(lambda dct: list(dct.values()), records))
    tbl = AsciiTable(header+values)
    click.echo(tbl.table)


def _generate_choice_list(choices):
    """
    Generate a neat numbered list
    """
    template = "{idx} - {task}"
    choices_numbered = [template.format(idx=idx, task=task) for idx, task in enumerate(choices, 1)]
    choice_list = "\n".join(choices_numbered)
    return choice_list


def task_selection(choices):
    """
    Generate a proper promt question based on choices
    """
    prefix = "What task did you finish?"
    choice_list = _generate_choice_list(choices)
    suffix = ", ".join(map(lambda i: str(i+1), range(len(choices))))
    task_selection = "\n".join([prefix, choice_list, suffix])
    return task_selection
