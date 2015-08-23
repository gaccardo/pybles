===========
Pybles
===========

This is a module designed to make table representations very easy and fast. This is how to use it:

    #!/usr/bin/env python

    import pybles

    PB = pybles.Pyble()

    PB.set_header(['First Name', 'Last Name'])

    PB.add_line(['John', 'Doe'])

    PB.show_table()
    

Output:

    --------------------------
    | First Name | Last Name |
    --------------------------
    | John       | Doe       |
    --------------------------
