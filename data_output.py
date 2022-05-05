table_out_1 = [
    ['R1', 'ln(R2/R1)', 'C расч', 'C пл', 'C изм', 'd=R2-R1'],
]

table_out_2 = [
    ['Ci', 'Coi', 'E'],
]

from data_input import table1, table2

for i in range(len(table1)-1):
    table_out_1.append(['', '', '', '', '', ''])

for i in range(len(table2) - 1):
    table_out_2.append(['', '', ''])
