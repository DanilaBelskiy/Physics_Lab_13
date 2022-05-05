from table_print import print_table
from data_input import R2, L, table1, table2
from data_output import table_out_1, table_out_2
from math import log as log

#constants-------------------------

Pi = 3.14
E0 = 1

#----------------------------------

for i in range(1, len(table1)):
    R1 = table1[i][0]
    C_izm = table1[i][1]
    C_rasch = (2 * Pi * E0 * L) / (log(R2/R1))
    C_pl = (2 * E0 * Pi * R1 * L) / (R2 - R1)
    table_out_1[i][0] = R1
    table_out_1[i][1] = round(log(R2/R1), 2)
    table_out_1[i][2] = round(C_rasch, 2)
    table_out_1[i][3] = round(C_pl, 2)
    table_out_1[i][4] = round(C_izm, 2)
    table_out_1[i][5] = round(R2-R1, 2)

for i in range(1, len(table2)):
    Ci = table2[i][0]
    Coi = table2[i][1]
    E = Ci / Coi
    table_out_2[i][0] = Ci
    table_out_2[i][1] = Coi
    table_out_2[i][2] = round(E, 2)

print('Таблица 1:')
print_table(table_out_1)
print('Таблица 2:')
print_table(table_out_2)
