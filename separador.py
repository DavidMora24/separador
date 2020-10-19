import time
import argparse

# Lectura del fichero
def read_file(file):
    with open(file) as f:
        document = f.read()
        rows = document.split(";")
        # import pdb; pdb.set_trace()
        return rows

# Guarda el nuevo fichero
def save_file(rows):
    fecha = time.strftime('%Y%m%d')
    hora = time.strftime('%H%M')
    with open("commands_to_execute_{}_{}.txt".format(fecha,hora),'w') as output_document:
        for row in rows:
            output_document.write(str(row).strip()+'\n')
        print('exportado OK')

# main
def perform_file():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="name file plus the extension, ejm:'text.txt'")
    args = parser.parse_args()
    file = args.file
    rows = read_file(file)
    save_file(rows)

if __name__ == "__main__":
    perform_file()

"""Execute since the command line: python separador.py text.txt"""