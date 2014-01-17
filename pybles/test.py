import pybles

a = pybles.Pyble(header_color='STRONG_RED', header_background_color='BG_WHITE')

a.add_column('First Name')
a.add_column('Last Name')
a.add_line(['John', 'Doe'])
a.show_table()
a.set_color(True)
a.show_table()

print a.get_table_as_json()
