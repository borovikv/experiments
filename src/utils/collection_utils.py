import csv


def write_to_csv(rows, file):
    writer = csv.writer(open(file,'w'))
    writer.writerows(rows)
