import pandas as pd
import os
import argparse

# OS functions
print("Path:{}".format(os.path))            # path module
print("Path:{}".format(os.getcwd()))        # Path curent file system
print("Path:{}".format(os.listdir('.')))    # Listar carpeta

# Parse
parse = argparse.ArgumentParser()
parse.add_argument("-f", help='entry_the_xls_file.xls')
parse.add_argument("-s", help='sheet.xls')
args = parse.parse_args()
# import pdb; pdb.set_trace()

complet_file = pd.read_excel(args.f, sheet_name=args.s)
print('num_filas = {}'.format(complet_file.shape[0]))
print('num_columnas = {}'.format(complet_file.shape[1]))
campos_importantes = [
    'grupo_funcional',
    'tabla hive',
    'tabla origen',
    'comentarios',
    'job name',
    'planificacion',
    'condicion previa'
    ]
for n in campos_importantes:
    print(40*'-')
    print('{} ='.format(n))
    print(complet_file[n])
    print(40*'-')

# for row in complet_file:
#     print(row)

"""Execute:
    python work_xls.py -f headers.xls -h SSMM"""