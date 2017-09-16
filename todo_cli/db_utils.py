import os
from tinydb import TinyDB
from contextlib import contextmanager


def construct_record(**kwargs):
    """
    Construct a record ased on an kwargs list
    """
    record = {"status" : "OPEN"}
    record.update(kwargs)
    return record


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


def insert_record(tinydb, **kwargs):
    """
    Insert a record into a tinyDB
    """
    # generate the record based on kwargs
    record = construct_record(**kwargs)
    # use a context manager to ensure the db is closed
    with get_tinydb(tinydb) as db:
        db.insert(record)


def retrieve_record(tinydb, **kwargs):
    """
    Retrieve record(s) from the TinyDB
    """
    # TODO - Implement it :-)
    pass
