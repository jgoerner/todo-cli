# Todo-CLI
A small CLI application to track todos based on [
click](http://click.pocoo.org/5/), 
[tinydb](http://tinydb.readthedocs.io/en/latest/) and 
[terminaltables](https://pypi.python.org/pypi/terminaltables).

## Sample usage
### add a task
```
todo new "read a book"

>> 'read a book' successfully added to your todo list test.tdb
```

### get the all open tasks
```
todo show

>> +----------+-------------+--------+
   | due      | task        | status |
   +----------+-------------+--------+
   | sometime | read a book | OPEN   |
   +----------+-------------+--------+
```

### get all tasks
```
todo show --all

>> +----------+--------------------------+--------+
   | due      | task                     | status |
   +----------+--------------------------+--------+
   | sometime | clean the kitchen        | CLOSED |
   | today    | gardening                | CLOSED |
   | sometime | cook fancy asia wok dish | CLOSED |
   | sometime | car to gasstation        | CLOSED |
   | sometime | call 555-NOSE            | CLOSED |
   | sometime | read a book              | OPEN   |
   +----------+--------------------------+--------+
```

### complete a task
```
todo done

>> What task did you finish?
   1 - read a book
   2 - clean the bathroom
   1, 2: 2
```

### get a cli like help
```
todo --help

>> Usage: todo [OPTIONS] COMMAND [ARGS]...

  Handle todos

Options:
  --help  Show this message and exit.

Commands:
  done  Mark a task as done
  new   Add a new task
  show  Show tasks
```
