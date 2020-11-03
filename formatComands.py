"""Execute since the command line: python formatComands.py text.txt"""

import time
import argparse

# Read file
def read_file(file):
    separator = ";"
    new_file = []
    with open(file) as f:
        for row in f.readlines():
            hive_lines = map(lambda x: x.strip(), row.split(separator))
            for hive_line in hive_lines:
                if hive_line[0] == 'h':
                    hdfs_lines = map(lambda x: x.strip(), hive_line.split("\t"))
                    for hdfs_line in hdfs_lines:
                        new_file.append(hdfs_line)
                else:
                    new_file.append(hive_line + separator)

            new_file.append("\t")
        new_file.pop(-1)
        return new_file

# Save file
def save_file(new_file):
    date = time.strftime('%Y%m%d')
    hour = time.strftime('%H%M')
    with open("commands_to_execute_{}_{}.txt".format(date,hour),'w') as output_document:
        for row in new_file:
            output_document.write(str(row)+'\n')
        print('transform OK')

# main
def perform_file():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="file_name.file_extension, ejm:'text.txt'")
    args = parser.parse_args()
    new_file = read_file(args.file)
    save_file(new_file)

if __name__ == "__main__":
    perform_file()
