===========
Pybles
===========

This is a module designed to make table representations very easy and fast. This is how to use it:

    #!/usr/bin/env python

    import pybles

    >>> PB = pybles.Pyble()
    >>> PB.set_header(['Product', 'Cost'])
    >>> PB.add_line(['PC', 1000])
    >>> PB.add_line(['Mouse', 10])
    >>> PB.add_separator()
    >>> PB.add_line(['TOTAL', 1010])
    >>> PB.show_table()
    ----------------------
    | PRODUCT     | COST |
    ----------------------
    | PC          | 1000 |
    | Mouse       | 10   |
    ----------------------
    | TOTAL       | 1010 |
    ----------------------

