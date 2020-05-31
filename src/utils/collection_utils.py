import csv


def write_to_csv(rows, file):
    writer = csv.writer(file)
    writer.writerows(rows)
