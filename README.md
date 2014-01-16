===========
Pybles
===========

This is a modules designed to make table representations very easy and fast. This is how to use it:

    #!/usr/bin/env python

    from pybles import pybles

    PB = pybles.Pyble()

    PB.add_column('First Name')

    PB.add_column('Last Name')

    PB.add_line(['John', 'Doe'])

    PB.show_table()


Output:

    --------------------------
    | First Name | Last Name |
    --------------------------
    | John       | Doe       |
    --------------------------

Now, table can have colors:

    #!/usr/bin/env python

    from pybles import pybles

    PB = pybles.Pyble(header_color='STRONG_RED',
        header_background_color='BG_WHITE')

    PB.set_color(True)
    
    
For further information see: http://pythonhosted.org//Pybles

    PB.add_column('First Name')

    PB.add_column('Last Name')

    PB.add_line(['John', 'Doe'])

    PB.show_table()
