import pybles

print pybles.VERSION

a = pybles.Pyble(header_color='STRONG_RED', header_background_color='BG_WHITE')

#a.add_column('First Name')
#a.add_column('Last Name')

a.set_header(['First Name', 'Last Name', 'DNI'])

a.add_line(['John', 'Doe', '3434556'])
a.add_line(['Tito', 'Puente', '5434990'])
a.show_table()
a.set_color(True)
a.show_table()

print a.get_table_as_json()

print a
