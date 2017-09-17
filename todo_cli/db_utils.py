import os
from tinydb import TinyDB, Query
from tinydb.operations import set as tdbset
from contextlib import contextmanager


@contextmanager
def get_tinydb(path):
    """
    Contextmanager to open/close TinyDBs
    """
    if not os.path.exists(path):
        raise ValueError("The DB {} does not exist".format(path))
    try:
        db = TinyDB(path)
        yield db
    finally:
        db.close()


def _construct_record(**kwargs):
    """
    Construct a record ased on an kwargs list
    """
    record = {"status" : "OPEN"}
    record.update(kwargs)
    return record


def insert_record(tinydb, **kwargs):
    """
    Insert a record into a tinyDB
    """
    # generate the record based on kwargs
    record = _construct_record(**kwargs)
    # use a context manager to ensure the db is closed
    with get_tinydb(tinydb) as db:
        db.insert(record)

def _get_due_query(due):
    if due == "alltime":
        query = ""
    elif due == "today":
        query = "Query()['due'] == 'today'"
    else:
        raise ValueError("{} is not a valid due parameter".format(due))
    return query


def _get_status_query(status):
    if status:
        query = ""
    else:
        query = "Query()['status'] == 'OPEN'"
    return query


def _construct_query(**kwargs):
    sub_conditions = []
    # get due condition
    sub_conditions.append(_get_due_query(kwargs["due"]))
    # get status condition
    sub_conditions.append(_get_status_query(kwargs["all"]))
    # combine sub_conditions
    # adjust if a single condition is set
    if len(list(filter(None, sub_conditions))) == 0:
        query = "db.all()"
    else:
        condition = " & ".join(map(lambda cond: "({})".format(cond),filter(None, sub_conditions)))
        query = "db.search({})".format(condition)
    return query


def retrieve_record(tinydb, **kwargs):
    """
    Retrieve record(s) from the TinyDB
    """
    q = _construct_query(**kwargs)
    #print(q)
    with get_tinydb(tinydb) as db:
        result = eval(q)
        #print(result)
    return result


def mark_done(tinydb, task):
    """
    Mark <task> as "CLOSED"
    """
    with get_tinydb(tinydb) as db:
        db.update(tdbset("status", "CLOSED"), Query()["task"] == task)

