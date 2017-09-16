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
