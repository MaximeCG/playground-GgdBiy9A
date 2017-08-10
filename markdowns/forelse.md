# The controversial for...else statement in Python

Among all the great features Python has to offer, the `for...else` statement is one of my favorites. However, when I talk about it, it seems that people do not really see the point of it. I'll show you what it does, how to use it and, more importantly, how not to use it.

In a loop, the `else` clause is executed at the end of the loop if it hasn't been terminated by a `break`, a `return` or an exception. Note that it will also be executed even if the body of the loop was never entered (e.g. iteration over an empty list). Here's a simple example from the [official documentation](https://docs.python.org/3.6/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops), feel free to play with the code.

@[For-Else Example]({"stubs": ["example1.py"], "command": "python3 example1.py"})

Without using the `else` statement, the easy solution would be to use a variable and test the variable at the end of the loop:

@[For-Else Example]({"stubs": ["example2.py"], "command": "python3 example2.py"})

Actually, when I feel the need of a `for-else`, the pattern is always the same:

```Python
found = False
for x in l:
    if check_condition(x):
        do_something(x)
        found = True
        break
if not found:
    do_something_else()
```

...becomes:

```Python
for x in l:
    if check_condition(x):
        do_something(x)
        break
else:
    do_something_else()
```

The main argument against the use of the `for-else` structure is the possible lack of code readability. For instance, people may believe that the `else` belongs to the `if` instead of the `for`. As a consequence, I'd recommend to seek for an alternative solution when possible.

In the first example, you could use a generator:

@[For-Else Example]({"stubs": ["example3.py"], "command": "python3 example3.py"})

And in a lot of cases, you can use `any`:

```Python
if any(check_condition(x) for x in l):
    do_something()
else:
    do_something_else()
```
